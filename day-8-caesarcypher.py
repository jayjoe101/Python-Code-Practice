alphabet = 'abcdefghijklmnopqrstuvwxyz'

def matching_char(l):
    for c in range(0, len(alphabet) + 1):
        if l.lower() == alphabet[c]:
            return c
    return None

def addtostring(string, l, i):
    if l.isupper():
        string += alphabet[i].upper()
    else:
        string += alphabet[i]
    return string

def encode(text, shift):
    t = ''
    for l in text:
        c = matching_char(l)
        if c != None:
            i = 0
            if c+1 + shift > 26:
                i = abs((26-(c+1)) - shift)
            else:
                i = c + shift
            t = addtostring(t,l,i)
        else:
            t += l
    return t

def decode(text, shift):
    t = ''
    for l in text:
        c = matching_char(l)
        if c != None:
            i = 0
            if c+1 - shift < 1:
                i = (c-1) - shift
            else:
                i = c - shift
            t = addtostring(t,l,i)
        else:
            t += l
    return t

while True:
    eORc = input('Type "encode" to ecrypt or "decode" to decrypt: ')
    message = input('Type your message: ')
    shift = int(input('Type the shift numebr: '))

    if eORc == 'encode':
        print (encode(message, shift))
    else:
        print (decode(message, shift))

    x = input('"Q" to quit or "R" to restart: ')
    if x.lower() == 'q':
        break