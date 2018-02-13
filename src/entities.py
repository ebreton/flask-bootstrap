""" Wraps data into python objects """
from datetime import datetime
from collections import deque
from itertools import islice


class Greeting:

    def __init__(self, name, timestamp=None):
        self.name = name
        self.timestamp = timestamp or datetime.now()

    def __repr__(self):
        return f"<{self.__class__.__name__} to {self.name} at {str(self.timestamp)}>"

    @classmethod
    def create_greeting(cls, data):
        return cls(
            data.get('name'),
            timestamp=data.get('time')
        )


class Store:

    def __init__(self):
        self.store = deque()

    def _index(self):
        # use index to emulate ids
        for index, greeting in enumerate(self.store):
            greeting.id = index

    def init_db(self):
        pass

    def init_app(self, app):
        pass

    def get(self, greeting_id):
        return self.store[greeting_id]

    def select(self):
        self._index()
        return self.store

    def flush(self, size):
        self.store = deque(islice(self.store, 0, size))
        self._index()

    def create(self, greeting):
        if not isinstance(greeting, Greeting):
            greeting = Greeting.create_greeting(greeting)
        self.store.appendleft(greeting)
        self._index()
        return greeting

    def __repr__(self):
        return f"<Store with {len(self.store)} greetings>"

    def __len__(self):
        return len(self.store)


storage = Store()
