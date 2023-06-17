from skimage import io, filters
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer

class Edge:
    """
    Represents an edge detection operation.
    """

    def __init__(self, ui, app):
        """
        Initializes a new instance of the Edge class.

        :param ui: The user interface.
        :param app: The application.
        """
        self.ui = ui
        self.app = app
        
    def roberts(self):
        """
        Applies the Roberts edge detection algorithm.
        """
        if self.app.source_image is not None:
            image = io.imread(self.app.source_image, as_gray=True)
            edge_image = filters.roberts(image)
            self.app.edit.clear_output()
            self.app.output_image = edge_image
            self.app.afterOperation()
            self.app.file.show_output_image(edge_image)
            self.app.statusBar().showMessage("Roberts filter applied.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
            self.app.edit.image_stack.append(edge_image)
            self.app.edit.current_index += 1
            
        else:
            QMessageBox.warning(self.ui.centralwidget, "Warning", "Image not found.")
                
    
    def sobel(self):
        """
        Applies the Sobel edge detection algorithm.
        """
        if self.app.source_image is not None:
            image = io.imread(self.app.source_image, as_gray=True)
            edge_image = filters.sobel(image)
            self.app.edit.clear_output()
            self.app.output_image = edge_image
            self.app.afterOperation()
            self.app.file.show_output_image(edge_image)
            self.app.statusBar().showMessage("Sobel filter applied.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
            self.app.edit.image_stack.append(edge_image)
            self.app.edit.current_index += 1
            
        else:
            QMessageBox.warning(self.ui.centralwidget, "Warning", "Image not found.")
    
    def scharr(self):
        """
        Applies the Scharr edge detection algorithm.
        """
        if self.app.source_image is not None:
            image = io.imread(self.app.source_image, as_gray=True)
            edge_image = filters.scharr(image)
            self.app.edit.clear_output()
            self.app.output_image = edge_image
            self.app.afterOperation()
            self.app.file.show_output_image(edge_image)
            self.app.statusBar().showMessage("Scharr filter applied.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
            self.app.edit.image_stack.append(edge_image)
            self.app.edit.current_index += 1
            
        else:
            QMessageBox.warning(self.ui.centralwidget, "Warning", "Image not found.")
    
    def prewitt(self):
        """
        Applies the Prewitt edge detection algorithm.
        """
        if self.app.source_image is not None:
            image = io.imread(self.app.source_image, as_gray=True)
            edge_image = filters.prewitt(image)
            self.app.edit.clear_output()
            self.app.output_image = edge_image
            self.app.afterOperation()
            self.app.file.show_output_image(edge_image)
            self.app.statusBar().showMessage("Prewitt filter applied.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
            self.app.edit.image_stack.append(edge_image)
            self.app.edit.current_index += 1
            
        else:
            QMessageBox.warning(self.ui.centralwidget, "Warning", "Image not found.")
