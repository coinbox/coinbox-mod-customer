import cbpos

from cbpos.mod.customer.models import Customer, CustomerGroup

from cbpos.mod.base.controllers import FormController

class CustomerGroupsFormController(FormController):
    cls = CustomerGroup
    
    def fields(self):
        return {"name": (cbpos.tr.auth._("Name"), ""),
                "comment": (cbpos.tr.auth._("Comment"), ""),
                }
    
    def items(self):
        session = cbpos.database.session()
        items = session.query(CustomerGroup.display, CustomerGroup).all()
        return items
    
    def canDeleteItem(self, item):
        return True
    
    def canEditItem(self, item):
        return True
    
    def canAddItem(self):
        return True
    
    def getDataFromItem(self, field, item):
        return getattr(item, field)

class CustomersFormController(FormController):
    cls = Customer
    
    def fields(self):
        import cbpos.mod.currency.controllers as currency
        
        return {"name": (cbpos.tr.auth._("Name"), ""),
                "code": (cbpos.tr.auth._("Code"), ""),
                "first_name": (cbpos.tr.auth._("First Name"), ""),
                "last_name": (cbpos.tr.auth._("Last Name"), ""),
                "discount": (cbpos.tr.auth._("Discount"), 0),
                "max_debt": (cbpos.tr.auth._("Maximum Debt"), 0),
                "currency": (cbpos.tr.auth._("Preferred Currency"), currency.default),
                "groups": (cbpos.tr.auth._("Groups"), []),
                "comment": (cbpos.tr.auth._("Comment"), ""),
                "contacts": (cbpos.tr.auth._("Contacts"), []),
                "addresses": (cbpos.tr.auth._("Addresses"), []),
                }
    
    def items(self):
        session = cbpos.database.session()
        items = session.query(Customer.display, Customer).all()
        return items
    
    def canDeleteItem(self, item):
        return True
    
    def canEditItem(self, item):
        return True
    
    def canAddItem(self):
        return True
    
    def getDataFromItem(self, field, item):
        return getattr(item, field)
