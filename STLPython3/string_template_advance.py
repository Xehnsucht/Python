import string


class myTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

template_text = '''
    Delimiter : %%
    Replaced  : %with_underscore
    Ignored   : %notunderscored
    Text      : %te_xt
'''

d = {
    'with_underscore': 'replaced',
    'notunderscored': 'not replaced',
    'te_xt': 'replaced',
}

t = myTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))
