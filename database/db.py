import pymysql

db_host = 'database-aws-jmbootcamp.cta2ckqq4c55.us-east-2.rds.amazonaws.com'
db_user = 'jmbootcamp'
db_passw = 'JvMr2024*'

try:
    connection = pymysql.connect(
        host = db_host,
        user = db_user,
        password = db_passw
    )
    print("Succefull connection to DB")
except Exception as err:
    print("Error:", err)
    connection = None

def add_user(Fecha_Inicio, Hora_Inicio, Fecha_Final,Hora_Final,Descripcion_Actividad,Proyecto,Horas_Trabajadas):
    instruction_sql = "INSERT INTO Actividades_Laborales.Actividad_Laboral(Actividad_Id, Fecha_Inicio, Hora_Inicio, Fecha_Final, Hora_FinaL, Descripcion_Actividad, Proyecto, Horas_Trabajadas) VALUES (null, '"+Fecha_Inicio+"', '"+Hora_Inicio+"', '"+Fecha_Final+"', '"+Hora_Final+"', '"+Descripcion_Actividad+"', '"+Proyecto+"', '"+Horas_Trabajadas+"')"
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        connection.commit()
        print("User added")
    except Exception as err:
        print("Error:", err)