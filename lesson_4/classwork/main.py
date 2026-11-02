# 1. Loops Quiz
# I can see you've linked to a quiz. Would you like me to help you with specific questions from it, or shall we move on to the other questions?


# 2. Difference between continue and break:
# break: Completely exits the loop immediately, stopping all further iterations.
# continue: Skips the rest of the current iteration and jumps to the next iteration of the loop.

# break example
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0, 1, 2

# continue example
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0, 1, 2, 4


# 3. Difference between for loop and while loop:
# for loop: Used when you know how many times you want to iterate (definite iteration). It iterates over a sequence (list, string, range, etc.).
# while loop: Used when you want to repeat as long as a condition is true (indefinite iteration). You don't necessarily know how many iterations in advance.
# for loop - iterating over a known sequence
for i in range(5):
    print(i)

# while loop - continuing until a condition is met
count = 0
while count < 5:
    print(count)
    count += 1


#     4. Nested for loop system:
# A nested loop is a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.
# Example: Multiplication table
for i in range(1, 4):  # outer loop
    for j in range(1, 4):  # inner loop
        print(f"{i} x {j} = {i*j}")
    print()  # blank line after each outer iteration
