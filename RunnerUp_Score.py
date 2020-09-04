if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    j = 0

    max1 = max(arr)

    while max(arr) == max1:
        arr.remove(max(arr))

    print(max(arr))
