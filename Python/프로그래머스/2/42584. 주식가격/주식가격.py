"""
15:09
가격이 떨어지지 않은 기간은 몇초?

1. 완전탐색? -> O(N^2) 비효율적
2. 

[1,2,3,2,3] (정답 [4,3,1,1,0])
3 [] 0 [3]
2 [3] 1 [3, 2]
3 [3, 2] 1 [3,2,3]
2 [3,2,3] 3 [3,2,3,2]
1 [3,2,3,2] 4 [3,2,3,2,1]

인덱스로 접근
1 [0]
2 [0,1]
3 [0,1,2]
2 [0,1,3] -> 감소시점 [_, _, 1]
3 [0,1,3,4] -> [4,3,1,1,0]


3,4,5,3,2,3 [3, 1, 1, 1,1,0]
3 [] 0 [3]
2 [3] 1 [3,2]
3 [3,2] 1 [3]
5 [3] 1 [5]
4 [5] 1 [5,4]
3 [5,4] 2 [5,4,3]

"""

def solution(prices):
    answer = [None]*len(prices)
    stack = []

    for i, price in enumerate(prices):
        # print(111, stack)
        if not stack:
            stack.append(i)
            # print(11)
        elif price >= prices[stack[-1]]:
            stack.append(i)
            # print(222)
        else:
            # print(333)
            while stack:
                if prices[stack[-1]] > price:
                    # print(stack)
                    idx = stack.pop()
                    answer[idx] = i-idx
                else:
                    break
            stack.append(i)
        # print(222, stack)
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices)-1-idx
    return answer

