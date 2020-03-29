user_input = int(input("Enter number: "))

# tens_digit = x//10

# ones_digit = x%10

# print(tens_digit)

# print(ones_digit)

if 0 <= user_input and user_input <= 9:
        print(singles.get(user_input))

elif 10 <= user_input and user_input <=19:
        print(teens.get(user_input))

singles = { 1 : 'one' , 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six' , 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten'}

teens = { 11 : 'eleven' , 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'}

doubles = { 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }