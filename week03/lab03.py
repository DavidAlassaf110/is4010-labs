"""Lab 03: Mad Lib generator and number-guessing game."""

import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return (
        f"One morning a {adjective} {noun} woke up early, "
        f"{verb} straight past the kitchen, "
        f"and decided that today was going to be different."
    )


def guessing_game():
    """Run an interactive number-guessing game."""
    secret = random.randint(1, 100)

    print("I am thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))

        if guess < secret:
            print(f"{guess} is too low. Try again.")
        elif guess > secret:
            print(f"{guess} is too high. Try again.")
        else:
            print(f"Correct! The number was {secret}.")
            return
