suits= ['H', 'D', 'C', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

lst3 = []

for i in suits:
    for j in ranks:
        lst3.append(j+i)
print(lst3)
print(len(lst3))

x=[i+j for j in suits for i in ranks]
print(x)
print(len(x))