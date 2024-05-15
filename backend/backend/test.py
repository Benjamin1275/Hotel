import jaydebeapi

# Parámetros de conexión
driver = 'org.postgresql.Driver'
url = 'jdbc:postgresql://nombre_servidor.postgres.database.azure.com:5432/nombre_base_datos'
user = 'usuario@nombre_servidor'
password = 'contraseña'

# Ruta al archivo JAR del controlador JDBC
jar_file = "ruta/al/jar/postgresql-42.2.8.jar"

# Establecer la conexión
conn = jaydebeapi.connect(driver, url, {'user': user, 'password': password}, jar_file)

# Realizar consultas y operaciones en la base de datos

# Cerrar la conexión
conn.close()
