import collections


print('\nAPI dictionary\n')
c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))

print('\nElements method\n')
c = collections.Counter('extremely')
c['z'] = 0
print(c)
print(list(c.elements()))

print('\nMost common\n')
"""
How often does the letter in system dict on unix-OS
"""
c = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())
print('Most common:')
for letter, count in c.most_common(3):
    print('{}: {:>7}'.format(letter, count))
