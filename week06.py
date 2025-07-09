def load_to_list(filepath: str) -> list[float]:
    values = []
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                values.append(float(line))
    return values

def descriptive_statistics(source_data: list[float]) -> None:
    total = 0
    count = 0
    minimum = source_data[0]
    maximum = source_data[0]

    for temperature in source_data:
        total += temperature
        count += 1
        if temperature < minimum:
            minimum = temperature
        if temperature > maximum:
            maximum = temperature

    average = round(total / count, 2)

    print(f"There are {count} values in the data source.")
    print(f"The average value is {average}")
    print(f"The highest value is {maximum} and the smallest value is {minimum}.")

def apply_markup(filepath: str) -> None:
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            words = line.split()
            formatted_line = ""

            for word in words:
                if word.startswith("."):
                    formatted_word = word[1:].upper()
                    formatted_line += formatted_word + " "
#^^ I will ask about this in class

#Reflection
# Incorrect indentation in loop in #1, causing to only evaluate last character fo foo. I also didnt check for duplicates.
# For #2 I did not use bolean alpha_only to end loop early. And didnt check if string is null. 
# In #3 I added non-letters to the result which is inverted.
# In #4 range is invalid because it should only allow 3 and shouldve used len(string) - 1 - len(string) % 2 for odd and even and for avoiding duplicates.
# In #5 I needed to use two pointers leftbound, and rightbound.
# Overall my code is way more complicated and nonefficient compared to the solutions, I still have a lot to learn, mostly in problems, 4-5.

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

