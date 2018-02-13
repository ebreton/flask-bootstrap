from datetime import datetime
from entities import Greeting, storage

greeting_foo = {"name": "foo", "time": datetime(2000, 1, 1)}
greeting_bar = {"name": "bar", "time": datetime(2018, 2, 13)}


def test_format():
    assert repr(Greeting.create_greeting(greeting_bar)) == \
        "<Greeting to bar at 2018-02-13 00:00:00>"


def test_create_greeting_foo():
    greeting = Greeting.create_greeting(greeting_foo)
    assert greeting.name == "foo"


def test_create_greeting_bar():
    greeting = Greeting.create_greeting(greeting_bar)
    assert greeting.name == 'bar'


def test_storage_repr():
    storage.init_app(None)
    assert repr(storage) == '<Store with 0 greetings>'


def test_store_create():
    storage.create(Greeting.create_greeting(greeting_bar))
    storage.create(greeting_foo)
    assert repr(storage) == '<Store with 2 greetings>'
    assert len(storage) == 2


def test_store_flush():
    storage.flush(1)
    assert len(storage) == 1
    storage.flush(0)
    assert len(storage) == 0


def test_store_select():
    assert list(storage.select()) == []
    greeting = Greeting.create_greeting(greeting_foo)
    storage.create(greeting)
    assert list(storage.select()) == [greeting]
    storage.flush(0)


def test_store_get():
    greeting = storage.create(greeting_foo)
    assert storage.get(0) == greeting
    storage.flush(0)
