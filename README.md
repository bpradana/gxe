# Graph Execution Engine
Execute Python code, graph style!

## Why?
I was bored. So I decided to write this monstrosity. It's a graph execution engine. It's a way to execute Python code in a graph just like in node based software like Blender, Unreal Engine, etc. It's a fun project and I'm sure it's not useful for anything. But it's fun to write and fun to use.

## Installation
```bash
echo "It's not a package yet. Just clone the repo and run the main.py file."
```

## Usage
```bash
python main.py
```

## How it works?
Basically, you create a graph with nodes. Each node is a Python function (or callable if you want to be more general). You connect the nodes with edges. When you run the graph, it executes the nodes in order based on the nodes dependencies.

## Example
```python
python -c "print('just clone the fucking repo and run the main.py file')"
```

## License
Graph Execution Engine is licensed under Do What The Fuck You Want To Public License. See the [LICENSE](LICENSE) file for more information.
