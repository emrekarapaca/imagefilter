from PyQt5.QtCore import QTimer
class Edit:
    """
    Represents an editing operation.
    """

    def __init__(self, ui, app):
        """
        Initializes a new instance of the Edit class.

        :param ui: The user interface.
        :param app: The application.
        """
        self.ui = ui
        self.app = app
        self.image_stack = []  # A stack to store the edited images.
        self.current_index = -1   # The index of the currently displayed image in the stack.
         
    
    def clear_source(self):
        """
        Clears the source code.

        This method clears the source code in the editor.

        """
        self.ui.source_label.clear()
        self.clear_output()
        self.app.firstScreen()
        self.app.statusBar().showMessage("Source Image Cleaned.")
        QTimer.singleShot(5000, self.app.statusBar().clearMessage)
        self.history = []
        self.history_index = -1
        

    def clear_output(self):
        """
        Clears the output.

        This method clears the output of the editor.

        """
        self.ui.output_label.clear()
        self.app.afterClearOutput()
    
    def undo_output(self):
        """
        Undoes the previous output action.

        This method undoes the last output action performed.

        """
        if self.current_index>0:
            prev_index = self.current_index
            self.current_index -= 1
            image = self.image_stack[self.current_index]
            self.app.file.show_output_image(image)
            
            if self.current_index == prev_index:
                self.app.statusBar().showMessage("No previous changes.")
            else:
                self.app.statusBar().showMessage("Undo completed.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
            
        else:
            self.app.statusBar().showMessage("No previous changes.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
                
    def redo_output(self):
        """
        Redoes the previously undone output action.

        This method redoes the last output action that was undone.

        """
        if self.current_index < len(self.image_stack) -1:
            prev_index = self.current_index
            self.current_index += 1
            image = self.image_stack[self.current_index]
            self.app.file.show_output_image(image)
            
            if self.current_index == prev_index:
                self.app.statusBar().showMessage("No future changes.")
            else:
                self.app.statusBar().showMessage("Redo completed.")
            QTimer.singleShot(5000, self.app.statusBar().clearMessage)
        else:
            self.app.statusBar().showMessage("No more changes.")
            QTimer.singleShot(2000, self.app.statusBar().clearMessage)
            
            
