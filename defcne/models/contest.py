from meta import Base
from meta import DBSession

from sqlalchemy import (
        Boolean,
        CheckConstraint,
        Column,
        DateTime,
        ForeignKey,
        Index,
        Integer,
        PrimaryKeyConstraint,
        String,
        Table,
        Unicode,
        UnicodeText,
        and_,
        )

from sqlalchemy.orm import (
        contains_eager,
        noload,
        relationship,
        )

from sqlalchemy.ext.hybrid import hybrid_property
from cvebase import (
        CVEBase,
        Power,
        WiredInternet,
        AccessPoint,
        )


class Contest(CVEBase):
    __table__ = Table('contests', Base.metadata,
            Column('id', Integer, ForeignKey('cve.id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
            Column('hrsofoperation', Unicode),
            Column('spacereq', Unicode),
            Column('tables', Integer),
            Column('chairs', Integer),
            Column('signage', UnicodeText),
            Column('projectors', Integer),
            Column('screens', Integer),
            Column('represent', Unicode),
            Column('numparticipants', Integer),
            Column('years', Integer),
            Column('blackbadge', Boolean, default=False),
            Column('blackbadge_consideration', UnicodeText),
            )
    __mapper_args__ = {
                'polymorphic_identity': 'contest',
            }

    power = relationship("Power")
    drops = relationship("WiredInternet")
    aps = relationship("AccessPoint")

    def from_appstruct(self, appstruct):
        super(Contest, self).from_appstruct(appstruct)

        self.hrsofoperation = appstruct['hrsofoperation']
        self.spacereq = appstruct['spacereq']
        self.tables = appstruct['tables']
        self.chairs = appstruct['chairs']
        self.signage = appstruct['signage']
        self.projectors = appstruct['projectors']
        self.screens = appstruct['screens']
        self.represent = appstruct['represent']
        self.numparticipants = appstruct['numparticipants']
        self.years = appstruct['years']
        self.blackbadge_consideration = appstruct['blackbadge_consideration']

        new_power_ids = set([p['id'] for p in appstruct['power'] if p['id'] != -1])
        cur_power_ids = set([p.id for p in self.power])
        del_power_ids = cur_power_ids - new_power_ids

        if len(del_power_ids):
            for power in self.power:
                if power.id in del_power_ids:
                    DBSession.delete(power)

        for power in appstruct['power']:
            if power['id'] in cur_power_ids:
                cur_power = [p for p in event.power if p.id == power['id']][0]
                cur_power.from_appstruct(power)
            else:
                npower = Power()
                npower.from_appstruct(power)
                self.power.append(npower)

        new_drop_ids = set([d['id'] for d in appstruct['drops'] if d['id'] != -1])
        cur_drop_ids = set([d.id for d in self.drops])
        del_drop_ids = cur_drop_ids - new_drop_ids

        if len(del_drop_ids):
            for drop in self.drops:
                if drop.id in del_drop_ids:
                    DBSession.delete(drop)

        for drop in appstruct['drops']:
            if drop['id'] in cur_drop_ids:
                cur_drop = [d for d in self.drops if d.id == drop['id']][0]
                cur_drop.from_appstruct(drop)
            else:
                ndrop = WiredInternet()
                ndrop.from_appstruct(drop)
                self.drops.append(ndrop)

        new_ap_ids = set([a['id'] for a in appstruct['aps'] if a['id'] != -1])
        cur_ap_ids = set([a.id for a in self.aps])
        del_ap_ids = cur_ap_ids - new_ap_ids

        if len(del_ap_ids):
            for ap in self.aps:
                if ap.id in del_ap_ids:
                    DBSession.delete(ap)

        for ap in appstruct['aps']:
            if ap['id'] in cur_ap_ids:
                cur_ap = [a for a in self.aps if a.id == ap['id']][0]
                cur_ap.from_appstruct(appstruct)
            else:
                nap = AccessPoint()
                nap.from_appstruct(ap)
                self.aps.append(nap)

    def to_appstruct(self):
        ret = super(Contest, self).to_appstruct()

        ret.update(
                    {
                        'id': self.id,
                        'hrsofoperation': self.hrsofoperation,
                        'spacereq': self.spacereq,
                        'tables': self.tables,
                        'chairs': self.chairs,
                        'signage': self.signage,
                        'projectors': self.projectors,
                        'screens': self.screens,
                        'represent': self.represent,
                        'numparticipants': self.numparticipants,
                        'years': self.years,
                        'blackbadge': self.blackbadge,
                        'blackbadge_consideration': self.blackbadge_consideration,
                        'power': [power.to_appstruct() for power in self.power],
                        'drops': [drop.to_appstruct() for drop in self.drops],
                        'aps': [ap.to_appstruct() for ap in self.aps],
                    }
                )

        return ret
