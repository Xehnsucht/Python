import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('\nPart 1\n')
print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))


print('\nPart 2\n')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

print('\nPart 3\n')
class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print('Equality:',
    actual_state == desired_state,
    actual_state == BugStatus.wont_fix)

print('Identity:',
    actual_state is desired_state,
    actual_state is BugStatus.wont_fix)

print('Ordered by value:')
try:
    print('Xn'.join(' ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print(' Cannot sort: {}'.format(err))
