def mutate_string(string, position, character):
    new_string = ""
    while True:
        for item in string:
            if position != len(new_string):
                new_string += item
                if len(new_string) == len(string):
                    break
            else:
                new_string += character
                if len(new_string) == len(string):
                    break
        return new_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
