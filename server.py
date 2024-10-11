from flask import Flask, render_template, request
from database.db import *
app = Flask(__name__)

@app.route("/")
def home_func():
    return render_template("home.html")

@app.route("/register_page")
def register_page_func():
    return render_template("register.html")

@app.route("/register_user", methods=["post"])
def register_render_func():
    data = request.form
    Fecha_Inicio = data["fechaInicio"]
    Hora_Inicio = data["horaInicio"]
    Fecha_Final = data["fechaFinal"]
    Hora_Final = data["horaFinal"]
    Descripcion_Actividad = data["descripcion"]
    Proyecto = data["proyecto"]
    Horas_Trabajadas = data["horasTrabajadas"]
    add_user(Fecha_Inicio, Hora_Inicio, Fecha_Final,Hora_Final, Descripcion_Actividad, Proyecto, Horas_Trabajadas)
    return "the user was added"

@app.route("/consult_page")
def consult_page_func():
    return "Vista de consultar"

if __name__ == "__main__":
    host = "172.31.39.82" #ip privada AWS
    port = "80"
    app.run(host, port)