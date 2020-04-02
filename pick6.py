import random

def main():
    winningNums = pick6()
    ticket = pick6()
    # testWin = [1,2,3,4,5,6]
    # testTik = [1,3,3,5,0,6]#should be 3 matches
    print('Winning Ticket ', winningNums, '\nTicket is ', ticket)
    num_matches(winningNums, ticket)

def pick6():
    setList = list()
    for i in range(0, 6):
        setList.append(create_random_number())
    return setList
    
# Ticket   [1, 3, 3, 5, 0, 6]
# Winning  [1, 2, 3, 4, 5, 6] 

def num_matches(winning, ticket):
    trueMatches = 0
    for idx1, tickVal in enumerate(ticket):
        for idx2, winVal in enumerate(winning):
            if tickVal == winVal and idx1 == idx2:
                trueMatches += 1
    print('true matches found. \nNumber of matches = ', trueMatches)


def create_random_number():
    return random.randint(1,99)

if __name__ == '__main__':
    main()

# X 100,000
# Generate earnings:
# Start your balance at 0
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000




# Version 2
# The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.