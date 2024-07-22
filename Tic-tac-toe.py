import random

class Move:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def is_valid(self):
        return 1 <= self._value <= 9
    
    def get_row(self):
        if self._value in (1, 2, 3):
            return 0
        if self._value in (4, 5, 6):
            return 1
        if self._value in (7, 8, 9):
            return 2

    def get_column(self):
        if self._value in (1, 4, 7):
            return 0
        if self._value in (2, 5, 8):
            return 1
        if self._value in (3, 6, 9):
            return 2

class Player:

    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, is_human = True):
        self._is_human = is_human

        if is_human:
            self._marker = Player.PLAYER_MARKER 
        else:
            self._marker = Player.COMPUTER_MARKER 

    @property
    def is_human(self):
        return self._is_human
    
    @property
    def marker(self):
        return self._marker
    
    def get_move (self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
        
    def get_human_move(self):
        while True:
            user_input = int(input("Please enter your move (1-9): "))
            move = Move(user_input)
            if move.is_valid():
                break
            else: 
                print("Please enter an interger between 1 and 9")
        return move   

    def get_computer_move(self):
        random_choice = random.choice(range(1, 10))
        move = Move(random_choice)
        print("Computer move: ", move.value)
        return move

class Board:

    def __init__ (self):
        self.game_board = [[],[],[]]

    

        