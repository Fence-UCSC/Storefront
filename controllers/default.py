# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import random

def search():
    # setting number of results per page
    results_per_page = 20
    start_idx = (int(request.vars.page)-1) * results_per_page if request.vars.page is not None else 0
    end_idx = int(request.vars.page) * results_per_page if request.vars.page is not None else results_per_page

    # get search categories form database
    search_categories = db().select(db.category.ALL)

    # performing search as user required
    search_key = request.vars.search_key
    search_option = request.vars.search_options
    rows = ''
    page_result = ''

    if search_key is '':
        redirect(URL('default', 'search'))
    elif search_key is not None:
        if search_option is None or search_option == 'all':
            rows = db(db.product.name.contains(search_key)).select()
            page_result = db(db.product.name.contains(search_key)).select(orderby=~db.product.created_on, limitby=(start_idx, end_idx))
        elif search_option.isdigit():
            q = (db.product.username.contains(search_key)) and (db.product.category == search_option)
            rows = db(q).select()
            page_result = db(q).select(orderby=~db.product.created_on, limitby=(start_idx, end_idx))
        else:
            pass

    # decide the amount of pages
    total_results = len(rows)
    if (total_results % results_per_page) is 0:
        num_of_page = total_results / results_per_page
    else:
        num_of_page = 1 + (total_results / results_per_page)

    return dict(results=page_result,
                search_key=search_key,
                total_results=total_results,
                num_of_page=num_of_page,
                search_categories=search_categories)

flavor_desc = [
    "We make sales personal.",
    "We connect people.",
    "Making trading easy.",
    "The new way to trade.",
    "Helping you find stuff in your neighborhood."
    ]
flavor_welcome = [
    "We're glad see you back!",
    "Hope you're having a nice day.",
    "Let's start selling!",
    "Check out what's new."
]

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
    products = db(db.product.status == True).select(
        orderby=~db.product.created_on, limitby=(0, 20)
    )

    flavortext = ""
    if auth.user_id is None:
        flavortext = random.choice(flavor_desc)
    else:
        flavortext = random.choice(flavor_welcome)

    return dict(message=T('Welcome to web2py!'),
                products=products,
                pretty_date=pretty_date,
                email_to_user_name=email_to_user_name,
                flavortext=flavortext)


    #stores = [
    #    dict(id=1,store_name="Target",store_uname="target"),
    #    dict(id=2,store_name="Safeway",store_uname="safeway"),
    #    dict(id=3,store_name="Baytree Bookstore",store_uname="ucsc")
    #]
    #return dict(message=T('Welcome to web2py!'),stores=stores,email_to_name=email_to_name)

def product():
    if db(db.category.id > 0).isempty():
        db.category.insert(name='Arts, Crafts & Sewing', description='Arts, Crafts & Sewing description')
        db.category.insert(name='Automotive Parts & Accessories', description='Automotive Parts & Accessories description')
        db.category.insert(name='Baby', description='Baby description')
        db.category.insert(name='Beauty & Personal Care', description='Beauty & personal care description')
        db.category.insert(name='Books', description='Books description')
        db.category.insert(name='CD & Vinyl', description='CD & Vinyl description')
        db.category.insert(name='Cell Phones & Accessories', description='Cell Phones & Accessories description')
        db.category.insert(name='Clothing, Shoes & Jewelry', description='Clothing Shoes & Jewelry description')
        db.category.insert(name='Computers', description='Computers description')
        db.category.insert(name='Game & Toys', description='Game description')
        db.category.insert(name='Electronics', description='Electronics description')
        db.category.insert(name='Grocery & Gourmet', description='Grocery Gourmet description')
        db.category.insert(name='Handmade', description='Handmade description')
        db.category.insert(name='Services', description='Services description')
        db.category.insert(name='Home & Kitchen', description=' description')
        db.category.insert(name='Luggage & Traveling Gear', description='Home & Traveling Gear description')
        db.category.insert(name='Music Instrument', description='Music Instrument description')
        db.category.insert(name='Office Products', description='Office Products description')
        db.category.insert(name='Pet Supplies', description='Pet Supplies description')
        db.category.insert(name='Software', description='Software description')
        db.category.insert(name='Vehicles', description='Vehicles description')
        db.category.insert(name='Wine', description='Wine description')
    form = None
    page_type = None
    product = None
    if request.args(0) is None:
        redirect(URL(args="add"))
    elif request.args(0) == "add":
        if auth.user_id is None:
            session.flash = T('Not logged in')
            redirect(URL('user', vars={'_next': URL('default/product', 'add')}))
        page_type = 'create'
        form = SQLFORM(db.product, showuser_id=False)
        form.add_button(T('Cancel'),URL('index'),_class='btn btn-warning')
    else:
        try:
            product = db(db.product.id == request.args(0)).select().first()
        except ValueError:
            session.flash = T('Invalid product id ' + request.args(0))
            redirect(URL('index'))
        if product is None:
            session.flash = T('Product #' + request.args(0) + ' does not exist')
            redirect(URL('default', 'index'))
        if product.user_id != auth.user_id:
            page_type = 'view'
            if not product.status:
                session.flash = T('Product no longer available')
                redirect(URL('index'))
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
    return dict(form=form,
                page_type=page_type,
                product=product,
                pretty_date=pretty_date,
                email_to_user_name=email_to_user_name)


def store():
    if request.args(0) is None:
        stores = db(db.auth_user).select(orderby=db.auth_user.first_name.lower())
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
            products = db(db.product.user_id == store).select(orderby=~db.product.created_on,limitby=(0, 5))
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
