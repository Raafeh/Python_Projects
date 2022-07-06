import random
count=0

range_top=  int(input("Type a Number : "))

if range_top <= 0:
    print("Please enter a number greater then 0")
    quit()
else:
    rand_num= random.randint(0,range_top)
  

while True:
    count +=1
    guess= int(input('Make a guess number: '))

    if guess== rand_num:
        print('You got it!')
        break
    elif guess > rand_num:
        print("You were above the number!")
    else:
        print("You were below the number!")
print('You got it in ',count,'guesses!')