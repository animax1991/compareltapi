class ProductService:
    def __init__(self):
        return

    @staticmethod
    def findWithTitle(productTitle):
        from api.product import models
        product = models.Product.query.filter_by(title=productTitle).first()
        if product:
            return True
        return False
        #return models.Product.query.filter_by(title=item).all(), 200

    @staticmethod
    def addProduct(title,picture,link,price):
        from api.product import models
        from api.app import db
        product = models.Product(title=title, picture=picture, link=link, price=price)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def loadProduct():
        from api.product import models
        products = models.Product.query.all()

        if products:
            #output = jsonify(Product=[product.serialize() for product in products])
            # output = ''
            # for product in products:
            #     output = output+product

            #json_string = json.dumps([product  for product in products])
            #data = json.load(json_string)
            data = []
            for product in products:
                 data.append(product.serialize())
            #jsonify(products.serialize())

            #output = json.dumps(products.serialize())
            return data
        return False

    @staticmethod
    def loadProductData(productTitle):
        from api.product import models
        product = models.Product.query.filter_by(title=productTitle).first()

        if product:
            return product.serialize()
        return False