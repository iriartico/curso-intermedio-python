# Crear un diccionario que tenga como llaves, los números del 1 al 100
# y los valores sean el cubo del valor de su llave.

def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(my_dict)


if __name__ == '__main__':
    run()
