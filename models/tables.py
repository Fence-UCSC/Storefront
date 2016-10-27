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
                Field('username', default=session.auth.user.first_name if session.auth else None),
                Field('name', 'string'),
                Field('description', 'text'),
                Field('image', 'upload'),
                Field('created_on', 'datetime', default=datetime.datetime.utcnow()),
                Field('status', requires=IS_IN_SET(['New', 'Used', 'Sold'])),
                Field('tags', 'string'),
                Field('price', 'double'),
                Field('gps_coordinates_lat', 'double'),
                Field('gps_coordinates_long', 'double')
                )

db.define_table('userReview',
                Field('vote', 'integer'),
                Field('description', 'string'),
                Field('created_on', 'datetime', default=datetime.datetime.utcnow()),
                )

# I don't want to display the user email by default in all forms.
db.product.name.requires = IS_NOT_EMPTY()
db.product.user_id.readable = db.product.user_id.writable = False
db.product.created_on.readable = db.product.created_on.writable = False
db.product.username.readable = db.product.username.writable = False


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
