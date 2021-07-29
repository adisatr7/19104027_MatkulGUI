# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.tabpane_login_window = QtWidgets.QTabWidget(Form)
        self.tabpane_login_window.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.tabpane_login_window.setObjectName("tabpane_login_window")
        self.tab_login = QtWidgets.QWidget()
        self.tab_login.setObjectName("tab_login")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_login)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 90, 191, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.login_layout_form = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.login_layout_form.setContentsMargins(0, 0, 0, 0)
        self.login_layout_form.setObjectName("login_layout_form")
        self.login_label_username = QtWidgets.QLabel(self.formLayoutWidget)
        self.login_label_username.setObjectName("login_label_username")
        self.login_layout_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.login_label_username)
        self.login_label_password = QtWidgets.QLabel(self.formLayoutWidget)
        self.login_label_password.setObjectName("login_label_password")
        self.login_layout_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.login_label_password)
        self.login_field_username = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.login_field_username.setObjectName("login_field_username")
        self.login_layout_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.login_field_username)
        self.login_field_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.login_field_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_field_password.setObjectName("login_field_password")
        self.login_layout_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.login_field_password)
        self.login_button = QtWidgets.QPushButton(self.tab_login)
        self.login_button.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.login_button.setObjectName("login_button")
        self.tabpane_login_window.addTab(self.tab_login, "")
        self.tab_register = QtWidgets.QWidget()
        self.tab_register.setObjectName("tab_register")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_register)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(80, 60, 241, 111))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.register_layout_form = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.register_layout_form.setContentsMargins(0, 0, 0, 0)
        self.register_layout_form.setObjectName("register_layout_form")
        self.register_label_username = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.register_label_username.setObjectName("register_label_username")
        self.register_layout_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.register_label_username)
        self.register_field_username = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.register_field_username.setObjectName("register_field_username")
        self.register_layout_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.register_field_username)
        self.register_password_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.register_password_label.setObjectName("register_password_label")
        self.register_layout_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.register_password_label)
        self.register_field_password = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.register_field_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_field_password.setObjectName("register_field_password")
        self.register_layout_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.register_field_password)
        self.register_field_confirmpassword = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.register_field_confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_field_confirmpassword.setObjectName("register_field_confirmpassword")
        self.register_layout_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.register_field_confirmpassword)
        self.register_field_email = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.register_field_email.setObjectName("register_field_email")
        self.register_layout_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.register_field_email)
        self.register_label_email = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.register_label_email.setObjectName("register_label_email")
        self.register_layout_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.register_label_email)
        self.register_label_confirmpassword = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.register_label_confirmpassword.setObjectName("register_label_confirmpassword")
        self.register_layout_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.register_label_confirmpassword)
        self.register_button = QtWidgets.QPushButton(self.tab_register)
        self.register_button.setGeometry(QtCore.QRect(160, 210, 75, 23))
        self.register_button.setObjectName("register_button")
        self.tabpane_login_window.addTab(self.tab_register, "")

        self.retranslateUi(Form)
        self.tabpane_login_window.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.login_label_username.setText(_translate("Form", "Username:"))
        self.login_label_password.setText(_translate("Form", "Password:"))
        self.login_button.setText(_translate("Form", "Login"))
        self.tabpane_login_window.setTabText(self.tabpane_login_window.indexOf(self.tab_login), _translate("Form", "Login"))
        self.register_label_username.setText(_translate("Form", "Username:"))
        self.register_password_label.setText(_translate("Form", "Password:"))
        self.register_label_email.setText(_translate("Form", "Email"))
        self.register_label_confirmpassword.setText(_translate("Form", "Confirm Password"))
        self.register_button.setText(_translate("Form", "Register"))
        self.tabpane_login_window.setTabText(self.tabpane_login_window.indexOf(self.tab_register), _translate("Form", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
