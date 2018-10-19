from app.models.product import Product
from tests.base_test import BaseTestCase
from flask import json


product_obj = Product()
class TestProducts(BaseTestCase):

    def test_data_structure(self):
        self.assertTrue(isinstance(product_obj.all_products, list))

    def test_add_product(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="rice", quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "product successfully added")
        self.assertEquals(response.status_code, 201)

    def test_add_product_exists(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))
        response2 = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))    

        reply = json.loads(response2.data)
        self.assertEquals(reply["message"], "product already exists, update its quantity")
        self.assertEquals(response2.status_code, 409)

    def test_add_product_with_without_a_name(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product=" ", quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "product name is missing")
        self.assertEquals(response.status_code, 400)

    def test_add_product_with_no_quantity(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity=" ", price="4000"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "quantity have only digits and must have no white spaces")
        self.assertEquals(response.status_code, 400)

    def test_add_product_with_no_price(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="rice", quantity="20", price=" "),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "price must be only digits and must have no white spaces")
        self.assertEquals(response.status_code, 400)

    def test_fetching_single_product(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products/1",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(response2.status_code, 200)

    def test_fetching_not_exist_single_product(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products/12",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(response2.status_code, 404)    

    def test_add_product_with_short_name(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="ric", quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "product name should be more than 6 characters long")
        self.assertEquals(response.status_code, 400)

    def test_add_product_with_missing_key(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "a 'key(s)' is missing in your request body")
        self.assertEquals(response.status_code, 400)        

    def test_add_product_with_no_price_2(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="rice", quantity="20", price=""),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "price is missing")
        self.assertEquals(response.status_code, 400)

    def test_fetching_products(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(response2.status_code, 200)

    def test_fetching_single_product_with_no_proper_id(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products/q",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(response2.status_code, 400)        
        

