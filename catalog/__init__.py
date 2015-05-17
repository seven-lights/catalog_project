from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory
from sqlalchemy import engine_from_config
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from security import groupfinder

#from pyramid.session import SignedCookieSessionFactory
#session_factory = SignedCookieSessionFactory('itsaseekreet')

from catalog.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a WSGI application.
    It is usually called by the PasteDeploy framework during 
    ``paster serve`` or ``pserve``.
    """
    #SQLAlchemy engine config for main DB 
    #Any setting that begins with 'sqlalchemy.' will be picked up
    db_engine = engine_from_config(settings,'sqlalchemy.')
    #Binding engine to the model
    initialize_sql(db_engine)
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                          root_factory='security.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    
    config.include('pyramid_jinja2')
    
    #The views/routes are added here
    config.add_static_view('static', './static/')
    config.scan()
    config.add_route("base",'/')
    config.add_route("login",'/login')
    config.add_route("list",'/list')
    config.add_route("index",'/index')
    #config.add_view('catalog.views.my_view',
    #route_name="my_route",renderer="mytemplate.jinja2")

    return config.make_wsgi_app()
