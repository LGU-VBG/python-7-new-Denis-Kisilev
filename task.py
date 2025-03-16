def listodict(list1, list2):
    return dict(zip(list1, list2))

products = ['apple', 'banana', 'bread', 'kanfetka']
prices = [52, 80, 50, 42]

r1 = listodict(list1=products, list2=prices)



r2 = listodict(products, list2=prices)

print(r1, r2)
