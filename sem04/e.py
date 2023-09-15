def is_palindrom(s: str) -> bool:
    return s == s[::-1]


def main():
    s = input()
    result = True

    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            if not is_palindrom(s[i + 1:len(s) - i]) and not is_palindrom(s[i:len(s) - i - 1]):
                result = False
            break

    print('yes' if result else 'no')


if __name__ == '__main__':
    main()
