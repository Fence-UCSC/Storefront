# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

import datetime

db.define_table('product',
                Field('user_id', 'reference auth_user', default=session.auth.user.id if session.auth else None ),
                Field('product_name', 'string'),
                Field('product_description', 'text'),
                Field('created_on', 'datetime', default=datetime.datetime.utcnow()),
                Field('price', 'double'),
                Field('gps_coordinates', 'double')
                )

# I don't want to display the user email by default in all forms.
db.product.product_name.requires = IS_NOT_EMPTY()
db.product.user_id.readable = db.product.user_id.writable = False
db.product.created_on.readable = db.product.created_on.writable = False


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
