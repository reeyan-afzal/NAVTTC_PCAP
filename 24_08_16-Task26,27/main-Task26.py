# Exploring Tuples and Dictionaries

dict_1 = {"name": "Reeyan Afzal",
          "email": "reeyanafzal1999@gmail.com",
          "products": ["product_x", "product_y", "product_z"]
          }

dict_2 = {"products": ["product_x", "product_y", "product_z", "product_w"]}

print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())

print()

for product in dict_1['products']:
    print(product)

print()

dict_1.update(dict_2)

print()

dict_1["products"].pop()
print(dict_1)
