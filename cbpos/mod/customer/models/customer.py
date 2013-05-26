import cbpos

import cbpos.database
import cbpos.mod.base.models.common as common

import cbpos.mod.currency.controllers as currency

from cbpos.mod.currency.models import Currency, CurrencyValue
from cbpos.mod.sales.models import TicketLine
from cbpos.mod.sales.models import Ticket

from sqlalchemy import func, Table, Column, Integer, String, Float, Boolean, MetaData, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method, Comparator

customer_group_link = Table('customer_group', cbpos.database.Base.metadata,
    Column('customer_id', Integer, ForeignKey('customers.id')),
    Column('group_id', Integer, ForeignKey('customergroups.id'))
)

class Customer(cbpos.database.Base, common.Item):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    code = Column(String(255), nullable=True, unique=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    discount = Column(Integer, nullable=False, default=0)
    max_debt = Column(CurrencyValue(), nullable=True)
    currency_id = Column(String(3), ForeignKey('currencies.id'))
    comment = Column(String(255), nullable=True)

    groups = relationship("CustomerGroup", secondary=customer_group_link, backref="customers")
    currency = relationship("Currency", backref="customers")

    @hybrid_property
    def debt(self):
        session = cbpos.database.session()
        query = session.query(func.sum(TicketLine.total), Currency) \
                             .filter((TicketLine.ticket_id == Ticket.id) & \
                                     (Ticket.customer == self) & \
                                     (Ticket.currency_id == Currency.id) & \
                                     (Ticket.payment_method == 'debt') & \
                                     ~Ticket.paid) \
                            .group_by(Ticket.currency_id)
        total = sum(currency.convert(c_total, c, self.currency) for (c_total, c) in query)
        return total

    @hybrid_property
    def display(self):
        return self.name
    
    @display.expression
    def display(self):
        return self.name

    def __repr__(self):
        return "<Customer %s>" % (self.name,)
