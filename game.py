import random
from static import choose_symbol, clear_screen, game_style, who_goes_first

# Unchanging variables:
# OPPOSITION & HUMAN distinguishes two teams
# AVAIL, HUMAN, OPPOSITION all represent the 3 potential states of the position
AVAIL = 0
HUMAN = -1
OPPOSITION = 1

WIN_COMBOS = {'0': [0, 1, 2], '1': [3, 4, 5], '2': [6, 7, 8],
              '3': [0, 3, 6], '4': [1, 4, 7], '5': [2, 5, 8],
              '6': [0, 4, 8], '7': [2, 4, 6]}


class Game:
    """
    TIC-TAC-TOE game with multiple settings:
    1) Player vs Player or Computer
    2) Player chooses who goes first
    3) Player chooses symbol 'O' or 'X'

    This game cannot be beaten
    """

    def __init__(self):
        """variables to be used in game"""
        self.board = [AVAIL, AVAIL, AVAIL, AVAIL, AVAIL, AVAIL, AVAIL, AVAIL, AVAIL]
        self.board_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def space_left(self):
        """
        If spaces on board are left, game continues
        :return:
        Boolean
        """
        for space in self.board:
            if space == AVAIL:
                return True
        return False

    def get_human_spot(self):
        """
        Allows for user input, covers all incorrect input
        :return:
        position (positive int)
        """
        spot = None
        while spot is None:
            try:
                spot = abs(int(input("Enter a number [0-8]: ")))  # in case input is negative spot is wrapped in abs
                if self.board_nums[spot] != "X" and self.board_nums[spot] != "O":
                    if self.board_nums[spot]:
                        self.board[spot] = HUMAN
                else:
                    print("Hey, I'm walkin' here. Pick an available number: ")
                    spot = None
            except ValueError:
                print("That's not a number, try again:")
                spot = None
            except IndexError:
                print("You're off the board! Try again:")
                spot = None
        return spot

    def get_best_move(self):
        """
        Computers AI utilising Minimax Algorithm
        if multiple moves are viable, it will pick randomly
        :return:
        random position from selection of best moves
        """
        if self.board[4] == AVAIL:
            return 4

        best_value = -2  # less than HUMAN
        comp_moves = []

        for move in range(0, 9):
            if self.board[move] == AVAIL:
                self.board[move] = OPPOSITION
                value = self.board_evaluation(HUMAN, OPPOSITION, -2, 2)
                self.board[move] = AVAIL  # returns to AVAIL after setting a value
                if value > best_value:
                    best_value = value
                    comp_moves = [move]

                if value == best_value:
                    comp_moves.append(move)
        return random.choice(comp_moves)

    def board_evaluation(self, player, next_player, alpha, beta):
        """
        Minimax algorithm: evaluates potential strength of moves in terms of distance from a win
        :return:
        either max value or min value depending on player
        """
        winner = self.winner()
        if winner != AVAIL:  # if someone won
            return winner
        elif not self.space_left():  # if there is a tie
            return 0

        # Looking at all potential moves
        for move in range(0, 9):
            if self.board[move] == AVAIL:
                self.board[move] = player
                value = self.board_evaluation(next_player, player, alpha, beta)
                self.board[move] = AVAIL
                if player == OPPOSITION:  # if player is computer, maximise result
                    if value > alpha:
                        alpha = value
                    if alpha >= beta:
                        return beta
                else:
                    if value < beta:
                        beta = value
                    if beta <= alpha:
                        return alpha
        if player == OPPOSITION:
            return_value = alpha
        else:
            return_value = beta
        return return_value

    def winner(self):
        for combo in WIN_COMBOS.values():
            combo_sum = self.board[int(combo[0])] + self.board[int(combo[1])] + self.board[int(combo[2])]
            if combo_sum == 3 or combo_sum == -3:  # tokens 1 * 3 or -1 * 3
                return self.board[int(combo[0])]
        return 0

    def __str__(self):
        """
        prints representation
        replace __str__ method with a visual of the game
        """
        clear_screen()
        print("\nWelcome to the cocky TIC-TAC-TOE game\n=====================================\n")

        print("{} | {} | {} \n===+===+===\n"
              "{} | {} | {} \n===+===+===\n"
              "{} | {} | {} \n".format(
               self.board_nums[0], self.board_nums[1], self.board_nums[2],
               self.board_nums[3], self.board_nums[4], self.board_nums[5],
               self.board_nums[6], self.board_nums[7], self.board_nums[8]))

    def start_game(self):

        while self.space_left() and self.winner() == AVAIL:
            self.__str__()
            if list(range(0, 9)) == self.board_nums:
                player2 = game_style()
                next_move = who_goes_first()
                symbol = choose_symbol()
            else:
                if player2 is None:
                    # Computers messages to player
                    print("COMPUTER:", random.choice(["Okay, that's my move...",
                                                      "Did'nt see that coming, did you...",
                                                      "You serious? This is easy...", "Make my day...",
                                                      "Hit me with your best shot...",
                                                      "I was born for this?!...", "weak moves bro...",
                                                      "BAM, your move...", "Oh you fell into my trap...",
                                                      "You're not as good as the last player..."]), '\n')

            if next_move == HUMAN and self.space_left():  # If player is first and human...
                human_spot = self.get_human_spot()
                self.board[human_spot] = HUMAN
                self.board_nums[human_spot] = symbol[0]
                next_move = OPPOSITION
                clear_screen()
                self.__str__()

            if next_move == OPPOSITION and self.space_left():
                if player2:  # if player2(human)
                    human_spot = self.get_human_spot()
                    self.board[human_spot] = OPPOSITION
                    self.board_nums[human_spot] = symbol[1]
                    next_move = HUMAN
                    clear_screen()

                else:
                    opposition_spot = self.get_best_move()  # if player2(computer)
                    self.board[opposition_spot] = OPPOSITION
                    self.board_nums[opposition_spot] = symbol[1]
                    next_move = HUMAN

        self.__str__()
        print("GAME OVER! \n")

if __name__ == '__main__':
    Game().start_game()
