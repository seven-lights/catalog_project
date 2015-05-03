from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory
from sqlalchemy import engine_from_config

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
    
    config = Configurator(settings=settings)
    
    config.include('pyramid_jinja2')
    
    #The views/routes are added here
    config.add_static_view('static', 'static')
    
    config.add_route("my_route",'/')
    config.add_view('catalog.views.my_view',
                    route_name="my_route",renderer="mytemplate.jinja2")
    
    return config.make_wsgi_app()
