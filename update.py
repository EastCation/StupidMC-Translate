import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem, QTextEdit, QLabel
)
import json


class MinecraftVersionViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minecraft 版本查看器")
        self.setGeometry(200, 200, 800, 500)

        # Layouts
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # UI Elements
        self.refresh_button = QPushButton("刷新当前版本")
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["版本号", "发布类型", "发布日期"])
        self.detail_view = QTextEdit()
        self.detail_view.setReadOnly(True)
        self.status_label = QLabel("状态：就绪")

        # Adding elements to the layout
        self.layout.addWidget(self.refresh_button)
        self.layout.addWidget(self.table_widget)
        self.layout.addWidget(QLabel("版本细节："))
        self.layout.addWidget(self.detail_view)
        self.layout.addWidget(self.status_label)

        # Connect signals
        self.refresh_button.clicked.connect(self.load_versions)
        self.table_widget.cellClicked.connect(self.show_version_details)

        # Data
        self.versions = {}

    def load_versions(self):
        """Fetch the version manifest and populate the table."""
        self.status_label.setText("状态：正在下载元文件")
        try:
            url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            self.versions = {version["id"]: version for version in data["versions"]}
            self.table_widget.setRowCount(len(self.versions))

            for row, version in enumerate(data["versions"]):
                self.table_widget.setItem(row, 0, QTableWidgetItem(version["id"]))
                self.table_widget.setItem(row, 1, QTableWidgetItem(version["type"]))
                self.table_widget.setItem(row, 2, QTableWidgetItem(version["releaseTime"]))

            self.status_label.setText("状态：版本载入完成！")
        except Exception as e:
            self.status_label.setText(f"Status: Error - {str(e)}")

    def show_version_details(self, row, column):
        """Display details of the selected version."""
        version_id = self.table_widget.item(row, 0).text()
        version_data = self.versions.get(version_id, {})
        self.detail_view.setPlainText(json.dumps(version_data, indent=4))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = MinecraftVersionViewer()
    viewer.show()
    sys.exit(app.exec_())
