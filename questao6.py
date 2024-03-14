print('Tabuada de 1 a 10\n-----------------')
num = int(input('Qual Tabuada Deseja Ver?: '))


if 1 <= num <= 10:
    tabuada = 0
    print('__________________')
    for x in range (1,10):
        tabuada += 1
        result = num * tabuada
        print(f'{num} x {tabuada} = {result}')
    print('__________________')
else:
    print('-------------------\nApenas Números de 1 a 10 Serão Mostrados')
