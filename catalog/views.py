from pyramid.i18n import TranslationStringFactory
from catalog.models import DBSession
from pyramid.view import (
    view_config,
    forbidden_view_config,
    )
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )
from pyramid.security import (
    remember,
    forget,
    )

import render_functions as r
import pyramid.session 
from security import USERS

_ = TranslationStringFactory('catalog')

@view_config( route_name='base',renderer = 'templates/base.html.jinja2', permission = 'view')
def base_view(request):
    session = DBSession()
    #Use session to make queries
    #session.query()
   
    return r.get_base_values(request)

@view_config(route_name='login',renderer = 'templates/login.html.jinja2', permission = 'view')
@forbidden_view_config(renderer='templates/login.html.jinja2')
def login_view(request):
	session = DBSession()
	print request.params
	if 'form.submitted' in request.params:
		login = request.params['login']
		password = request.params['password']
		if USERS.get(login)==password:
			headers = remember( request, login )
			return HTTPFound( location = '/index',
                           headers = headers )
	return r.get_base_values(request)

@view_config(route_name='list',renderer = 'templates/listing_3.html.jinja2', permission = 'edit')
def list_view(request):
    session = DBSession()
    #Use session to make queries
    #session.query()
   
    return r.get_base_values(request)

@view_config(route_name='index',renderer = 'templates/index.html.jinja2', permission = 'view')
def index_view(request):
    session = DBSession()
    #Use session to make queries
    #session.query()
    res = r.get_base_values(request)
    res["wolcome_message"] = "Hello World!"
    return res


