word = input().strip().upper()

# 모든 문자를 0으로 초기화하는 대신, Counter를 사용하면 더 간단하게 처리 가능
from collections import Counter
dic = Counter(word)

# 최대 빈도와 해당 문자를 구함
max_count = max(dic.values())
# 최대 빈도를 가진 모든 문자 리스트
max_chars = [char for char, count in dic.items() if count == max_count]

if len(max_chars) > 1:
    print('?')
else:
    print(max_chars[0])