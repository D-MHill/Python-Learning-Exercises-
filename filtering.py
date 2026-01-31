# @TASK: Complete this exercise.

print("")
print("Function: only_positive_numbers")

# Return a new list with only the positive numbers
def only_positive_numbers(numbers):
  positive_numbers = []
  for number in numbers:
    if number > 0:
      positive_numbers.append(number)
      return positive_numbers

print(only_positive_numbers([-4, 4, -3, 3]), [4, 3])
print(only_positive_numbers([-100]), [])
