def palindrome(string):
    # MANEJO DE EXCEPCIONES
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar cadenas vacias')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

    # MANEJO DE AFIRMACIONES
    # assert len(string) > 0, 'No se puede ingresar una cadena vacía'
    # return string == string[::-1]


def run():
    word = input('Escriba una palabra: ')
    try:
        print(palindrome(word))
    except TypeError:
        print('Solo se pueden ingresar string')


if __name__ == '__main__':
    run()
