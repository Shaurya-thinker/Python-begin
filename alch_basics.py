""" from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///mydatabase.db', echo=True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS people(name str, age int)"))

conn.commit()

from sqlalchemy.orm import Session

session = Session(engine)

session.execute(text('INSERT INTO people (name, age) VALUES ("Mike", 30);'))

session.commit() """



from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, insert, ForeignKey, func

engine = create_engine('sqlite:///mydatabase.db', echo=True)

meta = MetaData()

people = Table(
    "people",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer)
)

things = Table(
    "things",
    meta,
    Column('id', Integer, primary_key=True),
    Column('description', String, nullable=False),
    Column('value', Float),
    Column('owner', Integer, ForeignKey('people.id'))
)

meta.create_all(engine)  #create table in database

conn = engine.connect()

""" insert_statement = people.insert().values(name="Jane", age=24)
result = conn.execute(insert_statement)
conn.commit() """


""" select_statement = people.select()
result = conn.execute(select_statement)

for row in result.fetchall():
    print(row) """


insert_people = people.insert().values([
    {'name': 'Mike', 'age': 30},
    {'name': 'Bob', 'age': 35},
    {'name': 'Anna', 'age': 38},
    {'name': 'John', 'age': 50},
    {'name': 'Clara', 'age': 42},
])

insert_things = things.insert().values([
    {'owner': 2, 'description': 'Laptop', 'value': 800.50},
    {'owner': 2, 'description': 'Mouse', 'value': 50.50},
    {'owner': 2, 'description': 'Keyboard', 'value': 100.50},
    {'owner': 3, 'description': 'Book', 'value': 50},
    {'owner': 4, 'description': 'Bottle', 'value': 10.50},
    {'owner': 5, 'description': 'Speakers', 'value': 80.50},
])
    
# conn.execute(insert_people)
# conn.commit()

# conn.execute(insert_things)
# conn.commit()

""" join_statement = people.outerjoin(things, people.c.id == things.c.owner)
select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement)

result = conn.execute(select_statement)

for row in result.fetchall():
    print(row) """

group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.value)).group_by(things.c.owner).having(func.sum(things.c.value) > 50)

result = conn.execute(group_by_statement)

for row in result.fetchall():
    print(row)