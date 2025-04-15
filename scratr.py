fruits = ['apple', 'peaches', "oranges"]
guess = input("guess: ")
for fruit in fruits:
    if guess in fruit:
        fruits.remove(guess)

print(fruits)