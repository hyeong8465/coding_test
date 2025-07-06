from itertools import combinations
import sys
input = sys.stdin.readline

vowels = set(['a', 'e', 'i', 'o', 'u']) # 모음 집합 정의

L, C = map(int, input().split()) # 변수명 L, C로 변경하여 명확성 높임
candidates = list(input().rstrip().split(' '))
candidates.sort() # 입력 문자들을 미리 정렬

possible_passwords = [] # 생성된 암호를 저장할 리스트

# 모음과 자음을 분리할 필요 없이, 정렬된 전체 문자 집합에서 조합을 선택하는 방식으로 변경합니다.
# 이렇게 하면 나중에 모음/자음 개수 조건을 검사할 수 있습니다.
# (이전 코드처럼 미리 분리하고 조합하는 방식도 괜찮지만, 하나의 조합으로 다루는 것이 때로는 더 간단)

for combo_chars in combinations(candidates, L): # candidates에서 L개의 문자를 뽑는 모든 조합
    vowel_count = 0
    consonant_count = 0
    
    for char in combo_chars:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
            
    # 최소 한 개의 모음, 최소 두 개의 자음 조건 확인
    if vowel_count >= 1 and consonant_count >= 2:
        # 조합된 문자들은 이미 candidates가 정렬되어 있었기 때문에 자동으로 정렬된 상태입니다.
        # 따라서 별도의 total.sort()가 필요 없습니다.
        possible_passwords.append(''.join(combo_chars))

# 최종적으로 생성된 암호들이 이미 정렬되어 있으므로, 마지막 ans.sort()는 필요 없습니다.
# combinations는 입력 iterable의 순서를 유지합니다.
for password in possible_passwords:
    print(password)