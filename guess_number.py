# Guess Number Higher or Lower

# 1. Computer picks a number from 1 to 100. The User has to guess which number it picked.
# 2. Every time you guess wrong, the program tells you whether the number is higher or lower.
#    Messages:
#    - My number is lower
#    - My number is higher
#    - Congrats! You got it!
# 3. At the end of the game program inform the User how many guesses he's done:
#    Message:
#    - You guessed the number on the 8 try
# 4. User has just 10 tries to guess the number, otherwise he got a message:
#    - Oops! You lose this game.

print('-' * 60)
print('Guess Number Higher or Lower'.center(60, ' '))
print('Pick the number from 1 to 100. You have just 10th tries'.center(
    60, ' '))
print('-' * 60)

#Your code here
import random
r = random.randint(1, 100)
guess = int(input('Enter your guess:'))
count = 1
print(r)
for i in range(9):
    if guess == r:
        print('Congrats! You got it!')
        print(f'You guessed the number on the {count} try')
        break
    elif guess < r:
        print('My number is higher')
        guess = int(input('Enter your guess:'))
        count += 1
    elif guess > r:
        print('My number is lower')
        guess = int(input('Enter your guess:'))
        count += 1
else:
    print('-' * 60)
    print('Oops! You lose this game.')
    print('-' * 60)


# while guess != r:
#     guess = int(input('Enter your guess:'))
#     if r > guess:
#         print('число больше')
#     elif r < guess:
#         print('число меньше', t)
#         t =+ 1
#     elif guess == r:
#         print('ті угадал')
#     else:
#         print('ты проиграл')

#рандомный номер

# guess = int(input('Enter your guess:'))