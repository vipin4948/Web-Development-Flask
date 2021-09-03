# __init__ under myproject
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

#setting up key for form
app.config['SECRET_KEY'] = 'mysecretkey'

#setting up base directory


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')

#track changes
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# creating DATABASE by passing application into SQLAlchemy
db = SQLAlchemy(app)
#migrating whole thing by conncetion application to the database
Migrate(app,db)

# NOTE! These imports need to come after you've defined db, otherwise you will
# get errors in your models.py files.
## Grab the blueprints from the other views.py files for each "app"
from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint,url_prefix="/owners")
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
