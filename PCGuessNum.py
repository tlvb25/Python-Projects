import random
import time


def computer_guess():
    print('I the computer will try to guess your secret number!', end=" ")

    print('\n')
    time.sleep(3)
    secret = int(input('please enter a secret number between 1 and 10: '))
    low = 0
    answer = ""
    pc_guess = random.randint(low, secret)
    time.sleep(3)

    print(f'was your secret number {pc_guess}?', end=" ")
    answer = input()

    while answer == 'no':
        pc_guess = pc_guess = random.randint(low, secret)
        print(f'was your secret number {pc_guess}?', end=" ")
        answer = input()
    print('Yah, I guessed your number!')


computer_guess()
