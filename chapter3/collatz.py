# 하나의 number라는 이름의 매개변수를 가지는 collatz()함수를 만든다.
def collatz(number):
    # 짝수라면 number // 2를 출력
    if number % 2 == 0:
        return number // 2

    # 홀수라면 3 * number + 1을 출력
    else:
        return 3 * number + 1


while True:
    try:
        number = int(input())
    except ValueError:
        print('정수를 입력하세요.')
        break

    while True:
        if collatz(number) == 1:
            break
        else:
            number = collatz(number)
            print(collatz(number))