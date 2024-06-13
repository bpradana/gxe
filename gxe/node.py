class Node:
    def __init__(self, id, label, operation, inputs):
        self.id = id
        self.label = label
        self.operation = operation
        self.inputs = inputs
        self.output = None

        self.type = type(operation).__name__
        self._init_class() if self.type == "type" else None

    def _init_class(self):
        self.operation = self.operation(**self.inputs)
        self.inputs = {}

    def set_input(self, name, value):
        self.inputs[name] = value

    def execute(self):
        self.output = self.operation(**self.inputs)
