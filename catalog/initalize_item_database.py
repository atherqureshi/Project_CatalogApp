#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item

# Raw Data is loading from JSON
import json 


if __name__ == '__main__':
    engine = create_engine('sqlite:///catalog.db')
    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    # A DBSession() instance establishes all conversations with the database
    # and represents a "staging zone" for all the objects loaded into the
    # database session object. Any change made against the objects in the
    # session won't be persisted into the database until you call
    # session.commit(). If you're not happy about the changes, you can
    # revert all of them back to the last commit by calling
    # session.rollback()
    session = DBSession()

    print("Truncating tables in Database")

    # Clear out data in tables 
    session.execute('''DELETE FROM category''')
    session.execute('''DELETE FROM item''')
    session.commit()
    session.close()


    # Read JSON File of Data, to edit raw_data, edit them in raw_data folder
    with open('raw_data/categories.json') as f:
        category_data = json.load(f)
        for category in category_data:
            session.add(Category(name=category['name'], description=category['description']))
            session.commit()

    with open('raw_data/items.json') as f:
        item_data = json.load(f)
        for item in item_data:
            # Grab the category record that the item is attached to each item
            category = session.query(Category).filter_by(name=item['category']).one()
            session.add(Item(name=item['name'],description=item['description'],category=category))
            session.commit()

    print("Loaded Item Catalog Data into DB")
    print("Categories Added: %s" % session.query(Category).count())
    print("Items Added: %s" % session.query(Item).count())