
# asking user to enter the number
n = input('Please enter your number: ')

# in case user has entered not a number (yes I found it in the internet :p)
try:
    is_number = int(n)
except ValueError:
    print('Please use only digits')
    exit()

# checking that number is even or not
n = float(n)
even = n % 2 == 0

# all the task conditions
if not even and n > 20:
    print('Not Weird')
elif even and 6 <= n <= 20:
    print('Weird')
elif even and 2 <= n <= 5:
    print('Not Weird')
elif not even:
    print('Weird')

# this was not in the task condition, but I had tested this scenario too
elif even:
    print('This wasn\'t in task condition')
