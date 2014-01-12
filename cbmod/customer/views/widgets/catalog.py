import cbpos

from cbmod.base.views.widgets import Catalog

from cbmod.customer.models import Customer, CustomerGroup

class CustomerCatalog(Catalog):
    
    def getAll(self, search=None):
        session = cbpos.database.session()
        query = session.query(Customer)
        if search is not None:
            query = query.filter(Customer.name.like('%%%s%%' % (search,)))
        return query
    
    def getChildren(self, parent=None, search=None):
        session = cbpos.database.session()

        if parent is None:
            return [session.query(CustomerGroup),
                    session.query(Customer).filter(~Customer.groups.any())]
        else:
            return [[],
                    session.query(Customer).filter(Customer.groups.contains(parent))]
