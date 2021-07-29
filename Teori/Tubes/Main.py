# Import classes
from Teori.Tubes.Class.LoginWindow import *
from Teori.Tubes.Class.MenuWindow import *
from Teori.Tubes.Class.GameWindow import *
import mysql.connector

# -- Vars --
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()

# -- Main --
loginWindow = LoginWindow()
loginWindow.setupUi(Form)
Form.show()
sys.exit(app.exec_())
