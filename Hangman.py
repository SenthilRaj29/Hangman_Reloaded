import random

words = [
    "array", "asset", "bench", "board", "bytes", "cache", "class", "click", "cloud", "cable",
    "chips", "cores", "debug", "delay", "digit", "drive", "email", "enter", "error", "excel",
    "field", "files", "float", "frame", "graph", "group", "hertz", "input", "laser", "layer",
    "logic", "model", "modem", "motor", "nodes", "pixel", "print", "probe", "proxy", "query",
    "ramps", "robot", "rocks", "relay", "rails", "scope", "scale", "speed", "stack", "servo",
    "solid", "steel", "shell", "spice", "tools", "trace", "value", "vapor", "vlogs", "volts",
    "wires", "welds", "wheel", "zeros", "zener", "apple", "brave", "charm", "doubt", "eagle",
    "flame", "grape", "ideal", "jolly", "lemon", "mango", "nerdy", "ocean", "piano", "quake",
    "risky", "smile", "table", "uncle", "vivid", "witty", "yeast", "zebra", "stone", "thing",
    "urban", "trust", "event", "knife", "tools", "hacks", "codes", "logic", "array", "stack",
    "index", "error", "float", "queue", "print", "build", "trace", "admin", "bytes", "query"
]

hangman_art = [
    """
     _______
    |       |
    |       
    |       
    |       
    |       
    |_______|
    """,
    """
     _______
    |       |
    |      ( )
    |       
    |       
    |       
    |_______|
    """,
    """
     _______
    |       |
    |      ( )
    |       |
    |       |
    |       
    |_______|
    """,
    """
     _______
    |       |
    |      ( )
    |      /|
    |       |
    |       
    |_______|
    """,
    """
     _______
    |       |
    |      ( )
    |      /|\\
    |       |
    |       
    |_______|
    """,
    """
     _______
    |       |
    |      ( )
    |      /|\\
    |       |
    |      / 
    |_______|
    """,
    """
     _______
    |       |
    |      ( )
    |      /|\\
    |       |
    |      / \\
    |_______|
    """
]

def play_game():
    secret_word = random.choice(words)
    display = ["_"] * len(secret_word)
    guessed = []
    lives = 6

    print("\n🎮 Welcome to HANGMAN - ENGINEERING EDITION!")
    print("Guess the **5-letter** word before the stickman dies!\n")

    while lives > 0 and "_" in display:
        print(hangman_art[6 - lives])
        print("Word:  ", " ".join(display))
        print("Guessed:", ", ".join(guessed))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Enter only a single letter.\n")
            continue

        if guess in guessed:
            print("⚠️ Already guessed that.\n")
            continue

        guessed.append(guess)

        if guess in secret_word:
            print("✅ Correct!\n")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display[i] = guess
        else:
            lives -= 1
            print(f"❌ Wrong! {lives} lives left.\n")

    print(hangman_art[6 - lives])
    if "_" not in display:
        print("🎉 You saved the stickman!")
        print("✔️  The word was:", secret_word)
    else:
        print("💀 You killed the stickman!")
        print("☠️  The word was:", secret_word)

    again = input("\n🔁 Wanna play again? (yes/no): ").lower()
    if again == "yes":
        play_game()
    else:
        print("\n👋 Bye JD! Stickman salutes you 🫡")

play_game()
