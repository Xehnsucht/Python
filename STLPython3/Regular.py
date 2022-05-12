import re
print('Part 1')
pattern = 'this'
text = ' Does this text match the pattern ?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]
))


print('Part 2')
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')

    if regex.search(text):
        print('Match!')
    else:
        print('no match')

print('Part 3')

text = 'babababababababababba'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))

print('Part 4')

for match in re.finditer(pattern, text):
     s = match.start()
     e = match.end()
     print('Found {!r} at {:d}:{:d}'.format(
         text[s:e], s, e
     ))

print ('Test function')

def test_patterns(text, patterns):
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("'{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print(" {} '{}'".format(prefix, substr))
        print()
    return
if __name__ == '__main__':
    print('Default pattern')
    test_patterns('abbaaabbbaaaa',
                  [('ab', "'a' followed by 'b'"),
                   ])

    print('Repeat patterns')
    test_patterns(
        'abbaabbba',
        [('ab*', 'a followed by zero or more b'),
        ('ab+', 'a followed by one or more b'),
        ('ab?', 'a followed by zero or one b'),
        ('ab{3}', 'a followed by three b'),
        ('ab{2,3}', 'a followed by two to three b')],
    )

    print('Charset')

    test_patterns(
        'This is some text -- with punctuation.',
        [('[^-. ]+', 'sequences without -, ., or space')]
    )
    print('charset ranges')
    test_patterns(
        'This is some text — with punctuation.',
        [('[a-z]+', 'sequences of lowercase letters'),
         ('[A-Z]+', 'sequences of uppercase letters'),
         ('[a-zA-Z]+', 'sequences of lower- or uppercase letters'),
         ('[A-Z][a-z]+', 'one uppercase followed by lowercase')],
    )
