def generate_lucky_numbers(current_str, a, b, answer):
    # 현재 숫자가 범위 내에 있는지 확인
    if a <= int(current_str) <= b:
        answer.append(current_str)
    
    # 자리수에 맞춰 재귀적으로 '4', '7'을 추가
    if len(current_str) < len(str(b)):
        generate_lucky_numbers(current_str + '4', a, b, answer)
        generate_lucky_numbers(current_str + '7', a, b, answer)

def main():
    a, b = map(int, input().split())
    answer = []

    # 초기 숫자 생성 시작
    generate_lucky_numbers('4', a, b, answer)
    generate_lucky_numbers('7', a, b, answer)

    # 생성된 숫자 출력 및 카운트
    print(len(answer))

if __name__ == "__main__":
    main()