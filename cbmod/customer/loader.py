import cbpos
from cbpos.modules import BaseModuleLoader

class ModuleLoader(BaseModuleLoader):
    def load_models(self):
        from cbmod.customer.models import Customer, CustomerGroup, CustomerContact, CustomerAddress
        return [Customer, CustomerGroup, CustomerContact, CustomerAddress]

    def test_models(self):
        from cbmod.customer.models import Customer, CustomerGroup, CustomerContact, CustomerAddress
    
        session = cbpos.database.session()
    
        cg1 = CustomerGroup(name='Delivery', comment='Customers whose newspapers are being delivered to.')
        cg2 = CustomerGroup(name='Library', comment='Customers who have an account at the library.')
        cg3 = CustomerGroup(name='Offices', comment='Customers who buy products for their offices and/or companies.')
        
        from cbmod.currency.models import Currency
        LBP = session.query(Currency).filter_by(id="LBP").one()
        
        c1 = Customer(name='Abou El Jouj', code=None, first_name='Jad', last_name='Kik',
                      max_debt=200000, currency=LBP, comment='This guy talks too much.', discount=50, groups=[cg1, cg2])
        c2 = Customer(name='Abou El Imm', code='123', first_name='Imad', last_name='Ferneine',
                      max_debt=None, currency=LBP, comment='He is egyptian!', discount=0, groups=[cg3])
    
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
        from cbpos.interface import MenuRoot, MenuItem
        from cbmod.customer.views import CustomersPage, CustomerGroupsPage
        
        return [[MenuRoot('customers',
                          label=cbpos.tr.customer_('Customers'),
                          icon=cbpos.res.customer('images/menu-root-customers.png'),
                          rel=1,
                          priority=3
                          )],
                [MenuItem('customers', parent='customers',
                          label=cbpos.tr.customer_('Customers'),
                          icon=cbpos.res.customer('images/menu-customers.png'),
                          page=CustomersPage
                          ),
                 MenuItem('customer-groups', parent='customers',
                          label=cbpos.tr.customer_('Groups'),
                          icon=cbpos.res.customer('images/menu-groups.png'),
                          page=CustomerGroupsPage
                          )
                 ]
                ]
