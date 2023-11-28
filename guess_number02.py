# O computador deve adivinhar qual o número
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'correto':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'O número {guess} é muito alto (A), muito baixo (B), ou correto (C)??').lower()
        if feedback == 'alto':
            high = guess - 1
        elif feedback == 'baixo':
            low = guess + 1
    
    print(f'Uhu! O computador adivinhou seu número {guess} corretamente')

computer_guess(10)