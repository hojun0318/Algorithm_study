N = int(input())
money = list(map(int, input().split()))
M = int(input())


def binary_search(money):
    s = 0
    e = max(money)
    while s <= e:
        tot = 0
        mid = (s + e) // 2
        
        for num in money:
            if num >= mid:
                tot += mid
            else:
                tot += num

        if tot <= M:
            s = mid + 1

        else:
            e = mid - 1

    return e


print(binary_search(money))