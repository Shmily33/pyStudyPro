def str_reverse(str):
    return str[::-1]


def substr(str, x, y):
    return str[x:y + 1]


if __name__ == '__main__':
    print(str_reverse("abcd"))
    print(substr("abcdef", 0, 3))
