import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# 2-Atualização
id = 1
cursor.execute(
    """
    UPDATE carro set nome = ?
    WHERE id = ?
    """,
    ("S10 Midnight", id)
    
)
conexao.commit()