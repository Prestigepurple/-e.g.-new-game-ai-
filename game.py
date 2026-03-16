def main_menu():
    print("Welcome to Chutes & Ladders Trail!")
    print("1. Start New Journey")
    print("2. Load Saved Game")
    print("3. Instructions")
    print("4. Name Your Companion")
    print("5. Quit")
    choice = input("Choose an option: ")
    return choice


def instructions():
    print("\nInstructions:")
    print("Travel across the board from start to finish.")
    print("Watch out for chutes that send you backward and ladders that advance you forward.")
    print("Manage supplies and make choices along the way just like in Oregon Trail, but with a Chutes & Ladders twist!\n")
    input("Press Enter to return to the main menu...")


import random

# Your loyal companion who travels with you on the trail
companion_name = "Buddy"


def start_new_game():
    print("Starting a new Chutes & Ladders adventure...")
    print(f"{companion_name} is trekking by your side as you set out.")
    # simple board setup with chutes (down) and ladders (up)
    chutes_and_ladders = {
        # original 100-square board entries
        1: 38, 4: 14, 9: 31, 16: 6, 21: 42, 28: 84,
        36: 44, 47: 26, 49: 11, 51: 67, 56: 53, 62: 19,
        64: 60, 71: 91, 80: 100, 87: 24, 93: 73, 95: 75,
        98: 78,
        # additional squares for extended 150-board
        102: 122, 107: 90, 113: 137, 119: 99, 125: 145,
        132: 116, 140: 150, 148: 128
    }
    position = 0
    board_size = 150
    while position < board_size:
        input("Press Enter to roll the die...")
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}.")
        if position + roll > board_size:
            print("You need an exact roll to reach the end. Try again next turn.")
        else:
            position += roll
            print(f"You move to square {position}.")
            print(f"{companion_name} cheers you on as you move forward.")
            # special event: bridge over lava pit at 50
            if position == 50:
                print("You've reached the rickety bridge over a bubbling lava pit!")
                cross = input("Do you cross it? (y/n) ")
                if cross.lower() == 'y':
                    # 40% chance to fall
                    if random.random() < 0.4:
                        print("Oh no! The bridge collapses and you fall into lava!")
                        position = 1
                        print("You scramble back to the trail start at square 1.")
                    else:
                        print("You carefully cross the bridge safely.")
                else:
                    print("You decide not to risk the bridge and stay put.")
            # check for chute or ladder
            if position in chutes_and_ladders:
                new_pos = chutes_and_ladders[position]
                if new_pos > position:
                    print(f"A ladder! Climb up to {new_pos}.")
                else:
                    print(f"Oh no, a chute! Slide down to {new_pos}.")
                position = new_pos
            if position == board_size:
                print(f"Congratulations! You and {companion_name} have reached the end of the trail!")
                break
    input("Game over. Press Enter to return to the main menu...")


def load_game():
    print("Loading saved game...")
    # placeholder for loading logic


def name_companion():
    global companion_name
    new_name = input("What would you like to name your companion? ").strip()
    if new_name:
        companion_name = new_name
        print(f"Your companion is now named {companion_name}.")
    else:
        print("Companion name unchanged.")


def quit_game():
    print("Thanks for playing! Goodbye.")


def run():
    while True:
        choice = main_menu()
        if choice == '1':
            start_new_game()
        elif choice == '2':
            load_game()
        elif choice == '3':
            instructions()
        elif choice == '4':
            name_companion()
        elif choice == '5':
            quit_game()
            break
        else:
            print("Invalid selection, please try again.")


if __name__ == '__main__':
    run()
