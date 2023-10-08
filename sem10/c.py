import re


def main():
    s = input()
    print(re.sub(':-\)+|:-\(+', '', s))


if __name__ == '__main__':
    main()
