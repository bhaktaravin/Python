def main():
    dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    tmp = convert_to_array(dictionary)

    for c in tmp:
        print(c)

    
def convert_to_array(dictionary):
    lst = []
    if not dictionary:
        return "False"
    else:
        for key, value in dictionary.items():
            tmp = [key, value]
            lst.append(tmp)
        return lst


if __name__ == "__main__":
    main()