import json

from gxe import GraphExecutionEngine


def input(value):
    return value


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero.")


class SwapIncrement:
    def __init__(self, increment):
        self.increment = increment
        pass

    def __call__(self, a, b):
        return {"a": b + self.increment, "b": a + self.increment}


if __name__ == "__main__":
    with open("graph.json", "r") as f:
        graph = json.load(f)

    node_registry = {
        "input": input,
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "swap_increment": SwapIncrement,
    }

    engine = GraphExecutionEngine(graph, node_registry)
    engine.parse_node()
    result = engine.execute()

    for node_id, node in result.items():
        print(
            f"node {node_id} | label: {node.label} | inputs: {node.inputs} | output: {node.output}"
        )
