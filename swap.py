x = input()
y = input()
print('The value of x is {}'.format(x))
print('The value of y is {}'.format(y))
temp_var = x
x = y
y = temp_var
print('edited by sneha')
print('The value of x after swapping is {}'.format(x))
print('The value of y after swapping is {}'.format(y))
x=x+y
y=x-y
x=x-y
print(x)
print(y)
