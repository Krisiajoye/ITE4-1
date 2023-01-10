from django.core.files import File
from models import productTable

def upload():
    name = input("Product Name: ")
    price = int(input("Price: "))
    image_url = input("Image address: ")
    f = open(image_url, 'rb')
    m = productTable(prod_name=name, prod_price=price, image=File(f))
    m.save()

upload()