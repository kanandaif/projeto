import sqlite3

#1-Conectando no BD
conexao= sqlite3.connect('banco.db')

#cursor- para fazer conexão dentro do banco de dados
cursor= conexao.cursor()

#2- Inserindo dados
cursor.execute(
    """
        INSERT INTO carro (nome, ano, potenciaMotor,marca)
        VALUES ('S10 Midnight', 2024, 2.8, 'chevrolet')
    """
)
cursor.execute(
    """
        INSERT INTO carro (nome, ano, potenciaMotor,marca)
        VALUES ('Ford Raptor', 2023, 3.0, 'Ford')
    """
)
cursor.execute(
    """
        INSERT INTO carro (nome, ano, potenciaMotor,marca)
        VALUES ('Fiat Toro Ultra', 2022, 2.0, 'Fiat')
    """
)
conexao.commit()