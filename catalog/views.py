from pyramid.i18n import TranslationStringFactory
from catalog.models import DBSession


_ = TranslationStringFactory('catalog')

def my_view(request):
    session = DBSession()
    #Use session to make queries
    #session.query()
    return {'project':'catalog'}
