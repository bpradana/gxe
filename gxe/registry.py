class NodeRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, objs):
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
