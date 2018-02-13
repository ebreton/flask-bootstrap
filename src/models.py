from flask_sqlalchemy import SQLAlchemy

from entities import Greeting

db = SQLAlchemy()


class DBGreeting(db.Model, Greeting):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    timestamp = db.Column(db.DateTime)

    def __init__(self, name, timestamp=None):
        Greeting.__init__(
            self,
            name,
            timestamp=timestamp
        )

    def __repr__(self):
        return Greeting.__repr__(self)

    @classmethod
    def from_greeting(cls, greeting):
        return cls(
            greeting.name,
            timestamp=greeting.timestamp
        )


class DBStore:

    def __init__(self):
        self.db = db

    def init_db(self):
        self.db.create_all()
        DBGreeting.query.delete()

    def init_app(self, app):
        self.db.init_app(app)

    def get(self, greeting_id):
        return DBGreeting.query.get(greeting_id)

    def select(self):
        greetings = DBGreeting.query.all()
        greetings.reverse()
        return greetings

    def flush(self, size):
        count = len(self)
        if count <= size:
            return
        # FIXME make a bulk delete here
        for greeting in DBGreeting.query.limit(len(self)-size).all():
            db.session.delete(greeting)
        db.session.commit()

    def create(self, greeting):
        if not isinstance(greeting, Greeting):
            greeting = Greeting.create_greeting(greeting)
        db_greeting = DBGreeting.from_greeting(greeting)
        self.db.session.add(db_greeting)
        self.db.session.commit()
        return db_greeting

    def __repr__(self):
        return f"<DBStore with {len(self)} greetings>"

    def __len__(self):
        return DBGreeting.query.count()


storage = DBStore()
