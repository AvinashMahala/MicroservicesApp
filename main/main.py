from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
 'mysql://root:root@db/main'
CORS(app)

# db=SQLAlchemy(app)

# class Product(db.Model):
#     '''
#     now we have to make another change for the id here we will add here.
#     auto increment to false why did i add this field because the product will 
#     not be created in this app the product will be created in 
#     the django app and this app will just catch the event from rabbitmq
#     and it will create the product and when we create the product we don't
#     want the id to be auto increment because the id will be different than the the django app
#     so if we want the same id we have to put it onto incremental false and to insert
#     directly the id as it is from the django app
#     '''
#     id=db.Column(db.Integer, primary_key=True, autoincrement=False)
#     title=db.Column(db.String(200))
#     image=db.Column(db.String(200))

# class ProductUser(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     user_id=db.Column(db.Integer)
#     product_id=db.Column(db.Integer)

#     UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/')
def index():
    return 'Hello World!'

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')