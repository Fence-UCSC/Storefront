# -*- coding: utf-8 -*-

# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# request.requires_https()

# app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig

# once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
else:
    # connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    # store sessions and tickets there
    session.connect(request, response, db=db)
    #
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))

# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

# choose a style for forms
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# (optional) static assets folder versioning
# response.static_version = '0.0.0'

# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

## after auth = Auth(db)
auth.settings.extra_fields['auth_user'] = [
  Field('city'),
  Field('phone'),
  Field('lati', 'double'),
  Field('longi', 'double'),
  Field('review')]


## before auth.define_tables(username=True)

# create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

auth.settings.actions_disabled=['register','change_password','request_reset_password']
    #url="http://localhost:8000/%s/default/user/login" % request.application)

# configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True


# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield


import urllib2
from gluon.contrib.login_methods.oauth20_account import OAuthAccount

try:
    import json
except ImportError:
    from gluon.contrib import simplejson as json


class googleAccount(OAuthAccount):
    AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
    TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
    client_id = "33082267259-p2krav5l7kv6edb5i3dutur38p6mta4t.apps.googleusercontent.com"
    client_secret = "_HCLW6wrSk_v48vlwPX_mPDJ"

    def __init__(self):
        OAuthAccount.__init__(self,
                              client_id=self.client_id,
                              client_secret=self.client_secret,
                              auth_url=self.AUTH_URL,
                              token_url=self.TOKEN_URL,
                              approval_prompt='force', state='auth_provider=google',
                              scope='https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email')

    def get_user(self):
        token = self.accessToken()
        if not token:
            return None

        uinfo_url = 'https://www.googleapis.com/oauth2/v1/userinfo?access_token=%s' % urllib2.quote(token, safe='')
        uinfo = None
        try:
            uinfo_stream = urllib2.urlopen(uinfo_url)
        except:
            session.token = None
            return
        data = uinfo_stream.read()
        pic = "http://picasaweb.google.com/data/entry/api/user/ uinfo['id']  ?alt=json"
        uinfo = json.loads(data)
        return dict(first_name=uinfo['given_name'],
                    last_name=uinfo['family_name'],
                    username=uinfo['id'], email=uinfo['email'], pic=pic)


auth.settings.login_form = googleAccount()
db.auth_user.lati.readable = db.auth_user.lati.writable = False
db.auth_user.lati.readable = db.auth_user.lati.writable = False
db.auth_user.longi.readable = db.auth_user.longi.writable = False
db.auth_user.email.readable = db.auth_user.email.writable = False
db.auth_user.review.readable = db.auth_user.review.writable = False


######################
# Logging
import logging, sys
FORMAT = "%(asctime)s %(levelname)s %(process)s %(thread)s %(funcName)s():%(lineno)d %(message)s"
logging.basicConfig(stream=sys.stderr)
logger = logging.getLogger(request.application)
logger.setLevel(logging.INFO)

# Let's log the request.
logger.info("====> Request: %r %r %r %r" % (request.env.request_method, request.env.path_info, request.args, request.vars))
