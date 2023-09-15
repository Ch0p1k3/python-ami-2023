from collections import defaultdict


def main():
    n = int(input())
    dct = defaultdict(list)

    for _ in range(n):
        k, v = (e for e in input().split())
        dct[int(v)].append(k)

    for k in sorted(dct):
        print(k, list(sorted(dct[k])))


if __name__ == '__main__':
    main()
