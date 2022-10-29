from functools import reduce


def run():
    # MAP
    # my_list = [1, 2, 3, 4, 5]
    # squares = [i**2 for i in my_list]
    # squares = list(map(lambda x: x**2, my_list))

    # print(squares)

    # REDUCE
    my_list = [2, 2, 2, 2, 2]
    # all_multiplied = 1
    # for i in my_list:
    #     all_multiplied *= i
    all_multiplied = reduce(lambda a, b: a*b, my_list)

    print(all_multiplied)


if __name__ == '__main__':
    run()
