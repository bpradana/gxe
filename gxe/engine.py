from concurrent.futures import ThreadPoolExecutor, as_completed

from gxe.node import Node


class GraphExecutionEngine:
    """
    Executes a graph-based computation by traversing the nodes and their connections.

    Args:
        graph (dict): The graph representation containing nodes and edges.
        node_registry (dict): A registry of available node types.

    Attributes:
        graph (dict): The graph representation containing nodes and edges.
        node_registry (dict): A registry of available node types.
        nodes (dict): A dictionary of nodes in the graph, with node IDs as keys and Node objects as values.
        in_degree (dict): A dictionary that stores the in-degree of each node.

    """

    def __init__(self, graph, node_registry):
        self.graph = graph
        self.node_registry = node_registry
        self.nodes = {}
        self.in_degree = {}

    def parse_node(self):
        """
        Parses the nodes in the graph and initializes the nodes and in-degree dictionaries.

        """
        for node in self.graph["nodes"]:
            node_id = node["id"]
            node_type = node["type"]

            data = node["data"] if "data" in node else {}
            node_meta = data.pop("_meta", {})
            node_data = data

            self.nodes[node_id] = Node(
                node_id,
                node_type,
                self.node_registry[node_type],
                node_data,
                node_meta,
            )
            self.in_degree[node_id] = 0

        for edge in self.graph["edges"]:
            target_node_id = edge["target"]
            self.in_degree[target_node_id] += 1

    def execute(self):
        """
        Executes the graph by traversing the nodes and their connections.
        This method initializes a thread pool executor to execute the nodes in parallel.
        Nodes with no dependencies (in-degree of 0) are executed first.
        `futures` is used to keep track of nodes to be executed.
        After a node is executed, its output is passed to the target node through the edge connection and the in-degree of the target node is decremented.
        Nodes with no remaining dependencies are added to the queue for execution.

        Returns:
            dict: A dictionary of executed nodes, with node IDs as keys and Node objects as values.

        """
        queue = [node_id for node_id, degree in self.in_degree.items() if degree == 0]
        futures = []

        with ThreadPoolExecutor() as executor:
            while queue or futures:
                # Submit all nodes in the queue for parallel execution
                for node_id in queue:
                    future = executor.submit(self._execute_node, node_id)
                    futures.append(future)
                queue = []

                for future in as_completed(futures):
                    node_id = future.result()
                    futures.remove(future)
                    for edge in self.graph["edges"]:
                        if edge["source"] == node_id:
                            target_node_id = edge["target"]
                            target_node = self.nodes[target_node_id]
                            output = self._get_output_handle(self.nodes[node_id], edge)
                            target_node.set_input(edge["target_handle"], output)
                            self.in_degree[target_node_id] -= 1
                            if self.in_degree[target_node_id] == 0:
                                queue.append(target_node_id)

        return self.nodes

    def _execute_node(self, node_id):
        node = self.nodes[node_id]
        node.execute()
        return node_id

    def _get_output_handle(self, node, edge):
        if "source_handle" in edge:
            if edge["source_handle"] is not None:
                return node.output[edge["source_handle"]]
        return node.output
