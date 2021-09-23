"""My choose your own adventure project."""

__author__ = "730392059"

points: int = 0
player: str
fire_points: int = 0
water_points: int = 0
air_points: int = 0
earth_points: int = 0
fire: str = "\U0001F525"
water: str = "\U0001F4A7"
earth: str = "\U0001F331"
air: str = "\U0001f4a8"


def main() -> None:
    """The main function that is called."""
    greet()
    next_step()
    while_loop() 
    endgame() 


def greet() -> None:
    """The introduction function and first part."""
    print("Welcome")
    global player
    player = input("What is your name? ")
    return None


def next_step() -> None:
    """First options for the player."""
    global points
    print(f"What would you like to do next {player}?")
    starting_options: str = input("input 1 to start quiz, 2 to learn about the creator, 3 to skip the first question, or 4 to quit ")
    if starting_options == str(4):
        print(f"You obtained {str(points)} quiz points")
        print(f"{str(fire_points)}{fire} fire points")
        print(f"{str(water_points)}{water} water points")
        print(f"{str(air_points)}{air} air points")
        print(f"{str(earth_points)}{earth} earth points")
        print("Play again soon! And have a good day!")
        quit()
    if starting_options == str(3):
        print("Why would you skip the first question? ")
        print("Big mistake. You never skip the first question.")
        points = points + wrong_choice(points)
        print(f"You now have {str(points)} quizpoints ...you would be doing a lot better if you didn't skip the first question")
        print("Onto the next part!")
    if starting_options == str(2):
        print("The creator is named Alec Mulvaney. He's a sophmore at UNC, taking COMP110 with Kris Jordan!")
        print("This is his Choose Your Own Adventure Project!")
        next_step()
    if starting_options == str(1):
        print("Excellent choice!")
        print("Let's now begin the quiz")
        question_one()


def question_one() -> None:
    """First real question that affects end element."""
    print(f"So {player} what type of bender do you think you'll be?")
    print("(your options are 1 for fire, 2 for water, 3 for air, and 4 for earth)")
    initial_pick: int = int(input())
    global points
    points = points + 1
    if initial_pick == 1:
        global fire_points
        fire_points = fire_points + 1
    if initial_pick == 2:
        global water_points
        water_points = water_points + 1
    if initial_pick == 3:
        global air_points
        air_points = air_points + 1
    if initial_pick == 4:
        global earth_points
        earth_points = earth_points + 1
    print("interesting choice... we'll see if it holds true")


def wrong_choice(points: int) -> int:
    """If the player picked to skip first question."""
    points = points - 1
    mistake: int = int(input("On a scale of 1-10, how much do you regret skipping the first question? "))
    if mistake <= 5:
        print(f"{player}... seriously? I guess we'll move on then")
        points = 0
    else:
        print(f"hmmm... ok {player} I'll forgive you")
        points = 1
    return points  


def while_loop() -> None:
    """Bulk of the game, picking which option to figure out element."""
    global points 
    global fire_points
    global water_points 
    global air_points 
    global earth_points
    while fire_points < 4 and water_points < 4 and air_points < 4 and earth_points < 4:
        print(f"You currently have {str(points)} quiz points. Yes more is better")
        print("Would you like to quit now? or continue to find your bender type?")
        choice = int(input("1 for continue (which is highly recommend), or 2 for quit "))
        if choice == 2:
            print(f"You obtained {str(points)} quiz points.")
            print(f"{str(fire_points)}{fire} fire points")
            print(f"{str(water_points)}{water} water points")
            print(f"{str(air_points)}{air} air points")
            print(f"{str(earth_points)}{earth} earth points")
            print("Play again soon! And have a good day!")
            quit()
        else:
            points = points + 1
            from random import randint 
            random_question: int = int(randint(1, 6))
            if random_question == 1:
                choice_one: int = int(input("If you had to pick a superpower between, 1 breath underwater, 2 ablility to fly, 3 ability to control plants, or 4 ability to breath fire, which one would you pick? "))
                print("interesting choice...")
                if choice_one == 1:
                    water_points = water_points + 1
                if choice_one == 2:
                    air_points = air_points + 1
                if choice_one == 3:
                    earth_points = earth_points + 1
                if choice_one == 4:
                    fire_points = fire_points + 1
            if random_question == 2:
                choice_two: int = int(input("Which is cooler to you, 1 the desert, 2 the ocean, 3 the top of a mountain, or 4 a cave "))
                print("Hmmm...")
                if choice_two == 2:
                    water_points = water_points + 1
                if choice_two == 3:
                    air_points = air_points + 1
                if choice_two == 4:
                    earth_points = earth_points + 1
                if choice_two == 1:
                    fire_points = fire_points + 1   
            if random_question == 3:
                choice_three: int = int(input("Which one could you deal with the best? 1 a heat wave, 2 a flood, 3 a tornado, or 4 a mudslide "))
                print("Solid choice")
                if choice_three == 2:
                    water_points = water_points + 1
                if choice_three == 3:
                    air_points = air_points + 1
                if choice_three == 4:
                    earth_points = earth_points + 1
                if choice_three == 1:
                    fire_points = fire_points + 1
            if random_question == 4:
                choice_four: int = int(input("Ideal date. 1 a hiking trip, 2 roasting marshmellows and cuddling by a fire, 3 scuba diving, or 4 hot airballon dinner "))
                print("I would probably choose the same")
                if choice_four == 3:
                    water_points = water_points + 1
                if choice_four == 4:
                    air_points = air_points + 1
                if choice_four == 1:
                    earth_points = earth_points + 1
                if choice_four == 2:
                    fire_points = fire_points + 1
            if random_question == 5:
                choice_five: int = int(input("What is your favorite color? 1 white, 2 green, 3 red, or 4 blue? "))
                print("mine is definetly navy blue")
                if choice_five == 4:
                    water_points = water_points + 1
                if choice_five == 1:
                    air_points = air_points + 1
                if choice_five == 2:
                    earth_points = earth_points + 1
                if choice_five == 3:
                    fire_points = fire_points + 1
            if random_question == 6:
                choice_six: int = int(input("Which animal is the best? 1 eagle, 2 bear, 3 shark, or 4 pheonix "))
                print("Really? I would've picked a bark. Bear + Shark hybrid")
                if choice_six == 3:
                    water_points = water_points + 1
                if choice_six == 1:
                    air_points = air_points + 1
                if choice_six == 3:
                    earth_points = earth_points + 1
                if choice_six == 4:
                    fire_points = fire_points + 1


def endgame() -> None:
    """Final step in the game assuming they haven't quit."""      
    global points 
    global fire_points
    global water_points 
    global air_points 
    global earth_points
    print(f"Ok {player}, I think you've answered enough questions")
    print("I think you are a...")
    print("hmm...")

    if fire_points == 4:
        print("I think you would make a great fire bender!!!")
        print(f"{fire}{fire}{fire}{fire}{fire}")
    if water_points == 4:
        print("I think you would make a great water bender!!!")  
        print(f"{water}{water}{water}{water}{water}")          
    if earth_points == 4:
        print("I think you would make a great earth bender!!!")
        print(f"{earth}{earth}{earth}{earth}{earth}")
    if air_points == 4:
        print("I think you would make a great air bender!!!")
        print(f"{air}{air}{air}{air}{air}")
    print(f"Oh! And what's this? You have {points} quiz points")
    if points <= 5:
        print("Oh nevermind")
        print("ahahaha it's... irrelevant for you")
    if 9 >= points > 5:
        print("very very interesting... you might be able to master more than your chosen element")
    if points > 9:
        print(f"WAIT A MINUTE. {points} QUIZ POINTS!!!")
        input("Do you know what this means? ")   
        print("This means you can master all the elements...")
        print(f"{fire}{water}{earth}{air}")

    print("Thanks for playing!")
    print(f"You obtained {str(points)} quiz points")
    print(f"{str(fire_points)}{fire} fire points")
    print(f"{str(water_points)}{water} water points")
    print(f"{str(air_points)}{air} air points")
    print(f"{str(earth_points)}{earth} earth points")
    print("Try playing again and seeing how many quiz points you can get!")
    

if __name__ == "__main__":    
    main()
