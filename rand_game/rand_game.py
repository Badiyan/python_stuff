import random

secret = random.randint(1, 100)
guess = -1
attempt = 1


while guess != secret:
    guess = input('Давай сыграем с тобой игру, угадай какое число я загадал, это твоя {} попытка. '.format(attempt))
    if guess:
        guess_number = int(guess)
    attempt += 1
    if guess_number < secret:
        print('Ха-ха,число БОЛЬШЕ, пробуй еще')
    else:
        print('Ха-ха,число МЕНЬШЕ, пробуй еще')
print('Верно! Количество использованных попыток: ', attempt)