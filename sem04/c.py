def main():
    lst = [int(e) for e in input().split()]
    print('yes' if len(set(lst)) < len(lst) else 'no')


if __name__ == '__main__':
    main()
