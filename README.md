# Flask-login-MYSQL

This is a simple Flask application to register and login (for development).

## Requirements

- Python 3.7 or higher
- Flask 1.1.2 or higher

## Installation

### Create virtual environment
```
pip install virtualenv
python -m venv venv
```

### Activated environment
```
source venv/bin/activate
```

### configuration database and another in "app/__init__.py"
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://userdb:passworddb@localhost/database_name'
app.config['TEMPLATES_AUTO_RELOAD'] = True #if dont need you can change to False
app.config['SECRET_KEY'] = 'secret_key'
```

### for generate secret_key with python
```
>>> import os
>>> os.urandom(12).hex()
```

### Install Package
```
pip install -r requirements.txt
```

### Init Database and Migrate
```
flask db init
flask db migrate
flask db upgrade
```

### run application
```
flask run -h 0.0.0.0
```

you can access in http://localhost:5000

### result
1. Homepage
<img align="left" alt="Galih's Linkdein" src="https://cloud.bandaacehkota.go.id/index.php/apps/files_sharing/publicpreview/JJo7s6rfgWkK9Dt?x=1902&y=497&a=true&file=1.png&scalingup=0" />

2. Register
<img align="left" alt="Galih's Linkdein" src="https://cloud.bandaacehkota.go.id/index.php/apps/files_sharing/publicpreview/r5JAj5eWkRAkanM?x=1902&y=497&a=true&file=3.png&scalingup=0" />

3. Login
<img align="left" alt="Galih's Linkdein" src="https://cloud.bandaacehkota.go.id/index.php/apps/files_sharing/publicpreview/DjM9R6afqQ7mxyo?x=1902&y=497&a=true&file=2.png&scalingup=0" />

4. Dashboard
<img align="left" alt="Galih's Linkdein" src="https://cloud.bandaacehkota.go.id/index.php/apps/files_sharing/publicpreview/QJR8PGwp9JzCy5T?x=1902&y=497&a=true&file=4.png&scalingup=0" />