import psycopg2

connetion = psycopg2.connect(
    host="127.0.0.1",
    user= "postgres",
    password="password",
    database="pastgres",
    port="5434"
)

connetion.autocommit = True

def creartabla():
    cursor = connetion.cursor()
    query = ("CREATE TABLE lambda (id serial PRIMARY KEY, nombre varchar(50), apellido varchar(50), email varchar(50))")
    try:
        cursor.execute(query)
    except:
        print("La tabla ya existe")
    cursor.close()
def isertarDatos():
    cursor = connetion.cursor()
    query = """ INSERT INTO lambda (nombre, apellido, email) VALUES ('jhonatan','RAMIREZ', 'jhonatan@gmail.com' ) """
    cursor.execute(query)
    cursor.close()
def ActualizarDatos():
    cursor = connetion.cursor()
    query = """ UPDATE lambda SET nombre='Diaril' where nombre='jhonatan' """
    cursor.execute(query)
    cursor.close()
def eliminartabla():
    cursor = connetion.cursor()
    query = ("DROP TABLE lambda")
    try:
        cursor.execute(query)
    except:
        print("La tabla no existe")
    cursor.close()

# creartabla()
#eliminartabla()
isertarDatos()
# ActualizarDatos()
