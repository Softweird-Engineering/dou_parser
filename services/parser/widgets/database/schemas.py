from marshmallow import Schema, fields, validate


class JobSchema(Schema):
    id = fields.Integer(attribute='id')
    link = fields.String(attribute='link', validate=validate.URL(relative=False), required=True)


class UserSchema(Schema):
    id = fields.Integer(attribute='id')
    chat_id = fields.Integer(attribute='chat_id')

