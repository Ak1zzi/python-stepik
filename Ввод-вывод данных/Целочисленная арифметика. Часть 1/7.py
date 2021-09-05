# Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с клавиатуры.

a, b = int(input()), int(input())
c = a+b
d = a-b
e = a*b
print(
    a, '+', b, '=', c
)
print(
    a, '-', b, '=', d
)
print(
    a, '*', b, '=', e
)

# a, b = int(input()), int(input())
# print(f"{a} + {b} = {a + b}", f"{a} - {b} = {a - b}", f"{a} * {b} = {a * b}", sep='\n')