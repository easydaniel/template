from models import db
class Todo(db.Model):

    __tablename__ = 'Todo'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80))

    def __init__(self, id, task):
        self.id = id
        self.task = task

    def __repr__(self):
        return '<Todo %r>' % self.task
