from flask import Flask , jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
from dataclasses import dataclass

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
 'mysql://root:root@db/main'
CORS(app)

db=SQLAlchemy(app)
migrate = Migrate(app, db)

@dataclass
class Product(db.Model):
    id:int
    title:str
    image:str
    id=db.Column(db.Integer, primary_key=True, autoincrement=False)
    title=db.Column(db.String(200))
    image=db.Column(db.String(200))
    
    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'image': self.image
    #     }
    
    
@dataclass
class ProductUser(db.Model):
    id:int
    user_id:int
    product_id:int
    
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer)
    product_id=db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

# @app.route('/')
# def index():
#     return 'Hello World!'

@app.route('/api/products')
def index():
    # products=Product.query.all()
    # return jsonify([product.to_dict() for product in products])
    return jsonify(Product.query.all())

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')