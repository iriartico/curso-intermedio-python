def run():
    palindrome = lambda string:string == string[::-1]
    word = input('Escriba una palabra: ')
    try:
        print(palindrome(word))
    except TypeError:
        print('Solo se pueden ingresar string')


if __name__ == '__main__':
    run()
