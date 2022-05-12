import  textwrap
from textwrap_example import sample_text

print('Fill')
print(textwrap.fill(sample_text, width=50))

print('Dedend')
dedenter_text = textwrap.dedent(sample_text)
print('Dedenter:')
print(dedenter_text)

print('Dedent plus fill')
dedenter_text = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
    print('{} Columns:\n'.format(width))
    print(textwrap.fill(dedenter_text, width=width))
    print()


print('Decoding text blocks')
dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += '\n\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped, '>')
print('Quoted block:\n')
print(final)


print('Textwrap indent predicate')
def should_indent(line):
    print('Indent {!r}?'.format(line))
    return len(line.strip()) % 2 == 0

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(wrapped, 'EVEN ',
                        predicate=should_indent)
print('\nQuoted block:\n')
print(final)


print('Hanging')
dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=50,
                    ))
print('Shorten')

dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)

print('Original:\n')
print(original)

shortened = textwrap.shorten(original, 100)
shortened_warpped = textwrap.fill(shortened, width=50)

print('\nShortedd:\n')
print(shortened_warpped)

