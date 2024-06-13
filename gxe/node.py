class Node:
    def __init__(self, id, label, callable, inputs):
        self.id = id
        self.label = label
        self.callable = callable
        self.inputs = inputs
        self.output = None

    def set_input(self, name, value):
        self.inputs[name] = value

    def execute(self):
        self.output = self.callable(**self.inputs)
