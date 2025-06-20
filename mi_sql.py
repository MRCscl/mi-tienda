import mysql.connector


def conectar(consulta_sql, parametros=None):
    """
    Función que establece conexión con la base de datos MySQL y ejecuta consultas
    
    Parámetros:
    consulta_sql (str): Consulta SQL a ejecutar en la base de datos
    
    Retorna:
    list: Resultados de la consulta o None si hay error
    """
    
    # Configuración de credenciales para la conexión
    config = {
        'user': 'uny6nwhsl2130sgv',  
        'password': 'McTB25yUL5RJdeurHpJx',  
        'host': 'bdsukinarwhdghga6v7d-mysql.services.clever-cloud.com',  
        'database': 'bdsukinarwhdghga6v7d',  
        'raise_on_warnings': True  
    }
    
    # Intentamos establecer la conexión y ejecutar la consulta
    try:
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.")
        
        consulta = conexion.cursor()
        
        if parametros:
            consulta.execute(consulta_sql, parametros)
        else:
            consulta.execute(consulta_sql)
            
        # Para operaciones que modifican datos (INSERT, UPDATE, DELETE)
        if consulta_sql.strip().lower().startswith(('insert', 'update', 'delete')):
            conexion.commit()
            
        resultado = consulta.fetchall()
        return resultado
        
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None