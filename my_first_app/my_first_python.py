price_per_square = 100

def house_price(length, width):
    space = length * width
    return space * price_per_square


a =[(10,20), (20,30), (30,35)]

for i in a:
    print(house_price(i[0],i[1]))
b = [house_price(i[0],i[1]) for i in a]
print(b)

