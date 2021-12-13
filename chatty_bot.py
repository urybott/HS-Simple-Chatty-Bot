def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    q = "Why do we use methods?"
    ra = "2"
    c = ["To repeat a statement multiple times."]
    c.append("To decompose a program into several small subroutines.")
    c.append("To determine the execution time of a program.")
    c.append("To interrupt the execution of a program.")
    print(q)
    for i in range(len(c)):
        print(i + 1, c[i])
    a = ""
    while a != ra:
        a = input()
        if a != ra:
            print("Please, try again.")
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aibo', '2021')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
