letter1 = input("Input first letter ")
letter2 = input("Input second letter ")
place1 = ord(letter1) - ord('a') + 1
place2 = ord(letter2) - ord('a') + 1
distance = place2 - place1 - 1
print(f"Letter {letter1} is {place1} in alphabet")
print(f"Letter {letter2} is {place2} in alphabet")
print(f"{distance} letters between {letter1} and {letter2}")

