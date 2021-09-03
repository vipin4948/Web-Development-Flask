#  MODELS.PY
#setup db inside __init__.py under myproject
from myproject import db

class Puppy(db.Model):

    #setting up table name
    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    #adding relation ship between owner Column one to one relationship
    owner = db.relationship('Owner',backref ='puppy',uselist = False)



    def __init__(self,name):
        self.name = name

    #represnation to object

    def __repr__(self):
        if self.owner:
            return f"puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name: {self.name} and no owner assinged it"


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey("puppies.id"))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner name :{self.name}"
