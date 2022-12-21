# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

print('Enter an integer: ', end='')
num = int(input())
number_list = []
f = 1
if num < 0:
    print('Factorial does not exist for negative numbers')
elif num == 0:
    print('The factorial of 0 is 1')
else:
    for i in range(2, num + 1):
        f = f * i
        number_list.append(f)
print(number_list)
