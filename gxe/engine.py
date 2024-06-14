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

        Returns:
            dict: A dictionary of executed nodes, with node IDs as keys and Node objects as values.

        """
        queue = [node_id for node_id, degree in self.in_degree.items() if degree == 0]

        while queue:
            node_id = queue.pop(0)
            node = self.nodes[node_id]
            node.execute()

            for edge in self.graph["edges"]:
                if edge["source"] == node_id:
                    target_node_id = edge["target"]
                    target_node = self.nodes[target_node_id]
                    output = (
                        node.output[edge["source_handle"]]
                        if "source_handle" in edge
                        else node.output
                    )
                    target_node.set_input(edge["target_handle"], output)
                    self.in_degree[target_node_id] -= 1
                    if self.in_degree[target_node_id] == 0:
                        queue.append(target_node_id)

        return self.nodes
