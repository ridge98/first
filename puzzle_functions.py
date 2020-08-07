""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them.

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.

P1 = 'player one'
P2 = 'player two'
def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """
    if player_one_turn is True:
      return P1
    else:
      return P2

P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'
def get_winner(player_one_score: int, player_two_score: int) -> str:
    """Return 'player one wins' when player_one_score > player_two_score; 
    return 'player two wins' when player_one_score < player_two_score; 
    otherwise, return 'tie game' when player_one_score == player_two_score.
    
    >>> get_winner(10,9)
    P1_WINS
    >>> get_winner(9,10)
    P2_WINS
    >>> get_winner(10,10)
    TIE
    """
    
    if player_one_score > player_two_score:
      return P1_WINS
    elif player_one_score < player_two_score:
      return P2_WINS
    else:
      return TIE

def reverse(string: str) -> str:
    """Return a reverse order of message

    >>> reverse('cat')
    'tac'
    >>> reverse('dog')
    'god'
    """
    
    return string[::-1]

def get_row(puzzle: str, row_num: int) -> str:
    """Return row row_num of puzzle.

    Precondition: 0 <= row_num and row_num < number of rows in puzzle
    
    >>> get_row('a\nb\nc\n',1)
    'b'
    >>> get_row('d\ne\nf\n',2)
    'f'
    >>> get_row('defefefef\neefefefef\nfaeadfadf\nasdf',3)
    'asdf'
    """
    p = puzzle
    letter_n = 1
    actual_row_length = get_row_length(puzzle) + letter_n
    start_row_letter = actual_row_length * row_num
    end_row_letter = start_row_letter + actual_row_length - letter_n
    return p[start_row_letter:end_row_letter]

UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4
def get_factor(direction: str) -> int:
    """Return the multiplicative factors according to this direction 
    and direction factor
    
    >>> get_factor(UP)
    4
    >>> get_factor(DOWN)
    2
    >>> get_factor(FORWARD)
    1
    >>> get_factor(BACKWARD)
    3
    """
    if direction == UP:
        return UP_FACTOR
    elif direction == DOWN:
        return DOWN_FACTOR 
    elif direction == FORWARD:
        return FORWARD_FACTOR
    else:
        return BACKWARD_FACTOR
 

def get_points(direction: str, num_letters_left: int) -> int:
    """Return the points that we can find in this direction
    in terms of the point rule it provided.
    
    Precondition: num_letters_left >= 0, points >= 0.
    
    >>> get_points(UP,5)
    20
    >>> get_points(DOWN,3)
    14
    >>> get_points(FORWARD,1)
    21
    >>> get_points(BACKWARD,5)
    15
    """
    if num_letters_left >= THRESHOLD and num_letters_left >= 2:
            result = THRESHOLD * get_factor(direction)
    elif num_letters_left < THRESHOLD and THRESHOLD >= 2:
            result = ((2 * THRESHOLD) - 
                      num_letters_left) * get_factor(direction)
            if num_letters_left == 1:
                result = ((2 * THRESHOLD) - 
                      num_letters_left) * get_factor(direction) + BONUS
    elif num_letters_left == 1 and THRESHOLD == 1:
            result = ((2 * THRESHOLD) - 
                      num_letters_left) * get_factor(direction) + BONUS
    return result

def check_guess(puzzle: str, direction: str, guessed_word: str,
                row_col_num: int, num_letters_left: int) -> int:
    """Return the points earned for this guessed word at the chose 
    location in terms of row or column and direction;
    otherwise, result 0
    
    >>> check_guess('cat\nber\ncdf\ncar', FORWARD, 'cat', 0, 1)
    21
    >>> check_guess('canp\nabca\npabn\ncaro', DOWN, 'cap', 0, 3)
    14
    """
    
    if direction == UP:
        if contains(reverse(get_column(puzzle, row_col_num)),guessed_word):
            result = get_points(direction, num_letters_left)
        else:
            return 0             
    if direction == DOWN:
        if get_column(puzzle, row_col_num):
            if contains(get_column(puzzle, row_col_num),guessed_word):
                result = get_points(direction, num_letters_left)
            else:
                result = 0             
    if direction == FORWARD:
        if get_row(puzzle, row_col_num):
            if contains(get_row(puzzle, row_col_num),guessed_word):
                result = get_points(direction, num_letters_left) 
            else:
                result = 0             
    if direction == BACKWARD:
        if contains(reverse(get_row(puzzle, row_col_num)),guessed_word):
            result = get_points(direction, num_letters_left) 
        else:
            result = 0     
    return result
   
