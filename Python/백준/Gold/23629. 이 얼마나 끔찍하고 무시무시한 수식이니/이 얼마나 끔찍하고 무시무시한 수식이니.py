import sys
input = sys.stdin.readline

formula = input().rstrip()

str2num = {"ZERO": "0", "ONE":"1", "TWO":"2", "THREE":"3", "FOUR":"4", "FIVE":"5", "SIX":"6", "SEVEN":"7", "EIGHT":"8", "NINE":"9"}
num2str = {"0": "ZERO", "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR", "5": "FIVE", "6":"SIX", "7":"SEVEN", "8":"EIGHT", "9":"NINE"}

temp = '' # 캐릭터 단위로 문자 하나씩 추가
temp_str = '' # 연산기호 나오기전 덩어리를 문자열로 저장
formula2num = ''
for i in formula:
    # print(temp, temp_str)
    if i in ['+', '-', 'x', '/', '=']:
        if temp_str == '':
            print("Madness!")
            quit()
        if formula2num == '': # 처음 연산 기호 나오면 앞에 있던 수 answer에 저장
            answer = int(temp_str) # 연산 결과로 사용
            formula2num += temp_str # 변환 결과 저장
            temp_str = ''
            formula2num += i # 연산 기호 저장
        elif formula2num[-1] == '+':
            answer += int(temp_str)
            formula2num += temp_str
            temp_str = ''
            formula2num += i
        elif formula2num[-1] == '-':
            answer -= int(temp_str)
            formula2num += temp_str
            temp_str = ''
            formula2num += i
        elif formula2num[-1] == 'x':
            answer *= int(temp_str)
            formula2num += temp_str
            temp_str = ''
            formula2num += i
        elif formula2num[-1] == '/':
            val = int(answer / int(temp_str))
            answer = val
            formula2num += temp_str
            temp_str = ''
            formula2num += i
        if i == '=':
            print(formula2num + temp_str)
            answer_str = ''
            for a in str(answer):
                if a == '-':
                    answer_str += '-'
                else:
                    answer_str += num2str[a]
            print(answer_str)
    else:
        temp += i
        if temp in str2num:
            temp_str += str(str2num[temp])
            temp = ''