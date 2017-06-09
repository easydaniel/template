from flask_restplus import Namespace, Resource, fields
from flask import request
from models import db, Models

api = Namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})


@api.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @api.doc('list_todos')
    @api.header('Authorization', 'JWT Token', required=True)
    @api.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return Models.Todo.query.all()

    @api.doc('create_todo')
    @api.expect(todo)
    @api.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        payload = request.get_json()
        NewTask = Models.Todo(payload.get('id'), payload.get('task'))
        db.session.add(NewTask)
        db.session.commit()
        return NewTask, 201


@api.route('/<int:id>')
@api.response(404, 'Todo not found')
@api.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @api.doc('get_todo')
    @api.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return Models.Todo.query.filter_by(id=id).first()

    @api.doc('delete_todo')
    @api.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        NewTask = Models.Todo.query.filter_by(id=id).first()
        if NewTask:
            db.session.delete(NewTask)
            db.session.commit()
            return '', 204
        return '', 404

    @api.expect(todo)
    @api.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        payload = request.get_json()
        Target = Models.Todo.query.filter_by(id=id).first()
        Target.task = payload.get('task')
        db.session.commit()
        return 'Target'
