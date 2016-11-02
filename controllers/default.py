# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def email_to_name(email):
    """Returns a string corresponding to the user first and last names,
    given the user email."""
    u = db(db.auth_user.email == email).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])


def geolocation():
    row = ''
    return dict(row=row)


def search():
    search_key = request.vars.search_key
    search_option = request.vars.search_options
    rows = ''
    if search_key is '':
        redirect(URL('search'))
    if search_key is not None:
        if search_option == 'user':
            rows = db(db.product.username.contains(search_key)).select()
        else:
            rows = db(db.product.name.contains(search_key)).select()

    return dict(result=rows)


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
    elif isinstance(time,datetime):
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
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    #response.flash = T("Hello World")
    products = None

    # Gets the list of all checklists for the user.
    products = db().select(
        db.product.ALL, orderby=~db.product.created_on, limitby=(0, 10)
    )



    return dict(message=T('Welcome to web2py!'), products=products, date=pretty_date, email_to_name=email_to_name)


    #stores = [
    #    dict(id=1,store_name="Target",store_uname="target"),
    #    dict(id=2,store_name="Safeway",store_uname="safeway"),
    #    dict(id=3,store_name="Baytree Bookstore",store_uname="ucsc")
    #]
    #return dict(message=T('Welcome to web2py!'),stores=stores,email_to_name=email_to_name)

def product():
    if db(db.category.id > 0).isempty():
        db.category.insert(name='Books', description='Books description')
        db.category.insert(name='Phones', description='Phones description')
        db.category.insert(name='Other', description='Other description')
    form = None
    page_type = None
    product = None
    if request.args(0) is None:
        if auth.user_id is None:
            session.flash = T('Not logged in')
            redirect(URL('default', 'user', vars={'_next': 'product'}))
        page_type = 'create'
        form = SQLFORM(db.product, showuser_id=False)
        form.add_button(T('Cancel'),URL('index'),_class='btn btn-warning')
    else:
        product = db(db.product.id == request.args(0)).select().first()
        if product is None:
            session.flash = T('Product #' + request.args(0) + ' does not exist')
            redirect(URL('default', 'index'))
        if product.user_id != auth.user_id:
            page_type = 'view'
        else:
            page_type = 'edit'
            form = SQLFORM(db.product, product, deletable=True, showid=False)
            form.add_button(T('Cancel'),URL('product', args=product.id),_class='btn btn-warning')
    if form is not None and form.process().accepted:
        if page_type == 'create':
            session.flash = T('Added product listing')
        elif page_type == 'edit':
            session.flash = T('Edited product listing')
        redirect(URL('product', args=form.vars.id))
    return dict(form=form, page_type=page_type, product=product)

def store():
    if request.args(0) is None:
        stores = db(db.auth_user).select(orderby=~db.auth_user.first_name)
        products = None
    else:
        store = request.args(0)
        try:
            stores = db(db.auth_user.id == store).select()
        except ValueError:
            session.flash = T('Store ' + store + ' undefined.')
            redirect(URL('default', 'store'))
        if stores.first() is None:
            session.flash = T('Store ' + store + ' not found.')
            redirect(URL('default', 'store'))
        else:
            products = db(db.product.user_id == store).select(orderby=~db.product.created_on)
    return dict(stores=stores,products=products)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
