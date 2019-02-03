print('What is your name?')
name = input()
print('Hi, ' + name + '. How old are you?')
age = input()
print('You are ' + str(int(age)) + ' years old.')

if name == 'Alice':
    print('Hi, Alice.')
elif int(age) < 12:
    print('You are not Alice, kiddo.')
elif int(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif int(age) > 100:
    print('You are not Alice, grannie.')
else:
    print(int(age) <= 100)


