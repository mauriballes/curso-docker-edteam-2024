import psycopg2
import os

from flask import Flask


app = Flask(__name__)


def get_conexion():
	info = ''
	user = os.getenv('DB_USER','edteam-docker_owner')
	password = os.getenv('DB_PASS','l9CrYmiE3tZO')
	host = os.getenv('DB_HOST','ep-odd-sunset-a5buh2xe.us-east-2.aws.neon.tech')
	port = os.getenv('DB_PORT','5432')
	database = os.getenv('DB_NAME','edteam-docker')
	try:
		connection = psycopg2.connect(
			user=user, password=password, 
			host=host, port=port, database=database)
		info = str(connection.get_dsn_parameters())
		connection.close()
	except:
		info = 'ERROR'
	return info


@app.route('/', methods=['GET'])
def index():
	conexion = get_conexion()
	return {
		'mensaje': 'Hola EDTeam', 
		'conexion': conexion
	}


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

