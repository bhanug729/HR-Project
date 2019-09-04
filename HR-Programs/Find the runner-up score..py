if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for item in range(n):
        if arr[n - 1 - item] != arr[n - 2 - item]:
            print(arr[n - item - 2])
            break
