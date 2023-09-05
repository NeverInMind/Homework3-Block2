import re
# unpacking the tuple

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n",
               "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je",
               "i", "ji", "g")

TRANS = {}
CYRILLIC_SYMBOLS_TUP = tuple(CYRILLIC_SYMBOLS)
for c, l in zip(CYRILLIC_SYMBOLS_TUP, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    global TRANS
    result = name.translate(TRANS)
    return result


def normalize(old_name):
    name = translate(old_name)
    name = re.sub(r'\W', '_', name)
    return name
