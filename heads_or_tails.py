import random

print('Tossing a coin...')
coin_flip = ['heads', 'tails']

head_num = 0
tails_num = 0

head = random.randint(1,2)
tails = random.randint(1,2)

for i in range(0, 3):
    result = random.choice(coin_flip)
    if result == head:
      head_num+=1;
    else:
      tails_num+=1;
    print(f'Round 1: {result}')


print(f'Heads: {head}')
print(f'Tails: {tails}')

if head*head_num > tails*tails_num:
  print("You won")
else
  print("You lost")
  
