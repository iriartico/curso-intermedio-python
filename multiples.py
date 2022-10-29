# Crear una list comprehension, una lista de todos los múltiplos de 4 que a su vez
# sean también múltplos de 6 y 9, hasta 5 dígitos

def run():
    multiples = [i for i in range(
        1, 10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(multiples)


if __name__ == '__main__':
    run()
