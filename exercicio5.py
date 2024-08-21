
"""
def viola():
    quote = 'I shall destroy your happyend.'
    return quote

def davis(frase):
    print(frase)

sandra = viola()
davis(sandra)
"""

def viola():
    return 'I shall destroy your happyend.'


def davis(frase):
    return frase()


sandra = davis(viola)
print(sandra)

"""
def billie_holiday(all, ofme):

    print(all, ofme)


def billie():
    return 'all'

def holiday():
    return 'of Me'


play = billie()
play2 = holiday()
billie_holiday(play, play2)
"""


def billie_holiday(music, *args, **kwargs):
    return music (*args, **kwargs)


def billie(name):
    return f'Music: {name}'

def holiday(name, lyrics):
    return f'{name}, {lyrics}'



play = billie_holiday(billie, 'All of Me')
play2 = billie_holiday(holiday, 'All of Me', 'Why not take all of me...')
print(play)
print(play2)