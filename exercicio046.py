from time import sleep
print('Contagem regressiva de de {} a 0.'.format(10))
for i in range(10, 0, -1):
    sleep(1)
    print(i)
print('BOOM!')
