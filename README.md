# Como usar app de flask
Corra estos comandos en su terminal
```bash
python3 -m venv env
```
Activa el entorno virtual, este comando puede variar segun tu sistema operativo
```bash
source env/bin/activate
```
```bash
pip install -r requirements.txt
```
Este comando activa la app en el 127.0.0.1:5000
```bash
python app_flask/main.py
```

## Observaciones
- Se ha cargado un script que arma un esquema y llena una base de datos en mysql

- En el archivo conexion.py se usan variables de entorno, ignore de la linea 1 a la 6 y reemplaze lo necesario en las lineas 13 y 14
