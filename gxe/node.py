import inspect


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
        self._init_class() if (self.type == "type" and self.inputs) else None

    def _split_dictionary(self, dictionary, keys_to_pop):
        """
        Splits a dictionary into two dictionaries based on the keys to pop.

        Args:
            dictionary (dict): The dictionary to split.
            keys_to_pop (list): The keys to pop from the dictionary.

        Returns:
            dict, dict: Two dictionaries, one with the popped keys and one without the popped keys.
        """
        popped = {key: dictionary.pop(key) for key in keys_to_pop}
        return popped, dictionary

    def _init_class(self):
        """
        Initializes the operation if it is a class.
        """
        inputs, self.inputs = self._split_dictionary(
            self.inputs,
            inspect.getfullargspec(self.operation.__init__).args[1:],
        )
        self.operation = self.operation(**inputs)
        self.type = "function"

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
        if self.type == "type":
            self._init_class()
        self.output = self.operation(**self.inputs)
