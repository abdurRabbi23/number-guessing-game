import random

def game():
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!\n")

    guessed_num = random.randint(1, 100)  # Random number
    count = 1  # Start attempt count from 1

    while True:
        try:
            num = int(input("Enter your guess: "))

            if num < 1 or num > 100:
                print("⚠️ Please enter a number between 1 and 100!")
                continue  # Ask again without increasing count

            if num > guessed_num:
                print("📉 Opps high! Try guessing lower.")
            elif num < guessed_num:
                print("📈 Opps low! Try guessing higher.")
            else:
                print(f"🎉 Congrats! You guessed it right in {count} attempts.\n")
                break  # Exit loop when correct guess

            count += 1  # Increment count after a valid attempt

        except ValueError:
            print("⚠️ Invalid input! Please enter a valid integer.")

    # Ask for replay
    play_again = input("🔄 Want to play again? (yes/no): ").strip().lower()
    if play_again in ("yes", "y"):
        game()
    else:
        print("👋 Thanks for playing! See you next time.")


game()

