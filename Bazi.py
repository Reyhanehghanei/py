
# انتخاب یک ماژول برای انتخاب عدد تصادفی 
import random



# از کاربر بپرسیم که آیا مایل است چه چیزی را انتخاب کند 
user_action = input("Enter a choice (rock, paper, scissors): ")


#به صورت تصادفی 
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)



#یک عدد تصادفی پیدا میکند 
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# انتخاب دو بازیکن انجام شده است و اکنون باید راهی برای تصمیم گیری برنده مشخص شود
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

        import random

        # برسی کردن که انتخاب درست است یا ن

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

        