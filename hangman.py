import random
#impoting random module


class Fore:
    GREEN = "\033[92m"#ANSI escape code used for showing colors
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
#Forming a huge nested dictionary
categories = {#outer layer
    "technology": {#each value is another dictionaryand in which each value contains set
        "python": ["Named after a comedy troupe rather than the reptile many assume, this is known for code that reads almost like plain English.", "related to programming and software", "a popular programming language known for readability", "starts with the letter P, has 6 letters"],
        "hangman": ["In this activity, a wrong move slowly builds a grim little stick figure while you race against a limited number of mistakes.", "a word-guessing game", "the name of this very game you're playing", "starts with the letter H, has 7 letters"],
        "computer": ["This sits on countless desks worldwide, silently running countless invisible calculations behind whatever you see on its screen.", "a non-living device used for tasks", "an electronic device used for computing", "starts with the letter C, has 8 letters"],
        "keyboard": ["Dozens of small buttons, each pressed thousands of times a day, working together to turn your thoughts into text on a screen.", "a non-living input device", "used for typing on a computer", "starts with the letter K, has 8 letters"],
        "internet": ["An invisible web with no physical center, quietly linking strangers on opposite sides of the planet in an instant.", "a non-living network system", "a global network connecting devices worldwide", "starts with the letter I, has 8 letters"],
        "smartphone": ["Rarely more than an arm's length away, this pocket-sized companion has quietly replaced maps, cameras, and calendars all at once.", "a portable non-living device", "used for calls, texting and apps", "starts with the letter S, has 10 letters"],
        "algorithm": ["Not a physical object at all, but an invisible recipe of logical steps that machines follow without ever asking why.", "related to programming logic", "a set of steps used to solve a problem", "starts with the letter A, has 9 letters"],
        "database": ["Think of an enormous, tireless filing cabinet that never forgets and can hand back any record in a fraction of a second.", "a non-living organized system", "stores and organizes large amounts of data", "starts with the letter D, has 8 letters"],
        "robot": ["Built to repeat a task endlessly without complaint, sometimes shaped like us, sometimes nothing like us at all.", "a non-living automated machine", "can perform tasks automatically, often human-like", "starts with the letter R, has 5 letters"],
        "satellite": ["Circling far above the clouds, this silent object relays signals between places that could never see each other directly.", "a non-living orbiting object", "used for communication and orbits the earth", "starts with the letter S, has 9 letters"],
        "microphone": ["It turns the vibrations of your voice into something a machine can understand and pass along.", "non-living, used with sound", "used to record or amplify sound", "starts with the letter M, has 10 letters"],
        "spaceship": ["Built to survive where there's no air to breathe, this carries people or cargo far beyond anything we can walk to.", "a non-living vehicle used for travel", "travels through outer space", "starts with the letter S, has 9 letters"],
        "camera": ["This freezes a single instant in time, preserving it long after the moment itself has vanished.", "non-living, used to capture something", "used to take photos or videos", "starts with the letter C, has 6 letters"]
    },
    "science": {
        "microscope": ["Something too small for your eyes to ever notice on their own becomes suddenly enormous when viewed through this.", "a non-living instrument", "used to see very tiny things", "starts with the letter M, has 10 letters"],
        "telescope": ["Light that left its source thousands of years ago finally reaches your eye through this, revealing worlds impossibly far away.", "a non-living instrument", "used to observe distant objects in space", "starts with the letter T, has 9 letters"],
        "chemistry": ["This field explains why mixing two harmless things can sometimes create something explosive, colorful, or entirely new.", "studies substances", "studies matter and chemical reactions", "starts with the letter C, has 9 letters"],
        "physics": ["From why apples fall to why rockets fly, this field tries to explain the invisible rules the universe never breaks.", "studies natural phenomena", "studies energy, motion and forces", "starts with the letter P, has 7 letters"],
        "biology": ["This field is dedicated to understanding everything from a single cell to entire forests full of life.", "studies living things", "studies living organisms and life processes", "starts with the letter B, has 7 letters"],
        "metallurgy": ["This field explains why a sword, a coin, and a smartphone case can all come from the very same shiny raw material.", "studies materials", "studies metals and alloys", "starts with the letter M, has 10 letters"],
        "nuclear": ["Locked inside something almost too small to imagine is enough energy to light entire cities or, if misused, level them.", "involves atomic energy", "related to atomic energy and radioactivity, quite powerful", "starts with the letter N, has 7 letters"],
        "electron": ["Too small to ever be seen directly, this negatively charged traveler races endlessly around the core of every atom.", "subatomic and non-living", "a negatively charged subatomic particle", "starts with the letter E, has 8 letters"],
        "molecule": ["When two or more tiny building blocks link arms, they form something new with its own identity entirely.", "a group of tiny particles", "a group of atoms bonded together", "starts with the letter M, has 8 letters"],
        "gravity": ["You'll never see it, touch it, or hear it, yet it quietly keeps every one of your steps from floating off the ground.", "a non-living, invisible force", "pulls objects toward each other", "starts with the letter G, has 7 letters"],
        "earthquake": ["The ground beneath your feet feels permanent, until deep pressures suddenly remind everyone that it isn't.", "related to earth's movement", "caused by tectonic plate shifts", "starts with the letter E, has 10 letters"]
    },
    "nature": {
        "mountain": ["Some people spend years training just to stand for a moment at the very top of one of these.", "non-living, very large", "tall and rocky natural landform", "starts with the letter M, has 8 letters"],
        "river": ["It never stops moving, carving its own path across the land over centuries, on its way toward somewhere larger.", "non-living, flowing", "a body of water that flows continuously", "starts with the letter R, has 5 letters"],
        "ocean": ["More of this planet's surface is covered by this than by land, and most of what's inside it remains unexplored.", "non-living, very large", "a huge body of saltwater covering most of earth", "starts with the letter O, has 5 letters"],
        "forest": ["Step beneath its canopy and the temperature drops, the light dims, and thousands of unseen creatures go about their day.", "a large green area", "large area full of trees, home to wildlife", "starts with the letter F, has 6 letters"],
        "elephant": ["Despite its enormous size, this gentle giant is known for an unusually long memory and an even longer nose.", "living, large mammal", "has a trunk and big ears", "starts with the letter E, has 8 letters"],
        "dolphin": ["Playful and quick-witted, this ocean dweller is often said to be one of the smartest creatures in the sea.", "living, marine mammal", "known for intelligence and living in oceans", "starts with the letter D, has 7 letters"],
        "eagle": ["From incredible heights, this creature can spot the smallest movement on the ground far below.", "living, a bird", "a bird of prey known for sharp eyesight", "starts with the letter E, has 5 letters"],
        "tiger": ["No two of this creature's coats are marked exactly alike, each pattern as unique as a fingerprint.", "living, wild cat", "has orange and black stripes", "starts with the letter T, has 5 letters"],
        "penguin": ["Clumsy on land but graceful underwater, this creature thrives in some of the coldest places on earth.", "living, a bird", "a flightless bird found in cold regions", "starts with the letter P, has 7 letters"],
        "volcano": ["Silent for years, sometimes decades, before suddenly reminding everyone nearby of the fire sleeping just beneath the surface.", "non-living, can be dangerous", "can erupt with lava", "starts with the letter V, has 7 letters"]
    },
    "professions": {
        "doctor": ["When something inside you goes wrong, this is the person trained for years to figure out why and fix it.", "a medical field profession", "helps treat sick people", "starts with the letter D, has 6 letters"],
        "teacher": ["Long after you forget the exact lesson, you often remember the person who first made you curious about it.", "an education field profession", "educates students in schools", "starts with the letter T, has 7 letters"],
        "pilot": ["Thousands of feet above the ground, this person is trusted with the lives of everyone seated behind them.", "an aviation field profession", "flies aircraft", "starts with the letter P, has 5 letters"],
        "scientist": ["Endless questions, careful experiments, and a stubborn refusal to accept an answer without proof define this profession.", "a research field profession", "conducts research to study the world", "starts with the letter S, has 9 letters"],
        "artist": ["A blank canvas or an empty page becomes something entirely new in the hands of this person.", "a creative field profession", "creates visual or creative work", "starts with the letter A, has 6 letters"],
        "engineer": ["Bridges that don't collapse, machines that don't fail, and systems that quietly just work are usually this person's doing.", "a technical field profession", "solves problems using technical skills", "starts with the letter E, has 8 letters"],
        "pieas": ["Tucked away in Pakistan, this institution trains some of the country's sharpest minds in engineering and applied sciences.", "education related, in Pakistan", "a university in Pakistan focused on engineering", "starts with the letter P, has 5 letters"],
        "university": ["After years of school, many students move on to this kind of institution to specialize in a subject of their choosing.", "non-living, education related", "an institution of higher education", "starts with the letter U, has 10 letters"],
        "hospital": ["This building never fully closes, staying open through the night for anyone who might need urgent help.", "non-living, medical related", "a building for medical treatment", "starts with the letter H, has 8 letters"],
        "library": ["Silence is almost a rule here, in a building where thousands of stories sit quietly waiting to be opened.", "non-living, book related", "a building to read and borrow books", "starts with the letter L, has 7 letters"]
    },
    "everyday": {
        "guitar": ["Six taut strings, when plucked or strummed just right, can carry an entire song on their own.", "non-living, musical", "a musical instrument with strings", "starts with the letter G, has 6 letters"],
        "piano": ["Black and white keys line up side by side, each one waiting to strike a hidden string the moment it's pressed.", "non-living, musical", "a musical instrument with keys", "starts with the letter P, has 5 letters"],
        "bicycle": ["Balance on two wheels, powered by nothing but your own legs, and you're using one of the oldest simple machines still around.", "non-living, a vehicle", "a two-wheeled human-powered vehicle", "starts with the letter B, has 7 letters"],
        "airplane": ["Something heavier than air still manages to lift off the ground and cross entire oceans in hours.", "non-living, a vehicle", "a vehicle that flies through the air", "starts with the letter A, has 8 letters"],
        "recipe": ["Follow this closely and even a beginner in the kitchen can turn a handful of ingredients into a finished dish.", "non-living, related to food", "a set of instructions used for cooking", "starts with the letter R, has 6 letters"],
        "umbrella": ["The moment the sky darkens, this simple folding object becomes the difference between staying dry and getting soaked.", "non-living, everyday item", "used to stay dry in the rain", "starts with the letter U, has 8 letters"],
        "calendar": ["Without this hanging on the wall or sitting on a desk, keeping track of birthdays and deadlines would be far harder.", "non-living, everyday item", "used to track dates and time", "starts with the letter C, has 8 letters"]
    }
}

hangman_stages = [#is a plain list (not a dictionary this time) — just an ordered collection of 7 items, one for each stage of the hangman drawing.
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
]

score = {"wins": 0, "losses": 0}#a small dictionary with two keys

def choose_category():
    print("\nChoose a category:")
    for name in categories:#a bullet list of all 5 category names.
        print("-", name)
    choice = input("Category: ").lower()
    while choice not in categories:
        print("Invalid category, try again.")
        choice = input("Category: ").lower()#converts whatever they type to lowercase
    return categories[choice]

def play_round():
    word_hints = choose_category()
    word = random.choice(list(word_hints.keys()))
    hint_list = word_hints[word]
    hint_index = 0

    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("\nwelcome to Hangman")
    print(f"the word has {len(word)} letters.")

    display_word = ["_"] * len(word)
    show_hint_message = ""

    while wrong_guesses < max_wrong and "_" in display_word:
        print(hangman_stages[wrong_guesses])
        print("\nWord: " + " ".join(display_word))
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        if show_hint_message:
            print(show_hint_message)
            show_hint_message = ""

        guess = input("Guess a letter (or type 'hint' for a clue): ").lower()

        if guess == "hint":
            if hint_index < len(hint_list):
                if hint_index == 0:
                    show_hint_message = f"Hint {hint_index + 1} (free): {hint_list[hint_index]}"
                else:
                    show_hint_message = f"Hint {hint_index + 1}: {hint_list[hint_index]} (costs 1 wrong guess)"
                    wrong_guesses += 1
                hint_index += 1
            else:
                show_hint_message = "No more hints available for this word!"
            continue

        if len(guess) > 1:
            if guess == word:
                display_word = list(word)
                print(Fore.GREEN + "Correct! You guessed the whole word!" + Fore.RESET)
            else:
                print(Fore.RED + "That's not the word!" + Fore.RESET)
                wrong_guesses += 1
            continue

        if guess in guessed_letters:
            print(Fore.YELLOW + "You already guessed that letter!" + Fore.RESET)
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(Fore.GREEN + "Correct!" + Fore.RESET)
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            print(Fore.RED + "Wrong guess!" + Fore.RESET)
            wrong_guesses += 1

    if "_" not in display_word:
        print(Fore.GREEN + "\nCongratulations! You guessed the word: " + word + Fore.RESET)
        score["wins"] += 1
    else:
        print(Fore.RED + "\nGame Over! The word was: " + word + Fore.RESET)
        score["losses"] += 1

while True:
    play_round()
    print(f"\nScore -> Wins: {score['wins']}  Losses: {score['losses']}")
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print(f"\nFinal Score -> Wins: {score['wins']}  Losses: {score['losses']}")
        print("Thanks for playing!")
        break