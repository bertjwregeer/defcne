# File: Groups.py
# Author: Bert JW Regeer <bertjw@regeer.org>
# Created: 2013-01-05

from meta import Base
from meta import DBSession


from sqlalchemy import (
        Column,
        ForeignKey,
        Integer,
        PrimaryKeyConstraint,
        String,
        Table,
        Unicode,
        )

from sqlalchemy.orm import (
        relationship,
        )

from user import User

class Group(Base):
    __table__ = Table('groups', Base.metadata,
            Column('id', Integer, primary_key=True, unique=True),
            Column('name', Unicode(256), unique=True, index=True),
            Column('description', Unicode(256)),
            )

    users = relationship("User", secondary="user_groups")

    @classmethod
    def find_group(cls, name):
        return DBSession.query(cls).filter(cls.name == name).first()

    @classmethod
    def find_group_by_id(cls, id):
        return DBSession.query(cls).get(id)


class UserGroups(Base):
    __table__ = Table('user_groups', Base.metadata,
            Column('userid', Integer, ForeignKey('users.id', onupdate="CASCADE", ondelete="CASCADE"), index=True),
            Column('groupid', Integer, ForeignKey('groups.id', onupdate="CASCADE", ondelete="CASCADE"), index=True),

            PrimaryKeyConstraint('userid', 'groupid'),
            )
