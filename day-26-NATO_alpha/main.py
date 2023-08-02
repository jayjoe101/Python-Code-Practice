import pandas


pho_alpha = pandas.read_csv('nato_phonetic_alphabet.csv')
pho_dict = {row.letter:row.code for (index, row) in pho_alpha.iterrows()}


while True:
    try:
        word = [c.upper() for c in input('Enter a word: ')]

        result = [pho_dict[letter] for letter in word]
        print(result)
        if input('Want to generate another word? ') == 'n':
            break
    except KeyError:
        print(f'{word} contains characters outside of the alphabet')
