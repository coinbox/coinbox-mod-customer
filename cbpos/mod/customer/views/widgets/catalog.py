import cbpos

from cbpos.mod.base.views.widgets import Catalog

from cbpos.mod.customer.models import Customer, CustomerGroup

class CustomerCatalog(Catalog):
    
    def getAll(self, search=None):
        session = cbpos.database.session()
        query = session.query(Customer, Customer.name)
        if search is not None:
            query = query.filter(Customer.name.like('%%%s%%' % (search,)))
        return query.all()
    
    def getChildren(self, parent=None, search=None):
        session = cbpos.database.session()

        if parent is None:
            return [session.query(CustomerGroup, CustomerGroup.name).all(),
                    session.query(Customer, Customer.name).filter(~Customer.groups.any()).all()]
        else:
            return [[],
                    session.query(Customer, Customer.name).filter(Customer.groups.contains(parent)).all()]
