from hello import create_app

app, nav, storage = create_app(storage_type="models.storage")
app.app_context().push()
storage.init_db()

foo = {"name": "foo"}
bar = {"name": "bar"}


def test_format():
    assert repr(storage) == "<DBStore with 0 greetings>"


def test_create_foo():
    db_greeting = storage.create(foo)
    assert db_greeting.name == 'foo'


def test_create_bar():
    db_greeting = storage.create(bar)
    assert db_greeting.name == 'bar'
    assert len(storage) == 2


def test_store_create():
    storage.create(bar)
    storage.create(foo)
    assert repr(storage) == '<DBStore with 4 greetings>'
    assert len(storage) == 4


def test_store_flush():
    storage.flush(1)
    assert len(storage) == 1
    storage.flush(0)
    storage.flush(2)
    assert len(storage) == 0


def test_store_select():
    assert list(storage.select()) == []
    db_greeting = storage.create(bar)
    assert list(storage.select()) == [db_greeting]
    storage.flush(0)


def test_store_get():
    db_greeting = storage.create(foo)
    assert storage.get(db_greeting.id) == db_greeting
    storage.flush(0)
