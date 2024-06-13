from gxe.node import Node


class GraphExecutionEngine:
    def __init__(self, graph, node_registry):
        self.graph = graph
        self.node_registry = node_registry
        self.nodes = {}
        self.in_degree = {}

    def parse_node(self):
        for node in self.graph["nodes"]:
            node_id = node["id"]
            node_type = node["type"]
            node_data = node["data"] if "data" in node else {}

            self.nodes[node_id] = Node(
                node_id,
                node_type,
                self.node_registry[node_type],
                node_data,
            )
            self.in_degree[node_id] = 0

        for edge in self.graph["edges"]:
            target_node_id = edge["target"]
            self.in_degree[target_node_id] += 1

    def execute(self):
        queue = [node_id for node_id, degree in self.in_degree.items() if degree == 0]

        while queue:
            node_id = queue.pop(0)
            node = self.nodes[node_id]
            node.execute()

            for edge in self.graph["edges"]:
                if edge["source"] == node_id:
                    target_node_id = edge["target"]
                    target_node = self.nodes[target_node_id]
                    target_node.set_input(edge["target_handle"], node.output)
                    self.in_degree[target_node_id] -= 1
                    if self.in_degree[target_node_id] == 0:
                        queue.append(target_node_id)

        return self.nodes
