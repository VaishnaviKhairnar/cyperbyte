import random

def generate_number():
    return random.randint(1000, 9999)

def check_guess(secret_number, guess):
    secret_digits = [int(d) for d in str(secret_number)]
    guess_digits = [int(d) for d in str(guess)]
    
    correct_digits = sum(a == b for a, b in zip(secret_digits, guess_digits))
    
    return correct_digits

def play_game(player1, player2):
    print(f"{player1}, please set a 4-digit number for Player 2 to guess.")
    secret_number = int(input("Enter your secret number: "))
    
    attempts_player2 = 0
    while True:
        guess = int(input(f"{player2}, make your guess: "))
        attempts_player2 += 1
        
        if guess == secret_number:
            print(f"Congratulations, {player2}! You guessed the number in {attempts_player2} attempts.")
            return player2
        
        correct_digits = check_guess(secret_number, guess)
        print(f"Correct digits: {correct_digits}")

def main():
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    
    print(f"\n{player1}, you are up first!")
    winner_player1 = play_game(player1, player2)
    
    print(f"\n{player2}, it's your turn now!")
    winner_player2 = play_game(player2, player1)
    
    if winner_player1 is None and winner_player2 is None:
        print("It's a tie!")
    elif winner_player1 is None:
        print(f"Congratulations, {player2}! You are crowned Mastermind!")
    elif winner_player2 is None:
        print(f"Congratulations, {player1}! You are crowned Mastermind!")
    else:
        if winner_player1 == winner_player2:
            print(f"It's a tie! Both {winner_player1} and {winner_player2} are Masterminds!")
        elif winner_player1 == player1:
            print(f"Congratulations, {player1}! You are crowned Mastermind!")
        else:
            print(f"Congratulations, {player2}! You are crowned Mastermind!")

if __name__ == "__main__":
    main()
