# tuple
# Decart with list

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
for color in colors:
    for size in sizes:
        print((color, size))
print(type(tshirts))
for tshirts in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirts)
