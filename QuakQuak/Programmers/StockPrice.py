def solution(prices):
    pre = None
    list = []
    while prices:
        if pre == None:
            pre = prices.pop(0)
            continue
        if pre <= prices[0]:
            list.append(len(prices))
        elif pre > prices[0]:
            list.append(1)

        pre = prices.pop(0)
    list.append(0)
    return list

print(solution([1, 2, 3, 2, 3]))