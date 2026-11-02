# Homework
# 1
list1_1 = [1, 1, 2]
list1_2 = [2, 3, 4]

for i in list1_1:
    if i in list1_2:
        list1_1.remove(i)
        list1_2.remove(i)
new_list1 = list1_1 + list1_2
print(new_list1)


list2_1 = [1, 2, 3]
list2_2 = [4, 5, 6]

for i in list2_1:
    if i in list2_2:
        list2_1.remove(i)
        list2_2.remove(i)
new_list2 = list2_1 + list2_2
print(new_list2)


list3_1 = [1, 1, 2, 3, 4, 2]
list3_2 = [1, 3, 4, 5]

result = []

for i in list3_1:
    if i not in list3_2:
        result.append(i)

for i in list3_2:
    if i not in list3_1:
        result.append(i)

print(result)

# 2
n2_2 = int(input())
for i in range(1,n2_2):
    print(i**2)
    

# 3
txt = input()

done = "aeiou"

counter = 0
ans = ""

for i in range(len(txt)):
    counter += 1
    ans += txt[i]
    if i!=len(txt)-1 and counter>=3 and txt[i] not in done:
        done += txt[i]
        ans += "_"
        counter = 0

print(ans)


# 4
import random

while True:
    number = random.randint(1, 100)
    print(number)

    for attempt in range(1, 11):
        guess = int(input("Guess the number (1-100): "))

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You guessed it right!")
            break

    else:
        print("You lost. Want to play again? ")
        answer = input().lower()

        if answer not in ["y", "yes", "ok"]:
            break

# 5
password = input("Enter your password: ")

if len(password) < 8:
    print("Password is too short.")

elif not any(char.isupper() for char in password):
    print("Password must contain an uppercase letter.")

else:
    print("Password is strong.")


# 6
q6_pri_n = [2,3,5,7]

for i in range(2,101):
    if (i%2==0) or (i%3==0) or (i%5==0) or (i%7==0) :
        pass
    else:
        q6_pri_n.append(i)
print(q6_pri_n)
print(len(q6_pri_n))

# Bonus
import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:

    player = input("Choose rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Score:", player_score, "-", computer_score)
    print()

if player_score == 5:
    print("You won the match!")

else:
    print("Computer won the match!")




