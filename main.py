from design import Ui_MainWindow

from b2p_parser import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        metainfo, students_list = browse_file('empty.b2p')
        headers = students_list[0].get_all_params_keys()
        model = QStandardItemModel()
        model.setColumnCount(len(headers))
        model.setHorizontalHeaderLabels(headers)

        for row, student in enumerate(students_list):
            row = [QStandardItem(x) for x in student.get_all_params_values()]
            model.appendRow(row)

        self.tableView.setModel(model)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            selected_indexes = self.tableView.selectionModel().selectedIndexes()
            for index in selected_indexes:
                self.tableView.model().setData(index, "")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

# обвязка для запуска
app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec_())


