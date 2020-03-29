def convert_to_c(temp):
  return ((9 / 5) * (temp_input + 32))

def convert_to_f(temp):
  return ((5 / 9) * (temp_input - 32))

input = ()
def main():
input_temp = float(input('enter a temperature: '))
input('enter a unit: ')
convert_to_unit = input('enter a unit to convert to: ')

if convert_to_unit in ('c', 'C'):
    converted_temp = convert_to_f(temp)
elif convert_to_unit in ('f', 'F'):
    converted_temp = convert_to_c(temp)
    print(converted_temp)

else:
    print('no temp entered')
  
  