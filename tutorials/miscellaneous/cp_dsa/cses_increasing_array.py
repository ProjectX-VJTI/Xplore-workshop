def main():
    # CSES Increasing Array problem: https://cses.fi/problemset/task/1094

    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(1, n):
        # If the current element is less than the previous one, we need to increase it
        if a[i] < a[i - 1]:
            ans += a[i - 1] - a[i]
            a[i] = a[i - 1]

    print(ans)

if __name__ == "__main__":
    main()