if __name__ == '__main__':
    n = int(input())
    if n < 1 or n > 20:
        print("n is out of range")
    for i in range(n):
        print(i**2)