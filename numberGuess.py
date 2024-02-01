import random

#Enter range and check if inputs are valid!
err = "The value you entered is not valid, please enter an Integer"
while True : 
  try:
    range_begin = int(input("Enter the starting number of your range: "))
    range_end = int(input("Enter the ending number of your range: "))
  except ValueError:
    print(err)
    continue
  else:
    break
  
print("The range is [",range_begin,",",range_end,"]")

num = random.randint(range_begin,range_end)
print(num)

guess_counter = 0
guess_number = 0
while (guess_number!= num) : 
    

    try:
      guess_number = int(input("Enter you guess: "))
    except ValueError:
      print(err)

      print(guess_number)


    if (guess_number > range_end or guess_number < range_begin ) :
      print("Your guess is out of range")

    elif guess_number == num :
      guess_counter = guess_counter + 1
      print("Congratulations! You guessed right in attempt number: ", guess_counter)
      break;
    
    elif guess_number < num :
      print("You guess is to low")
      guess_counter = guess_counter + 1
    elif guess_number > num :
      print("Your guess is to high")
      guess_counter = guess_counter + 1
