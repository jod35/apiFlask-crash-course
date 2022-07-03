from apiflask.schemas import Schema
from apiflask import fields


"""
    class Task:
        id int
        content str
        date_added datetime
        is_complete bool
"""


class TaskOutputSchema(Schema):
    id = fields.Integer()
    content = fields.String()
    date_added = fields.DateTime()
    is_complete = fields.Boolean()


class TaskCreateSchema(Schema):
    content = fields.String(required=True)


class TaskUpdateSchema(Schema):
    content = fields.String(required=True)
    is_complete = fields.Boolean(required=True)
