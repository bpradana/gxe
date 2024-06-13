class Node:
    """
    Represents a node in a graph execution engine.

    Attributes:
        id (str): The unique identifier of the node.
        label (str): The label of the node.
        operation (callable): The operation to be performed by the node.
        inputs (dict): The inputs required for the operation.
        output: The output of the node after execution.
        type (str): The type of the operation.
    """

    def __init__(self, id, label, operation, inputs):
        self.id = id
        self.label = label
        self.operation = operation
        self.inputs = inputs
        self.output = None

        self.type = type(operation).__name__
        self._init_class() if self.type == "type" else None

    def _init_class(self):
        """
        Initializes the operation if it is a class.
        """
        self.operation = self.operation(**self.inputs)
        self.inputs = {}

    def set_input(self, name, value):
        """
        Sets the input value for the given input name.

        Args:
            name (str): The name of the input.
            value: The value of the input.
        """
        self.inputs[name] = value

    def execute(self):
        """
        Executes the operation and stores the output.
        """
        self.output = self.operation(**self.inputs)
