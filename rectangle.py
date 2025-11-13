def area(a, b):
    '''Вычисляет площадь прямоугольника по 2 сторонам'''
    return a * b 

def perimeter(a, b): 
    '''Вычисляет периметр прямоугольника по 2 сторонам'''
    return 2 * (a + b) 

import heapq
from collections import defaultdict
import sys

class FibonacciHeap:
    def __init__(self):
        self.heap = []
        self.elements = defaultdict(int)
    
    def insert(self, x):
        heapq.heappush(self.heap, x)
        self.elements[x] += 1
    
    def extract_min(self):
        while self.heap and self.elements[self.heap[0]] == 0:
            heapq.heappop(self.heap)
        
        if not self.heap:
            return None
        
        min_val = heapq.heappop(self.heap)
        self.elements[min_val] -= 1
        return min_val
    
    def merge(self, other):
        new_heap = FibonacciHeap()
        
        new_heap.heap = list(self.heap) + list(other.heap)
        heapq.heapify(new_heap.heap)

        for val, count in self.elements.items():
            new_heap.elements[val] = count
        for val, count in other.elements.items():
            new_heap.elements[val] += count
        
        return new_heap
    
    def decrease_key(self, x, y):
        if self.elements[x] > 0:
            self.elements[x] -= 1  
            self.elements[y] += 1  
            heapq.heappush(self.heap, y)

heaps = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    parts = line.split()
    cmd = parts[0]
    
    if cmd == 'create':
        heaps.append(FibonacciHeap())
    
    elif cmd == 'insert':
        k = int(parts[1])
        x = int(parts[2])
        heaps[k].insert(x)
    
    elif cmd == 'extract-min':
        k = int(parts[1])
        result = heaps[k].extract_min()
        print(result if result is not None else '*')
    
    elif cmd == 'merge':
        k = int(parts[1])
        m = int(parts[2])
        new_heap = heaps[k].merge(heaps[m])
        heaps.append(new_heap)
    
    elif cmd == 'decrease-key':
        k = int(parts[1])
        x = int(parts[2])
        y = int(parts[3])
        heaps[k].decrease_key(x, y)