from PyQt5.QtWidgets import QMessageBox ,QApplication, QLabel, QSpinBox, QDialogButtonBox, QFormLayout, QDialog, QDoubleSpinBox
from skimage import io, color
import numpy as np
from skimage.segmentation import chan_vese, morphological_chan_vese, checkerboard_level_set
from PyQt5.QtCore import QTimer
import time
from skimage.filters import threshold_multiotsu


class Segmentation:
    """
    Represents an image segmentation operation.
    """

    def __init__(self, ui, app):
        """
        Initializes a new instance of the Segmentation class.

        :param ui: The user interface.
        :param app: The application.
        """
        self.ui = ui
        self.app = app
    
    def multi_otsu(self):
        """
        Performs multi-level Otsu image segmentation.

        This method applies the multi-level Otsu algorithm to segment the image.

        """
        if self.app.source_image is not None:
            image = io.imread(self.app.source_image)
            if image.ndim != 2:
                if image.shape[2] == 4:
                    image = image[:,:,:3]
                    
                if image.shape[2] == 3:
                    image = color.rgb2gray(image)
                
            thresholds = threshold_multiotsu(image)
            regions = np.digitize(image, bins=thresholds)
            
        
            
            
            self.app.edit.clear_output()
            self.app.output_image = regions
            self.app.afterOperation()
            self.app.file.show_output_image(regions)
            self.app.statusBar().showMessage("Multi-Otsu completed.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)

            
            
            self.app.edit.image_stack.append(regions)
            self.app.edit.current_index += 1
            
            
                
            
                
        else:
            QMessageBox.warning(self.ui.centralwidget, "Warning", "No source image selected.")
            
    
    def chan_vese(self):
        """
        Performs Chan-Vese image segmentation.

        This method applies the Chan-Vese algorithm to segment the image.

        """
        if self.app.source_image is not None:
            self.app.statusBar().clearMessage()  
            QApplication.processEvents()  
            time.sleep(0.1)  
            self.app.statusBar().showMessage("Processing Chan-Vese...")
            image = io.imread(self.app.source_image)
           
            if image.ndim != 2:
                if image.shape[2] == 4:
                    image = image[:,:,:3]
                    
                if image.shape[2] == 3:
                    image = color.rgb2gray(image)
            
            dialog = QDialog(self.ui.centralwidget)
            dialog.setWindowTitle("Chan-Vese Segmentation")
            
            num_iter_label = QLabel("Number of iterations:")
            num_iter_input = QSpinBox()
            num_iter_input.setMinimum(1)
            num_iter_input.setMaximum(1000)
            num_iter_input.setValue(200)
            
            mu_value_label = QLabel("Mu value (0,1]:")
            mu_value_input = QDoubleSpinBox()
            mu_value_input.setMinimum(0.1)
            mu_value_input.setMaximum(1)
            mu_value_input.setValue(0.5)
            
            dt_value_label = QLabel("dt value:")
            dt_value_input = QDoubleSpinBox()
            dt_value_input.setMinimum(0.1)
            dt_value_input.setValue(0.50)
            
            button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            layout = QFormLayout()
            layout.addRow(num_iter_label, num_iter_input)
            layout.addRow(mu_value_label, mu_value_input)
            layout.addRow(dt_value_label, dt_value_input)
            layout.addRow(button_box)
            dialog.setLayout(layout)
            button_box.accepted.connect(dialog.accept)
            button_box.rejected.connect(dialog.reject)
            
            if dialog.exec() == QDialog.Accepted:
                num_iter = num_iter_input.value()
                mu = mu_value_input.value()
                dt = dt_value_input.value()
            
                cv = chan_vese(image, mu=mu, lambda1=1, lambda2=1, tol=1e-3,
                               max_num_iter=num_iter, dt=dt, init_level_set="checkerboard",
                               extended_output=True)
            
            self.app.edit.clear_output()
            self.app.output_image = cv[0]
            self.app.afterOperation()
            self.app.statusBar().showMessage("Chan-Vese completed.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
            self.app.file.show_output_image(cv[0])
            
            self.app.edit.image_stack.append(cv[0])
            self.app.edit.current_index += 1
            
            
            
                
           
            
                
    
    def morp_snakes(self):
        """
        Performs morphological snakes image segmentation.

        This method applies the morphological snakes algorithm to segment the image.

        """
        if self.app.source_image is not None:
            self.app.statusBar().clearMessage()  
            QApplication.processEvents()  
            time.sleep(0.1)  
            self.app.statusBar().showMessage("Processing Morphological-Snakes...")
            image = io.imread(self.app.source_image)
           
            if image.ndim != 2:
                if image.shape[2] == 4:
                    image = image[:,:,:3]
                    
                if image.shape[2] == 3:
                    image = color.rgb2gray(image)
            
            dialog = QDialog(self.ui.centralwidget)
            dialog.setWindowTitle("Morphological Snakes Segmentation")
            
            
            num_iter_label = QLabel("Number of iterations:")
            num_iter_input = QSpinBox()
            num_iter_input.setMinimum(1)
            num_iter_input.setMaximum(1000)
            num_iter_input.setValue(35)
            
            smoothing_label = QLabel("Smoothing value:")
            smoothing_input = QSpinBox()
            smoothing_input.setMinimum(1)
            smoothing_input.setMaximum(10)
            smoothing_input.setValue(2)
            
            lambda1_label = QLabel("Outer region parameter (l1):")
            lambda1_input = QDoubleSpinBox()
            lambda1_input.setMinimum(0.1)
            lambda1_input.setValue(0.50)
            
            lambda2_label = QLabel("Inner region parameter (l2):")
            lambda2_input = QDoubleSpinBox()
            lambda2_input.setMinimum(0.1)
            lambda2_input.setValue(0.50)
            
            button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            layout = QFormLayout()
            layout.addRow(num_iter_label, num_iter_input)
            layout.addRow(smoothing_label, smoothing_input)
            layout.addRow(lambda1_label, lambda1_input)
            layout.addRow(lambda2_label, lambda2_input)
            layout.addRow(button_box)
            dialog.setLayout(layout)
            button_box.accepted.connect(dialog.accept)
            button_box.rejected.connect(dialog.reject)
            
            if dialog.exec() == QDialog.Accepted:
                num_iter = num_iter_input.value()
                smoothing = smoothing_input.value()
                lambda1 = lambda1_input.value()
                lambda2    = lambda2_input.value()
                init_ls = checkerboard_level_set(image.shape, 6)
                cv =  morphological_chan_vese(image, num_iter=num_iter, init_level_set=init_ls,
                             smoothing=smoothing, lambda1=lambda1, lambda2=lambda2)
            
            self.app.edit.clear_output()
            self.app.output_image = cv
            self.app.afterOperation()
            self.app.statusBar().showMessage("Morphological Snakes completed.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
            
            self.app.file.show_output_image(cv)
            
            self.app.edit.image_stack.append(cv)
            self.app.edit.current_index += 1
