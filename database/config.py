SECRET_KEY = 'novic'

# CONEXÃO COM O BANCO DE DADOS (MYSQL)
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'cryptoradar'
        
    )

