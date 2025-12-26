#WHILE LOOP

count = 0 
while count < 5:
    print("Count is:", count)
    count += 1  # Increment the count to avoid infinite loop
print("Finished counting!")

city = "Bhopal"
count = 0
while count < len(city):
    print("Character at index", count, "is", city[count])
    count += 1
print("Finished iterating through the city name!")

#BREAK AND CONTINUE

num = 0
while num < 10:
    if num == 5:
        print("Breaking the loop at num =", num)
        break  # Exit the loop when num is 5
    print("Current number is:", num)
    num += 1
print("Loop ended due to break statement.")

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print("Current odd number is:", num)