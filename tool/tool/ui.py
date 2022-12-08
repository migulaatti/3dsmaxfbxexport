from PySide2.QtWidgets import QWidget, QDialog, QLabel, QPushButton, QLineEdit, QFormLayout, QDateEdit
from pymxs import runtime as rt
from .export import export_files

class PyMaxDialog(QDialog):
    def __init__(self, parent=QWidget.find(rt.windows.getMAXHWND())):
        super(PyMaxDialog, self).__init__(parent)
        self.setWindowTitle('Export tool')
        self.init_ui()

    def init_ui(self):
        """ Prepare Qt UI layout for custom dialog """

        self.nameText = ''
        self.dateText = ''

        label = QLabel("Grabs a .jpg from a gdrive folder, exports .max, and converted .fbx files along with a .json file that includes the name and date, to gdrive")

        #inputmask
        xString = "X"
        for char in xString:
            xString += char * 250

        #text input
        self.name = QLineEdit(self)
        self.name.setInputMask(xString + ";")
        self.name.setMaxLength(250)

        #date input
        self.date = QDateEdit(self)

        btn = QPushButton("Export")

        #export files etc. when button is pressed
        btn.clicked.connect(lambda: export_files(self.nameText, self.dateText))

        #layout
        flo = QFormLayout()
        flo.addRow(label)
        flo.addRow("File name:", self.name)
        flo.addRow("Date:", self.date)
        flo.addRow(btn)

        self.setLayout(flo)

        #get strings from the input field/qlineedit()
        self.name.textChanged[str].connect(self.get_text)
        self.date.editingFinished.connect(self.get_text)
    
    def get_text(self):
            #set string
            self.nameText = self.name.text()
            self.dateText = self.date.date().toString("dd.MM.yyyy")
