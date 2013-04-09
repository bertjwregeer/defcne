# File: acl.py
# Author: Bert JW Regeer <bertjw@regeer.org>
# Created: 2013-02-08

from pyramid.security import (
        ALL_PERMISSIONS,
        Allow,
        Authenticated,
        Deny,
        Everyone,
        )

import models as m

# The traversal for /user/

class User(object):
    __acl__ = [
                (Allow, Authenticated, 'view'),
                (Allow, Authenticated, 'edit'),
              ]

    def __init__(self, request):
        pass

    def __getitem__(self, key):
        raise KeyError

# The traversal for /u/

class Username(object):
    __acl__ = []

    def __init__(self, request):
        pass

    def __getitem__(self, key):
        raise KeyError


# The traversal for /g/

class Goons(object):
    __acl__ = []

    def __init__(self, request):
        pass

    def __getitem__(self, key):
        raise KeyError

# The traversal for /e/

class Events(object):
    __acl__ = [
                (Allow, Authenticated, 'create'),
            ]

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        try:
            if key == 'create':
                return EventCreate(self, self.request)

            dc = int(key)
            return DefconEvent(self, dc)

        except ValueError:
            raise KeyError

class EventCreate(object):
    def __init__(self, parent, request):
        self.__parent__ = parent
        self.__name__ = 'create'
        self.request = request

    def __getitem__(self, key):
        raise KeyError

class DefconEvent(object):
    def __init__(self, events, dc):
        self.__parent__ = events
        self.__name__ = dc
        self.dc = dc

    def __getitem__(self, key):
        event = m.Event.find_event_short(key)

        if event is None:
            return None
        else:
            return Event(self, event)

class Event(object):
    @property
    def __acl__(self):

        acl = [
                (Allow, "group:administrators", 'edit'),
                (Allow, "group:administrators", 'view'),
                (Allow, "group:staff", 'edit'),
                (Allow, "group:staff", 'view'),
                ]

        for user in self.event.owner:
            acl.append((Allow, "userid:{id}".format(id=user.id), 'edit'))
            acl.append((Allow, "userid:{id}".format(id=user.id), 'manage'))
        return acl

    def __init__(self, dc, event):
        self.__parent__ = self.dc = dc
        self.event = event
        self.__name__ = event.shortname

    def __getitem__(self, key):
        raise KeyError

# The traversal for /magic/

class Magic(object):
    __acl__ = [
                (Allow, 'group:administrators', 'view'),
                (Allow, 'group:administrators', 'edit'),
                (Allow, 'group:staff', 'view'),
                (Allow, 'group:staff', 'edit'),
              ]

    def __init__(self, request):
        pass

    def __getitem__(self, key):
        raise KeyError

