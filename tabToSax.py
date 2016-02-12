SEMITONE_SHIFT = -3

NOTES = (
    'A',
    'A#',
    'B',
    'C',
    'C#',
    'D',
    'Eb',
    'E',
    'F',
    'F#',
    'G',
    'G#',
)

GUITAR = (
    7,
    0,
    5,
    10,
    2,
    7,
)

def shift(tab):
    for t in tab:
        yield t[0], (t[1] +SEMITONE_SHIFT)

def to_sax(tab):
    for t in shift(tab):
        yield NOTES[(GUITAR[t[0]-1]+t[1])%12]

def reader():
    while True:
        c = input().split(' ')
        yield int(c[0]), int(c[1])


if __name__ == '__main__':
    p = ""
    try:
        for t in to_sax(reader()):
            p += t + '\n'
    except:
        print(p)