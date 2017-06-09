from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from views.index import index_view
from models import db
from apis import api
import config

app = Flask(__name__, static_url_path='/static')
app.config.from_object(config.DevelopmentConfig)

for ext in (db, api):
    ext.init_app(app)

app.register_blueprint(index_view)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
