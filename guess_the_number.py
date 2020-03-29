import random
while True:


    computer = random.randint(1,3)
    print('Guess a number ')
    user_input = input()
    print('the users input is: ')
    print(user_input)
    if int(user_input) == computer :
    #if bla==2 :
        print(computer)
        print('You Win!')
        # break
    elif user_input != computer : 
        print('the comps input is: ')
        print(computer)
        print('Try again')
