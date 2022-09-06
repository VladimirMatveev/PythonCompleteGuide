# Let's play Paper Rock Scissors. The two players take turns making their choice.
# After they have played three times, the game ends and the winner is declared.

#Messages:
#"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
#"Player 1 wins this round!"
#"It's a draw"
#"Player 2 wins this game!"

#Players can input just numbers from 0 to 2, otherwise throw the message:
#"You typed an invalid number. Try again"

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def scissors_v():
    print(scissors)

def rock_v():
    print(rock)

def paper_v():
    print(paper)

def start():
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    player1 = int(input('Player 1: '))
    player2 = int(input('Player 2: '))
    return player1, player2

def play(player1, player2):
    if player1 == 0:
        rock_v()
    if player1 == 1:
        paper_v()
    if player1 == 2:
        scissors_v()
    else:
        print('------------------------|')

    if player2 == 0:
        rock_v()
    if player2 == 1:
        paper_v()
    if player2 == 2:
        scissors_v()
    else:
        print('-------------------------')

#  r0 > s2 > p1
#  s2 > p1 > r0

def defin_winner(player1, player2, score):
    if (player1 == 0 and player2 == 2) or (player1 == 2 and player2 == 1) or (player1 == 2 and player2 == 1) or (player1 == 1 and player2 == 0):
        print('player 1 win')
        score['player1'] += 1
    elif (player2 == 0 and player1 == 2) or (player2 == 2 and player1 == 1) or (player2 == 2 and player1 == 1) or (player2 == 1 and player1 == 0):
        print('player 2 win')
        score['player2'] += 1
    else:
        print('OK')
 

score = {'player1': 0, 'player2': 0}
for i in range(3):

    player1, player2 = start()
    play(player1, player2)
    print(player1, player2)
    defin_winner(player1, player2, score)

if score['player1'] > score['player2']:
    print('player 1 win this game')
else:
    print('player 2 win this game')