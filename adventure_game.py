import time
import random


def print_pause(msg_to_print):
        print(msg_to_print)
        time.sleep(2)


def intro(a, b):
        print_pause("You find yourself standing in an open field, filled "
                    "with grass and yellow wildflowers.")
        print_pause("Rumor has it that a " + b + " is somewhere around "
                    "here, and has been terrifying the nearby village.")
        print_pause("In front of you is a house.")
        print_pause("To your right is a dark cave.")
        print_pause("In your hand you hold your trusty (but not very "
                    "effective) dagger.")


def cave(a, b):
        if "sword" in a:
            print_pause("You carefully go to the cave.")
            print_pause("You've been here before, and everyone has got"
                        " the good stuff. It's just an empty cave"
                        " now.")
            print_pause("You go back to the field.")
        else:
            print_pause("You carefully go to the cave.")
            print_pause("It's only a very small cave.")
            print_pause("Your eye catches a glint of metal behind a "
                        "rock.")
            print_pause("You have found the magical Sword of Ogoroth!")
            print_pause("You abandon your silly old dagger and carry "
                        "the sword with you.")
            print_pause("You walk back out to the field.")
            a.append("sword")
            field(a, b)


def house(a, b):
    print_pause("You knock on the door of the house.")
    print_pause("You are gonna knock "
                "opens and out steps a " + b + ".")
    print_pause("Eep! This is the " + b + "'s house!")
    print_pause("The " + b + " attacks you!")
    if "sword" not in a:
        print_pause("You feel a little bit ready for it, "
                    "With only a small dagger.")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run?")
        if choice2 == "1":
            if "sword" in a:
                print_pause("As the " + b + " moves to attack, "
                            "you unsheath your new sword.")
                print_pause("The Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("But the " + b + "takes one look at "
                            "Your shiny new toy and run!")
                print_pause("You got rid of the city " + b +
                            ". You are victorious!\n")
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the " +
                            b + ".")
                print_pause("You have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been "
                        "followed.")
            field(a, b)
            break


def field(a, b):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)")
        if choice1 == "1":
            house(a, b)
            break
        elif choice1 == "2":
            cave(a, b)
            break


def play_again():
    again = input("Would you like to play again? (yes/no)").lower()
    if again == "yes":
        print_pause("\n\n\n OK! Restart ...\n\n\n")
        play_game()
    elif again == "no":
        print_pause("\n\n\nThanks for playing! See you again.\n\n\n")
    else:
        play_again()


def play_game():
        a = []
        b = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                           "gorgon"])
        intro(a, b)
        field(a, b)

play_game()
