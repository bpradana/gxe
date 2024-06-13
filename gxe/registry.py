class NodeRegistry:
    """
    A registry for storing and accessing objects by name.

    This class provides a way to register objects and retrieve them by their name.
    It supports various operations such as getting an object by name, checking if an object is registered,
    iterating over the registered objects, and getting the number of registered objects.

    Attributes:
        _registry (dict): A dictionary to store the registered objects.

    Methods:
        register(objs): Register one or more objects.
        get(name): Get the object with the specified name.
        __getitem__(name): Get the object with the specified name using the indexing syntax.
        __contains__(name): Check if an object with the specified name is registered.
        __iter__(): Iterate over the registered objects.
        __len__(): Get the number of registered objects.
        __repr__(): Get a string representation of the registry.
        __str__(): Get a string representation of the registry.
    """

    def __init__(self):
        self._registry = {}

    def register(self, objs):
        """
        Register objects in the registry.

        Args:
            objs (list): A list of objects to be registered.

        Returns:
            None
        """
        for obj in objs:
            self._registry[obj.__name__] = obj

    def get(self, name):
        return self._registry.get(name)

    def __getitem__(self, name):
        return self.get(name)

    def __contains__(self, name):
        return name in self._registry

    def __iter__(self):
        return iter(self._registry)

    def __len__(self):
        return len(self._registry)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self._registry}>"

    def __str__(self):
        return str(self._registry)
