# from flask import Flask, request, jsonify
# from flask_mysqldb import MySQL
# import mysql.connector

# app = Flask(__name__)
# mysql = MySQL(app)
# app.config['MYSQL_HOST'] = 'localhost:3306'  # Dirección de tu servidor MySQL
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'db_pruebas'


# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost:3306",
#         user="root",
#         password="root",
#         database="db_pruebas"
#     )

# @app.route('/usuarios', methods=['GET'])
# def obtener_usuarios():
#     try:
#         cur = mysql.connection.cursor()
#         cur.execute('SELECT * FROM tipo_usuarios')
#         resultados = cur.fetchall()
#         cur.close()
        
#         # Convierte resultados a una lista de diccionarios
#         usuarios = []
#         for fila in resultados:
#             usuarios.append({
#                 'id': fila[0],  # Cambia los índices según tus columnas
#                 'nombre': fila[1],
#             })
        
#         return jsonify(usuarios)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    



# if __name__ == '__main__':
#     app.run(debug=True)