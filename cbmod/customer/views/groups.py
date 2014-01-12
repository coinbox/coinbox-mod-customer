from PySide import QtGui

import cbpos

from cbmod.customer.controllers import CustomerGroupsFormController
from cbmod.customer.models import CustomerGroup

from cbmod.base.views import FormPage

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
