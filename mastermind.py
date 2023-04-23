import random

# Setting the number of digits in the password and the maximum number of guesses
DIGITS = 4
MAX_GUESSES = 10

# Generate a random secret code
def generate_code():
    code = ''
    for i in range(DIGITS):
        code += str(random.randint(0, 9))
    return code

# Check the guess against the secret code
def check_guess(code, guess):
    exact = 0
    partial = 0
    for i in range(DIGITS):
        if code[i] == guess[i]:
            exact += 1
        elif guess[i] in code:
            partial += 1
    return (exact, partial)

# Main game loop
def play_game():
    print('MASTERMIND')
    print('')
    print('Guess the {}-digit code in {} tries or fewer.'.format(DIGITS, MAX_GUESSES))
    print('Digits range from 0 to 9.')
    print('')
    code = generate_code()
    guesses = 0
    while guesses < MAX_GUESSES:
        guess = input('Guess {}: '.format(guesses+1))
        if len(guess) != DIGITS:
            print('Invalid guess. Must be {} digits.'.format(DIGITS))
            continue
        if not guess.isdigit():
            print('Invalid guess. Must be all digits.')
            continue
        guesses += 1
        result = check_guess(code, guess)
        if result[0] == DIGITS:
            print('Congratulations! You guessed the code in {} tries.'.format(guesses))
            return
        else:
            print('Result: {} exact, {} partial.'.format(result[0], result[1]))
            print('')
    print('Sorry, you ran out of guesses. The secret code was {}.'.format(code))

# Start the game
play_game()
