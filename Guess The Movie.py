import random

# Step 1: Movie data
movies = [
    {"hero": "Prabhas", "heroine": "Anushka", "song": "Hamsa Naava", "movie": "Baahubali 2"},
    {"hero": "MaheshBabu", "heroine": "Keerthy Suresh", "song": "Kalavathi", "movie": "Sarkaru Vaari Paata"},
    {"hero": "Nani", "heroine": "Nazriya", "song": "Entha Chitram", "movie": "Ante Sundaraniki"},
    {"hero": "RamCharan", "heroine": "Alia Bhatt", "song": "Komuram Bheemudo", "movie": "RRR"},
    {"hero": "Venkatesh", "heroine": "Nayanthara", "song": "Laxmi Bava", "movie": "Lakshmi"},
    {"hero": "Ram", "heroine": "Genelia", "song": "Appudo Ippudo", "movie": "Bommarillu"},
    {"hero": "Nagarjuna", "heroine": "Tabu", "song": "Ruk Ruk Ruk", "movie": "Ninne Pelladatha"},
    {"hero": "Pawan Kalyan", "heroine": "Bhumika", "song": "Cheliya Cheliya", "movie": "Kushi"},
    {"hero": "Dhanush", "heroine": "Shruti Haasan", "song": "Why This Kolaveri Di", "movie": "3"},
    {"hero": "Karthi", "heroine": "Tamannaah", "song": "Arare Vaana ", "movie": "Awara"},
    {"hero": "Vijay Dhalapathy", "heroine": "Samantha", "song": "Kannullo Unnavau ", "movie": "Policoodu"},
    {"hero": "Rana", "heroine": "Kajal", "song": " Jogendra ", "movie": "Nene Raju Nene Mantri"},
    {"hero": "Suriya", "heroine": "Sruthi Haasan", "song": "Yellelama", "movie": "Seventh Sense"},
    {"hero": "Balakrishna", "heroine": "Urvasi Rautela", "song": "Dabidi Dhibidi", "movie": "Daaku Maharaj"},
    {"hero": "Sudheer Babu", "heroine": "Krithi Shetty", "song": "Aa Ammayi Gurinchi", "movie": "Aa Ammayi Gurinchi Meeku Cheppali"},
    {"hero": "Vishwak Sen", "heroine": "Nivetha Pethuraj", "song": "Kanapadavaa", "movie": "Paagal"},
    {"hero": "Akhil Akkineni", "heroine": "Pooja Hegde", "song": " Guchhe Gulabi", "movie": "Most Eligible Bachelor"},
    {"hero": "Varun Tej", "heroine": "Sai Pallavi", "song": "Hey Pillagaada ", "movie": "Fidaa"},
    {"hero": "Naga Chaitanya", "heroine": "Sai Pallavi", "song": "Hey Pilla", "movie": "Love Story"},
    {"hero": "Raj Tarun", "heroine": "Hebah Patel", "song": "Kumari 21F", "movie": "Kumari 21F"},
    {"hero": "Allu Arjun", "heroine": "Pooja Hegde", "song": "Buttabomma", "movie": "Ala Vaikuntapuramulo"},
    {"hero": "Dulquer Salmaan", "heroine": "Mrunal Thakur", "song": "Vasthaa Ne venteney", "movie": "Sita Ramam"}
]

def play_game():
    selected = random.choice(movies)
    score = 0
    max_attempts = 5

    def get_hint(value, letters_to_show):
        return value[:letters_to_show] + "*" * (len(value) - letters_to_show)

    print("\n--- Guess the Movie Combo Game ---")
    print("You have 5 attempts. Each correct guess gives you 20 points.")

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt} of {max_attempts}")
        hint_len = attempt

        print("Hints:")
        print("Hero: ", get_hint(selected["hero"], hint_len))
        print("Heroine: ", get_hint(selected["heroine"], hint_len))
        print("Song: ", get_hint(selected["song"], hint_len))
        print("Movie: ", get_hint(selected["movie"], hint_len))

        guess_hero = input("Your guess for Hero: ").strip()
        guess_heroine = input("Your guess for Heroine: ").strip()
        guess_song = input("Your guess for Song: ").strip()
        guess_movie = input("Your guess for Movie: ").strip()

        if guess_hero.lower() == selected["hero"].lower():
            print("Correct Hero!")
            score += 20
        else:
            print("Wrong Hero!")

        if guess_heroine.lower() == selected["heroine"].lower():
            print("Correct Heroine!")
            score += 20
        else:
            print("Wrong Heroine!")

        if guess_song.lower() == selected["song"].lower():
            print("Correct Song!")
            score += 20
        else:
            print("Wrong Song!")

        if guess_movie.lower() == selected["movie"].lower():
            print("Correct Movie!")
            score += 20
        else:
            print("Wrong Movie!")

        if score == 80:
            print("\nAwesome! You guessed everything correctly!")
            break

    print("\nGame Over!")
    print("Final Score:", score)
    print("Correct Answers:")
    print("Hero:", selected["hero"])
    print("Heroine:", selected["heroine"])
    print("Song:", selected["song"])
    print("Movie:", selected["movie"])

    if score >= 60:
        bonus = input("\nWant to play a Bonus Round for extra points? (yes/no): ").strip().lower()
        if bonus == "yes":
            print("\n--- Bonus Round ---")
            play_game()

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again == "yes":
        play_game()

# Start the game
play_game()