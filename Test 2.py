# Function with syntax errors
def multiply_numbers(a, b):
   result = a * b  # IndentationError
   return result
print(multiply_numbers(3, 5))  # Missing argument error
# Loop with an off-by-one error
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):
   print(numbers[i])
