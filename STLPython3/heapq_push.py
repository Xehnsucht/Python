import heapq
from heapq_data import data
from heapq_showtree import show_tree

heap = []
print('random:', data)
print()
for n in data:
    print('add {:>3}'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)

heapq.heapify(data)
print('heapified:')
show_tree(data)

print('Heap Pop')
for i in range(2):
    smallest = heapq.heappop(data)
    print('pop {:>3}:'.format(smallest))
    show_tree(data)