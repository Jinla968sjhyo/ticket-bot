print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height>=120 :
  print("you can ride")

  if height <= 160 :
    print("bruh, you are too short i will book u a baby seat")
  age= int(input("what is your age?"))
  if age < 12:
    bill=5
    print("ticket for children is 5 dollars")
  elif age <= 18:
    bill=8
    print("ticket for teens is 8 dollars")
  else:
    bill=12
    print("ticket for adults is 12 dollars.")

  ask_photo= input("do you wanna take a photo? (Y/N).")
  if ask_photo== "Y" :
    bill += 3
  print(f"your bill will be {bill} dollars.")

else:
  print("you can't ride")
