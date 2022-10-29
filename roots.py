# Crear un dictionary comprehension donde las llaves serán los primeros 1000 números
# naturales con sus raíces cuadradas como valores.

from math import sqrt


def run():
    roots = {i: round(sqrt(i), 2) for i in range(1, 101)}

    print(roots)


if __name__ == '__main__':
    run()
