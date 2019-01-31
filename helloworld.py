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
