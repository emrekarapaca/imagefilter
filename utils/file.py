from PyQt5.QtWidgets import QFileDialog, QMessageBox
from skimage import io
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QImage
import numpy as np

class File:
    """
    Represents file operations.
    """

    def __init__(self, ui, app):
        """
        Initializes a new instance of the File class.

        :param ui: The user interface.
        :param app: The application.
        """
        self.ui = ui
        self.app = app
        
    def open_source(self):
        """
        Opens a source file.

        This method opens a source file for editing.

        """
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Image Files (*.jpeg *.png *.jpg)")
        file_dialog.exec()
        
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            file_path = selected_files[0]
            if self.app.source_image is not None:
                self.app.edit.clear_source()
            self.app.source_image = file_path
            self.app.afterOpen()
            self.show_source_image(file_path)
            self.app.statusBar().showMessage("File selected.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
            
    def save_output(self):
        """
        Saves the output.

        This method saves the output to a file.

        """
        if self.app.output_image is not None:
            save_path = self.app.source_image
            io.imsave(save_path, self.app.output_image)
            self.app.statusBar().showMessage("Output saved.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
        else:
            QMessageBox.warning(self.ui.centralwidget, "Warning","There is no image to save.")
    
    def save_as_output(self):
        """
        Saves the output with a new filename.

        This method allows saving the output with a different filename.

        """
        if self.app.output_image is not None:
            save_path, _ = QFileDialog.getSaveFileName(self.ui.centralwidget,"Save Output","","JPEG Image (*.jpg)")
            if save_path:
                io.imsave(save_path, self.app.output_image)
                self.app.statusBar().showMessage("Output saved.")
                QTimer.singleShot(5000, self.app.statusBar().clearMessage)
        else:
            QMessageBox.warning(self.ui.centralwidget, "Warning","There is no image to save.")
            
                
    
    def export_as_source(self):
        """
        Exports the output as source code.

        This method exports the output as source code file.

        """
        if self.app.source_image is not None:
            save_path, _ = QFileDialog.getSaveFileName(caption="Export As Source",
                                                       filter="Image Files (*.jpg);; (*.png)")
            if save_path:
                io.imsave(save_path, self.app.source_image)
                self.app.statusBar().showMessage("Source exported.")
                QTimer.singleShot(5000, self.app.statusBar().clearMessage)
        else:
            QMessageBox.warning(self.ui.centralwidget, "Warning","There is no image to save.")
            
            
    
    def export_as_output(self):
        """
        Exports the output.

        This method exports the output to a file.

        """
        if self.app.output_image is not None:
           save_path, _ = QFileDialog.getSaveFileName(caption="Save As Output",
                                                      filter="Image Files (*.jpg);; (*.png)")
           if save_path:
               io.imsave(save_path, self.app.output_image)
               self.app.statusBar().showMessage("Output exported.")
               QTimer.singleShot(2000, self.app.statusBar().clearMessage)
        else:
            QMessageBox.warning(self.ui.centralwidget, "Warning","There is no image to export.")
    
    def close_app(self):
        """
        Closes the application.

        This method closes the application.

        """
        reply = QMessageBox.question(self.app, "Close Application", "Are you sure you want to close the application?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.app.close()
    
    def about_me(self):
        """
        Displays information about the developer.

        This method shows information about the application, such as the version and author.

        """
        message_box = QMessageBox()
        message_box.setWindowTitle("About me")
        message_box.setText("Emre Karapaça\n151220184005")
        message_box.setIcon(QMessageBox.Information)
        message_box.exec()
    
    def show_source_image(self, image_path):
        """
        

        Parameters
        ----------
        image_path : takes source image_path as string
        
        Displays source image.
        
        Returns
        -------
        None.

        """
        pixmap = QPixmap(image_path).scaled(self.ui.source_label.size(), aspectRatioMode=Qt.IgnoreAspectRatio)
        self.ui.source_label.setPixmap(pixmap)
        self.ui.source_label.show()
    
    def show_output(self, image_path):
        """
        

        Parameters
        ----------
        image_path : takes output image_path as string
        
        Displays output image.

        Returns
        -------
        None.

        """
        pixmap = QPixmap(image_path).scaled(self.ui.output_label.size(), aspectRatioMode=Qt.AspectRatioMode.IgnoreAspectRatio)
        self.ui.output_label.setPixmap(pixmap)
        self.ui.output_label.show()
        
    def show_output_image(self, image_array):
        """
        

        Parameters
        ----------
        image_array : takes output image_array as array.
        
        Displays output image.

        Returns
        -------
        None.

        """
        if len(image_array.shape) == 2:
            image_array = (image_array * 255).astype(np.uint8)
            height, width = image_array.shape
            image = QImage(image_array.data, width, height, width, QImage.Format_Grayscale8)
        else:
            image_array = (image_array * 255).astype(np.uint8)
            height, width, _ = image_array.shape
            image = QImage(image_array.data, width, height, width * 3, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image).scaled(self.ui.output_label.size(), aspectRatioMode=Qt.IgnoreAspectRatio)
        self.ui.output_label.setPixmap(pixmap)
        self.ui.source_label.show()
        
            