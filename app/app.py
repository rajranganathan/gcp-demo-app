from google.cloud import datastore

ds_client = datastore.Client()
KEY_TYPE = 'Record'

def insert(**data):
    entity = datastore.Entity(key=ds_client.key(KEY_TYPE))
    entity.update(**data)
    ds_client.put(entity)

def query(limit):
    return ds_client.query(kind=KEY_TYPE).fetch(limit=limit)
