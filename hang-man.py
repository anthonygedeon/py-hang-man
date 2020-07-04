import copy

stick_man = [

    '''
    ________
    |       |
    |
    |
    |
    |__________
    ''',

    '''
    ________
    |       |
    |       O
    |
    |
    |__________
    ''',

    '''
    ________
    |       |
    |       O
    |       |
    |
    |__________
    ''',

    '''
    ________
    |       |
    |       O
    |       |\\
    |
    |__________
    ''',

    '''
    ________
    |       |
    |       O
    |      /|\\
    |
    |__________
    ''',

    '''
    ________
    |       |
    |       O
    |      /|\\
    |      /
    |__________
    ''',

    '''
    ________
    |       |
    |       O
    |      /|\\
    |      / \\
    |__________
    ''']


word = input('Please enter your secret word: ')
characters = list(word)
wrong_letters = []
loop = True
points = 0

def hide_word():
    """Loops through the character list and replaces each letter with an * """
    copied_word = copy.copy(characters)

    for index, letter in enumerate(copied_word):
        copied_word[index] = '*'

    return copied_word

hidden_characters = hide_word()
guess_word = [characters, hidden_characters] # [ ['h', 'a', 'n', 'g', 'm', 'a', 'n'], ['*', '*', '*', '*', '*', '*', '*'] ]

def get_letter_matches(player_answer):
    """
        Check if player input matches any of letters in the given word
        and returns the position and duplicates of that letter
    """
    word = guess_word[0] # ['h', 'a', 'n', 'g', 'm', 'a', 'n']

    indexes = [index for index in range(len(word)) if word[index] == player_answer] # Don't know exactly what this code does
    letter_indexes = { player_answer: indexes }

    return letter_indexes # {'a': [1, 5]}

def reveal_letters(dict, player_answer):
    """
        Takes the player input and if the letter matches the word then it will
        unhidden the letter in the guess_word list
    """
    hidden_word = guess_word[1]

    for index in dict[player_answer]:
        hidden_word[index] = player_answer

    return ''.join(hidden_word) # dict[player_answer] -> [1, 5]

def print_stick_board(number):
    """Print the right stick man board"""

    length = len(number)
    print(stick_man[length])

def get_incorrect_letters(player_answer):
    """Tally up all the incorrect words"""
    word = guess_word[0]

    if player_answer not in word:
        wrong_letters.append(player_answer)

    return wrong_letters

def get_point(letter):
    """Give player 100 points for getting the correct letter"""
    global points
    if letter in characters:
        points += 100
        print('Points earned: {}'.format(points))
    else:
        print('Points earned: {}'.format(points))

def is_winner(complete_word, secret_word):
    """Determine the winner and loser"""
    global loop

    if secret_word == complete_word:
        print('You Won!')
        loop = False


def game_loop():

    while loop:

        print('__________________________________________________')
        player_letter = input('Choose a letter: ')

        hidden = reveal_letters( get_letter_matches( player_letter ), player_letter )
        incorrect_letters = get_incorrect_letters( player_letter )

        print('Your word looks like this:\n{}'.format( hidden ))

        try:
            print_stick_board( incorrect_letters )
        except IndexError:
            print('You Lost!')
            break

        get_point(player_letter)
        print('You\'ve entered (wrong): {}'.format( incorrect_letters ))
        is_winner(''.join(guess_word[0]), hidden)


game_loop()
