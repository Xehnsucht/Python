import string
import inspect

t = string.Template('$var')
print(t.pattern.pattern)


def is_str(value):
    return isinstance(value, str)

for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%rXn' % (name, value))