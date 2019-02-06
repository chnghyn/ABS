spam = 42  # global variable


def eggs():
    spam = 42  # local variable


print('Some code here.')
print('Some more code.')


def spam():
    global eggs
#    eggs = 99
    bacon()
    print(eggs)


eggs = 42


def bacon():
    ham = 101
    eggs = 0


spam()

