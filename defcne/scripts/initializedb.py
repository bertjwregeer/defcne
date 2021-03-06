import os
import sys
import transaction
import datetime

from sqlalchemy import engine_from_config
from sqlalchemy.exc import IntegrityError

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import *

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


defaults = {
        'groups': [
            (u'event_owners', u'Event owners'),
            (u'event_staff', u'Event staff'),
            (u'event_maybe', u'Possible event owner. Once event is approved becomes an event owner'),
            (u'goons', u'Defcon Contests and Events goons'),
            (u'staff', u'Defcon staff'),
            (u'administrators', u'Site administrators')
            ],
        'users': [
            (u'X-Istence', u'Bert JW Regeer', u'xistence@0x58.com', 'testing123'),
            ],
        'user_groups': [
            (u'X-Istence', u'administrators'),
            (u'X-Istence', u'goons'),
            (u'X-Istence', u'staff'),
            ],
        'defcon': [
            (21, u'http://www.defcon.org'),
            (22, u'http://www.defcon.org'),
            ]
        }

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    with transaction.manager:
        for (kw, items) in defaults.items():
            if kw == 'groups':
                for (name, desc) in items:
                    sp = transaction.savepoint()
                    try:
                        group = Group(name=name, description=desc)
                        DBSession.add(group)
                        DBSession.flush()
                    except IntegrityError, e:
                        sp.rollback()
                        print 'Group "{name}" already exists.'.format(name=name)
            if kw == 'users':
                for (u, r, e, c) in items:
                    sp = transaction.savepoint()
                    try:
                        user = User(username=u, realname=r, email=e, credentials=c, validated=True)
                        DBSession.add(user)
                        DBSession.flush()
                    except IntegrityError, e:
                        sp.rollback()
                        print 'User "{name}" already exists.'.format(name=u)
            if kw == 'user_groups':
                for (u, g) in items:
                    sp = transaction.savepoint()
                    try:
                        user = User.find_user(u)
                        group = Group.find_group(g)

                        user.groups.append(group)

                        DBSession.flush()
                    except IntegrityError, e:
                        sp.rollback()
                        print 'User "{name}" already part of "{group}"'.format(name=u, group=g)
            if kw == 'defcon':
                for (i, u) in items:
                    sp = transaction.savepoint()
                    try:
                        dc = Defcon(id=i, url=u)
                        DBSession.add(dc)
                        DBSession.flush()
                    except IntegrityError, e:
                        sp.rollback()
                        print 'Defcon "{id}" already exists.'.format(id=i)


