# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

import datetime

db.define_table('category',
                Field('name', 'string'),
                Field('description', 'string')
                )

db.define_table('product',
                Field('user_id', 'reference auth_user', default=session.auth.user.id if session.auth else None ),
                Field('category', 'reference category', requires=IS_IN_DB(db, 'category.id', '%(name)s')),
                Field('username', default=session.auth.user.first_name if session.auth else None),
                Field('name', 'string'),
                Field('description', 'text'),
                Field('image', 'upload'),
                Field('created_on', 'datetime', default=datetime.datetime.utcnow()),
                Field('object_status', requires=IS_IN_SET(['New', 'Used', 'Refurbished']), default='New'),
                Field('tags', 'string'),
                Field('status', 'boolean', default=True),
                Field('price', 'double'),
                Field('gps_coordinates_lat', 'double'),
                Field('gps_coordinates_long', 'double')
                )

db.define_table('user_review',
                Field('reviewed_id', 'reference auth_user'),
                Field('user_id', 'reference auth_user', default=session.auth.user.id if session.auth else None),
                Field('title' , 'string'),
                Field('vote', 'integer'),
                Field('description', 'string'),
                Field('created_on', 'datetime', default=datetime.datetime.utcnow()),
                )



# I don't want to display the user email by default in all forms.
db.product.name.requires = IS_NOT_EMPTY()
db.product.user_id.readable = db.product.user_id.writable = False
db.product.created_on.readable = db.product.created_on.writable = False
db.product.username.readable = db.product.username.writable = False
db.product.gps_coordinates_lat.readable = db.product.gps_coordinates_lat.writable = False
db.product.status.readable = db.product.status.writable = False
db.product.gps_coordinates_long.readable = db.product.gps_coordinates_long.writable = False
db.product.created_on.readable = db.product.created_on.writable = False
db.user_review.created_on.readable = db.user_review.created_on.writable = False
db.product.username.readable = db.product.username.writable = False


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
