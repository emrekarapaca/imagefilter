from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from skimage import io, color


class Conversion:
    """
    Represents an image conversion operation.
    """

    def __init__(self, ui, app):
        """
        Initializes a new instance of the Conversion class.

        :param ui: The user interface.
        :param app: The application.
        """
        self.ui = ui
        self.app = app
    
    def rgb_to_gs(self):
        """
        Converts an RGB image to grayscale.

        This method takes an RGB image as input and returns a grayscale version of the image.

        :return: None
        """
        if self.app.source_image is not None:
            try:
                image = io.imread(self.app.source_image)
                image = image[:,:,:3] 
                gs_image = color.rgb2gray(image)
                self.app.edit.clear_output()
                self.app.output_image = gs_image
                self.app.afterOperation()
                self.app.file.show_output_image(gs_image)
                self.app.statusBar().showMessage("Conversion completed.")
                QTimer.singleShot(5000, self.app.statusBar().clearMessage)
                self.app.edit.image_stack.append(gs_image)
                self.app.edit.current_index += 1
            except IndexError:
                QMessageBox.warning(self.ui.centralwidget,"Warning","Selected image is not in RGB format.")
    
    def rgb_to_hsv(self):
        """
        Converts an RGB image to HSV color space.

        This method takes an RGB image as input and returns the corresponding HSV image.

        :return: None
        """
        if self.app.source_image is not None:
            try: 
                image = io.imread(self.app.source_image)
                image = image[:,:,:3] 
                hsv_image = color.rgb2hsv(image)
                self.app.edit.clear_output()
                self.app.output_image = hsv_image
                self.app.afterOperation()
                self.app.file.show_output_image(hsv_image)
                self.app.statusBar().showMessage("Conversion completed.")
                QTimer.singleShot(5000, self.app.statusBar().clearMessage)
                self.app.edit.image_stack.append(hsv_image)
                self.app.edit.current_index += 1
            except IndexError:
                QMessageBox.warning(self.ui.centralwidget,"Warning","Selected image is not in RGB format.")
                
