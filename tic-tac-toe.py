import pprint

board = {"top-l": ' ', "top-m": ' ', "top-r": ' ',
         "mid-l": ' ', "mid-m": ' ', "mid-r": ' ',
         "low-l": ' ', "low-m": ' ', "low-r": ' '
         }

# pprint.pprint(board)
print("\n")
p1 = input("What's yours P1' ? X|O ?: ")
p2 = ""

while True:
    
    if p1 != "X" and p1 != "O":
        print("Please try again...! \n")

    else:

        if p1 == "O":
            p2 = "X"
        
        else:
            p2 = "O"

        print(f'\nPlayer p1 has \'{p1}\'')
        print(f'Player p2 has \'{p2}\'\n')

        move = True

        if move == True:
            print(f'Your move P1 ( Follow the rules..! )')
            print(f'top-, mid-, low- & l,m,r\n')
            pmove = input("What's your move? P1: ")

        else:
            print(f'Your move P2 ( Follow the rules..! )')
            print(f'top-, mid-, low- & l,m,r\n')
            pmove = input("What's your move? P1: ")

        move = False

        if pmove == "top-l":
            board['top-l'] = p1

        if pmove == "top-m":
            board['top-m'] = p1

        print("\n")
        print(f'{board["top-l"]} | {board["top-m"]} | {board["top-r"]}')
        print(f'⎯   ⎯   ⎯')    
        print(f'{board["mid-l"]} | {board["mid-m"]} | {board["mid-r"]}')
        print(f'⎯   ⎯   ⎯')
        print(f'{board["low-l"]} | {board["low-m"]} | {board["low-r"]}\n')

        # break
    