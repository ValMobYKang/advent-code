import re, os
from collections import defaultdict

with open("puzzle", 'r') as f:
    puzzle = f.readlines()

def get_ROOT_NUM(puzzle):
    ROOT_NUM = {}
    for idx, line in enumerate(puzzle):
        left_right = line.strip().split(': ')[-1]
        left, right = left_right.split(' | ')
        result = set(left.split(' ')) & set(right.split(' '))
        
        if '' in result: result.remove('')
        
        ROOT_NUM[idx+1] = len(result) if result else 0
    return ROOT_NUM

ROOT_NUM = get_ROOT_NUM(puzzle)
TOTAL = defaultdict(int)
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next_nodes = []
    
    def collect_next_nodes(self):
        for delta in range(ROOT_NUM[self.value]):
            next_node_value = self.value + delta + 1
            self.next_nodes.append(Node(next_node_value))

    def __repr__(self) -> str:
        return str(f"[{self.value}]: {ROOT_NUM[self.value]}")
    

def foo(node:Node):
    if ROOT_NUM[node.value] == 0: 
        return 
    node.collect_next_nodes()
    for next_node in node.next_nodes:
        TOTAL[next_node.value] += 1
        foo(next_node)
    return node


for value in ROOT_NUM.keys():
    TOTAL[value] += 1 
    result = foo(Node(value=value))


print(sum(v for v in TOTAL.values()))