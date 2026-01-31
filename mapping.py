# @TASK: Complete this exercise.

print("")
print("Function: add_one_hundred_to_numbers")

# Return a new list of each number with 100 added
def add_one_hundred_to_numbers(numbers):
  added_numbers = []
  for number in numbers:
      added_numbers.append(number + 100)
      return added_numbers


print(add_one_hundred_to_numbers([1, 2, 3, 4]), [101, 102, 103, 104])
print(add_one_hundred_to_numbers([2, 3, 4, 5]), [102, 103, 104, 105])