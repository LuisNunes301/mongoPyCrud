from pymongo import MongoClient

uri = 'mongodb://root:pass@localhost:27017/'

client = MongoClient(uri)


db = client['Luis']  # Tradicional
coll = db['pessoas']

def insert(**args):
    coll.insert(args)
    # coll.insert(
    #     {}  # dict
    # )
def read(**args):
    """
    Um único registro: find_one
    find
    find_one
    find_many
    """
    coll.find(  # vários
       args
    )


def update(**args):
    coll.update(args
    )


def delete(**args):
    coll.remove(args

    )