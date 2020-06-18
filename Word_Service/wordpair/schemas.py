from marshmallow import Schema, fields

class BookSchema(Schema):
     id = fields.Int(required=True)	
     id_word_pack = fields.Int(required=True)	
     word_1 = fields.Str(required=True)	
     word_2 = fields.Str(required=True)	
     Status = fields.Str(required=True)	
     created_at = fields.Str(required=True)	
     Updated_at = fields.Str(required=True)