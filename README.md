# Proyecto: Operaciones con PostgreSQL usando psycopg2

Este proyecto contiene un script en Python que realiza operaciones básicas con PostgreSQL utilizando la biblioteca `psycopg2`. Estas operaciones incluyen la creación de tablas, inserción de datos, actualización de registros y eliminación de tablas.

---

## **Requisitos Previos**

1. **Python**
   - Instala Python 3.x desde [python.org](https://www.python.org/).

2. **PostgreSQL**
   - Asegúrate de tener PostgreSQL instalado y configurado correctamente.

3. **psycopg2**
   - Instala la biblioteca psycopg2 ejecutando:
     ```bash
     pip install psycopg2
     ```

4. **Credenciales de la base de datos**
   - Reemplaza las credenciales en el código por las correspondientes a tu configuración:
     ```python
     connection = psycopg2.connect(
         host="localhost",
         user="postgres",
         password="tu_contraseña",
         database="nombre_base_datos",
         port="5432"
     )
     ```

---

## **Estructura del Proyecto**

### **Funciones Principales**

1. **`creartabla()`**
   - Crea una tabla llamada `lambda` con las siguientes columnas:
     - `id` (serial, clave primaria)
     - `nombre` (varchar de 50 caracteres)
     - `apellido` (varchar de 50 caracteres)
     - `email` (varchar de 50 caracteres)
   - Si la tabla ya existe, imprime un mensaje de aviso.

2. **`insertarDatos()`**
   - Inserta un registro en la tabla `lambda` con los valores:
     - `nombre`: "jhonatan"
     - `apellido`: "RAMIREZ"
     - `email`: "jhonatan@gmail.com"

3. **`ActualizarDatos()`**
   - Actualiza el campo `nombre` del registro donde el nombre sea "jhonatan" y lo cambia a "Diaril".

4. **`eliminartabla()`**
   - Elimina la tabla `lambda` si existe. Si no existe, imprime un mensaje de aviso.

---

## **Instrucciones de Uso**

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <url_del_repositorio>
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd <nombre_del_proyecto>
   ```

3. Ejecuta el archivo Python:
   ```bash
   python <nombre_del_archivo>.py
   ```

4. Activa las funciones que desees en el script principal:
   - Puedes descomentar las funciones necesarias como:
     ```python
     #creartabla()
     #insertarDatos()
     #ActualizarDatos()
     #eliminartabla()
     ```

---

## **Notas Adicionales**

- **Seguridad:** Nunca expongas tu contraseña o credenciales de la base de datos en repositorios públicos.
- **Manejo de Errores:** Se recomienda mejorar el manejo de excepciones para capturar errores específicos de `psycopg2` y la base de datos.

---

## **Autor**
Jhonatan Ramírez

