import requests

"""
=================================================================================================
GET REQUEST
=================================================================================================
"""

#GET
BASE_URL = 'https://fakestoreapi.com'

query_params = {
    "limit": 3
}

response = requests.get(f"{BASE_URL}/products", params=query_params)
print(response.json())

"""
=================================================================================================
GET SINGLE REQUEST
=================================================================================================
"""
#GET single
BASE_URL = 'https://fakestoreapi.com'

response = requests.get(f"{BASE_URL}/products/18")
print(response.json())

"""
=================================================================================================
POST REQUEST
=================================================================================================
"""

#POST
BASE_URL = 'https://fakestoreapi.com'

new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

response = requests.post(f"{BASE_URL}/products", json=new_product)
print(response.json())

"""
=================================================================================================
PUT REQUEST
=================================================================================================
"""

#PUT
BASE_URL = 'https://fakestoreapi.com'

updated_product = {
    "title": 'updated_product_by_ale',
    "category": 'clothing'
}

response = requests.put(f"{BASE_URL}/products/21", json=updated_product)
print(response.json())

"""
=================================================================================================
PATCH REQUEST
=================================================================================================
"""
#PATCH
BASE_URL = 'https://fakestoreapi.com'

updated_product = {
    "category": 'electronic_games'
}

response = requests.patch(f"{BASE_URL}/products/21", json=updated_product)
print(response.json())

"""
=================================================================================================
DELETE REQUEST
=================================================================================================
"""
#DELETE
BASE_URL = 'https://fakestoreapi.com'


response = requests.delete(f"{BASE_URL}/products/21")
print("Succesfully deleted",response.json())