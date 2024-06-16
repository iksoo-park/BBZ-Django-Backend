import os.path

from product.entity.models import Product
from product.repositiory.product_repository import ProductRepository


class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return Product.objects.all()

    def create(self, productName, productLocation, productActivity, productDining, productPrice, productImage):
        uploadDirectory = r"/Users/j213h/Documents/Python/SKN AI Camp/proj/SK-Networks-AI-1/ui/JaehyukHan/first/src/assets/images/uploadImages"

        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, productImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in productImage.chunks():
                destination.write(chunk)

        product = Product(
            productName=productName,
            productLocation=productLocation,
            productActivity=productActivity,
            productDining=productDining,
            productPrice=productPrice
        )
        product.save()
        return product
