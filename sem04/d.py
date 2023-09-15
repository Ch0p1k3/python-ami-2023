def main():
    message = input()
    n = int(input())
    result = ''

    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                result += chr((ord(letter) - ord('A') + n) % (ord('Z') - ord('A') + 1) + ord('A'))
            else:
                result += chr((ord(letter) - ord('a') + n) % (ord('z') - ord('a') + 1) + ord('a'))
        else:
            result += letter

    print(result)


if __name__ == '__main__':
    main()
