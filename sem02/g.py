def main():
    lst = [int(e) for e in input().split()]
    n = len(lst)
    sm = sum(lst)
    print(n * (n + 1) // 2 - sm)


if __name__ == '__main__':
    main()
