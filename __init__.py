import cbpos
from cbpos.modules import BaseModuleLoader

class ModuleLoader(BaseModuleLoader):
    dependencies = ('base', 'currency')
    config = []
    name = 'Customer and Customer Groups Support'

    def load(self):
        from cbpos.mod.customer.models import Customer
        from cbpos.mod.customer.models import CustomerGroup
        from cbpos.mod.customer.models import CustomerContact
        from cbpos.mod.customer.models import CustomerAddress
        return [Customer, CustomerGroup, CustomerContact, CustomerAddress]

    def test(self):
        from cbpos.mod.customer.models.customer import Customer
        from cbpos.mod.customer.models.group import CustomerGroup
        from cbpos.mod.customer.models.contact import CustomerContact
        from cbpos.mod.customer.models.address import CustomerAddress
    
        session = cbpos.database.session()
    
        cg1 = CustomerGroup(name='Delivery', comment='Customers whose newspapers are being delivered to.')
        cg2 = CustomerGroup(name='Library', comment='Customers who have an account at the library.')
        cg3 = CustomerGroup(name='Offices', comment='Customers who buy products for their offices and/or companies.')
        
        from cbpos.mod.currency.models.currency import Currency
        LL = session.query(Currency).filter_by(id=1).one()
        
        c1 = Customer(name='Abou El Jouj', code=None, first_name='Jad', last_name='Kik',
                      max_debt=200000, currency=LL, comment='This guy talks too much.', discount=0.5, groups=[cg1, cg2])
        c2 = Customer(name='Abou El Imm', code='123', first_name='Imad', last_name='Ferneine',
                      max_debt=None, currency=LL, comment='He is egyptian!', discount=0, groups=[cg3])
    
        cc1 = CustomerContact(name='email', value='jadkik94@gmail.com', customer=c1)
        cc2 = CustomerContact(name='mobile', value='70695924', customer=c1)
        cc3 = CustomerContact(name='phone', value='04972721', customer=c1)
        cc4 = CustomerContact(name='phone', value='+9701238422', customer=c2)
        
        ca1 = CustomerAddress(country='Lebanon', region='Metn', city='Beit Mery', details='Tal3it Kafra', customer=c1)
        ca2 = CustomerAddress(country='Lebanon', region='Beirut', city='Ashrafieh', details='7ad el dekkeneh', customer=c2)
    
        session.add(c1)
        session.add(c2)
        session.commit()

    def menu(self):
        from cbpos.mod.customer.pages import CustomersPage
        from cbpos.mod.customer.pages import CustomerGroupsPage
            
        return [[{'label': 'Customers', 'rel': 1, 'priority': 3, 'image': self.res('images/menu-root-customers.png')}],
                [{'parent': 'Customers', 'label': 'Customers', 'page': CustomersPage, 'image': self.res('images/menu-customers.png')},
                 {'parent': 'Customers', 'label': 'Groups', 'page': CustomerGroupsPage, 'image': self.res('images/menu-groups.png')}]]
