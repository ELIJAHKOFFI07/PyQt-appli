# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_appYDsBXu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(945, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout = QVBoxLayout(self.drop_shadow_frame)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.head_frame_menu = QFrame(self.drop_shadow_frame)
        self.head_frame_menu.setObjectName(u"head_frame_menu")
        self.head_frame_menu.setMinimumSize(QSize(0, 75))
        self.head_frame_menu.setMaximumSize(QSize(16777215, 80))
        self.head_frame_menu.setStyleSheet(u"#head_frame_menu{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton{border:none}")
        self.head_frame_menu.setFrameShape(QFrame.NoFrame)
        self.head_frame_menu.setFrameShadow(QFrame.Raised)
        self.head_menu_layout = QHBoxLayout(self.head_frame_menu)
        self.head_menu_layout.setSpacing(0)
        self.head_menu_layout.setObjectName(u"head_menu_layout")
        self.head_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.logo_btn = QPushButton(self.head_frame_menu)
        self.logo_btn.setObjectName(u"logo_btn")
        self.logo_btn.setMinimumSize(QSize(150, 60))
        icon = QIcon()
        icon.addFile(u":/img/Resources/image/photo_2023-08-04_13-32-33.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_btn.setIcon(icon)
        self.logo_btn.setIconSize(QSize(150, 95))

        self.head_menu_layout.addWidget(self.logo_btn)

        self.toogle_menu = QPushButton(self.head_frame_menu)
        self.toogle_menu.setObjectName(u"toogle_menu")
        self.toogle_menu.setMinimumSize(QSize(70, 35))
        self.toogle_menu.setMaximumSize(QSize(60, 16777215))
        self.toogle_menu.setStyleSheet(u"#toogle_menu:hover {\n"
"    background-color: rgba(241, 139, 14, 50); /* Couleur de fond au survol */\n"
"    border-radius: 8px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/Resources/feather/align-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toogle_menu.setIcon(icon1)
        self.toogle_menu.setIconSize(QSize(80, 50))

        self.head_menu_layout.addWidget(self.toogle_menu)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.head_menu_layout.addItem(self.horizontalSpacer)

        self.frame_search_box = QFrame(self.head_frame_menu)
        self.frame_search_box.setObjectName(u"frame_search_box")
        self.frame_search_box.setMaximumSize(QSize(400, 55))
        self.frame_search_box.setStyleSheet(u"#frame_search_box {\n"
"    border: 1px solid rgba(241, 139, 14, 155);\n"
"    border-radius: 13px;\n"
"}\n"
"\n"
"#seach_line {\n"
"    background-color: rgba(0, 0, 0, 0); /* Fond transparent */\n"
"    border: none; /* Pas de bordure */\n"
"    padding: 8px; /* Espacement interne */\n"
"    font-size: 14px;\n"
"    color: #333; /* Couleur du texte */\n"
"    width: 100%; /* Largeur de la zone de recherche */\n"
"}\n"
"\n"
"#search_btn {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure */\n"
"    padding: 0; /* Pas de rembourrage */\n"
"    margin: 0; /* Pas de marge */\n"
"}\n"
"\n"
"#search_btn:hover {\n"
"    background-color: rgba(241, 139, 14, 50); /* Couleur de fond au survol */\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.frame_search_box.setFrameShape(QFrame.StyledPanel)
        self.frame_search_box.setFrameShadow(QFrame.Raised)
        self.layout_seach_box = QHBoxLayout(self.frame_search_box)
        self.layout_seach_box.setSpacing(0)
        self.layout_seach_box.setObjectName(u"layout_seach_box")
        self.layout_seach_box.setContentsMargins(0, 0, 10, 0)
        self.seach_line = QLineEdit(self.frame_search_box)
        self.seach_line.setObjectName(u"seach_line")
        self.seach_line.setMinimumSize(QSize(0, 40))

        self.layout_seach_box.addWidget(self.seach_line)

        self.search_btn = QPushButton(self.frame_search_box)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(45, 45))
        icon2 = QIcon()
        icon2.addFile(u":/img/Resources/image/search_FILL0_wght400_GRAD0_opsz40.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon2)
        self.search_btn.setIconSize(QSize(40, 45))

        self.layout_seach_box.addWidget(self.search_btn)


        self.head_menu_layout.addWidget(self.frame_search_box)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.head_menu_layout.addItem(self.horizontalSpacer_2)

        self.notifiy_frame = QFrame(self.head_frame_menu)
        self.notifiy_frame.setObjectName(u"notifiy_frame")
        self.notifiy_frame.setMinimumSize(QSize(50, 50))
        self.notifiy_frame.setMaximumSize(QSize(60, 50))
        self.notifiy_frame.setStyleSheet(u"/*QFrame{  \n"
"background-color: #c6e2ff;\n"
"     border: 2px solid #fff;\n"
"       border-radius: 25px;\n"
"}*/\n"
"#panier_btn{\n"
"border:none;\n"
"}\n"
"#notifiy_frame:hover {\n"
"    background-color: rgba(241, 139, 14, 50); /* Couleur de fond au survol */\n"
"    border-radius: 22px;\n"
"}\n"
"")
        self.notifiy_frame.setFrameShape(QFrame.StyledPanel)
        self.notifiy_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.notifiy_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.panier_btn = QPushButton(self.notifiy_frame)
        self.panier_btn.setObjectName(u"panier_btn")
        self.panier_btn.setMinimumSize(QSize(45, 45))
        self.panier_btn.setMaximumSize(QSize(45, 45))
        self.panier_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/img/Resources/image/shopping_cart_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.panier_btn.setIcon(icon3)
        self.panier_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.panier_btn, 0, Qt.AlignHCenter)

        self.label_number_notify_2 = QLabel(self.notifiy_frame)
        self.label_number_notify_2.setObjectName(u"label_number_notify_2")
        self.label_number_notify_2.setMinimumSize(QSize(20, 20))
        self.label_number_notify_2.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_number_notify_2.setFont(font)
        self.label_number_notify_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_number_notify_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.head_menu_layout.addWidget(self.notifiy_frame)

        self.frame_5 = QFrame(self.head_frame_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(150, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.head_menu_layout.addWidget(self.frame_5)

        self.user_btn = QPushButton(self.head_frame_menu)
        self.user_btn.setObjectName(u"user_btn")
        icon4 = QIcon()
        icon4.addFile(u":/img/Resources/image/account_circle_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon4)
        self.user_btn.setIconSize(QSize(50, 60))

        self.head_menu_layout.addWidget(self.user_btn)


        self.drop_shadow_layout.addWidget(self.head_frame_menu)

        self.frame_contain = QFrame(self.drop_shadow_frame)
        self.frame_contain.setObjectName(u"frame_contain")
        self.frame_contain.setFrameShape(QFrame.NoFrame)
        self.frame_contain.setFrameShadow(QFrame.Raised)
        self.contain = QHBoxLayout(self.frame_contain)
        self.contain.setObjectName(u"contain")
        self.frame_left_menu = QFrame(self.frame_contain)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMaximumSize(QSize(0, 16777215))
        self.frame_left_menu.setStyleSheet(u"\n"
"#frame_left_menu {\n"
"    background-color: rgba(241, 139, 14, 50); /* Couleur de fond */\n"
"    border-radius: 10px; /* Arrondi des coins */\n"
"	image: url(:/img/Resources/image/combio-removebg-preview.png)\n"
"}\n"
"\n"
"#accueil_btn, #commande_btn, #space_client_btn,#space_admin_btn {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #fff; /* Couleur du texte */\n"
"    font-size: 16px;\n"
"    padding: 10px 20px; /* Espacement interne (haut et bas, gauche et droite) */\n"
"    text-align: left;\n"
"    transition: background-color 0.2s, border-radius 0.2s;\n"
"}\n"
"\n"
"#accueil_btn:hover, #commande_btn:hover, #space_client_btn:hover,#space_admin_btn:hover {\n"
"    background-color: rgba(241, 139, 14, 50); /* Couleur de fond au survol */\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#accueil_btn:pressed, #commande_btn:pressed, #space_client_btn:pressed,#space_admin_btn:pressed {\n"
"    background-color: rgba(241, 139, 14, 100); /* Couleur de fond enfonc\u00e9e */\n"
"    b"
                        "order-radius: 5px; /* Bordure l\u00e9g\u00e8rement arrondie enfonc\u00e9e */\n"
"    color: #fff; /* Couleur du texte enfonc\u00e9 */\n"
"}\n"
"\n"
"")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.left_menu_layout = QVBoxLayout(self.frame_left_menu)
        self.left_menu_layout.setObjectName(u"left_menu_layout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.accueil_btn = QPushButton(self.frame_left_menu)
        self.accueil_btn.setObjectName(u"accueil_btn")
        self.accueil_btn.setMinimumSize(QSize(0, 45))
        icon5 = QIcon()
        icon5.addFile(u":/white/Resources/feather_w/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accueil_btn.setIcon(icon5)
        self.accueil_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.accueil_btn)

        self.commande_btn = QPushButton(self.frame_left_menu)
        self.commande_btn.setObjectName(u"commande_btn")
        self.commande_btn.setMinimumSize(QSize(0, 45))
        icon6 = QIcon()
        icon6.addFile(u":/white/Resources/feather_w/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.commande_btn.setIcon(icon6)
        self.commande_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.commande_btn)

        self.space_client_btn = QPushButton(self.frame_left_menu)
        self.space_client_btn.setObjectName(u"space_client_btn")
        self.space_client_btn.setMinimumSize(QSize(0, 45))
        icon7 = QIcon()
        icon7.addFile(u":/white/Resources/feather_w/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.space_client_btn.setIcon(icon7)
        self.space_client_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.space_client_btn)


        self.left_menu_layout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 258, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.left_menu_layout.addItem(self.verticalSpacer)

        self.space_admin_btn = QPushButton(self.frame_left_menu)
        self.space_admin_btn.setObjectName(u"space_admin_btn")
        self.space_admin_btn.setMinimumSize(QSize(0, 45))
        icon8 = QIcon()
        icon8.addFile(u":/white/Resources/feather_w/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.space_admin_btn.setIcon(icon8)
        self.space_admin_btn.setIconSize(QSize(28, 28))

        self.left_menu_layout.addWidget(self.space_admin_btn)


        self.contain.addWidget(self.frame_left_menu)

        self.page = QStackedWidget(self.frame_contain)
        self.page.setObjectName(u"page")
        self.page.setFrameShape(QFrame.NoFrame)
        self.page.setFrameShadow(QFrame.Raised)
        self.pagePage1 = QWidget()
        self.pagePage1.setObjectName(u"pagePage1")
        self.page.addWidget(self.pagePage1)

        self.contain.addWidget(self.page)


        self.drop_shadow_layout.addWidget(self.frame_contain)


        self.verticalLayout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_btn.setText("")
        self.toogle_menu.setText("")
        self.seach_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.search_btn.setText("")
        self.panier_btn.setText("")
        self.label_number_notify_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.user_btn.setText("")
        self.accueil_btn.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.commande_btn.setText(QCoreApplication.translate("MainWindow", u"commande", None))
        self.space_client_btn.setText(QCoreApplication.translate("MainWindow", u"Espace Clients", None))
        self.space_admin_btn.setText(QCoreApplication.translate("MainWindow", u"Espace Administrateur", None))
    # retranslateUi

