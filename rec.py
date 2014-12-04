
def rec_sum(num):
   if num ==1:
      return num
   else:
     return num + rec_sum(num-1)












num = int(raw_input('Enter a number:'))

if num < 1:
    print('Enter a positive number' )
else:
    print('The recursion is:',rec_sum(num))
