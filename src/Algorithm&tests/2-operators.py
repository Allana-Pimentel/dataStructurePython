if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = a + b
    d = a - b
    e = a * b

    if a < 1 or a > 10**10:
        print("a is out of range")
    elif b < 1 or b > 10**10:
        print("b is out of range")
    else:
        print(c)
        print(d)
        print(e)