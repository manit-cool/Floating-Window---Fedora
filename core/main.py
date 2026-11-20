import GUI as GUI
import sys

if __name__ == "__main__":

    app = GUI.QApplication(sys.argv)

    window = GUI.FloatingWindow()
    window.show()
    window.raise_()
    
    sys.exit(app.exec())