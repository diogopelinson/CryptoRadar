import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='admin'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)


cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `cryptoradar`;")
cursor.execute("CREATE DATABASE `cryptoradar`;")
cursor.execute("USE `cryptoradar`;")

# criando tabelas
TABLES = {}

TABLES['usuarios'] = ('''
    CREATE TABLE `usuarios` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,                  
    `usuario` varchar(20) NOT NULL,
    `email` varchar(100) NOT NULL UNIQUE,                 
    `senha` varchar(100) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (usuario, email, senha) VALUES (%s, %s, %s)'
usuarios = [
    ('Jay Hawkins', 'jay@hotmail.com', generate_password_hash('jay123').decode('utf-8')),
    ('Tyler Ortiz', 'tyler@host.com', generate_password_hash('tyler123').decode('utf-8')),
]

cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from cryptoradar.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])


# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()