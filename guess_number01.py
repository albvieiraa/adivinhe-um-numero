import random
def guess(x):
    random_number = random.randint(1, x) #retorna um número aleatório para adivinharmos
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if guess < random_number:
            print('Desculpe, adivinhe novamente. Muito baixo!')
        elif guess > random_number:
            print('Desculpe, adivinhe novamente. Muito alto!')
    
    print('Parabéns, você adivinhou! O número secreto é {}'.format(random_number))

guess(10)