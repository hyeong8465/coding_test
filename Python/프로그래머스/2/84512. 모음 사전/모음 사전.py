"""
15:21
AEIOU로 만들 수 있는 길이 5 이하의 모든 단어의 수 -> 약 sum(5, 5^2, 5^3, 5^4, 5^5) = 3905

dfs

"""
def solution(word):
    word = list(word)
    global answer
    global cnt
    answer = 0
    cnt = 0
    def dfs(word_list):
        global answer
        global cnt
        # print(cnt, word_list)
        if word_list == word:
            answer = cnt

        if len(word_list) == 5:
            return

        for c in ["A", "E", "I", "O", "U"]:
            word_list.append(c)
            cnt += 1
            dfs(word_list)
            word_list.pop()

    dfs([])
    # print(answer)
    return answer
