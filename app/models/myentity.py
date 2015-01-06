from app import db

class Myentity(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    myattr = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            myattr = self.myattr,
            id = self.id
        )

    def __repr__(self):
        return '<Myentity %r>' % (self.id)
