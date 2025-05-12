# get the # rows & columns
rows, columns = map(int, input().split())
# define main pattern
design_1 = '.|.'
design_2 = '-'
for i in range(1,rows+1):
  # top cone
  if i <= (rows//2) :
    print(((2*i-1)*design_1).center(columns,design_2))
  # center
  elif i == (rows//2+1):
    print('WELCOME'.center(columns, design_2))
  # bottom cone
  elif i > (rows//2):
    print((((2*rows+1)-(2*i))*design_1).center(columns,design_2))