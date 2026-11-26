
import sqlite3

def conectar():
    conexao = sqlite3.connect("bovinus.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pratos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alimento TEXT NOT NULL,
            categoria TEXT NOT NULL,
            peso REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS filas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            etapa TEXT NOT NULL,
            tempo INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mesas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mesa TEXT NOT NULL,
            status TEXT NOT NULL,
            tempo TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS qualidade (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alimento TEXT NOT NULL,
            nota INTEGER NOT NULL,
            sobras TEXT NOT NULL,
            comentario TEXT
        )
    """)

    conexao.commit()
    conexao.close()
