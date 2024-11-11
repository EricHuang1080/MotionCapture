from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QImage, QPixmap, QIcon
import nbimporter
from CamCalibration import camera_calibration
from ui_untitled import Ui_Form

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.button_init()

    #dick
    def happy1(self):
        pass

    def button_init(self):
        # Connect the button to the custom method `run_camera_calibration`
        self.ui.OK.clicked.connect(self.happy)
        self.ui.file_select_btn.clicked.connect(self.read_string)

    def read_string(self):
        
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', '', "Image Files (*.jpg *.gif *.png *.jpeg)")
        CamID=self.ui.CamID.text()
        height=float(self.ui.height.text())
        x_range=float(self.ui.x_range.text())
        y_range=float(self.ui.y_range.text())
        
        camera_calibration(CamID,height,x_range,y_range,file_name)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', '', "Image Files (*.jpg *.gif *.png *.jpeg)")
        if file_name:
            image = QImage(file_name)
            if image.isNull():
                print("Failed to load image.")
            else:
                pixmap = QPixmap.fromImage(image)
                self.ui.label.setPixmap(pixmap)
            self.ui.input_file_path.setText(file_name)  # Assume there's a QLineEdit for the file path



if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()