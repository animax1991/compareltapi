from flask_restx import Namespace, Resource, reqparse, fields
from flask import flash
from api.product.service import *

Product = Namespace(name="Product", description="Product API")

product_fields = Product.inherit('Get Product', {
    'productTitle': fields.String(description='Product Title', required=True, example="DKU"),
    'productPicture': fields.String(description='Product Picture', required=True, example="picturelink"),
    'productLink': fields.String(description='Product Link', required=True, example="www.abc.com"),
    'productPrice': fields.String(description='Product Price', required=True, example="20"),
})

parser = reqparse.RequestParser()
parser.add_argument('productTitle', type=str)
parser.add_argument('productPicture', type=str)
parser.add_argument('productLink', type=str)
parser.add_argument('productPrice', type=str)


@Product.route('/all')
class Products(Resource):
    @Product.doc(response={200:'OK'})
    @Product.doc(response={400:'BAD REQUEST'})
    def get(self):
         return ProductService.loadProduct(),200

@Product.route('/Duplicated/<string:productTitle>')
class ProductDuplicated(Resource):
    @Product.doc(response={200:'OK'})
    @Product.doc(response={400:'BAD REQUEST'})
    def get(self,productTitle):
        if ProductService.findWithTitle(productTitle) == True:
            return True,200
        else:
            return False,200

@Product.route('/<string:productTitle>')
class ProductDetail(Resource):
    @Product.doc(response={200:'OK'})
    @Product.doc(response={400:'BAD REQUEST'})
    def get(self,productTitle):
     return ProductService.loadProductData(productTitle),200