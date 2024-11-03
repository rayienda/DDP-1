#Lab-03
#Rayienda Hasmaradana

#start of the code
print('Lab 03\n')
print('From decimal to hexadecimal')
print('---------------------------')

# read the user's input
myInt = int(input('Give a positive integer in decimal representation: '))

# convert the integer stored in myInt to hex digits
hexstr = '' # accumulator for hex digits, starting with empty string
temp = myInt
while temp != 0:
    hexdigit = temp % 16
    if hexdigit < 10: #get one hex digit: 0,1,2,3,4,5,6,7,8,9
        hexstr = str(hexdigit) + hexstr
    else: #get one hex digit: A, B, C, D, E, F
        hexstr = chr(ord('A') + hexdigit - 10) + hexstr #formula
    temp = (temp // 16)

print('The hexadecimal representation of',myInt,'is','0x' + hexstr)
print()
print('From hexadecimal to decimal')
print('---------------------------')

# read the hex string from the user
hexstr = input('Give a positive integer in hexadecimal representation: ')

# convert the hex string to a correct decimal integer
temp = hexstr[2::] # remove '0x' using string slicing
newInt = 0 # accumulator for decimal value
power = 0
while temp:
    hexdigitstr = temp[-1] # get the rightmost hex digit
    if '0' <= hexdigitstr <= '9':
        decimal = int(hexdigitstr)
    else:
        decimal = ord(hexdigitstr.upper()) - ord('A') + 10 #formula

    newInt += decimal *(16 ** power) # add the appropriate power
    temp = temp[:-1] # remove the rightmost hex digit
    power +=1
 
print('The decimal representation of', hexstr, 'is', newInt)
print()
print('Thanks for using this program.')
print()
input('Press Enter to continue ...') # hold the screen display
#the end of the program