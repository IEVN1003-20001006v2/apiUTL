class DevelopmentConfig:
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'  # Asegúrate de agregar tu usuario de MySQL
    MYSQL_PASSWORD = ''  # Cambia esto si tu contraseña es diferente
    MYSQL_DB = 'api_utl'
 
config = {
    'development': DevelopmentConfig
}