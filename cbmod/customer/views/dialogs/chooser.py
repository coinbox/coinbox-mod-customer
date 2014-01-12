from PySide import QtGui, QtCore

import cbpos

from cbmod.customer.views.widgets import CustomerCatalog

class CustomerChooserDialog(QtGui.QDialog):
    
    chosen = QtCore.Signal('QVariant')
    
    def __init__(self):
        super(CustomerChooserDialog, self).__init__()
        
        self.setModal(True)
        
        self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Reset | QtGui.QDialogButtonBox.Cancel)
        
        self.catalog = CustomerCatalog()
        
        self.selectedLbl = QtGui.QLabel(cbpos.tr.customer._("Selected"))
        self.selected = QtGui.QLineEdit()
        self.selected.setReadOnly(True)
        self.selected.setPlaceholderText(cbpos.tr.customer._("No customer selected"))
        
        selected = QtGui.QHBoxLayout()
        selected.addWidget(self.selectedLbl)
        selected.addWidget(self.selected)
        
        selected.setStretch(0, 0)
        selected.setStretch(1, 1)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.catalog)
        layout.addLayout(selected)
        layout.addWidget(self.buttonBox)
        
        self.setLayout(layout)
        
        self.buttonBox.clicked.connect(self.onButton)
        self.catalog.childSelected.connect(self.onCustomerSelected)
    
    def setCustomer(self, c):
        self.customer = c
        if c is not None:
            self.selected.setText(c.name)
        else:
            self.selected.setText("")
    
    def onButton(self, btn):
        role = self.buttonBox.buttonRole(btn)
        if role == QtGui.QDialogButtonBox.AcceptRole:
            self.accept()
        elif role == QtGui.QDialogButtonBox.RejectRole:
            self.reject()
        elif role == QtGui.QDialogButtonBox.ResetRole:
            self.setCustomer(None)
            self.accept()
    
    def onCustomerSelected(self, c):
        self.setCustomer(c)
