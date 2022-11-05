import random
import os


def clear():
    os.system('clear')


def random_word():
    words = []
    with open("./files/data.txt", 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line[:-1].upper())
    word = words[random.randint(0, 170)]
    _word = ''
    for i, value in enumerate(word):
        if i < len(word) - 1:
            _word += value + " "
        else:
            _word += value
    return _word


def hide_word(word):
    # result = re.findall('\w', word)
    for i, value in enumerate(word):
        if i % 2 != 1 and (random.randint(0, 500)) % 2 != 0:
            word = word.replace(value, '_')
    return word


def show_word(word, _word, charter):
    new_word = ''
    for i, value in enumerate(word):
        if value == _word[i] or value == charter:
            new_word += word[i]
        else:
            new_word += '_'
    return new_word


def show_screen(word):
    clear()
    menu = '''
-----------------------------
¡Adivina la palabra!
-----------------------------
%s
''' % (word)
    print(menu)


def run():
    word = random_word()
    _word = hide_word(word)
    while True:
        show_screen(_word)
        text = input('Ingrese una letra: ')
        assert len(text) == 1, 'Solo debe ingresar una letra'
        assert text.isnumeric() == False, 'No se admiten datos de tipo numérico'
        print(text.isnumeric())
        _word = show_word(word, _word, text.upper())
        if word == _word:
            show_screen(_word)
            print('¡¡¡Ganaste!!! \n\n*** La palabra era: ' + word + ' ***\n')
            break


if __name__ == '__main__':
    run()
