def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Fancy', 'price': 14900}

apply_discount(shoes, 0.25)
# apply_discount(shoes, 2.0)

# def delete_product(prod_id, user):
#     assert user.is_admin(), 'Must be admin'
#     assert store.has_product(prod_id), 'Unknown product'
#     store.get_product(prod_id).delete()

# assert(1 == 2, 'This should fail')
# assert 1 == 2, '2 > ..'

