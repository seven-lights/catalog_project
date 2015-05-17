from pyramid.security import (
    Allow,
    Everyone,
    )

USERS = {'admin' : 'admin',
          'guest' : 'guest',
			 'registered' : 'registered'}
GROUPS = {'admin' : ['group:admins','group:registered'],
			'registered' : ['group:registered']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])

class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'view') ,
                (Allow, 'group:registered', 'view_registered'),
                (Allow, 'group:admins', 'edit') ]
    def __init__(self, request):
        pass

