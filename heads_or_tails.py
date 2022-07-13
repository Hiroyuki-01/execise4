import random

print('Who are you?')
val = str(input())
print(f'Hello, {val}!')


coin_flip = ['heads', 'tails']

for i in range(0, 3):
    result = random.choice(coin_flip)
    print(f'Round 1: {result}')


print(f'Heads: {random.randint(1,2)}')
print(f'Tails: {random.randint(1,2)}')
