import random

print('Tossing a coin...')
print('Who are you?')
val = str(input())
print(f'Hello, {val}!')


coin_flip = ['heads', 'tails']

head_num = 0
tails_num = 0

head = random.randint(1,2)
tails = random.randint(1,2)

for i in range(0, 3):
    result = random.choice(coin_flip)
    if result == 'heads':
      head_num+=1;
    else:
      tails_num+=1;
    print(f'Round 1: {result}')


print(f'Heads: {head_num}')
print(f'Tails: {tails_num}')

if head_num > tails_num:
  print(f'{val} won!')
else:
  print(f'{val} lost!')
