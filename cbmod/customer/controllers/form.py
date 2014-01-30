import cbpos

from cbmod.customer.models import Customer, CustomerGroup

from cbmod.base.controllers import FormController

class CustomerGroupsFormController(FormController):
    cls = CustomerGroup
    
    def fields(self):
        return {"name": (cbpos.tr.customer_("Name"), ""),
                "comment": (cbpos.tr.customer_("Comment"), ""),
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
        
        return {"name": (cbpos.tr.customer_("Name"), ""),
                "code": (cbpos.tr.customer_("Code"), ""),
                "first_name": (cbpos.tr.customer_("First Name"), ""),
                "last_name": (cbpos.tr.customer_("Last Name"), ""),
                "discount": (cbpos.tr.customer_("Discount"), 0),
                "max_debt": (cbpos.tr.customer_("Maximum Debt"), 0),
                "currency": (cbpos.tr.customer_("Preferred Currency"), currency.default),
                "groups": (cbpos.tr.customer_("Groups"), []),
                "comment": (cbpos.tr.customer_("Comment"), ""),
                "contacts": (cbpos.tr.customer_("Contacts"), []),
                "addresses": (cbpos.tr.customer_("Addresses"), []),
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
