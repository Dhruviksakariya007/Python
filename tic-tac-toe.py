import pprint

board = {"top-l": ' ', "top-m": ' ', "top-r": ' ',
         "mid-l": ' ', "mid-m": ' ', "mid-r": ' ',
         "low-l": ' ', "low-m": ' ', "low-r": ' '
         }

# pprint.pprint(board)
print("\n")
p1 = input("What's yours P1' ? X|O ?: ")
p2 = ""

def ttt(player):
        
        print(f'\nPlayer p1 has \'{p1}\'')
        print(f'Player p2 has \'{p2}\'\n')

        print(f'Please follow the rules..! ')
        print(f'top-, mid-, low- & l,m,r\n')
        move = input(f"What's next move?{player}: ")

        if move == "top-l":
            board['top-l'] = player

        elif move == "top-m":
            board['top-m'] = player

        elif move == "top-r":
            board['top-r'] = player

        elif move == "mid-r":
            board['mid-r'] = player

        elif move == "mid-m":
            board['mid-m'] = player

        elif move == "mid-l":
            board['mid-l'] = player

        elif move == "low-l":
            board['low-l'] = player

        elif move == "low-m":
            board['low-m'] = player

        elif move == "low-r":
            board['low-r'] = player

        else: 
            print(f'Your move is wrong so you have to pay Penalty...!  ')

        print("\n")
        print(f'{board["top-l"]} | {board["top-m"]} | {board["top-r"]}')
        print(f'⎯   ⎯   ⎯')    
        print(f'{board["mid-l"]} | {board["mid-m"]} | {board["mid-r"]}')
        print(f'⎯   ⎯   ⎯')
        print(f'{board["low-l"]} | {board["low-m"]} | {board["low-r"]}\n')

while True:
    
    if p1 != "X" and p1 != "O":
        print("Please try again...! \n")

    else:

        if p1 == "O":
            p2 = "X"
        
        else:
            p2 = "O"


        ttt(p1)
        ttt(p2)