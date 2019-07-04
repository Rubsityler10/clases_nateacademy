player1_number = None
while player1_number is None:
    try:
        player1_number = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid value.")
print(""">>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          >>
          """)

player2_number = None
while player2_number is None:
    try:
        player2_number = int(input("Select a number: "))
    except ValueError:
        print("Please enter a valid value.")

while player2_number != player1_number:
    print("You guessed wrong... Try again!")
    try:
        player2_number = int(input("Select a number: "))
    except ValueError:
        print("Please enter a valid value.")
    continue
else:
    print("You guessed right! Good job!")

