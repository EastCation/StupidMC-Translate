import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QHBoxLayout

class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("沙雕翻译包实用程序（测试版）")
        self.setGeometry(100, 100, 800, 600)

        self.tableWidget = QTableWidget()
        self.loadButton = QPushButton("载入翻译文件")
        self.saveButton = QPushButton("写入翻译文件")
        self.insertButton = QPushButton("插入键值与键名")

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.loadButton)
        buttonLayout.addWidget(self.saveButton)
        buttonLayout.addWidget(self.insertButton)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addLayout(buttonLayout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.loadButton.clicked.connect(self.load_json)
        self.saveButton.clicked.connect(self.save_json)
        self.insertButton.clicked.connect(self.insert_row)

    def load_json(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "打开翻译文件", "", "JSON Files (*.json);;All Files (*)", options=options)
        if fileName:
            try:
                with open(fileName, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.tableWidget.setRowCount(len(data))
                    self.tableWidget.setColumnCount(2)
                    self.tableWidget.setHorizontalHeaderLabels(["本地化键名", "键值"])

                    for row, (key, value) in enumerate(data.items()):
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(key))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(value))

                    # 调整Value列的宽度
                    self.tableWidget.setColumnWidth(1, 400)
            except Exception as e:
                QMessageBox.warning(self, "呜喵~ 出错啦！", f"无法载入文件，原因如下: {e}")

    def save_json(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "保存翻译文件", "", "JSON Files (*.json);;All Files (*)", options=options)
        if fileName:
            try:
                data = {}
                for row in range(self.tableWidget.rowCount()):
                    key = self.tableWidget.item(row, 0).text()
                    value = self.tableWidget.item(row, 1).text()
                    data[key] = value

                with open(fileName, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
            except Exception as e:
                QMessageBox.warning(self, "呜喵~ 出错啦！", f"无法写入文件，原因如下: {e}")

    def insert_row(self):
        currentRow = self.tableWidget.currentRow()
        if currentRow == -1:  # 如果没有选中任何行，则在末尾插入
            currentRow = self.tableWidget.rowCount()
        self.tableWidget.insertRow(currentRow)
        self.tableWidget.setItem(currentRow, 0, QTableWidgetItem("新的本地化键名"))
        self.tableWidget.setItem(currentRow, 1, QTableWidgetItem("新的键值"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec_())
