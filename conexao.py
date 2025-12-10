import mysql.connector

conexao = mysql.connector.connect(
    host="Localhost",
    user="root",
    password="87654321",
    database="cep"
)

print("Conexão bem sucedida!")

cursor = conexao.cursor()
cursor.execute("SELECT * FROM sua_tabela LIMIT 5")

resultados = cursor.fetchall()

print("Dados do MySQL:")
for linha in resultados:
    print(linha)

cursor.close()
conexao.close()
