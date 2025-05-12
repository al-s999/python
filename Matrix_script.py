import re

# Read the matrix dimensions
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])  # Number of rows
m = int(first_multiple_input[1])  # Number of columns

# Read the matrix
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Transpose the matrix to read columns as rows
decoded_script = ''.join([matrix[i][j] for j in range(m) for i in range(n)])

# Replace non-alphanumeric characters between alphanumeric characters with a single space
cleaned_script = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_script)

# Print the cleaned decoded script
print(cleaned_script)