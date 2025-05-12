from collections import OrderedDict

od = OrderedDict()

for _ in range(int(input())):
    line = input()
    *item_parts, price = line.rsplit(' ', 1)
    item = ' '.join(item_parts)
    price = int(price)
    if item in od:
        od[item] += price
    else:
        od[item] = price

for item, total in od.items():
    print(f'{item} {total}')
    
