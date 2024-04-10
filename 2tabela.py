import sqlite3

#1-Conectando no BD
conexao= sqlite3.connect('banco.db')

#cursor- para fazer conexão dentro do banco de dados
cursor= conexao.cursor()

#2-Criação da tabela 
cursor.execute(
    """
        CREATE TABLE carro (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL ,
        ano INT NOT NULL,
        potenciaMotor REAL NOT NULL,
        marca TEXT NOT NULL
        );
    """
)

conexao.close()
print("Tabela foi criada")
