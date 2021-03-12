from PyQt5 import QtCore, QtGui, QtWidgets


class Monopoly(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1513, 904)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_treasury1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_treasury1.setGeometry(QtCore.QRect(1110, 760, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_treasury1.setFont(font)
        self.pushButton_treasury1.setStyleSheet("background-color: rgb(191, 180, 255);")
        self.pushButton_treasury1.setObjectName("pushButton_treasury1")
        self.buttonGroup_treasury = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_treasury.setObjectName("buttonGroup_treasury")
        self.buttonGroup_treasury.addButton(self.pushButton_treasury1)
        self.pushButton_treasury2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_treasury2.setGeometry(QtCore.QRect(10, 240, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_treasury2.setFont(font)
        self.pushButton_treasury2.setStyleSheet("background-color: rgb(191, 180, 255);")
        self.pushButton_treasury2.setObjectName("pushButton_treasury2")
        self.buttonGroup_treasury.addButton(self.pushButton_treasury2)
        self.pushButton_treasury3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_treasury3.setGeometry(QtCore.QRect(1290, 210, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_treasury3.setFont(font)
        self.pushButton_treasury3.setStyleSheet("background-color: rgb(191, 180, 255);")
        self.pushButton_treasury3.setObjectName("pushButton_treasury3")
        self.buttonGroup_treasury.addButton(self.pushButton_treasury3)
        self.pushButton_chance1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chance1.setGeometry(QtCore.QRect(420, 760, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_chance1.setFont(font)
        self.pushButton_chance1.setStyleSheet("background-color: rgb(255, 197, 114);")
        self.pushButton_chance1.setObjectName("pushButton_chance1")
        self.buttonGroup_chance = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_chance.setObjectName("buttonGroup_chance")
        self.buttonGroup_chance.addButton(self.pushButton_chance1)
        self.pushButton_chance2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chance2.setGeometry(QtCore.QRect(290, 0, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_chance2.setFont(font)
        self.pushButton_chance2.setStyleSheet("background-color: rgb(255, 197, 114);")
        self.pushButton_chance2.setObjectName("pushButton_chance2")
        self.buttonGroup_chance.addButton(self.pushButton_chance2)
        self.pushButton_chance3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chance3.setGeometry(QtCore.QRect(1290, 430, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_chance3.setFont(font)
        self.pushButton_chance3.setStyleSheet("background-color: rgb(255, 197, 114);")
        self.pushButton_chance3.setObjectName("pushButton_chance3")
        self.buttonGroup_chance.addButton(self.pushButton_chance3)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(1410, 760, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_jai = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_jai.setGeometry(QtCore.QRect(10, 760, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_jai.setFont(font)
        self.pushButton_jai.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.pushButton_jai.setObjectName("pushButton_jai")
        self.pushButton_camp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_camp.setGeometry(QtCore.QRect(10, 0, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_camp.setFont(font)
        self.pushButton_camp.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.pushButton_camp.setObjectName("pushButton_camp")
        self.pushButton_into_prison = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_into_prison.setGeometry(QtCore.QRect(1410, 0, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_into_prison.setFont(font)
        self.pushButton_into_prison.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.pushButton_into_prison.setObjectName("pushButton_into_prison")
        self.pushButton_tax1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tax1.setGeometry(QtCore.QRect(850, 760, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_tax1.setFont(font)
        self.pushButton_tax1.setStyleSheet("background-color: rgb(200, 177, 195);")
        self.pushButton_tax1.setObjectName("pushButton_tax1")
        self.buttonGroup_tax = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_tax.setObjectName("buttonGroup_tax")
        self.buttonGroup_tax.addButton(self.pushButton_tax1)
        self.pushButton_tax2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tax2.setGeometry(QtCore.QRect(1290, 590, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_tax2.setFont(font)
        self.pushButton_tax2.setStyleSheet("background-color: rgb(200, 177, 195);")
        self.pushButton_tax2.setObjectName("pushButton_tax2")
        self.buttonGroup_tax.addButton(self.pushButton_tax2)
        self.pushButton_saint_petersburg = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_saint_petersburg.setGeometry(QtCore.QRect(1200, 760, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_saint_petersburg.setFont(font)
        self.pushButton_saint_petersburg.setStyleSheet("background-color: rgb(170, 85, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("монополия/Санкт-Петербург.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_saint_petersburg.setIcon(icon)
        self.pushButton_saint_petersburg.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_saint_petersburg.setObjectName("pushButton_saint_petersburg")
        self.buttonGroup_brown = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_brown.setObjectName("buttonGroup_brown")
        self.buttonGroup_brown.addButton(self.pushButton_saint_petersburg)
        self.pushButton_Krasnoyarsk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Krasnoyarsk.setGeometry(QtCore.QRect(940, 760, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Krasnoyarsk.setFont(font)
        self.pushButton_Krasnoyarsk.setStyleSheet("background-color: rgb(170, 85, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("монополия/Красноярск.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Krasnoyarsk.setIcon(icon1)
        self.pushButton_Krasnoyarsk.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Krasnoyarsk.setObjectName("pushButton_Krasnoyarsk")
        self.buttonGroup_brown.addButton(self.pushButton_Krasnoyarsk)
        self.pushButton_Samara = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Samara.setGeometry(QtCore.QRect(510, 760, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Samara.setFont(font)
        self.pushButton_Samara.setStyleSheet("background-color: rgb(0, 170, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("монополия/Самара.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Samara.setIcon(icon2)
        self.pushButton_Samara.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Samara.setObjectName("pushButton_Samara")
        self.buttonGroup_sky = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_sky.setObjectName("buttonGroup_sky")
        self.buttonGroup_sky.addButton(self.pushButton_Samara)
        self.pushButton_Cheboksary = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cheboksary.setGeometry(QtCore.QRect(260, 760, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Cheboksary.setFont(font)
        self.pushButton_Cheboksary.setStyleSheet("background-color: rgb(0, 170, 255);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("монополия/Чебоксары.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cheboksary.setIcon(icon3)
        self.pushButton_Cheboksary.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Cheboksary.setObjectName("pushButton_Cheboksary")
        self.buttonGroup_sky.addButton(self.pushButton_Cheboksary)
        self.pushButton_Penza = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Penza.setGeometry(QtCore.QRect(100, 760, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Penza.setFont(font)
        self.pushButton_Penza.setStyleSheet("background-color: rgb(0, 170, 255);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("монополия/Пенза.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Penza.setIcon(icon4)
        self.pushButton_Penza.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Penza.setObjectName("pushButton_Penza")
        self.buttonGroup_sky.addButton(self.pushButton_Penza)
        self.pushButton_Chelyabinsk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Chelyabinsk.setGeometry(QtCore.QRect(10, 690, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Chelyabinsk.setFont(font)
        self.pushButton_Chelyabinsk.setStyleSheet("background-color: rgb(255, 85, 255);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("монополия/Челябинск.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Chelyabinsk.setIcon(icon5)
        self.pushButton_Chelyabinsk.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Chelyabinsk.setObjectName("pushButton_Chelyabinsk")
        self.buttonGroup_pink = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_pink.setObjectName("buttonGroup_pink")
        self.buttonGroup_pink.addButton(self.pushButton_Chelyabinsk)
        self.pushButton_barnaul = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_barnaul.setGeometry(QtCore.QRect(10, 550, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_barnaul.setFont(font)
        self.pushButton_barnaul.setStyleSheet("background-color: rgb(255, 85, 255);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("монополия/Барнаул.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_barnaul.setIcon(icon6)
        self.pushButton_barnaul.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_barnaul.setObjectName("pushButton_barnaul")
        self.buttonGroup_pink.addButton(self.pushButton_barnaul)
        self.pushButton_Pskov = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Pskov.setGeometry(QtCore.QRect(10, 480, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Pskov.setFont(font)
        self.pushButton_Pskov.setStyleSheet("background-color: rgb(255, 85, 255);")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("монополия/Псков.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Pskov.setIcon(icon7)
        self.pushButton_Pskov.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Pskov.setObjectName("pushButton_Pskov")
        self.buttonGroup_pink.addButton(self.pushButton_Pskov)
        self.pushButton_Bataysk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Bataysk.setGeometry(QtCore.QRect(10, 340, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Bataysk.setFont(font)
        self.pushButton_Bataysk.setStyleSheet("background-color: rgb(255, 170, 0);")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("монополия/Батайск.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Bataysk.setIcon(icon8)
        self.pushButton_Bataysk.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Bataysk.setObjectName("pushButton_Bataysk")
        self.buttonGroup_orange = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_orange.setObjectName("buttonGroup_orange")
        self.buttonGroup_orange.addButton(self.pushButton_Bataysk)
        self.pushButton_Voronezh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Voronezh.setGeometry(QtCore.QRect(10, 170, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Voronezh.setFont(font)
        self.pushButton_Voronezh.setStyleSheet("background-color: rgb(255, 170, 0);")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("монополия/Воронеж.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Voronezh.setIcon(icon9)
        self.pushButton_Voronezh.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Voronezh.setObjectName("pushButton_Voronezh")
        self.buttonGroup_orange.addButton(self.pushButton_Voronezh)
        self.pushButton_Syktyvkar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Syktyvkar.setGeometry(QtCore.QRect(10, 100, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Syktyvkar.setFont(font)
        self.pushButton_Syktyvkar.setStyleSheet("background-color: rgb(255, 170, 0);")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("монополия/Сыктывкар.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Syktyvkar.setIcon(icon10)
        self.pushButton_Syktyvkar.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Syktyvkar.setObjectName("pushButton_Syktyvkar")
        self.buttonGroup_orange.addButton(self.pushButton_Syktyvkar)
        self.pushButton_rostovnadonu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rostovnadonu.setGeometry(QtCore.QRect(100, 0, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_rostovnadonu.setFont(font)
        self.pushButton_rostovnadonu.setStyleSheet("background-color: rgb(255, 0, 0);")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("монополия/Ростов-на-Дону.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rostovnadonu.setIcon(icon11)
        self.pushButton_rostovnadonu.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_rostovnadonu.setObjectName("pushButton_rostovnadonu")
        self.buttonGroup_red = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_red.setObjectName("buttonGroup_red")
        self.buttonGroup_red.addButton(self.pushButton_rostovnadonu)
        self.pushButton_Ryazan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Ryazan.setGeometry(QtCore.QRect(380, 0, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Ryazan.setFont(font)
        self.pushButton_Ryazan.setStyleSheet("background-color: rgb(255, 0, 0);")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("монополия/Рязань.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Ryazan.setIcon(icon12)
        self.pushButton_Ryazan.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Ryazan.setObjectName("pushButton_Ryazan")
        self.buttonGroup_red.addButton(self.pushButton_Ryazan)
        self.pushButton_Moscow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Moscow.setGeometry(QtCore.QRect(510, 0, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Moscow.setFont(font)
        self.pushButton_Moscow.setStyleSheet("background-color: rgb(255, 0, 0);")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("монополия/Москва.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Moscow.setIcon(icon13)
        self.pushButton_Moscow.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Moscow.setObjectName("pushButton_Moscow")
        self.buttonGroup_red.addButton(self.pushButton_Moscow)
        self.pushButton_Arkhangelsk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Arkhangelsk.setGeometry(QtCore.QRect(780, 0, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Arkhangelsk.setFont(font)
        self.pushButton_Arkhangelsk.setStyleSheet("background-color: rgb(255, 255, 0);")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("монополия/Архангельск.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Arkhangelsk.setIcon(icon14)
        self.pushButton_Arkhangelsk.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Arkhangelsk.setObjectName("pushButton_Arkhangelsk")
        self.buttonGroup_yellow = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_yellow.setObjectName("buttonGroup_yellow")
        self.buttonGroup_yellow.addButton(self.pushButton_Arkhangelsk)
        self.pushButton_Obninsk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Obninsk.setGeometry(QtCore.QRect(950, 0, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Obninsk.setFont(font)
        self.pushButton_Obninsk.setStyleSheet("background-color: rgb(255, 255, 0);")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("монополия/Обнинск.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Obninsk.setIcon(icon15)
        self.pushButton_Obninsk.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Obninsk.setObjectName("pushButton_Obninsk")
        self.buttonGroup_yellow.addButton(self.pushButton_Obninsk)
        self.pushButton_Novosibirsk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Novosibirsk.setGeometry(QtCore.QRect(1230, 0, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Novosibirsk.setFont(font)
        self.pushButton_Novosibirsk.setStyleSheet("background-color: rgb(255, 255, 0);")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("монополия/Новосибирск.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Novosibirsk.setIcon(icon16)
        self.pushButton_Novosibirsk.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Novosibirsk.setObjectName("pushButton_Novosibirsk")
        self.buttonGroup_yellow.addButton(self.pushButton_Novosibirsk)
        self.pushButton_Surgut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Surgut.setGeometry(QtCore.QRect(1290, 290, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Surgut.setFont(font)
        self.pushButton_Surgut.setStyleSheet("background-color: rgb(0, 170, 0);")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("монополия/Сургут.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Surgut.setIcon(icon17)
        self.pushButton_Surgut.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Surgut.setObjectName("pushButton_Surgut")
        self.buttonGroup_green = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_green.setObjectName("buttonGroup_green")
        self.buttonGroup_green.addButton(self.pushButton_Surgut)
        self.pushButton_Kurgan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Kurgan.setGeometry(QtCore.QRect(1290, 160, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Kurgan.setFont(font)
        self.pushButton_Kurgan.setStyleSheet("background-color: rgb(0, 170, 0);")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("монополия/Курган.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Kurgan.setIcon(icon18)
        self.pushButton_Kurgan.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Kurgan.setObjectName("pushButton_Kurgan")
        self.buttonGroup_green.addButton(self.pushButton_Kurgan)
        self.pushButton_Severodvinsk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Severodvinsk.setGeometry(QtCore.QRect(1290, 100, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Severodvinsk.setFont(font)
        self.pushButton_Severodvinsk.setStyleSheet("background-color: rgb(0, 170, 0);")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("монополия/Северодвинск.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Severodvinsk.setIcon(icon19)
        self.pushButton_Severodvinsk.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Severodvinsk.setObjectName("pushButton_Severodvinsk")
        self.buttonGroup_green.addButton(self.pushButton_Severodvinsk)
        self.pushButton_Ekaterinburg = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Ekaterinburg.setGeometry(QtCore.QRect(1290, 690, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Ekaterinburg.setFont(font)
        self.pushButton_Ekaterinburg.setStyleSheet("background-color: rgb(0, 0, 255);")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("монополия/Екатеринбург.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Ekaterinburg.setIcon(icon20)
        self.pushButton_Ekaterinburg.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Ekaterinburg.setObjectName("pushButton_Ekaterinburg")
        self.buttonGroup_blue = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_blue.setObjectName("buttonGroup_blue")
        self.buttonGroup_blue.addButton(self.pushButton_Ekaterinburg)
        self.pushButton_Perm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Perm.setGeometry(QtCore.QRect(1290, 520, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Perm.setFont(font)
        self.pushButton_Perm.setStyleSheet("background-color: rgb(0, 0, 255);")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("монополия/Пермь.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Perm.setIcon(icon21)
        self.pushButton_Perm.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Perm.setObjectName("pushButton_Perm")
        self.buttonGroup_blue.addButton(self.pushButton_Perm)
        self.pushButton_Tolmachevo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Tolmachevo.setGeometry(QtCore.QRect(670, 760, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Tolmachevo.setFont(font)
        self.pushButton_Tolmachevo.setStyleSheet("background-color: rgb(55, 239, 255);")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("монополия/Самолет.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Tolmachevo.setIcon(icon22)
        self.pushButton_Tolmachevo.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Tolmachevo.setObjectName("pushButton_Tolmachevo")
        self.buttonGroup_azure = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_azure.setObjectName("buttonGroup_azure")
        self.buttonGroup_azure.addButton(self.pushButton_Tolmachevo)
        self.pushButton_36_Pulkovo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36_Pulkovo.setGeometry(QtCore.QRect(10, 410, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_36_Pulkovo.setFont(font)
        self.pushButton_36_Pulkovo.setStyleSheet("background-color: rgb(55, 239, 255);")
        self.pushButton_36_Pulkovo.setIcon(icon22)
        self.pushButton_36_Pulkovo.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_36_Pulkovo.setObjectName("pushButton_36_Pulkovo")
        self.buttonGroup_azure.addButton(self.pushButton_36_Pulkovo)
        self.pushButton_Koltsovo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Koltsovo.setGeometry(QtCore.QRect(630, 0, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Koltsovo.setFont(font)
        self.pushButton_Koltsovo.setStyleSheet("background-color: rgb(55, 239, 255);")
        self.pushButton_Koltsovo.setIcon(icon22)
        self.pushButton_Koltsovo.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Koltsovo.setObjectName("pushButton_Beltway")
        self.buttonGroup_azure.addButton(self.pushButton_Koltsovo)
        self.pushButton_sheremetievo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sheremetievo.setGeometry(QtCore.QRect(1290, 360, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sheremetievo.setFont(font)
        self.pushButton_sheremetievo.setStyleSheet("background-color: rgb(55, 239, 255);")
        self.pushButton_sheremetievo.setIcon(icon22)
        self.pushButton_sheremetievo.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_sheremetievo.setObjectName("pushButton_sheremetievo")
        self.buttonGroup_azure.addButton(self.pushButton_sheremetievo)
        self.pushButton_communication1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_communication1.setGeometry(QtCore.QRect(10, 620, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_communication1.setFont(font)
        self.pushButton_communication1.setStyleSheet("background-color: rgb(195, 255, 181);")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("монополия/Телефон.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_communication1.setIcon(icon23)
        self.pushButton_communication1.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_communication1.setObjectName("pushButton_communication1")
        self.buttonGroup_communication = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_communication.setObjectName("buttonGroup_communication")
        self.buttonGroup_communication.addButton(self.pushButton_communication1)
        self.pushButton_communication2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_communication2.setGeometry(QtCore.QRect(1090, 0, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_communication2.setFont(font)
        self.pushButton_communication2.setStyleSheet("background-color: rgb(195, 255, 181);")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("монополия/Компьютер.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_communication2.setIcon(icon24)
        self.pushButton_communication2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_communication2.setObjectName("pushButton_communication2")
        self.buttonGroup_communication.addButton(self.pushButton_communication2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 180, 141, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label.setObjectName("label")
        self.plainTextEdit_chane = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_chane.setEnabled(False)
        self.plainTextEdit_chane.setGeometry(QtCore.QRect(340, 250, 161, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_chane.setFont(font)
        self.plainTextEdit_chane.setPlainText("")
        self.plainTextEdit_chane.setObjectName("plainTextEdit_chane")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 200, 181, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("монополия/Казна.png"))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_treasury = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_treasury.setEnabled(False)
        self.plainTextEdit_treasury.setGeometry(QtCore.QRect(940, 260, 161, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_treasury.setFont(font)
        self.plainTextEdit_treasury.setPlainText("")
        self.plainTextEdit_treasury.setObjectName("plainTextEdit_treasury")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 510, 211, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("монополия/Игрок.png"))
        self.label_3.setObjectName("label_3")
        self.plainTextEdit_player = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_player.setEnabled(True)
        self.plainTextEdit_player.setGeometry(QtCore.QRect(530, 570, 181, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_player.setFont(font)
        self.plainTextEdit_player.setPlainText("")
        self.plainTextEdit_player.setObjectName("plainTextEdit_player")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(770, 480, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(950, 520, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(800, 560, 431, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_end = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_end.setGeometry(QtCore.QRect(610, 330, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_end.setFont(font)
        self.pushButton_end.setObjectName("pushButton_end")
        self.pushButton_progress = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_progress.setGeometry(QtCore.QRect(610, 280, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_progress.setFont(font)
        self.pushButton_progress.setObjectName("pushButton_progress")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1513, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttons = [self.pushButton_start, self.pushButton_saint_petersburg, self.pushButton_treasury1,
                                self.pushButton_Krasnoyarsk,
                                self.pushButton_tax1, self.pushButton_Tolmachevo, self.pushButton_Samara,
                                self.pushButton_chance1, self.pushButton_Cheboksary, self.pushButton_Penza,
                                self.pushButton_jai,
                                self.pushButton_Chelyabinsk, self.pushButton_communication1, self.pushButton_barnaul,
                                self.pushButton_Pskov, self.pushButton_36_Pulkovo, self.pushButton_Bataysk,
                                self.pushButton_treasury2,
                                self.pushButton_Voronezh, self.pushButton_Syktyvkar, self.pushButton_camp,
                                self.pushButton_rostovnadonu, self.pushButton_chance2, self.pushButton_Ryazan,
                                self.pushButton_Moscow, self.pushButton_Koltsovo, self.pushButton_Arkhangelsk,
                                self.pushButton_Obninsk, self.pushButton_communication2, self.pushButton_Novosibirsk,
                                self.pushButton_into_prison, self.pushButton_Severodvinsk, self.pushButton_Kurgan,
                                self.pushButton_treasury3, self.pushButton_Surgut, self.pushButton_sheremetievo,
                                self.pushButton_chance3, self.pushButton_Perm, self.pushButton_tax2,
                                self.pushButton_Ekaterinburg]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_treasury1.setText(_translate("MainWindow", "Казна"))
        self.pushButton_treasury2.setText(_translate("MainWindow", "Казна"))
        self.pushButton_treasury3.setText(_translate("MainWindow", "Казна"))
        self.pushButton_chance1.setText(_translate("MainWindow", "Шанс"))
        self.pushButton_chance2.setText(_translate("MainWindow", "Шанс"))
        self.pushButton_chance3.setText(_translate("MainWindow", "Шанс"))
        self.pushButton_start.setText(_translate("MainWindow", "Старт"))
        self.pushButton_jai.setText(_translate("MainWindow", "Тюрьма"))
        self.pushButton_camp.setText(_translate("MainWindow", "Стоянка"))
        self.pushButton_into_prison.setText(_translate("MainWindow", "В тюрьму"))
        self.pushButton_tax1.setText(_translate("MainWindow", "Налог"))
        self.pushButton_tax2.setText(_translate("MainWindow", "Налог"))
        self.pushButton_saint_petersburg.setText(_translate("MainWindow", "Санкт-Петербург"))
        self.pushButton_Krasnoyarsk.setText(_translate("MainWindow", "Красноярск"))
        self.pushButton_Samara.setText(_translate("MainWindow", "Самара"))
        self.pushButton_Cheboksary.setText(_translate("MainWindow", "Чебоксары"))
        self.pushButton_Penza.setText(_translate("MainWindow", "Пенза"))
        self.pushButton_Chelyabinsk.setText(_translate("MainWindow", "Челябинск"))
        self.pushButton_barnaul.setText(_translate("MainWindow", "Барнаул"))
        self.pushButton_Pskov.setText(_translate("MainWindow", "Псков"))
        self.pushButton_Bataysk.setText(_translate("MainWindow", "Батайск"))
        self.pushButton_Voronezh.setText(_translate("MainWindow", "Воронеж"))
        self.pushButton_Syktyvkar.setText(_translate("MainWindow", "Сыктывкар"))
        self.pushButton_rostovnadonu.setText(_translate("MainWindow", "Ростов-на-Дону"))
        self.pushButton_Ryazan.setText(_translate("MainWindow", "Рязань"))
        self.pushButton_Moscow.setText(_translate("MainWindow", "Москва"))
        self.pushButton_Arkhangelsk.setText(_translate("MainWindow", "Архангельск"))
        self.pushButton_Obninsk.setText(_translate("MainWindow", "Обнинск"))
        self.pushButton_Novosibirsk.setText(_translate("MainWindow", "Новосибирск"))
        self.pushButton_Surgut.setText(_translate("MainWindow", "Сургут"))
        self.pushButton_Kurgan.setText(_translate("MainWindow", "Курган"))
        self.pushButton_Severodvinsk.setText(_translate("MainWindow", "Северодвинск"))
        self.pushButton_Ekaterinburg.setText(_translate("MainWindow", "Екатеринбург"))
        self.pushButton_Perm.setText(_translate("MainWindow", "Пермь"))
        self.pushButton_Tolmachevo.setText(_translate("MainWindow", "Толмачево"))
        self.pushButton_36_Pulkovo.setText(_translate("MainWindow", "Пулково"))
        self.pushButton_Koltsovo.setText(_translate("MainWindow", "Кольцево"))
        self.pushButton_sheremetievo.setText(_translate("MainWindow", "Шереметьево"))
        self.pushButton_communication1.setText(_translate("MainWindow", "Мобильная связь"))
        self.pushButton_communication2.setText(_translate("MainWindow", "Интернет"))
        self.label.setText(_translate("MainWindow", " ?"))
        self.label_5.setText(_translate("MainWindow", "История"))
        self.pushButton_end.setText(_translate("MainWindow", "Закончить"))
        self.pushButton_progress.setText(_translate("MainWindow", "Следущий ход"))


class MainWindow(QtWidgets.QDialog):  # Основное окно
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(300, 300, 700, 600)
        self.list_of_players = []

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 0, 311, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("монополия/new_game_icon1.jpg"))
        self.label.setObjectName("label")

        self.plainTextEdit_rules = QtWidgets.QPlainTextEdit("Добро пожаловать в игру Монополия!\n"
"В игре могут участвовать 2 - 8 человек. \n"
"Введите имена игроков и добавьте их в список участников.\n", self)
        self.plainTextEdit_rules.setEnabled(False)
        self.plainTextEdit_rules.setGeometry(QtCore.QRect(360, 40, 221, 211))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit_rules.setFont(font)
        self.plainTextEdit_rules.setStyleSheet("color: rgb(0, 0, 0);")
        self.plainTextEdit_rules.setObjectName("plainTextEdit_rules")

        self.plainTextEdit_list_of_players = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit_list_of_players.setEnabled(False)
        self.plainTextEdit_list_of_players.setGeometry(QtCore.QRect(30, 380, 211, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_list_of_players.setFont(font)
        self.plainTextEdit_list_of_players.setStyleSheet("color: rgb(0, 0, 0);")
        self.plainTextEdit_list_of_players.setPlainText("")
        self.plainTextEdit_list_of_players.setObjectName("plainTextEdit_list_of_players")

        self.lineEdit_name = QtWidgets.QLineEdit(self)
        self.lineEdit_name.setGeometry(QtCore.QRect(400, 350, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.label_2 = QtWidgets.QLabel("Имя", self)
        self.label_2.setGeometry(QtCore.QRect(320, 350, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton_name = QtWidgets.QPushButton("Добавить", self)
        self.pushButton_name.setGeometry(QtCore.QRect(340, 410, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_name.setFont(font)
        self.pushButton_name.setObjectName("pushButton")
        self.pushButton_name.clicked.connect(self.add_player)

        self.pushButton_end = QtWidgets.QPushButton("Начать", self)
        self.pushButton_end.setGeometry(QtCore.QRect(410, 510, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_end.setFont(font)
        self.pushButton_end.setObjectName("pushButton")
        self.pushButton_end.clicked.connect(self.end)

        self.label_4 = QtWidgets.QLabel("", self)
        self.label_4.setGeometry(QtCore.QRect(350, 280, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_3")

        self.label_3 = QtWidgets.QLabel("Список игроков", self)
        self.label_3.setGeometry(QtCore.QRect(50, 330, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

    def add_player(self): # добавление игроков
        if len(self.list_of_players) < 8:
            player = self.lineEdit_name.text()
            for i in self.list_of_players:
                if i == player:
                    self.label_4.setText('Имена игорокв должны быть уникальными')
                    return
            self.plainTextEdit_list_of_players.appendPlainText(player)
            self.list_of_players.append(player)
        else:
            self.label_4.setText('Достаточно игроков. Начинайте игру')

    def end(self):  # проверка игроков по нескольким условиям
        if self.list_of_players:
            if len(self.list_of_players) < 2:
                self.label_4.setText('Недостаточно игроков')
            else:
                self.close()
        else:
            self.label_4.setText('Введите имена игроков')


class Window_property_purchase(QtWidgets.QDialog):  # Окно аукциона и покупки собственности
    def __init__(self, players, name, price, number_player, parent=None):
        self.players = players
        self.winner = players[number_player]
        self.name = name
        self.price = price
        self.list_money = []
        self.number_player = number_player
        super(Window_property_purchase, self).__init__(parent)
        self.setGeometry(300, 300, 1000, 650)

        self.label = QtWidgets.QLabel("Собственность никому не принадлежит. Купите ее или устройте аукцион", self)
        self.label.setGeometry(QtCore.QRect(40, 20, 821, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton("Аукцион", self)
        self.pushButton.setGeometry(QtCore.QRect(70, 100, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.auction)

        self.pushButton_2 = QtWidgets.QPushButton("Купить собственность", self)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 100, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(540, 90, 47, 541))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")

        self.label_cost = QtWidgets.QLabel(self)
        self.label_cost.setGeometry(QtCore.QRect(600, 180, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_cost.setFont(font)
        self.label_cost.setText("")
        self.label_cost.setObjectName("label_cost")

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 280, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_cost_2 = QtWidgets.QLabel(self)
        self.label_cost_2.setGeometry(QtCore.QRect(30, 170, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_cost_2.setFont(font)
        self.label_cost_2.setText("")
        self.label_cost_2.setObjectName("label_cost_2")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 400, 211, 231))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.label_3 = QtWidgets.QLabel("Рейтинг участников", self)
        self.label_3.setGeometry(QtCore.QRect(10, 350, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton_4 = QtWidgets.QPushButton("Закончить", self)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 570, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton("Добавить", self)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 340, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")

        self.label_4 = QtWidgets.QLabel("Имя", self)
        self.label_4.setGeometry(QtCore.QRect(200, 230, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 290, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_5 = QtWidgets.QLabel("Сумма", self)
        self.label_5.setGeometry(QtCore.QRect(190, 290, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(310, 230, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.item()

        self.pushButton_2.clicked.connect(self.purchase)
        self.pushButton_5.clicked.connect(self.addPeople)
        self.pushButton_4.clicked.connect(self.end_auction)
        self.pushButton_3.clicked.connect(self.end_purchase)

    def item(self):
        for i in self.players:
            self.comboBox.addItem(i.name)

    def purchase(self):
        self.label_cost.setText(f'{self.name} стоит {self.price}.')
        self.pushButton_3.setText(f'Купить за {self.price}')

    def end_purchase(self):
        self.close()

    def auction(self):
        self.label_cost_2.setText(f'Начинается аукцион. Покупайте {self.name}')

    def addPeople(self):  # добавляем в список игроков для аукциона
        name = self.comboBox.currentText()
        money = int(self.lineEdit_2.text())
        for i in range(len(self.list_money)):
            if self.list_money[i][0] == name:
                del self.list_money[i]
                break
        self.list_money.append([name, money])
        self.list_money.sort(key=lambda x: x[1], reverse=True)  # сортируем полученный список денег
        self.player_data()

    def player_data(self):
        self.plainTextEdit.clear()
        for i in self.list_money:
            self.plainTextEdit.appendPlainText(f'Игрок {i[0]} предложил {i[1]}')

    def end_auction(self):  # проверка по нескольким условиям результатов аукциона
        if self.list_money:
            if len(self.list_money) > 1 and self.list_money[0][1] == self.list_money[1][1]:
                self.label_cost_2.setText('Невозможно точно определить победителя')
            else:
                for i in self.players:
                    if i.name == self.list_money[0][0]:
                        self.winner = i
                        self.price = self.list_money[0][1]
                        break
                self.close()
        else:
            self.label_cost_2.setText('Сначала внесите в список покупателей')


class Window_sale_and_purchase(QtWidgets.QDialog):  # Окно продажи, залога или выкупа
    def __init__(self, players, own, property, price, pledge=False, parent=None):
        self.players = players
        self.property = property
        self.own = own
        self.winner = None
        self.price = price
        self.pledge = pledge
        self.prov = False
        super(Window_sale_and_purchase, self).__init__(parent)
        self.setGeometry(300, 300, 1000, 650)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(120, 240, 301, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("монополия/new_game_icon1.jpg"))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(350, 10, 47, 481))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel("Продажа собственности другому игроку", self)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(410, 40, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(490, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")

        self.label_5 = QtWidgets.QLabel("Цена", self)
        self.label_5.setGeometry(QtCore.QRect(410, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(520, 230, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.label_6 = QtWidgets.QLabel("Кому:", self)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(130, 100, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.item()

        self.label_7 = QtWidgets.QLabel("Цена:", self)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 159, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_2 = QtWidgets.QPushButton("Продать", self)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 220, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        if self.pledge:
            self.label_4.setText(f'Выкуп {self.property.name}')
            self.lineEdit.setText(f'Цена выкупа: {self.price}')
            self.pushButton.setText(f'Выкупить')
        else:
            self.label_4.setText(f'Заложить {self.property.name}')
            self.lineEdit.setText(str(self.price))
            self.pushButton.setText(f'Заложить')
        self.pushButton.clicked.connect(self.laying)
        self.pushButton_2.clicked.connect(self.sale)

    def item(self):
        for i in self.players:
            if self.own.name != i.name:
                self.comboBox.addItem(i.name)

    def sale(self):  # если игрок продает собственность
        name = self.comboBox.currentText()
        for i in self.players:
            if i.name == name:
                self.winner = i
        self.price = self.lineEdit_2.text()
        self.close()

    def laying(self):  # если игрок собственность закладывает или выкупает
        self.prov = True
        self.close()


class Window_Jail(QtWidgets.QDialog):  # окно тюрьмы
    def __init__(self, players, parent=None):
        self.players = players
        self.paying = []
        super(Window_Jail, self).__init__(parent)
        self.setGeometry(300, 300, 1000, 650)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 0, 821, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("монополия/Тюрьма.jpg"))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 221, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("монополия/Преступник.png"))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel("Это тюрьма. Чтобы выбраться, заплатите 500k", self)
        self.label_3.setGeometry(QtCore.QRect(290, 30, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(340, 110, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.item()

        self.pushButton = QtWidgets.QPushButton("Заплатить", self)
        self.pushButton.setGeometry(QtCore.QRect(360, 170, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pay)

    def item(self):  # заполняем comboBox значениями
        for i in self.players:
            self.comboBox.addItem(i.name)

    def pay(self):  # игрок платит, чтобы выйти из тюрьмы
        name = self.comboBox.currentText()
        for i in range(len(self.players)):
            if self.players[i].name == name:
                name = self.players[i]
                del self.players[i]
                self.comboBox.clear()
                self.item()
                break
        self.paying.append(name)  # добавляем в список заплативших


import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randrange
from PyQt5 import QtCore, QtMultimedia


class Property:
    def __init__(self, sete):
        self.name = sete[0]
        self.rent1 = sete[1]
        self.pledge = sete[2]
        self.color = sete[3]
        self.price = sete[4]

    def rent(self, n):  # высчитываем ренту
        return self.rent1 * n


class Transport:
    def __init__(self, sete):
        self.name = sete[0]
        self.rent1 = sete[1]
        self.rent2 = sete[2]
        self.rent3 = sete[3]
        self.rent4 = sete[4]
        self.pledge = sete[5]
        self.price = sete[6]
        self.color = None

    def rent(self, n):  # высчитываем ренту
        if n == 1:
            return self.rent1
        elif n == 2:
            return self.rent2
        elif n == 3:
            return self.rent3
        return self.rent4


class Communication:
    def __init__(self, sete):
        self.name = sete[0]
        self.pledge = sete[2]
        self.price = sete[1]
        self.color = None

    def rent(self, n):  # высчитываем ренту
        k = randrange(1, 13)
        if n == 1:
            return k * 40000
        return k * 100000


class Player:  # класс Игрок
    def __init__(self, name):
        self.name = name
        self.money = 15000000
        self.list_of_properties = []  # список незаложенной собственности
        self.list_of_pledged_properties = []  # список заложенной собственности
        self.location = 0  # позиция игрока
        self.in_jail = False  # переменная bool (в тюрьме?)

    def player_move(self, k):  # игрок ходит
        self.location += k
        if self.location >= 40:  # если прошел поле
            self.money += 2000000
            self.location -= 40

    def all_money(self):  # подсчет общей суммы (деньги и собственность)
        n = self.money
        for i in self.list_of_properties:
            n += i.price
        for i in self.list_of_pledged_properties:
            n += i.price
        return n

    def check_for_bankruptcy(self):   # игрок банкрот или нет
        if self.money <= 0 and not self.list_of_properties and not self.list_of_pledged_properties:
            return True
        return False

    def add_property(self, property, price=None):  # добавить собственность
        if price:
            self.money -= int(price)  # игрок платит деньги (если аукцион)
        else:
            self.money -= property.price  # игрок платит деньги за собственность
        self.list_of_properties.append(property)  # добавление собственности

    def sale_property(self, property, price):  # продажа собственности
        for i in range(len(self.list_of_properties)):
            if self.list_of_properties[i].name == property.name:
                del self.list_of_properties[i]  # удаляем собственность
                break
        self.money += int(price)

    def list_property(self):  # возвращаем список собственности (заложенной и незаложенной)
        sete = []
        for i in self.list_of_properties:
            sete.append(i.name)
        for i in self.list_of_pledged_properties:
            sete.append(i.name)
        return sete

    def quanity_propery_color(self, color):  # сколько собственностей данного цвета есть у игрока
        n = 0
        for i in self.list_of_properties:
            if i.color == color:
                n += 1
        for i in self.list_of_pledged_properties:
            if i.color == color:
                n += 1
        return n

    def property_playment(self, property):  # получаем ренту
        n = self.quanity_propery_color(property.color)  # проверяем цену (чем больше городов, данного цвета, тем больше рента)
        self.money += property.rent(n)

    def self_property_playment(self, owner, property):  # платим ренту
        n = owner.quanity_propery_color(property.color)  # проверяем цену
        self.money -= property.rent(n)

    def payment_of_money(self, money):  # получаем деньги (за карточки Шанс и Казна)
        self.money += int(money)

    def property_as_collateral(self, property):  # игрок отдает в залог собственность
        for i in range(len(self.list_of_properties)):
            if self.list_of_properties[i].name == property.name:  # если это данная собственность
                del self.list_of_properties[i]
                break
        self.list_of_pledged_properties.append(property)  # добавляем в список заложенной собственности данную
        self.money += property.pledge  # получаем деньги за залог

    def the_redemption_of_the_property(self, property):  # выкупаем собственность
        for i in range(len(self.list_of_pledged_properties)):
            if self.list_of_pledged_properties[i].name == property.name:  # если это данная собственность
                del self.list_of_pledged_properties[i]
        self.list_of_properties.append(property)  # добавляем в список незаложенной собственности
        self.money -= (property.pledge + property.pledge // 10)  # платим цену


class MyWidget(QMainWindow, Monopoly):  # основной класс
    def __init__(self):
        super(MyWidget, self).__init__()
        self.players = []  # список игроков
        self.list_of_own = []  # список собственности
        self.progress = False  # переменная bool для учета прогресса
        self.filling_in_the_property_list(Communication, "communication")   # список коммуникации
        self.filling_in_the_property_list(Transport, "transport")   # список транспорта
        self.filling_in_the_property_list(Property, "property")   # список собственности
        self.player_number = -1  # номер игрока, который ходит в данный момент
        self.new_game()  # новая игра

    def filling_in_the_property_list(self, cl, name):  # функция для заполнения списков
        self.list_of_own.append([])
        f = sqlite3.connect("monopoly_db.db")  # получаеи результат из базы данных
        cur = f.cursor()
        x = f'select * from {name}'
        result = cur.execute(x).fetchall()
        for i in result:
            self.list_of_own[-1].append(cl(i))  # заполняем список полученными значениями
        f.close()

    def checking_player_loss(self):  # функция для банкротства игрока
        i = 0
        while i < len(self.players):
            if self.players[i].check_for_bankruptcy():  # то есть, если банкрот - удаляем из списка
                del self.players[i]
            else:
                i += 1

    def new_game(self):  # функция новой игры
        ex2 = MainWindow(self)  # открываем начальное окно
        ex2.exec_()
        self.registration_of_participants(ex2.list_of_players)  # регистрируем полученных пользователей
        self.setupUi(self)  # подключаем интерфейс основного окна игры
        self.connecting_buttons()  # подключаем кнопки
        self.play()  # подключаем музыку
        self.next_move()  # делаем первый шаг

    def play(self):  # подключаем музыку
        filename ='монополия\music1.mp3'
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def game_end(self):  # конец игры
        self.plainTextEdit.clear()
        # выводим рейтинг участников
        for i in sorted(self.players, key=lambda x: x.all_money(), reverse=True):
            self.plainTextEdit.appendPlainText(f'Игрок {i.name} обладает общей суммой {i.all_money()}')

    def connecting_buttons(self):  # подключаем кнопки
        for i in self.buttons:
            if i.text() in [k.name for j in self.list_of_own for k in j]:
                i.clicked.connect(self.work_property)  # кнопки собственности
            elif i.text() == 'Шанс':
                i.clicked.connect(self.work_chance)  # кнопки Шанс
            elif i.text() == 'Налог':
                i.clicked.connect(self.work_tax)  # кнопки Налог
            elif i.text() == 'Казна':
                i.clicked.connect(self.work_treasury)  # кнопки Казна
        self.pushButton_start.clicked.connect(self.relax)  # остановка
        self.pushButton_progress.clicked.connect(self.next_move)  # следующий шаг
        self.pushButton_end.clicked.connect(self.game_end)  # конец игры
        self.pushButton_jai.clicked.connect(self.jai)  # тюрьма
        self.pushButton_into_prison.clicked.connect(self.jai)  # в тюрьму
        self.pushButton_camp.clicked.connect(self.relax)  # остановка на финише или старте

    def relax(self):  # отдых (просто вывод текста)
        self.progress = False
        self.plainTextEdit.appendPlainText(f'Игрок {self.players[self.player_number].name} выпил коктейль и готов идти дальше')

    def jai(self):  # тюрьма
        if self.checking_the_position(self.sender().text(),
                                      self.players[self.player_number].location):  # если на позиции Тюрьма
            self.progress = False  # прогресс есть -> можно идти дальше
        players = []  # заполняем список находящихся в тюрьме
        for i in self.players:
            if i.location == 30:  # если на позиции Тюрьма (уникальный номер 30) -> добавляем
                players.append(i)
        if players:
            ex2 = Window_Jail(players, parent=self)  # открываем окно Тюрьма
            ex2.exec_()
            for i in ex2.paying:  # список заплативших
                i.in_jail = False  # выводим из тюрьмы
                i.location += 1
                self.plainTextEdit.appendPlainText(f'Игрок {i.name} заплатил 500k и вышел из тюрьмы')

    def registration_of_participants(self, players):  # регистрация игроков
        for i in players:
            self.players.append(Player(i))

    def next_move(self):  # следующий шаг
        if not self.progress:  # если есть прогресс
            self.progress = True  # отменяем прогресс
            self.checking_player_loss()  # проверяем игроков на банкротство
            self.player_number += 1  # ходит следующий игрок
            if len(self.players) == self.player_number:
                self.player_number = 0
            if self.players[self.player_number].location == 30:  # если на позиции В тюрьму -> отправляем в тюрьму
                self.players[self.player_number].in_jail = True
            if not self.players[self.player_number].in_jail:  # если нет игрока в тюрьме
                self.cube = randrange(2, 13)  # рандомное количество ходов от 1 до 12 (так как бросаем 2 кубика)
                self.players[self.player_number].player_move(self.cube)  # игрок ходит
                self.label_4.setText(f'Сейчас ходит игрок {self.players[self.player_number].name} - {self.cube}')
            self.changing_player_data()  # выодим информацию о бюджете и собственностях игрока

    def changing_player_data(self):  # взаимодействие с консолью (бюджет и собственности игрока)
        self.plainTextEdit_player.clear()
        for i in self.players:
            self.plainTextEdit_player.appendPlainText(f'Игрок {i.name} на позиции {self.buttons[i.location].text()}')
            print(i.name, i.money)
            print('Собственность в залоге: ')
            for j in i.list_of_pledged_properties:
                print(j.name, j.color)
            print('Собственность:')
            for j in i.list_of_properties:
                print(j.name, j.color)
            print('-------------------------')

    def checking_the_position(self, name, location):  # проверяем, на данной позиции стоит игрок или нет
        if self.buttons[location].text() == name:
            return True
        return False

    def work_property(self):  # работа с собственностью
        owner = None
        for i in self.players:
            if self.sender().text() in i.list_property():
                owner = i  # проверяем, есть ли у данной собственности хозяин
        for i in self.list_of_own:
            for j in i:
                if j.name == self.sender().text():
                    property = j  # находим саму собственность
        if self.progress and self.checking_the_position(self.sender().text(),
                                                        self.players[self.player_number].location):  # если нажимает игрок, который ходит
            if not owner:  # если нет собственника
                ex2 = Window_property_purchase(self.players, self.sender().text(),
                                               property.price, self.player_number, parent=self)  # отскрываем окно аукциона или покупки
                ex2.exec_()
                ex2.winner.add_property(property, ex2.price)  # отдаем собственность покупаетелю
                self.plainTextEdit.appendPlainText(f'''Игрок {ex2.winner.name}
покупает {property.name} за {ex2.price}. Теперь бюджет: {ex2.winner.money}''')
            elif owner.name != self.players[self.player_number].name:  # если игрок не владеет собственностью
                self.plainTextEdit.appendPlainText(f'''Игрок {self.players[self.player_number].name}
платит ренту игроку {owner.name} за {property.name}
{property.rent(owner.quanity_propery_color(property.color))}''')
                self.players[self.player_number].self_property_playment(owner, property)
                owner.property_playment(property)  # игрок платит ренту
            self.progress = False  # есть прогресс
        else:  # если нажимает игрок, который сейчас не ходит
            pr = False
            for i in self.players:
                for j in i.list_of_pledged_properties:
                    if self.sender().text() == j.name:
                        owner = i  # ищем собственность в списке заложенных (игрок не платит ренту за заложенную собственность)
                        pr = True
            if owner:  # если игрок, который нажал на кнопку - хозяин
                ex2 = Window_sale_and_purchase(self.players, owner, property,
                                               property.pledge, pledge=pr, parent=self)  # открываем окно продажи, залога или выкупа
                ex2.exec_()
                if ex2.winner:  # если есть покупатель
                    owner.sale_property(property, ex2.price)   # продаем собственность
                    ex2.winner.add_property(property, ex2.price)  # собственность достается покупателю
                    self.plainTextEdit.appendPlainText(f'''Игрок {ex2.winner.name}
покупает у игрока {owner.name} за {ex2.price} {property.name}''')
                elif ex2.prov:  # если собственник отдал в залог или выкупил
                    if pr:  # если выкупил
                        owner.the_redemption_of_the_property(property)  # возвращаем собственность в список незаложенных
                        self.plainTextEdit.appendPlainText(f'''Игрок {owner.name}
выкупает {property.name} за {property.pledge + property.pledge // 10}''')
                    else:  # если отдает в залог
                        owner.property_as_collateral(property)  # переносим собственность в список заложенных
                        self.plainTextEdit.appendPlainText(f'''Игрок {owner.name}
отдает в залог {property.name}, получая {property.pledge}''')

    def work_treasury(self):  # кнопка Казна
        if self.progress and self.checking_the_position(self.sender().text(),
                                                        self.players[self.player_number].location): # если позиция игрока верна
            self.progress = False  # есть прогресс
            self.plainTextEdit_treasury.clear()
            f = sqlite3.connect("monopoly_db.db")
            cur = f.cursor()
            k = randrange(1, 11)
            x = f'select text, money from treasury where id = {k}'
            result = cur.execute(x).fetchone()  # вытаскиваем рандомную карточку Казна
            self.plainTextEdit_treasury.appendPlainText(result[0])
            self.players[self.player_number].payment_of_money(result[1])  # игрок платит или получает деньги
            if result[1] < 0:
                self.plainTextEdit.appendPlainText(f'Игрок {self.players[self.player_number].name} платит в казну {abs(result[1])}')
            else:
                self.plainTextEdit.appendPlainText(f'Игрок {self.players[self.player_number].name} получает {result[1]}')

    def work_chance(self):  # кнопка Шанс
        if self.progress and self.checking_the_position(self.sender().text(),
                                                        self.players[self.player_number].location):  # если позиция верна
            self.progress = False  # прогресс есть
            self.plainTextEdit_chane.clear()
            f = sqlite3.connect("monopoly_db.db")
            cur = f.cursor()
            k = randrange(1, 7)
            x = f'select text, money from chance where id = {k}'
            result = cur.execute(x).fetchone()  # вытаскиваем рандомную карточку Шанс
            self.plainTextEdit_chane.appendPlainText(result[0])
            self.players[self.player_number].payment_of_money(result[1])  # игрок получает или отдает деньги
            if result[1] < 0:
                self.plainTextEdit.appendPlainText(
                    f'Игрок {self.players[self.player_number].name} платит в казну {abs(result[1])}')
            else:
                self.plainTextEdit.appendPlainText(f'Игрок {self.players[self.player_number].name} получает {result[1]}')

    def work_tax(self):  # карточка Налог
        if self.progress and self.checking_the_position(self.sender().text(),
                                                        self.players[self.player_number].location):  # если позиция верна
            self.progress = False  # прогресс есть
            self.players[self.player_number].payment_of_money(-1000000)  # игрок платит налог
            self.plainTextEdit.appendPlainText(
                    f'Игрок {self.players[self.player_number].name} платит налог 1000000')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
