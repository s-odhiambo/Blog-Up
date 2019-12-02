import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/images'
    SUBJECT_PREFIX = 'BLOG-UP'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:12345@localhost/blog_up'


    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'samuelangienda1998@gmail.com'
    
    MAIL_USE_TLS = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
        debug = os.environ.get("DEBUG")
        SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_CRIMSON_URL")


class TestConfig(Config):
    pass


class DevConfig(Config):
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}