def res(compute):
    res = compute(2, 3)
    print(res)


def compute(x, y):
    return x + y


res(compute)


def res1(compute1):
    res = compute1(2, 3)
    print(res)

res1(lambda x,y : x-y)
