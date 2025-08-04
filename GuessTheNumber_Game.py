import random as rd

target = rd.randint(1, 100)

while True:
  InputVal = input("Enter Your Guess or Quit(Type Q):")
  if InputVal == "Q" or "q":
    print("You quite the game.")
    break

  InputVal = int(InputVal)
  if InputVal == target:
    print("You have successfully guessed the number!!")
    break
  elif InputVal < target:
    print("You have guessed smaller value, Guess bigger value.")
  else:
    print("You have guessed bigger value, Guess smaller value.")

