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
source venv/bin/activated
```

### configuration database and another in app/__init__.py
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://userdb:passworddb@localhost/database_name'
app.config['TEMPLATES_AUTO_RELOAD'] = True #if dont need you can change to False
app.config['SECRET_KEY'] = 'secret_key'
```

### Init Database and Migrate
```
flask db init
flask db migrate
```

### run application
```
flask run
```

you can access in http://localhost:5000

### result
