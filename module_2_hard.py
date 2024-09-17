n = int(input('Введите число от 3 до 20: ', ))
while n < 3 or n > 20:
    print('Число не подходит, повторте ввод')
    n = int(input('Введите число от 3 до 20: ', ))
result = ''
for i in range(1,n):
    for j in range (1,n):
        if n % (i+j) == 0 and j>i:
            result += str(i)+str(j)
print(result)
