# This program says hello and asks for my name.
# 이 프로그램은 인사를 하고 내 이름을 묻는 프로그램이다.

print('Hello world!')
print('What is your name? ')  # ask for their name 그들의 이름을 묻는다
myName = input()
print('It is good to meet you, ' + myName)  # 내게 인사한다
print('THe length of your name is:')
print(len(myName))
print('What is your age? ')  # ask for their age 그들의 나이를 묻는다
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')  # 일 년 후에 몇 살이 될거라고 말한다

# print(): 전달하는 문자열을 화면에 표시한다.
# input(): 사용자가 키보드로 텍스트를 입력하고 Enter 키를 누를 때까지 기다린다.
# len(): 문자열을 전달할 수 있고, 문자열의 문자 개수를 정수 형식으로 리턴한다.
# str(): 전달되는 값을 문자열 형식으로 리턴한다.
# int(): 전달되는 값을 정수 형식으로 리턴한다.
# float(): 전달되는 값을 부동 소수점 형식으로 리턴한다.
