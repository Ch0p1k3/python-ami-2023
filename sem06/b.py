def permutations(s: str) -> list[str]:
    if len(s) <= 1:
        return [s[0]]

    result = []
    for i, c in enumerate(s):
        result.extend([c + p for p in permutations(s[:i] + s[i + 1:])])
    return result


def main():
    print(*sorted(permutations(input())), sep='\n')


if __name__ == '__main__':
    main()
