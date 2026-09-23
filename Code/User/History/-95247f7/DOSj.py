lst1= ['H', 'D', 'C', 'S']
lst2 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

lst3 = []

for i in lst1:
    for j in lst2:
        lst3.append(i+j)
print(lst3)