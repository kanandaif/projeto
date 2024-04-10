import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# 2-Exclusão
id = (1, 2)
cursor.execute(
    """
    DELETE FROM carro
    WHERE id in (?,?)
    """,
    id
)
conexao.commit()