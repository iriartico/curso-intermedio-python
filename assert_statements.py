def divisors(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    return divisors


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric() and int(num) > 0, 'Debes ingresar únicamente números positivos'
    print(divisors(int(num)))
    print('Finished')


if __name__ == '__main__':
    run()
