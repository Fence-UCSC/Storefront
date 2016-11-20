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
                Field('user_id', 'reference auth_user'),
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

# Global functions
def email_to_user_name(email):
    """Returns a string corresponding to the user first and last names,
    given the user email."""
    u = db(db.auth_user.email == email).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])

def id_to_user_name(id):
    """Returns a string corresponding to the user first and last names,
    given the user email."""
    u = db(db.auth_user.id == id).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])

def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.utcnow()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 14:
        return "a week ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 62:
        return "a month ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    if day_diff < 730:
        return "a year ago"
    return str(day_diff / 365) + " years ago"
