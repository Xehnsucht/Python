import array
import binascii
import tempfile
fmt = '{:>12}'
print(fmt.format('*'*60))
print("   Array   последовательность данных фиксированного типа")
print(fmt.format('*'*60))

print('Part 1')
fmt = '{:>12}'
print(fmt.format('-'*60))
s = b'This is array.'
a = array.array('b', s)

print('As byte string:', s)
print('As array:', a)
print('As hex:', binascii.hexlify(a))

print('Part 2')
fmt = '{:>12}'
print(fmt.format('-'*60))
a = array.array('i', range(3))
print('Initial :', a)
a.extend(range(3))
print('Extended:', a)
print('Slice :', a[2:5])
print('Iterator: ' )
print(list(enumerate(a)))

print('Part 3')
fmt = '{:>12}'
print(fmt.format('-'*60))
a = array.array('i', range(5))
print('A1:', a)

output = tempfile.NamedTemporaryFile()
a.tofile(output.file)
output.flush()

with open(output.name, 'rb') as input:
    raw_data = input.read()
    print('Raw Contents:', binascii.hexlify(raw_data))

    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print('A2:', a2)

print('Part 4')
fmt = '{:>12}'
print(fmt.format('-'*60))
as_bytes = a.tobytes()
print('Bytes:', binascii.hexlify(as_bytes))

a2 = array.array('i')
a2.frombytes(as_bytes)
print('A2:', a2)

print('Part 5 C Python')
fmt = '{:>12}'
print(fmt.format('-'*60))
def to_hex(a):
    chars_per_item = a.itemsize * 2 # two 16-numbers
    hex_version = binascii.hexlify(a)
    num_chunks  = len(hex_version) # chars per item
    for i in range(num_chunks):
        start = i * chars_per_item
        end   = start + chars_per_item
        yield hex_version[start:end]

start = int ('0x12345678', 16)
end = start + 5
a1 = array.array('i', range(start, end))
a2 = array.array('i', range(start, end))
a2.byteswap()

fmt = '{:>12} {:>12} {:>12} {:>12}'

print(fmt.format('A1 hex', 'A1', 'A2 hex', 'A2'))
print(fmt.format('-' * 12, '-' * 12, '-' * 12, '-' * 12, '-' * 12))
fmt = '{!r:>12} {:12} {!r:>12} {:12}'
for values in zip(to_hex(a1), a1, to_hex(a2), a2):
    print(fmt.format(*values))
