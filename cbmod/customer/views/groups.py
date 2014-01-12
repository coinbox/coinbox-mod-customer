from PySide import QtGui

import cbpos

from cbpos.mod.customer.controllers import CustomerGroupsFormController
from cbpos.mod.customer.models import CustomerGroup

from cbpos.mod.base.views import FormPage

class CustomerGroupsPage(FormPage):
    controller = CustomerGroupsFormController()
    
    def widgets(self):
        menu_restrictions = QtGui.QTreeWidget()
        menu_restrictions.setHeaderHidden(True)
        
        return (("name", QtGui.QLineEdit()),
                ("comment", QtGui.QTextEdit()),
                )
    
    def getDataFromControl(self, field):
        if field in ('name', 'comment'):
            data = self.f[field].text()
        return (field, data)
    
    def setDataOnControl(self, field, data):
        if field in ('name', 'comment'):
            self.f[field].setText(data)
