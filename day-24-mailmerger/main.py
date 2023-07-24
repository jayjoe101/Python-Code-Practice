letter = []
names = []

with open('names.txt', mode='r') as file:
    n = file.read()
    for name in n.split('\n'):
        names.append(name)
file.close()

with open('letter.txt', mode='r') as l:
    lc = l.read()
    for word in lc.split('\n'):
        letter.append(word)
l.close()

with open('finished_letters', mode='w') as f:
    for n in range(len(names)-1):
        letter[1] = f'Dear {names[n]},'
        f.write('\n'.join(letter))
f.close()
            
        