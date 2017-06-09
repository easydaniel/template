from flask_restplus import Api, Namespace
import pkgutil
import inspect


api = Api(
    version='1.0',
    title='TodoMVC API',
    description='A simple TodoMVC API',
    doc='/api/docs',
    prefix='/api/v1'
)

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    if hasattr(module, 'api') and isinstance(module.api, Namespace):
        api.add_namespace(module.api)
