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


word = 'hangman'
characters = list(word)
wrong_letters = []
loop = True


def hide_word(): # replace each letter with a *

    copied_word = copy.copy(characters)

    for index, letter in enumerate(copied_word):
        copied_word[index] = '*'

    return copied_word

hidden_characters = hide_word()
guess_word = [characters, hidden_characters]
# [ ['h', 'a', 'n', 'g', 'm', 'a', 'n'], ['*', '*', '*', '*', '*', '*', '*'] ]



def get_letter_matches(player_answer):
    # Player answer will be a single alphabet letter
    word = guess_word[0] # ['h', 'a', 'n', 'g', 'm', 'a', 'n']

    indexes = [index for index in range(len(word)) if word[index] == player_answer] # Don't know exactly what this code does
    letter_indexes = { player_answer: indexes }

    return letter_indexes # {'a': [1, 5]}



def reveal_letters(dict, player_answer):
    hidden_word = guess_word[1]

    for index in dict[player_answer]:
        hidden_word[index] = player_answer

    return ''.join(hidden_word)

    # dict[player_answer] -> [1, 5]



def print_stick_board(number):
    length = len(number)
    print(stick_man[length])



def get_incorrect_letters(player_answer):
    word = guess_word[0]

    if player_answer not in word:
        wrong_letters.append(player_answer)

    return wrong_letters



# def is_winner(asterisk):
#     if asterisk == guess_word[0]:
#         print('You Won!')
#     else:
#         print('You Lost :(')
#

#def get_point():



def game_loop():

    while loop:

        player_letter = input('Choose a letter: ')

        hidden = reveal_letters( get_letter_matches( player_letter ), player_letter )
        incorrect_letters = get_incorrect_letters( player_letter )

        print('Your word looks like this:\n{}'.format( hidden ))

        print_stick_board( incorrect_letters )

        print('You\'ve entered (wrong): {}'.format( incorrect_letters ))

    #is_winner(hidden)


game_loop()
