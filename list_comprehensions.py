# Crear una list comprehension que eleve al cuadrado los números del 1 al 100
# y verificar que sean exclusivamente múltiplos de 3.

def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)


if __name__ == '__main__':
    run()
