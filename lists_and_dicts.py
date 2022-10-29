def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Jose", "Lastname": "Iriarte"}

    super_list = [
      {"firstname": "Jose", "Lastname": "Iriarte"},
      {"firstname": "Miguel", "Lastname": "Otrillas"},
      {"firstname": "Sergio", "Lastname": "Jurado"},
      {"firstname": "Andrés", "Lastname": "Gonzalez"},
    ]

    super_dict = {
      "natural_nums": [1,2,3,4,5],
      "integer_nums": [-1,-2,0,1,2],
      "float_nums": [-1.3,-2.45,0.3,1.9,2.12],
    }

    # for key, value in super_dict.items():
      # print(key, "-", value)
    for item in super_list:
      print(item["firstname"], item["Lastname"])

if __name__ == '__main__':
    run()
