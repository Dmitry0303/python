dict1 = {"Name": [1, 2, 3, 4],
         "Surname": [3, 46, 5, 6, 7, 8],
         "Fathername": [3, 4, 55, 6, 7, 8]}


def write_dict(mydict):
    if type(mydict) != dict:
        exit(1)
    else:
        for k, v in mydict.items():
            with open(f"{k}.txt", "w") as file:
                for i in v:
                    file.write(f"{str(i)}\n")
            file.close()


write_dict(dict1)
