# testing

# my project here


# some more stuff

import __main__


print("hello")

# test

Grid = []
Attempts = []
player_one_sunk_ships = []
player_two_sunk_ships = []
player_one_ship_coordinates = []
player_two_ship_coordinates = []
player_one_bomb_attempts = []
player_two_bomb_attempts = []

def initialise_board():
    return[["~"] * 12 for _ in range(8)]

def show_instructions():

    print("Welcome to Battleships on python terminal! ")
    print("Do you have what it takes to defeat your opponent? ")
    print("The rules are simple: ")
    print("Sink your opponents ships before they sink yours.")
    print(".                       You can choose where to place your ships on a 12 x 8 grid. ")
    print(".                       You will be able to place three ships, each with a length of one ")
    print(".                       coordinate. You can choose were to place your ships on the grid but")
    print("                        you can only them horizontally or vertically. ")
    print("The aim of the game is to sink your opposition’s ships before they sink yours.")
    print("You and your opponent will each have 1 turn to try and sink their opponent's ships.")
    print("You will be able to see your attempts to sink the opponent's ship.")
    print("If you have hit a part of your opponent's ship. The coordinate will display a yellow colour.")
    print("If you have sunk your opponent's ship, then the ship’s coordinates will be displayed in a red colour. ")
    print("")
    print("If you have missed completely, then the coordinates will display a blue colour.")
    print("The game is over when you or your opponent have no more ships floating.")
    print("If you would like to play again, then there will be an option to at the end.")
    print("That is all from me so happy battles! ")

board = ""
def select_ships():
    valid_selection_ships = []
    selection = False
    columns = "ABCDEFGHIJKL"
    
    while selection == False:
        selection = (input("Player 1 place your ships:"))
        for i in range(1, 9):
            if selection[0] in columns:  
                if i == int(selection[1]):
                
                    if len(selection) == 2:
                        print(f"You successfully placed a ship at, {selection}")
                        p1_selection = True
                        return selection
                    
        print("Invalid column/row/length of selection  please try again") # should this be repeated?


def place_ships(selection, board):
    ''' looks at the selection given by the player e.g. D4.  E7, K1 etc.
    and places ONE ship boat emoji INSIDE the board array at the correct position
    
    example D4 converts to [3][3] and then a emoji is placed at [3][3]'''

    ## here is a reminder of how to use arrays
    names = ["Isher", "Ishaan", "Xavier"]
    names[0] = "Fred"
    Boat_Emoji_p1 = "🚤"
    Boat_Emoji_p2 = "🛥️"
    
    # convert the string into integer

    # for example .... convert : D4 into 

    # just make sure you're aware board is a 2D list, not a 1D list

    return board         
           
# the if staement checks the first letter only but what if the column is 10 or more ?

                    



            





    pass


def display_board(board):
    pass


# terminal
#>>> 
#>>> print("isher\njohal")
#isher
#ohal
#>>> print("isher\tjohal")
#isher	johal
#>>> print("isher johal".center(50))
#                   isher johal                    
#>>> print("isher johal".rjust(50, "X"))
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXisher johal

def check_if_hit():
    pass


def tests():
    board = initialise_board()
    
    coordinate = select_ships()
    
    board = place_ships(coordinate, board)


if __name__ == "__main__":
    tests()
    # setup
    # show_instructions()
    # board = initialise_board()
    # display_board(board)
    # board = select_ships(board)
    # winner = False


    p1_selection = select_ships()
    p2_selection = select_ships()

    # while winner == False:
    #     # step 1
    #     x, y = choose_coordinates(board)
    #     # step 2
    #     check_if_hit() #     return... hit, sink,
        
    #     # step 3

    #     # step 4
    #     winner = check_if_boats_remain(board)
    #     print("hello")