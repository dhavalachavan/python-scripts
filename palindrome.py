my_str = raw_input("Enter a string:")

my_str = my_str.lower()

ym_str = reversed(my_str)

if list(my_str) == list(ym_str):
  print("The string is palindrome")
else:
  print("The string is not palindrome")
