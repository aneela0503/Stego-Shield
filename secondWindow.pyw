from PyQt5 import QtCore, QtGui, QtWidgets
import lsb_steganography as stego
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPixmap, QIcon
import webbrowser

class Ui_MainWindow(object):

    # Function to display message/error/information
    def displayMsg(self, title, msg, ico_type=None):
        MsgBox = QtWidgets.QMessageBox()
        MsgBox.setText(msg)
        MsgBox.setWindowTitle(title)
        if ico_type == 'err':
            ico = QtWidgets.QMessageBox.Critical
        else:
            ico = QtWidgets.QMessageBox.Information
        MsgBox.setIcon(ico)
        MsgBox.exec()

    # Function to choose input file
    def getFile(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', "", "Image files (*.jpg *.png *.bmp)")
        if file_path != '':
            self.lineEdit.setText(file_path)
            # Load and display the selected image for preview
            pixmap = QtGui.QPixmap(file_path)
            self.label_image_preview.setPixmap(pixmap.scaledToWidth(300))

    # Function to display save file dialog
    def saveFile(self):
        output_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Save encoded file', "", "PNG File(*.png)")
        return output_path

    # Function to encode data and save file
    def encode(self):
        input_path = self.lineEdit.text()
        text = self.plainTextEdit.toPlainText()
        password = self.lineEdit_2.text()
        if input_path == '':
            self.displayMsg('Error: No file chosen', 'You must select input image file!', 'err')
        elif text == '':
            self.displayMsg('Text is empty', 'Please enter some text to hide!')
        elif password == '':
            self.displayMsg('Error: No password given', 'Please enter a password!', 'err')
        else:
            output_path = self.saveFile()
            if output_path == '':
                self.displayMsg('Operation cancelled', 'Operation cancelled by user!')
            else:
                try:
                    loss = stego.encode(input_path, text, output_path, password, self.progressBar)
                except stego.FileError as fe:
                    self.displayMsg('File Error', str(fe), 'err')
                except stego.DataError as de:
                    self.displayMsg('Data Error', str(de), 'err')
                else:
                    self.displayMsg('Success',
                                     'Encoded Successfully!\n\nImage Data Loss = {:.5f} %'.format(loss))
                    self.progressBar.setValue(0)

    #Function to decode data
    def decode(self):
        input_path = self.lineEdit.text()
        password = self.lineEdit_3.text()
        if input_path == '':
            self.displayMsg('Error: No file chosen','You must select input image file!','err')
        elif password == '':
            self.displayMsg('Error: No password given','Please enter a password!','err')
        else:
            try:
                data = stego.decode(input_path,password,self.progressBar_2)
            except stego.FileError as fe:
                self.displayMsg('File Error',str(fe),'err')
            except stego.PasswordError as pe:
                self.displayMsg('Password Error',str(pe),'err')
                self.progressBar_2.setValue(0)
            else:
                self.displayMsg('Success','Decoded successfully!')
                self.plainTextEdit_2.document().setPlainText(data)
                self.progressBar_2.setValue(0)

    def openWebsite(self, url):
        webbrowser.open(url)

    def aboutDialog(self):
        print("About dialog triggered")  # Debugging statement
        about_text = "This is a steganography application developed using PyQt5.\n\nVersion: 1.0\nDeveloper: Aneela Usmani"
        QtWidgets.QMessageBox.about(self.centralwidget, "About", about_text)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-image: url('background_image.jpg');")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(30, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_6.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setEnabled(True)
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_7.addWidget(self.progressBar_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_3.addWidget(self.plainTextEdit_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem14)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(10, 10, 900, 30))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.aboutDialog)  # Connect the action to the aboutDialog method
        self.menuHelp.addAction(self.actionAbout)

        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.label_decoded_image = QtWidgets.QLabel(self.centralwidget)
        self.label_decoded_image.setObjectName("label_decoded_image")
        self.verticalLayout_5.addWidget(self.label_decoded_image)
        self.label_decoded_image.setText("Decoded Image Preview")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Slots
        self.pushButton.clicked.connect(self.getFile)
        self.pushButton_2.clicked.connect(self.encode)
        self.pushButton_3.clicked.connect(self.decode)
        self.checkBox.stateChanged.connect(
            lambda: self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal) if self.checkBox.isChecked() else self.lineEdit_2.setEchoMode(
                QtWidgets.QLineEdit.Password))
        self.checkBox_2.stateChanged.connect(
            lambda: self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal) if self.checkBox_2.isChecked() else self.lineEdit_3.setEchoMode(
                QtWidgets.QLineEdit.Password))

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
            action = QtWidgets.QAction(MainWindow)
            action.setObjectName(website)
            action.setText(website)
            action.triggered.connect(lambda checked, url=url: self.openWebsite(url))
            self.menuAdditionalResources.addAction(action)

        # Add the Additional Resources menu to the main menu bar
        self.menubar.addAction(self.menuAdditionalResources.menuAction())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STEGO SHIELD: Fortifying WebApp Security"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:900; background-color:white ;font-size:16pt;\">Step 1:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Input Image File:"))
        self.pushButton.setText(_translate("MainWindow", "Choose File"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-weight:900; font-family: Palatino Linotype;background-color:white ; color:charcoal;\">ENCODE</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-weight:900; font-family: Palatino Linotype; background-color:white ;color:charcoal;\">DECODE</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:900;background-color:white;font-size:16pt;\">Step 2:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; background-color:white ;font-size:12pt;\">Enter text to hide:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:900;background-color:white;font-size:16pt;\">Step 3:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-weight:600; background-color:white ;font-size:12pt;\">Enter Password:</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Show Password"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:200; font-size:12pt;\">Progress</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Encode & Save"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:900; background-color:white; font-size:16pt;\">Step 2:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; background-color:white ;font-size:12pt;\">Enter Password:</span></p></body></html>"))
        self.checkBox_2.setText(_translate("MainWindow", "Show Password"))
        self.pushButton_3.setText(_translate("MainWindow", "Decode"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:200; font-size:12pt;\">Progress</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; background-color:white ;font-size:12pt;\">Decoded Data:</span></p></body></html>"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

        # Add a label for image preview
        self.label_image_preview = QtWidgets.QLabel(self.centralwidget)
        self.label_image_preview.setObjectName("label_image_preview")
        self.verticalLayout_5.addWidget(self.label_image_preview)
        self.label_image_preview.setText(_translate("MainWindow", "Image Preview"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
