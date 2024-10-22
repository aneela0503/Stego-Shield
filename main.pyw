from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import webbrowser

# Append the directory containing y.pyw to sys.path
script_dir = os.path.dirname(os.path.realpath(r"C:\Users\aneel\OneDrive\Desktop\StegoShield\y"))
module_dir = os.path.join(script_dir, 'StegoShield')
sys.path.append(module_dir)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.windows = []  # Keep references to the new windows

    def openWebsite(self, url):
        webbrowser.open(url)

    def aboutDialog(self):
        print("About dialog triggered")  # Debugging statement
        about_text = "This is a steganography application developed using PyQt5.\n\nVersion: 1.0\nDeveloper: Aneela Usmani"
        QtWidgets.QMessageBox.about(self.centralwidget, "About", about_text)


    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1400, 900)

        # Create a central widget and set it
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setObjectName("centralwidget")

        # Load the background image
        background_image = QtGui.QPixmap('background_image1.jpg')
        background_image = self.set_image_opacity(background_image, 0.5)  # Set image opacity to 50%

        # Create a QLabel for the background image
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(0, 0, 1400, 900)
        self.background_label.setPixmap(background_image)
        self.background_label.setScaledContents(True)  # Ensure the image scales with the window size

        # Create a vertical layout
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Add heading label
        self.heading = QtWidgets.QLabel("WELCOME TO STEGOSHIELD\n\nFortifying WebApp Security", self.centralwidget)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setStyleSheet("font-size: 50px; font-family: 'Times New Roman'; font-weight: bold; color: black; background-color: rgba(128, 128, 128, 180);")
        self.layout.addWidget(self.heading)

        # Add text box
        self.heading = QtWidgets.QLabel("In the digital age, steganography is the artist's brush,\npainting secrets into the fabric of our media.",self.centralwidget)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setStyleSheet("font-size: 38px; font-family: 'Times New Roman'; color: white; background-color: charcoal ;")
        self.layout.addWidget(self.heading, alignment=QtCore.Qt.AlignCenter)


        # Add push button
        self.pushButton = QtWidgets.QPushButton("Proceed", self.centralwidget)
        self.pushButton.setFixedSize(200, 70)  # Set the size of the button
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("font-size: 22px; font-family: 'Times New Roman';color: white; background-color:green;")
        self.layout.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)

        self.menubar = self.menuBar()
        self.menubar.setGeometry(QtCore.QRect(10, 10, 900, 30))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)
        self.statusbar = self.statusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction("About", self)  # Create the About action
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.aboutDialog)  # Connect the action to the aboutDialog method
        self.menuHelp.addAction(self.actionAbout)  # Add the About action to the Help menu
        self.menubar.addAction(self.menuHelp.menuAction())

        # Define the URLs for relevant websites
        website_urls = {
            "What is Steganography": "https://www.kaspersky.com/resource-center/definitions/what-is-steganography",
            "Guide to Steganography": "https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/what-is-steganography-guide-meaning-types-tools/",
            "Implementation of LSB": "https://medium.com/@renantkn/lsb-steganography-hiding-a-message-in-the-pixels-of-an-image-4722a8567046",
            "The Hacker News": "https://thehackernews.com/",
            # Add more websites and URLs as needed
        }

        # Create the Additional Resources menu
        self.menuAdditionalResources = QtWidgets.QMenu(self.menubar)
        self.menuAdditionalResources.setObjectName("menuAdditionalResources")
        self.menuAdditionalResources.setTitle("Additional Resources")

                # Create sub-actions for each website
        for website, url in website_urls.items():
            action = QtWidgets.QAction(self)
            action.setObjectName(website)
            action.setText(website)
            action.triggered.connect(lambda checked, url=url: self.openWebsite(url))
            self.menuAdditionalResources.addAction(action)

        # Add the Additional Resources menu to the main menu bar
        self.menubar.addAction(self.menuAdditionalResources.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def set_image_opacity(self, pixmap, opacity):
        image = pixmap.toImage()
        alpha = int(opacity * 255)
        for y in range(image.height()):
            for x in range(image.width()):
                color = image.pixelColor(x, y)
                color.setAlpha(alpha)
                image.setPixelColor(x, y, color)
        return QtGui.QPixmap.fromImage(image)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("StegoShield: Fortifying WebApp Security", "Steganography"))

        # Connect button click to openNewWindow function
        self.pushButton.clicked.connect(self.openNewWindow)
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def openNewWindow(self):
        print("Button clicked, attempting to open new window...")
        try:
            import y  # Importing here to avoid circular imports
            new_window = QtWidgets.QMainWindow()  # Create a new QMainWindow
            ui = y.Ui_MainWindow()  # Instantiate the UI class from y.pyw
            ui.setupUi(new_window)  # Set up the UI for the new window
            new_window.show()  # Show the new window
            self.windows.append(new_window)  # Keep a reference to prevent garbage collection
            print("New window opened successfully.")
        except Exception as e:
            print(f"Failed to open new window: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


