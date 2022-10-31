def divisors(num):
    try:
        if num < 1:
            raise ValueError('El número no deber negativo')
        divisors = [i for i in range(1, num+1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print('Finished')
    except ValueError:
        print('Debe ingresar un número')


if __name__ == '__main__':
    run()
