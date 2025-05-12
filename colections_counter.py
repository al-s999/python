from collections import Counter  # Import the Counter class from the collections module

no_of_shoes = int(input())  # Read the number of shoes available in the shop
shoe_size = map(int, input().split())  # Read the sizes of the shoes and convert them to integers
cus = int(input())  # Read the number of customers
earnings = 0  # Initialize earnings to zero
shop = Counter(shoe_size)  # Create a Counter object to count the occurrences of each shoe size

for i in range(cus):  # Loop through each customer
    cus_shoe_size, price = map(int, input().split())  # Read the customer's requested shoe size and price
    if shop[cus_shoe_size] > 0:  # Check if the requested shoe size is available
        shop[cus_shoe_size] -= 1  # Decrease the count of that shoe size by 1
        earnings += price  # Add the price to the total earnings

print(earnings)  # Print the total earnings

# example :   input =   5
#                     38 39 40 41 39
#                     3
#                     39 100
#                     38 150
#                     40 200
#             outout = 450
# note :- The first line `5` indicates there are 5 shoes available.
        # - The second line `38 39 40 41 39` lists the sizes of the shoes available in the shop.
        # - The third line `3` indicates there are 3 customers.
        # - The next lines represent each customer's request:
        # - The first customer wants size `39` and is willing to pay `100`.
        # - The second customer wants size `38` and is willing to pay `150`.
        # - The third customer wants size `40` and is willing to pay `200`.
        # - The earnings are calculated as follows:
        # - The first customer buys size `39` for $100.
        # - The second customer buys size `38` for $150.
        # - The third customer buys size `40` for $200.
        # - Total earnings = $100 + $150 + $200 = $450.