# Напишите программу вычисления значения функции f(a,b) =3(a + b)^3 + 275b^2 − 127a − 41
# по введеным целым значениям a и b.

a = int(input())
b = int(input())
f = 3*((a+b)*(a+b)*(a+b))+275*(b*b)-127*a-41
print(f)

# Способ со звездочками
# a = int(input())
# b = int(input())
# f = 3*(a+b)**3+275*b**2-127*a-41
# print(f)