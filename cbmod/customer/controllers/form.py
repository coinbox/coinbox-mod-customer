import cbpos

from cbmod.customer.models import Customer, CustomerGroup

from cbmod.base.controllers import FormController

class CustomerGroupsFormController(FormController):
    cls = CustomerGroup
    
    def fields(self):
        return {"name": (cbpos.tr.customer._("Name"), ""),
                "comment": (cbpos.tr.customer._("Comment"), ""),
                }
    
    def items(self):
        session = cbpos.database.session()
        return session.query(CustomerGroup)
    
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
        import cbmod.currency.controllers as currency
        
        return {"name": (cbpos.tr.customer._("Name"), ""),
                "code": (cbpos.tr.customer._("Code"), ""),
                "first_name": (cbpos.tr.customer._("First Name"), ""),
                "last_name": (cbpos.tr.customer._("Last Name"), ""),
                "discount": (cbpos.tr.customer._("Discount"), 0),
                "max_debt": (cbpos.tr.customer._("Maximum Debt"), 0),
                "currency": (cbpos.tr.customer._("Preferred Currency"), currency.default),
                "groups": (cbpos.tr.customer._("Groups"), []),
                "comment": (cbpos.tr.customer._("Comment"), ""),
                "contacts": (cbpos.tr.customer._("Contacts"), []),
                "addresses": (cbpos.tr.customer._("Addresses"), []),
                }
    
    def items(self):
        session = cbpos.database.session()
        return session.query(Customer)
    
    def canDeleteItem(self, item):
        return True
    
    def canEditItem(self, item):
        return True
    
    def canAddItem(self):
        return True
    
    def getDataFromItem(self, field, item):
        return getattr(item, field)
