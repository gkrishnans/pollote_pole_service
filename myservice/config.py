class DevConfig:
    CONFIG_NAME = "dev"
    DEBUG = True
    DATABASE = 'pollote'
    DB_HOST = 'localhost'
    DB_PORT = 27017
    #DB_USERNAME = "admin"
    #DB_PASSWORD = 'genie_dev_db_admin'
    #APP_HOST = '127.0.0.1'
    #APP_PORT = '8080'
    #REFRESH_SEC_KEY = '21345'
    #ACCESS_SEC_KEY = '34213'
    #REFRESH_EXP_MIN = 3
    #ACCESS_EXP_MIN = 1


class ProdConfig:
    CONFIG_NAME = "prod"
    DEBUG = False
    CASSANDRA_DB_URI = "cassandra://username:password@localhost/database_name"
    CASSANDRA_KEYSPACE = 'genie'
    CASSANDRA_HOSTS = ['127.0.0.1']
    CQLENG_ALLOW_SCHEMA_MANAGEMENT = 'CQLENG_ALLOW_SCHEMA_MANAGEMENT'
