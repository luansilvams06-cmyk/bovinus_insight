
from flask import Flask, render_template, request
from collections import Counter
from database import criar_tabelas, conectar

app = Flask(__name__)


criar_tabelas()
def buscar_registros(tabela):
    tabelas_permitidas = ["pratos", "filas", "mesas", "qualidade"]

    if tabela not in tabelas_permitidas:
        return []

    conexao = conectar()
    registros = conexao.execute(
        f"SELECT * FROM {tabela} ORDER BY id"
    ).fetchall()
    conexao.close()

    return [dict(registro) for registro in registros]

registros_pratos = []
registros_filas = []
registros_mesas = []
registros_qualidade = []


def calcular_indicadores():
    registros = buscar_registros("pratos")

    quantidade = len(registros)

    peso_total = sum(
        float(registro["peso"])
        for registro in registros
    )

    categorias = Counter(
        registro["categoria"]
        for registro in registros
    )

    if categorias:
        categoria_principal = categorias.most_common(1)[0][0]
    else:
        categoria_principal = "Nenhuma"

    return {
        "quantidade": quantidade,
        "peso_total": peso_total,
        "categoria_principal": categoria_principal,
        "grafico_labels": list(categorias.keys()),
        "grafico_valores": list(categorias.values())
    }

def calcular_indicadores_filas():
    registros = buscar_registros("filas")

    quantidade = len(registros)

    if quantidade > 0:
        tempos = [int(registro["tempo"]) for registro in registros]
        media = sum(tempos) / quantidade
        maior = max(tempos)
    else:
        media = 0
        maior = 0

    return {
        "quantidade": quantidade,
        "media": round(media, 1),
        "maior": maior
    }

@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        indicadores_pratos=calcular_indicadores(),
        indicadores_filas=calcular_indicadores_filas(),
       total_avaliacoes=len(buscar_registros("qualidade"))
    )


@app.route("/modulo/<nome>")
def modulo(nome):
    modulos = {
        "pratos": "Plate Analytics",
        "filas": "Flow Analytics",
        "mesas": "Table Analytics",
        "qualidade": "Food Feedback"
    }

    if nome not in modulos:
        return "Módulo não encontrado", 404

    if nome == "pratos":
        return render_template(
            "pratos.html",
            registros=buscar_registros("pratos"),
            indicadores=calcular_indicadores()
        )

    if nome == "filas":
        return render_template(
        "filas.html",
        registros=buscar_registros("filas"),
        indicadores=calcular_indicadores_filas()
    )
    if nome == "mesas":
        return render_template(
        "mesas.html",
        registros=buscar_registros("mesas")
    )
    if nome == "qualidade":
        return render_template(
        "qualidade.html",
        registros=buscar_registros("qualidade")
    )

    return f"""
    <h1>{modulos[nome]}</h1>
    <p>Módulo do Bovinus Insight</p>
    <a href="/">Voltar ao painel</a>
    """


@app.route("/registrar-prato", methods=["POST"])
def registrar_prato():
    conexao = conectar()

    conexao.execute(
        """
        INSERT INTO pratos (alimento, categoria, peso)
        VALUES (?, ?, ?)
        """,
        (
            request.form.get("alimento"),
            request.form.get("categoria"),
            request.form.get("peso")
        )
    )

    conexao.commit()
    conexao.close()

    return render_template(
        "pratos.html",
        registros=buscar_registros("pratos"),
        indicadores=calcular_indicadores(),
        mensagem="Alimento registrado com sucesso!"
    )


@app.route("/registrar-fila", methods=["POST"])
def registrar_fila():
    conexao = conectar()

    conexao.execute(
        """
        INSERT INTO filas (etapa, tempo)
        VALUES (?, ?)
        """,
        (
            request.form.get("etapa"),
            request.form.get("tempo")
        )
    )

    conexao.commit()
    conexao.close()

    return render_template(
        "filas.html",
        registros=buscar_registros("filas"),
        indicadores=calcular_indicadores_filas(),
        mensagem="Tempo de espera registrado com sucesso!"
    )

@app.route("/registrar-mesa", methods=["POST"])
def registrar_mesa():
    conexao = conectar()

    conexao.execute(
        """
        INSERT INTO mesas (mesa, status, tempo)
        VALUES (?, ?, ?)
        """,
        (
            request.form.get("mesa"),
            request.form.get("status"),
            request.form.get("tempo") or "Não informado"
        )
    )

    conexao.commit()
    conexao.close()

    return render_template(
        "mesas.html",
        registros=buscar_registros("mesas"),
        mensagem="Mesa registrada com sucesso!"
    )


@app.route("/registrar-qualidade", methods=["POST"])
def registrar_qualidade():
    conexao = conectar()

    conexao.execute(
        """
        INSERT INTO qualidade (alimento, nota, sobras, comentario)
        VALUES (?, ?, ?, ?)
        """,
        (
            request.form.get("alimento"),
            request.form.get("nota"),
            request.form.get("sobras"),
            request.form.get("comentario")
        )
    )

    conexao.commit()
    conexao.close()

    return render_template(
        "qualidade.html",
        registros=buscar_registros("qualidade"),
        mensagem="Avaliação registrada com sucesso!"
    )
if __name__ == "__main__":  
    app.run(debug=True)
