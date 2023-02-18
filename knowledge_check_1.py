greeting = 'Hello, World'
print(greeting)

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1[1])

beer_dictionary = {'Brabble' : 'Blonde Ale', 
                   'Kapowski' : 'Amber Ale', 
                   'Linchpin' : 'Hazy IPA', 
                   'Mcpoyle' : 'Milk Stout'}

print(beer_dictionary['Linchpin'])

#Tuple contains, ABV, IBU, price for 8 oz, price for 13 oz

Linchpin_Tuple = (6.5 , 65 , 4.50 , 6.50)
w, x, y, z = Linchpin_Tuple

print('$', z)