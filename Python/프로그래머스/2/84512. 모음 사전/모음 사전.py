def solution(word):
    word = list(word)

    def dfs(word_list, cnt, answer):
        if word_list == word:
            answer = cnt
        if len(word_list) == 5:
            return cnt, answer
        for c in ["A", "E", "I", "O", "U"]:
            word_list.append(c)
            cnt, answer = dfs(word_list, cnt+1, answer)
            word_list.pop()
        return cnt, answer

    _, answer = dfs([], 0, 0)
    return answer