from mongoengine import *


MONGDB_DOCKER_IP = '127.0.0.1'
MONGODB_PORT = '27017'
MONGDB_DB = 'wa_mine'

connect('miner', host='mongodb://' +
        MONGDB_DOCKER_IP + ':' + MONGODB_PORT + '/' + MONGDB_DB)


class WebAccessibility(DynamicDocument):
    url = URLField(required=True)
    classification = StringField()
    number_images= IntField()
    number_text= IntField()
    known = IntField()
    potential = IntField()
    likely = IntField()
    description = StringField()
    urltype = StringField()
    keywords = StringField()
    type_known = DictField()
    type_potential = DictField()
    type_likely = DictField()
