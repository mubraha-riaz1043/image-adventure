import time

def print_with_delay(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def ask_to_continue(prompt="Do you want to continue? (yes/no): "):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please type 'yes' or 'no'.")

def get_choice(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option['desc']}")
    while True:
        choice = input("Choose a number (1-5): ").strip()
        if choice in ['1','2','3','4','5']:
            return int(choice) - 1
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

adventure = {
    "stages": [
        {   # Stage 1
            "desc": "Stage 1: The Whispering Forest",
            "levels": [
                {
                    "desc": "You stand before a thick, misty forest. Five paths glimmer faintly:",
                    "choices": [
                        {"desc": "A path lined with glowing blue mushrooms."},
                        {"desc": "A narrow trail covered in fallen golden leaves."},
                        {"desc": "A muddy route where strange footprints appear."},
                        {"desc": "A rocky path echoing distant music."},
                        {"desc": "A shadowy passage filled with flickering lights."},
                    ],
                    "correct": 2,
                    "sublevels": [
                        {
                            "desc": "You follow the muddy route and reach a clearing with five ancient stones:",
                            "choices": [
                                {"desc": "Touch the stone covered in moss."},
                                {"desc": "Sit on the stone etched with runes."},
                                {"desc": "Inspect the cracked stone glowing faintly."},
                                {"desc": "Circle the stone with carvings of animals."},
                                {"desc": "Jump over the stone with strange markings."},
                            ],
                            "correct": 2,
                        },
                        {
                            "desc": "The glowing stone hums softly, revealing five glowing symbols hovering in air:",
                            "choices": [
                                {"desc": "Touch the symbol shaped like a star."},
                                {"desc": "Touch the symbol shaped like a crescent moon."},
                                {"desc": "Touch the symbol shaped like a flame."},
                                {"desc": "Touch the symbol shaped like a leaf."},
                                {"desc": "Touch the symbol shaped like a drop of water."},
                            ],
                            "correct": 0,
                        },
                        {
                            "desc": "A spirit appears and offers five gifts. Choose wisely:",
                            "choices": [
                                {"desc": "A silver dagger shimmering with runes."},
                                {"desc": "A cloak that shifts colors with the light."},
                                {"desc": "A small vial glowing with golden liquid."},
                                {"desc": "A leather-bound book of forgotten spells."},
                                {"desc": "A compass that points to hidden secrets."},
                            ],
                            "correct": 3,
                        },
                        {
                            "desc": "You find a hidden door carved into a giant tree. It has five locks:",
                            "choices": [
                                {"desc": "Unlock with a key shaped like a sun."},
                                {"desc": "Unlock with a key shaped like a tree."},
                                {"desc": "Unlock with a key shaped like a flame."},
                                {"desc": "Unlock with a key shaped like a moon."},
                                {"desc": "Unlock with a key shaped like a star."},
                            ],
                            "correct": 1,
                        },
                        {
                            "desc": "Behind the door, a spiral staircase leads down to five tunnels:",
                            "choices": [
                                {"desc": "Tunnel filled with sparkling crystals."},
                                {"desc": "Tunnel echoing with ancient chants."},
                                {"desc": "Tunnel glowing with phosphorescent moss."},
                                {"desc": "Tunnel smelling of fresh rain and earth."},
                                {"desc": "Tunnel with walls carved in strange symbols."},
                            ],
                            "correct": 4,
                        },
                    ]
                }
            ]
        }
    ]
}

def play_sublevels(sublevels):
    made_wrong_choice = False
    for i, sub in enumerate(sublevels):
        print_with_delay(f"\nSub-level {i+1}: {sub['desc']}\n")
        choice = get_choice(sub['choices'])
        if choice == sub['correct']:
            print_with_delay("You chose wisely and proceed.\n")
        else:
            print_with_delay("Hmm... That might not have been the best choice...\n")
            made_wrong_choice = True
    return made_wrong_choice

def play_level(level):
    print_with_delay(f"\n{level['desc']}\n")
    made_wrong_choice = False
    choice = get_choice(level['choices'])
    if choice == level['correct']:
        print_with_delay("You took the right path and venture deeper.\n")
    else:
        print_with_delay("You chose a risky path, but press onward...\n")
        made_wrong_choice = True

    sub_wrong = play_sublevels(level['sublevels'])
    if sub_wrong:
        made_wrong_choice = True

    if made_wrong_choice:
        print_with_delay("Suddenly, a hidden trap triggers! You couldn't survive this time. 💀\nGame Over.\n")
        return False
    else:
        print_with_delay("You found a mysterious gift glowing softly in your hands! 🎁\n")
        return True

def play_stage(stage):
    print_with_delay(f"\n\n=== {stage['desc']} ===\n")
    for i, level in enumerate(stage['levels']):
        print_with_delay(f"\nLevel {i+1}:")
        survived = play_level(level)
        if not survived:
            return False
        if i < len(stage['levels']) - 1:
            if not ask_to_continue("Do you want to continue to the next level? (yes/no): "):
                print_with_delay("Thanks for playing! Come back for more adventure soon.\n")
                return False
    return True

def main():
    print_with_delay("🌟 Welcome to the Grand Mysterious Adventure! 🌟\n")
    stages = adventure['stages']

    for i in range(1):  # Only 1 stage for demo, add more if you want
        print_with_delay(f"\n--- Starting Stage {i+1} ---\n")
        stage = stages[0]
        survived = play_stage(stage)
        if not survived:
            print_with_delay("Your journey ends here. Try again to unlock all secrets.\n")
            break
        if i < 0:
            if not ask_to_continue("Do you want to continue to the next stage? (yes/no): "):
                print_with_delay("Thanks for playing! See you next time.\n")
                break
    else:
        print_with_delay("\n🎉 Congratulations! You completed the adventure! 🎉\n")

if __name__ == "__main__":
    main()
