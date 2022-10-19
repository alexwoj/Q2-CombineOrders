from combineorders.orders import Orders

orders = [70, 30, 10]
n_max = 100
expected_orders = 2

how_many = Orders().combine_orders(orders, n_max)
print(how_many)
assert how_many == expected_orders
