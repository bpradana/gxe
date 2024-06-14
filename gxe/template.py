import inspect


class TemplateGenerator:
    def __init__(self, node_registry):
        self.node_registry = node_registry

    def generate(self, path):
        for node in self.node_registry.items():
            if node.type == "function":
                inputs = inspect.getfullargspec(node).args
            else:
                inputs = (
                    inspect.getfullargspec(node).args[1:]
                    + inspect.getfullargspec(node.__call__).args
                )
