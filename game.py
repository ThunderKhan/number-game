import random


def play_game():
	secret_number = random.randint(1, 10)
	attempts = 0

	print("I'm thinking of a number between 1 and 10.")

	while True:
		try:
			guess = int(input("Your guess: "))
		except ValueError:
			print("Please enter a whole number.")
			continue

		attempts += 1

		if guess < secret_number:
			print("Too low! Try again.")
		elif guess > secret_number:
			print("Too high! Try again.")
		else:
			print(f"Correct! You guessed it in {attempts} attempt(s).")
			break


if __name__ == "__main__":
	play_game()
