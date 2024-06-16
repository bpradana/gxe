import json
import random
import time

from gxe import GraphExecutionEngine, NodeRegistry


def input(value):
    time.sleep(1)
    return value


def add(a, b):
    time.sleep(1)
    return a + b


def subtract(a, b):
    time.sleep(1)
    return a - b


def multiply(a, b):
    time.sleep(1)
    return a * b


def divide(a, b):
    time.sleep(1)
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero.")


class SwapIncrement:
    def __init__(self, increment):
        self.increment = increment

    def __call__(self, a, b):
        time.sleep(1)
        return {"a": b + self.increment, "b": a + self.increment}


if __name__ == "__main__":
    with open("graph.json", "r") as f:
        graph = json.load(f)

    node_registry = NodeRegistry()
    node_registry.register(
        [
            input,
            add,
            subtract,
            multiply,
            divide,
            SwapIncrement,
        ]
    )

    engine = GraphExecutionEngine(graph, node_registry)
    engine.parse_node()

    start_time = time.time()
    result = engine.execute()
    end_time = time.time()

    print(f"Execution time: {end_time - start_time:.2f} seconds")

    for node in result.values():
        print(node)
