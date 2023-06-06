import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    database='cadastro',
    password='password',
    cursorclass=pymysql.cursors.DictCursor
    )
cursor = conexao.cursor()