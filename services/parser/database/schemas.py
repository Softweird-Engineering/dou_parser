from marshmallow import Schema, fields, validate


class JobSchema(Schema):
    id = fields.Integer(attribute='id')
    title = fields.String(attribute='title', validate=validate.Length(max=200))
    description = fields.String(attribute='description')
    company = fields.String(attribute='company')
    date = fields.Date(attribute='date')

class UserSchema(Schema):
    id = fields.Integer(attribute='id')
    chat_id = fields.Integer(attribute='chat_id')

