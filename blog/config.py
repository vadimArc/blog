import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://vadimvzorov:@localhost:5432/blogful"
    DEBUG = True
    SECRET_KEY = os.environ.get("BLOGFUL_SECRET_KEY", os.urandom(12))

class ProductionConfig(object):
    DEBUG = True

class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://vadimvzorov:@localhost:5432/blogful-test"
    DEBUG = False
    SECRET_KEY = "Not secret"
