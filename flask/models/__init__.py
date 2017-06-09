from flask_sqlalchemy import SQLAlchemy
import pkgutil
import inspect

db = SQLAlchemy()


class Models:
    pass

for loader, name, ispkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for classname, classobj in inspect.getmembers(module, inspect.isclass):
        setattr(Models, classname, classobj)
