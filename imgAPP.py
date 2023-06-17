from ui.imgAppUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QPushButton
import sys
from utils.file import File
from utils.edit import Edit
from utils.conversion import Conversion
from utils.segmentation import Segmentation
from utils.edgedetection import Edge

class ImgFilterAPP(QMainWindow):
    """
    Represents the main application for the image filtering operation.

    Attributes
    ----------
    ui : Ui_MainWindow
        User interface object.
    file : File
        File-related operations object.
    edit : Edit
        Edit-related operations object.
    conversion : Conversion
        Conversion-related operations object.
    segmentation : Segmentation
        Segmentation-related operations object.
    edge : Edge
        Edge detection-related operations object.
    source_image : None or object
        The source image for filtering.
    output_image : None or object
        The output image after filtering.
    """

    def __init__(self):
        """
        Initializes a new instance of the ImgFilterAPP class.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.file = File(self.ui, self)
        self.edit = Edit(self.ui, self)
        self.conversion = Conversion(self.ui, self)
        self.segmentation = Segmentation(self.ui, self) 
        self.edge = Edge(self.ui, self)

        self.source_image = None #holds path
        self.output_image = None #holds array
        
        self.connections()
        self.firstScreen()
        
        
        
    def connections(self):
        """
        Establishes the connections between the UI elements and the corresponding methods.
        """
        #file menu actions and buttons connections
        self.ui.open_source_action.triggered.connect(self.file.open_source)
        self.ui.save_output_action.triggered.connect(self.file.save_output)
        self.ui.save_as_output_action.triggered.connect(self.file.save_as_output)
        self.ui.export_as_source_action.triggered.connect(self.file.export_as_source)
        self.ui.export_as_output_action.triggered.connect(self.file.export_as_output)
        self.ui.close_action.triggered.connect(self.file.close_app)
        
        #buttons
        self.ui.open_source_button.clicked.connect(self.file.open_source)
        self.ui.save_output_button.clicked.connect(self.file.save_output) 
        self.ui.save_as_output_button.clicked.connect(self.file.save_as_output)
        self.ui.export_as_source_button.clicked.connect(self.file.export_as_source)
        self.ui.export_as_output_button.clicked.connect(self.file.export_as_output)
    
        #edit menu actions and buttons connections
        self.ui.clear_source_action.triggered.connect(self.edit.clear_source)
        self.ui.clear_output_action.triggered.connect(self.edit.clear_output)
        self.ui.undo_output_action.triggered.connect(self.edit.undo_output)
        self.ui.redo_output_action.triggered.connect(self.edit.redo_output)
        
        #buttons
        self.ui.clear_source_button.clicked.connect(self.edit.clear_source)
        self.ui.clear_output_button.clicked.connect(self.edit.clear_output)
        self.ui.undo_output_button.clicked.connect(self.edit.undo_output)
        self.ui.redo_output_button.clicked.connect(self.edit.redo_output)
        
        #conversion menu actions and buttons connections
        self.ui.rgb_to_gs_action.triggered.connect(self.conversion.rgb_to_gs)
        self.ui.rgb_to_hsv_action.triggered.connect(self.conversion.rgb_to_hsv)
        
        #buttons
        self.ui.rgb_to_gs_button.clicked.connect(self.conversion.rgb_to_gs)
        self.ui.rgb_to_hsv_button.clicked.connect(self.conversion.rgb_to_hsv)
        
        #segmentation menu actions and buttons connections
        self.ui.multi_otsu_action.triggered.connect(self.segmentation.multi_otsu)
        self.ui.chan_vese_action.triggered.connect(self.segmentation.chan_vese) 
        self.ui.morphological_snakes_action.triggered.connect(self.segmentation.morp_snakes)
        
        #buttons
        self.ui.multi_otsu_button.clicked.connect(self.segmentation.multi_otsu)
        self.ui.chan_vese_button.clicked.connect(self.segmentation.chan_vese)
        self.ui.morphological_snakes_button.clicked.connect(self.segmentation.morp_snakes)
        
        #edge detection menu actions and buttons connections
        self.ui.roberts_action.triggered.connect(self.edge.roberts)
        self.ui.sobel_action.triggered.connect(self.edge.sobel)
        self.ui.scharr_action.triggered.connect(self.edge.scharr)
        self.ui.prewitt_action.triggered.connect(self.edge.prewitt)
        
        #buttons
        self.ui.roberts_button.clicked.connect(self.edge.roberts)
        self.ui.sobel_button.clicked.connect(self.edge.sobel)
        self.ui.scharr_button.clicked.connect(self.edge.scharr)
        self.ui.prewitt_button.clicked.connect(self.edge.prewitt)
        
        self.ui.actionAbout.triggered.connect(self.file.about_me)
    
    def firstScreen(self):
        """
        Displays the first screen of the application.
        """
        for menu in self.menuBar().findChildren(QMenu):
            for action in menu.actions():
                action.setEnabled(False)
        for button in self.findChildren(QPushButton):
            button.setEnabled(False)
        
        self.ui.open_source_action.setEnabled(True)
        self.ui.open_source_button.setEnabled(True)
        self.ui.close_action.setEnabled(True)
        self.ui.actionAbout.setEnabled(True)
        self.statusBar().showMessage("Ready")
                
    
    def afterOpen(self):
        """
        Actions to perform after opening an image.
        """
        for action in self.ui.edit_menu.actions():
            action.setEnabled(True)
        
        for action in self.ui.file_menu.actions():
            action.setEnabled(True)
        self.ui.save_as_output_action.setEnabled(False)
        self.ui.save_output_action.setEnabled(False)
        self.ui.export_as_source_button.setEnabled(True)   
        
        self.ui.clear_source_action.setEnabled(True)
        self.ui.clear_output_action.setEnabled(False)
        self.ui.undo_output_action.setEnabled(False)
        self.ui.redo_output_action.setEnabled(False)
        
        self.ui.clear_source_button.setEnabled(True)
        

        self.ui.export_as_source_action.setEnabled(True)
        
        for action in self.ui.conversion_menu.actions():
            action.setEnabled(True)
        
        for action in self.ui.segmentation_menu.actions():
            action.setEnabled(True)
            
        for action in self.ui.edge_detection_menu.actions():
            action.setEnabled(True)
            
        for button in self.ui.conversion_groupBox.findChildren(QPushButton):
            button.setEnabled(True)
            
        for button in self.ui.segmentation_groupBox.findChildren(QPushButton):
            button.setEnabled(True)
            
        for button in self.ui.edge_detection_groupBox.findChildren(QPushButton):
            button.setEnabled(True)
        
        
    
    def afterOperation(self):
        """
        Actions to perform after applying an image operation.
        """
        self.ui.save_output_action.setEnabled(True)
        self.ui.save_as_output_action.setEnabled(True)
        self.ui.export_as_output_action.setEnabled(True)
        self.ui.undo_output_action.setEnabled(True)
        self.ui.redo_output_action.setEnabled(True)
        self.ui.clear_output_action.setEnabled(True)
        
        for button in self.ui.output_tab_widget.findChildren(QPushButton):
            button.setEnabled(True)
            
    def afterClearOutput(self):
        """
        After applying clear output function, it makes disable output buttons and actions.

        """
        self.ui.save_output_action.setEnabled(False)
        self.ui.save_as_output_action.setEnabled(False)
        self.ui.export_as_output_action.setEnabled(False)
        self.ui.undo_output_action.setEnabled(False)
        self.ui.redo_output_action.setEnabled(False)
        self.ui.clear_output_action.setEnabled(False)
        
        for button in self.ui.output_tab_widget.findChildren(QPushButton):
            button.setEnabled(False)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImgFilterAPP()
    window.show()
    sys.exit(app.exec())
    


