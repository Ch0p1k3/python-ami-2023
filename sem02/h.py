def main():
    lst = [int(e) for e in input().split()]
    ptr = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[ptr] = lst[i]
            ptr += 1
    for i in range(ptr, len(lst)):
        lst[i] = 0
    print(*lst)


if __name__ == '__main__':
    main()
