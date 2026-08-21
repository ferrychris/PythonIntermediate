import random
import questionary
from dbconnect import *

COLORS      = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "black", "white"]
CODE_LENGTH = 4      # how many colours the secret code has
MAX_ATTEMPTS = 5     # how many guesses the player gets
POINTS_PER_HIT = 2  # points for each correct colour in the right position


def generate_code():
    """Randomly pick CODE_LENGTH colours to form the secret code."""
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]


def options():
    choice = questionary.select(
        "What do you want to do?",
        choices=[
            "Play Game",
            "Display Leaderboard",
            "Update users",
            "Delete Users",
            "Exit"
        ]
    ).ask()
    if choice == "Play Game":
        guess_code()
    elif choice == "Display Leaderboard":
        display_leaderboard()
    elif choice == "Update users":
        update_users()
    elif choice == "Delete Users":
        delete_users()
    elif choice == "Exit":
        exit


def display_leaderboard():
    get_leaderboard()


def score_guess(secret, guess):
    """Return how many positions match exactly."""
    return sum(s == g for s, g in zip(secret, guess))


def guess_code():
    print("=" * 50)
    print(f"Guess {CODE_LENGTH} colours. You have {MAX_ATTEMPTS} attempts.")
    print(f"Min 8 points wins you $12,000!")
    print(f"Valid colours: {', '.join(COLORS)}")
    print("=" * 50)

    # Ask if player is ready
    choice = questionary.select(
        "Are You Ready?",
        choices=["True", "False"]
    ).ask()

    if choice == "False":
        print("Thanks for checking out — see you next time!")
        return

    # Get player name to save to database
    player_name = input("Enter your name: ").strip() or "Anonymous"

    # Generate secret code
    secret = generate_code()
    total_points = 0
    won = False

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"\n── Attempt {attempt}/{MAX_ATTEMPTS} ──")
        raw = input(f"Enter {CODE_LENGTH} colours separated by spaces: ").lower().split()

        # Validate input length
        if len(raw) != CODE_LENGTH:
            print(f"Please enter exactly {CODE_LENGTH} colours. Try again.")
            continue

        # Check each colour is valid
        invalid = [c for c in raw if c not in COLORS]
        if invalid:
            print(f"Unknown colour(s): {invalid}. Try again.")
            continue

        hits = score_guess(secret, raw)
        points_this_round = hits * POINTS_PER_HIT
        total_points += points_this_round

        print(f"Correct positions: {hits}/{CODE_LENGTH}  (+{points_this_round} pts, total: {total_points})")

        if hits == CODE_LENGTH:
            print("\n🎉 You cracked the code! You WIN $12,000!")
            won = True
            break
    else:
        print(f"\nGame over! The secret code was: {secret}")

    print(f"\nFinal score: {total_points} pts")

    # ── Save result to database ──────────────────────────────────────────────
    save_result(player_name, total_points, won)
    
# ── Entry point ───────────────────────────────────────────────────────────────
guess_code()
options()