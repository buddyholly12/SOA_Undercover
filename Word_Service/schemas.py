from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Int(required=True) 
    status = fields.Str(required=True) 
    created_at = fields.Str(required=True) 
    last_update = fields.Str(required=True) 