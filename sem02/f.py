def main():
    password = input()
    print(not password.islower() and not password.isupper() and not password.isdigit())


if __name__ == '__main__':
    main()
