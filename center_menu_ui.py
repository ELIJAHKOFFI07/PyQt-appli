# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'center_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(975, 557)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        StackedWidget.addWidget(self.home_page)
        self.gest_prod_page = QWidget()
        self.gest_prod_page.setObjectName(u"gest_prod_page")
        self.gest_prod_page.setStyleSheet(u"#gest_prod_page{background-color: rgba(255, 255, 255, 100);}\n"
"#label_title_gestprod {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    background-color: #f8f9fa;\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #dee2e6;\n"
"}\n"
"\n"
"#frame_contain_gest_p {\n"
"    border: 1px solid #dee2e6;\n"
"    border-radius: 8px;\n"
"    margin: 10px;\n"
"    padding: 10px;\n"
"    background-color: #f8f9fa;\n"
"}\n"
"\n"
"#frame_add_prod {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dee2e6;\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"#label_nom_prod,\n"
"#label_catergeorie,\n"
"#label_prix,\n"
"#label_descr {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#nom_prod_le,\n"
"#categorie_prod_le,\n"
"#prix_prod_le,\n"
"#textEdit {\n"
"    font-size: 16px;\n"
"    padding: 5px;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#nom_prod_le:focus,\n"
"#categorie_prod_le:focus,\n"
"#prix_prod_le:focus,\n"
"#textEdit:fo"
                        "cus {\n"
"    border-color: #80bdff;\n"
"    outline: 0;\n"
"    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);\n"
"}\n"
"\n"
"#bouton_modifier {\n"
"    background-color: #ffc107; /* Couleur jaune */\n"
"    border: 1px solid #ffc107; /* Bordure jaune */\n"
"    color: #FFFFFF; /* Couleur du texte par d\u00e9faut */\n"
"    border-radius: 5px; /* Bords arrondis */\n"
"    padding: 5px 10px; /* Espacement interne du bouton */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Police en gras */\n"
"}\n"
"\n"
"#bouton_modifier:hover {\n"
"    background-color: #e0a800; /* Couleur jaune fonc\u00e9e */\n"
"    border: 1px solid #e0a800; /* Bordure jaune fonc\u00e9e */\n"
"}\n"
"\n"
"#bouton_modifier:pressed {\n"
"    background-color: #b58905; /* Couleur jaune fonc\u00e9e lorsque le bouton est enfonc\u00e9 */\n"
"    border: 1px solid #b58905; /* Bordure jaune fonc\u00e9e lorsque le bouton est enfonc\u00e9 */\n"
"}\n"
"\n"
"#bouton_ajouter {\n"
"    background-color: #28a745; /* Co"
                        "uleur verte */\n"
"    border: 1px solid #28a745; /* Bordure verte */\n"
"    color: #FFFFFF; /* Couleur du texte par d\u00e9faut */\n"
"    border-radius: 5px; /* Bords arrondis */\n"
"    padding: 5px 10px; /* Espacement interne du bouton */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Police en gras */\n"
"}\n"
"\n"
"#bouton_ajouter:hover {\n"
"    background-color: #218838; /* Couleur verte fonc\u00e9e */\n"
"    border: 1px solid #218838; /* Bordure verte fonc\u00e9e */\n"
"}\n"
"\n"
"#bouton_ajouter:pressed {\n"
"    background-color: #1e7e34; /* Couleur verte fonc\u00e9e lorsque le bouton est enfonc\u00e9 */\n"
"    border: 1px solid #1e7e34; /* Bordure verte fonc\u00e9e lorsque le bouton est enfonc\u00e9 */\n"
"}\n"
"\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.gest_prod_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_title_gestprod = QLabel(self.gest_prod_page)
        self.label_title_gestprod.setObjectName(u"label_title_gestprod")
        self.label_title_gestprod.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setBold(True)
        self.label_title_gestprod.setFont(font)

        self.verticalLayout_5.addWidget(self.label_title_gestprod)

        self.frame_contain_gest_p = QFrame(self.gest_prod_page)
        self.frame_contain_gest_p.setObjectName(u"frame_contain_gest_p")
        self.frame_contain_gest_p.setStyleSheet(u"")
        self.frame_contain_gest_p.setFrameShape(QFrame.StyledPanel)
        self.frame_contain_gest_p.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_contain_gest_p)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_9 = QFrame(self.frame_contain_gest_p)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_add_prod = QFrame(self.frame_9)
        self.frame_add_prod.setObjectName(u"frame_add_prod")
        self.frame_add_prod.setMaximumSize(QSize(600, 16777215))
        self.gridLayout_2 = QGridLayout(self.frame_add_prod)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_nom_prod = QLabel(self.frame_add_prod)
        self.label_nom_prod.setObjectName(u"label_nom_prod")

        self.gridLayout_2.addWidget(self.label_nom_prod, 0, 1, 1, 1)

        self.categorie_prod_le = QLineEdit(self.frame_add_prod)
        self.categorie_prod_le.setObjectName(u"categorie_prod_le")
        self.categorie_prod_le.setMinimumSize(QSize(44, 0))
        self.categorie_prod_le.setMaximumSize(QSize(300, 60))

        self.gridLayout_2.addWidget(self.categorie_prod_le, 1, 4, 1, 1)

        self.textEdit = QTextEdit(self.frame_add_prod)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_2.addWidget(self.textEdit, 5, 4, 1, 1)

        self.label_catergeorie = QLabel(self.frame_add_prod)
        self.label_catergeorie.setObjectName(u"label_catergeorie")

        self.gridLayout_2.addWidget(self.label_catergeorie, 1, 1, 1, 1)

        self.label_prix = QLabel(self.frame_add_prod)
        self.label_prix.setObjectName(u"label_prix")

        self.gridLayout_2.addWidget(self.label_prix, 2, 1, 1, 1)

        self.bouton_ajouter = QPushButton(self.frame_add_prod)
        self.bouton_ajouter.setObjectName(u"bouton_ajouter")

        self.gridLayout_2.addWidget(self.bouton_ajouter, 6, 4, 1, 1)

        self.prix_prod_le = QLineEdit(self.frame_add_prod)
        self.prix_prod_le.setObjectName(u"prix_prod_le")
        self.prix_prod_le.setMinimumSize(QSize(44, 0))
        self.prix_prod_le.setMaximumSize(QSize(300, 60))

        self.gridLayout_2.addWidget(self.prix_prod_le, 2, 4, 1, 1)

        self.nom_prod_le = QLineEdit(self.frame_add_prod)
        self.nom_prod_le.setObjectName(u"nom_prod_le")
        self.nom_prod_le.setMinimumSize(QSize(44, 0))
        self.nom_prod_le.setMaximumSize(QSize(300, 60))

        self.gridLayout_2.addWidget(self.nom_prod_le, 0, 4, 1, 1)

        self.label_descr = QLabel(self.frame_add_prod)
        self.label_descr.setObjectName(u"label_descr")
        self.label_descr.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_descr, 5, 1, 1, 1)

        self.toolButton = QToolButton(self.frame_add_prod)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.toolButton, 5, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_add_prod)

        self.bouton_modifier = QPushButton(self.frame_9)
        self.bouton_modifier.setObjectName(u"bouton_modifier")
        self.bouton_modifier.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout_4.addWidget(self.bouton_modifier)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_contain_gest_p)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.option_stockage = QGroupBox(self.frame_8)
        self.option_stockage.setObjectName(u"option_stockage")
        self.option_stockage.setMaximumSize(QSize(549, 110))
        self.option_stockage.setStyleSheet(u"#option_stockage{\n"
"background-color:#f1f1f1;\n"
"border:1px solid #ccc;\n"
"border-radius:12px;\n"
"}\n"
"/* Styliser le bouton \"Modifier\" */\n"
"QPushButton#retirer_produit_btn {\n"
"    background-color: #ffc107; /* Couleur jaune */\n"
"    color: #FFFFFF; /* Couleur du texte par d\u00e9faut */\n"
"    border: 1px solid #ffc107; /* Bordure jaune */\n"
"    border-radius: 5px; /* Bords arrondis */\n"
"    padding: 8px 16px; /* Espacement interne */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Police en gras */\n"
"}\n"
"\n"
"QPushButton#retirer_produit_btn:hover {\n"
"    background-color: #e0a800; /* Couleur jaune fonc\u00e9e au survol */\n"
"    border: 1px solid #e0a800; /* Bordure jaune fonc\u00e9e au survol */\n"
"}\n"
"\n"
"QPushButton#retirer_produit_btn:pressed {\n"
"    background-color: #b58905; /* Couleur jaune fonc\u00e9e lorsque le bouton est enfonc\u00e9 */\n"
"    border: 1px solid #b58905; /* Bordure jaune fonc\u00e9e lorsque le bouton est enfonc\u00e9 "
                        "*/\n"
"}\n"
"/* Styliser le bouton \"Supprimer\" */\n"
"QPushButton#supprimer_produit_btn {\n"
"    background-color: #dc3545; /* Couleur rouge */\n"
"    color: #FFFFFF; /* Couleur du texte par d\u00e9faut */\n"
"    border: 1px solid #dc3545; /* Bordure rouge */\n"
"    border-radius: 5px; /* Bords arrondis */\n"
"    padding: 8px 16px; /* Espacement interne */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Police en gras */\n"
"}\n"
"\n"
"QPushButton#supprimer_produit_btn:hover {\n"
"    background-color: #c82333; /* Couleur rouge fonc\u00e9e au survol */\n"
"    border: 1px solid #c82333; /* Bordure rouge fonc\u00e9e au survol */\n"
"}\n"
"\n"
"QPushButton#supprimer_produit_btn:pressed {\n"
"    background-color: #b21f2d; /* Couleur rouge fonc\u00e9e lorsque le bouton est enfonc\u00e9 */\n"
"    border: 1px solid #b21f2d; /* Bordure rouge fonc\u00e9e lorsque le bouton est enfonc\u00e9 */\n"
"}\n"
"/* Styliser le bouton \"Ajouter\" */\n"
"QPushButton#ajouter_produit_btn {\n"
""
                        "    background-color: #28a745; /* Couleur verte */\n"
"    color: #FFFFFF; /* Couleur du texte par d\u00e9faut */\n"
"    border: 1px solid #28a745; /* Bordure verte */\n"
"    border-radius: 5px; /* Bords arrondis */\n"
"    padding: 8px 16px; /* Espacement interne */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Police en gras */\n"
"}\n"
"\n"
"QPushButton#ajouter_produit_btn:hover {\n"
"    background-color: #218838; /* Couleur verte fonc\u00e9e au survol */\n"
"    border: 1px solid #218838; /* Bordure verte fonc\u00e9e au survol */\n"
"}\n"
"\n"
"QPushButton#ajouter_produit_btn:pressed {\n"
"    background-color: #1e7e34; /* Couleur verte fonc\u00e9e lorsque le bouton est enfonc\u00e9 */\n"
"    border: 1px solid #1e7e34; /* Bordure verte fonc\u00e9e lorsque le bouton est enfonc\u00e9 */\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_3 = QGridLayout(self.option_stockage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.layout_tool_btn = QHBoxLayout()
        self.layout_tool_btn.setObjectName(u"layout_tool_btn")
        self.ajouter_produit_btn = QPushButton(self.option_stockage)
        self.ajouter_produit_btn.setObjectName(u"ajouter_produit_btn")
        self.ajouter_produit_btn.setMinimumSize(QSize(0, 30))

        self.layout_tool_btn.addWidget(self.ajouter_produit_btn)

        self.retirer_produit_btn = QPushButton(self.option_stockage)
        self.retirer_produit_btn.setObjectName(u"retirer_produit_btn")
        self.retirer_produit_btn.setMinimumSize(QSize(0, 30))

        self.layout_tool_btn.addWidget(self.retirer_produit_btn)


        self.gridLayout_3.addLayout(self.layout_tool_btn, 0, 1, 1, 1)

        self.layout_list = QHBoxLayout()
        self.layout_list.setObjectName(u"layout_list")
        self.liste_prod_combo_box = QComboBox(self.option_stockage)
        self.liste_prod_combo_box.setObjectName(u"liste_prod_combo_box")
        self.liste_prod_combo_box.setMinimumSize(QSize(250, 0))
        self.liste_prod_combo_box.setStyleSheet(u"/* Styliser le bouton d\u00e9roulant du QComboBox */\n"
"QComboBox {\n"
"    background-color: #e9ecef; /* Couleur de fond */\n"
"    color: #495057; /* Couleur du texte par d\u00e9faut */\n"
"    border: 1px solid #ced4da; /* Bordure */\n"
"    border-radius: 8px; /* Bords arrondis */\n"
"    padding: 8px; /* Espacement interne */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Police en gras */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #dee2e6; /* Couleur au survol */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #ced4da; /* Couleur lorsque le bouton est enfonc\u00e9 */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 25px; /* Largeur de la fl\u00e8che du bouton d\u00e9roulant */\n"
"    border: none; /* Supprimer la bordure de la fl\u00e8che */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(arrow_down.png); /* Remplacer \"arrow_down.png\" par le chemin vers votre image de fl\u00e8che personnalis\u00e9e */\n"
"}\n"
"\n"
"/* Styli"
                        "ser la liste d\u00e9roulante du QComboBox */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #e9ecef; /* Couleur de fond de la liste d\u00e9roulante */\n"
"    border: 1px solid #ced4da; /* Bordure de la liste d\u00e9roulante */\n"
"    border-radius: 8px; /* Bords arrondis */\n"
"    padding: 8px; /* Espacement interne */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Police en gras */\n"
"    min-width: 200px; /* Largeur minimale de la liste d\u00e9roulante */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    height: 30px; /* Hauteur de chaque \u00e9l\u00e9ment de la liste */\n"
"    padding: 5px 15px; /* Espacement interne des \u00e9l\u00e9ments */\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #007bff; /* Couleur bleue pour l'\u00e9l\u00e9ment s\u00e9lectionn\u00e9 */\n"
"    color: #FFFFFF; /* Couleur du texte de l'\u00e9l\u00e9ment s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QComboBox QAbstr"
                        "actItemView::item:hover {\n"
"    background-color: #ced4da; /* Couleur au survol */\n"
"}\n"
"")

        self.layout_list.addWidget(self.liste_prod_combo_box)

        self.quantite_spin_box = QSpinBox(self.option_stockage)
        self.quantite_spin_box.setObjectName(u"quantite_spin_box")
        self.quantite_spin_box.setMaximumSize(QSize(73, 41))
        self.quantite_spin_box.setStyleSheet(u"/* Styliser le QSpinBox */\n"
"QSpinBox {\n"
"    background-color: #e9ecef; /* Couleur de fond */\n"
"    color: #495057; /* Couleur du texte par d\u00e9faut */\n"
"    border: 1px solid #ced4da; /* Bordure */\n"
"    border-radius: 8px; /* Bords arrondis */\n"
"    padding: 8px; /* Espacement interne */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Police en gras */\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    background-color: #dee2e6; /* Couleur au survol */\n"
"}\n"
"\n"
"QSpinBox:pressed {\n"
"    background-color: #ced4da; /* Couleur lorsque le bouton est enfonc\u00e9 */\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border; /* Positionnement du bouton d'incr\u00e9mentation */\n"
"    subcontrol-position: top right; /* Positionnement du bouton d'incr\u00e9mentation */\n"
"    width: 30px; /* Largeur du bouton d'incr\u00e9mentation */\n"
"    border-left: none; /* Supprimer la bordure \u00e0 gauche du bouton d'incr\u00e9mentation */\n"
"    border-top-right-"
                        "radius: 8px; /* Bords arrondis \u00e0 droite du bouton d'incr\u00e9mentation */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover,\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: #007bff; /* Couleur bleue pour le bouton d'incr\u00e9mentation au survol et lorsque le bouton est enfonc\u00e9 */\n"
"    color: #FFFFFF; /* Couleur du texte du bouton d'incr\u00e9mentation au survol et lorsque le bouton est enfonc\u00e9 */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border; /* Positionnement du bouton de d\u00e9cr\u00e9mentation */\n"
"    subcontrol-position: bottom right; /* Positionnement du bouton de d\u00e9cr\u00e9mentation */\n"
"    width: 30px; /* Largeur du bouton de d\u00e9cr\u00e9mentation */\n"
"    border-left: none; /* Supprimer la bordure \u00e0 gauche du bouton de d\u00e9cr\u00e9mentation */\n"
"    border-bottom-right-radius: 8px; /* Bords arrondis \u00e0 droite du bouton de d\u00e9cr\u00e9mentation */\n"
"}\n"
"\n"
"QSpinBox::down-button:hover,\n"
"QSpinBox::down-button:pres"
                        "sed {\n"
"    background-color: #dc3545; /* Couleur rouge pour le bouton de d\u00e9cr\u00e9mentation au survol et lorsque le bouton est enfonc\u00e9 */\n"
"    color: #FFFFFF; /* Couleur du texte du bouton de d\u00e9cr\u00e9mentation au survol et lorsque le bouton est enfonc\u00e9 */\n"
"}\n"
"\n"
"QSpinBox::up-arrow,\n"
"QSpinBox::down-arrow {\n"
"    image: url(arrow_up_down.png); /* Remplacer \"arrow_up_down.png\" par le chemin vers votre image d'ic\u00f4ne d'incr\u00e9mentation/d\u00e9cr\u00e9mentation */\n"
"    width: 20px; /* Largeur de l'ic\u00f4ne d'incr\u00e9mentation/d\u00e9cr\u00e9mentation */\n"
"    height: 20px; /* Hauteur de l'ic\u00f4ne d'incr\u00e9mentation/d\u00e9cr\u00e9mentation */\n"
"}\n"
"")

        self.layout_list.addWidget(self.quantite_spin_box)


        self.gridLayout_3.addLayout(self.layout_list, 0, 0, 1, 1)

        self.supprimer_produit_btn = QPushButton(self.option_stockage)
        self.supprimer_produit_btn.setObjectName(u"supprimer_produit_btn")
        self.supprimer_produit_btn.setMinimumSize(QSize(0, 30))
        self.supprimer_produit_btn.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_3.addWidget(self.supprimer_produit_btn, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.option_stockage, 2, 0, 1, 2)

        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_9.setFont(font1)

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.stock_tab = QTableWidget(self.frame_8)
        if (self.stock_tab.columnCount() < 2):
            self.stock_tab.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.stock_tab.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.stock_tab.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.stock_tab.setObjectName(u"stock_tab")
        self.stock_tab.setMaximumSize(QSize(600, 16777215))
        self.stock_tab.setStyleSheet(u"/* Style de la table sublime */\n"
"            QTableWidget {\n"
"                border: 1px solid #dee2e6;\n"
"                border-collapse: collapse;\n"
"                width: 100%;\n"
"                font-size: 16px;\n"
"            }\n"
"\n"
"            /* Style des cellules de la table sublime */\n"
"            QTableWidget::item {\n"
"                border: 1px solid #dee2e6;\n"
"                padding: 10px;\n"
"                text-align: center;\n"
"                background-color: #f2f2f2;\n"
"                color: #333;\n"
"            }\n"
"\n"
"            /* Style de l'en-t\u00eate de la table sublime */\n"
"            QTableWidget::item:selected {\n"
"                background-color: #007bff;\n"
"                color: #ffffff;\n"
"            }\n"
"\n"
"            /* Style des lignes paires de la table sublime */\n"
"            QTableWidget::item:alternate {\n"
"                background-color: #e9ecef;\n"
"            }\n"
"\n"
"            /* Style des lignes impaires de la "
                        "table sublime */\n"
"            QTableWidget::item:!alternate {\n"
"                background-color: #ffffff;\n"
"            }\n"
"\n"
"            /* Style des lignes au survol de la table sublime */\n"
"            QTableWidget::item:hover {\n"
"                background-color: #d4edda;\n"
"            }\n"
"\n"
"            /* Style de l'en-t\u00eate de la table sublime */\n"
"            QHeaderView::section {\n"
"                background-color: #f8f9fa;\n"
"                color: #212529;\n"
"                padding: 3px;\n"
"                border: 1px solid #dee2e6;\n"
"                font: 700 11pt \"Segoe UI\";\n"
"            }\n"
"\n"
"            /* Style des barres de d\u00e9filement de la table sublime */\n"
"            QScrollBar:vertical, QScrollBar:horizontal {\n"
"                background-color: #f8f9fa;\n"
"                width: 8px;\n"
"            }\n"
"\n"
"            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"                background-color: #007bff;\n"
""
                        "                border-radius: 4px;\n"
"            }\n"
"\n"
"            QScrollBar::add-line:vertical, QScrollBar::add-line:horizontal,\n"
"            QScrollBar::sub-line:vertical, QScrollBar::sub-line:horizontal {\n"
"                background: none;\n"
"            }\n"
"\n"
"            QScrollBar::add-page:vertical, QScrollBar::add-page:horizontal,\n"
"            QScrollBar::sub-page:vertical, QScrollBar::sub-page:horizontal {\n"
"                background: none;\n"
"            }")
        self.stock_tab.horizontalHeader().setMinimumSectionSize(180)
        self.stock_tab.horizontalHeader().setDefaultSectionSize(200)
        self.stock_tab.horizontalHeader().setProperty("showSortIndicator", True)
        self.stock_tab.horizontalHeader().setStretchLastSection(True)
        self.stock_tab.verticalHeader().setHighlightSections(False)
        self.stock_tab.verticalHeader().setProperty("showSortIndicator", True)
        self.stock_tab.verticalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.stock_tab, 3, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_5.addWidget(self.frame_contain_gest_p)

        StackedWidget.addWidget(self.gest_prod_page)
        self.gest_client_page = QWidget()
        self.gest_client_page.setObjectName(u"gest_client_page")
        self.verticalLayout_6 = QVBoxLayout(self.gest_client_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_title_list_clients = QLabel(self.gest_client_page)
        self.label_title_list_clients.setObjectName(u"label_title_list_clients")
        font2 = QFont()
        font2.setPointSize(33)
        self.label_title_list_clients.setFont(font2)
        self.label_title_list_clients.setStyleSheet(u"font-size:30em\n"
"")

        self.verticalLayout_6.addWidget(self.label_title_list_clients)

        self.frame_7 = QFrame(self.gest_client_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"padding-left:50px;")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"padding-left:130px;")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"padding-left:70px;")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_13)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.scroll = QScrollArea(self.gest_client_page)
        self.scroll.setObjectName(u"scroll")
        self.scroll.setStyleSheet(u"   \n"
"            QScrollArea {\n"
"                background-color: transparent;\n"
"                border: none;\n"
"            }\n"
"table_info {\n"
"                background-color: #fff;\n"
"                border-radius: 5px;\n"
"                border: 1px solid #ccc;\n"
"                padding: 10px;\n"
"                margin: 5px;\n"
"            }\n"
"            QPushButton {\n"
"                background-color: #007bff;\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                padding: 8px 15px;\n"
"                font-size: 14px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0056b3;\n"
"            }\n"
"        ''')\n"
"")
        self.scroll.setWidgetResizable(True)
        self.scroll_area_content = QWidget()
        self.scroll_area_content.setObjectName(u"scroll_area_content")
        self.scroll_area_content.setGeometry(QRect(0, 0, 957, 426))
        self.scroll.setWidget(self.scroll_area_content)

        self.verticalLayout_6.addWidget(self.scroll)

        StackedWidget.addWidget(self.gest_client_page)
        self.panier_page = QWidget()
        self.panier_page.setObjectName(u"panier_page")
        self.panier_page.setStyleSheet(u"#panier_page{\n"
"	\n"
"	background-color: rgba(91, 224, 239, 22);\n"
"	\n"
"	background-image: url(:/icon/Resources/image/combio-removebg-preview.png);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.panier_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_head_panier = QFrame(self.panier_page)
        self.frame_head_panier.setObjectName(u"frame_head_panier")
        self.frame_head_panier.setMinimumSize(QSize(231, 0))
        self.frame_head_panier.setMaximumSize(QSize(231, 73))
        self.horizontalLayout_10 = QHBoxLayout(self.frame_head_panier)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_logo_panier_2 = QLabel(self.frame_head_panier)
        self.label_logo_panier_2.setObjectName(u"label_logo_panier_2")
        self.label_logo_panier_2.setMinimumSize(QSize(51, 71))
        self.label_logo_panier_2.setMaximumSize(QSize(51, 71))
        self.label_logo_panier_2.setPixmap(QPixmap(u":/icon/Resources/image/shopping_cart_FILL0_wght400_GRAD0_opsz48.svg"))

        self.horizontalLayout_10.addWidget(self.label_logo_panier_2)

        self.label_panier_ti_2 = QLabel(self.frame_head_panier)
        self.label_panier_ti_2.setObjectName(u"label_panier_ti_2")
        self.label_panier_ti_2.setMaximumSize(QSize(16777215, 60))
        font4 = QFont()
        font4.setPointSize(26)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_panier_ti_2.setFont(font4)
        self.label_panier_ti_2.setStyleSheet(u"color: rgba(33, 33, 33, 210);")
        self.label_panier_ti_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_panier_ti_2)


        self.verticalLayout_2.addWidget(self.frame_head_panier)

        self.frame = QFrame(self.panier_page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"\n"
"    QFrame#frame_panier {\n"
"        background-color: #f8f9fa; /* Couleur de fond */\n"
"        border-radius: 8px; /* Bords arrondis */\n"
"    }\n"
"    QLabel#label_panier_nb {\n"
"        color: #212529; /* Couleur du texte */\n"
"    }\n"
"    QFrame#frame_recap {\n"
"        background-color: #f8f9fa; /* Couleur de fond */\n"
"        border-radius: 8px; /* Bords arrondis */\n"
"    }\n"
"    QLabel#label_title_recap {\n"
"        color: #212529; /* Couleur du texte */\n"
"    }\n"
"    QFrame#recap_facure_frame {\n"
"        background-color: #f8f9fa; /* Couleur de fond */\n"
"        border-radius: 8px; /* Bords arrondis */\n"
"        border: 1px solid #dee2e6; /* Bordure */\n"
"    }\n"
"    QLabel#label_livraison_ti, QLabel#label_total_ti, QLabel#label_soustotal_ti {\n"
"        color: rgba(41, 41, 41, 200); /* Couleur du texte */\n"
"        padding-left: 12px; /* Espacement \u00e0 gauche */\n"
"        font-size: 17px; /* Taille de la police */\n"
"        font-weight: bold; /* Police"
                        " en gras */\n"
"    }\n"
"    QLabel#label_livraison, QLabel#label_total, QLabel#label_sous_total {\n"
"        font-family: \"Sora ExtraLight\"; /* Police personnalis\u00e9e */\n"
"        font-size: 16px; /* Taille de la police */\n"
"    }\n"
"\n"
"\n"
"    QPushButton#passer_commande_btn {\n"
"        background-color: #007bff; /* Couleur bleue */\n"
"        color: #FFFFFF; /* Couleur du texte */\n"
"        border-radius: 5px; /* Bords arrondis */\n"
"        padding: 5px 10px; /* Espacement interne du bouton */\n"
"        font-size: 14px; /* Taille de la police */\n"
"        font-weight: bold; /* Police en gras */\n"
"    }\n"
"    QPushButton#passer_commande_btn:hover {\n"
"        background-color: #0056b3; /* Couleur bleue fonc\u00e9e au survol */\n"
"    }\n"
"    QPushButton#passer_commande_btn:pressed {\n"
"        background-color: #003974; /* Couleur bleue fonc\u00e9e lorsque le bouton est enfonc\u00e9 */\n"
"    }\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_panier = QFrame(self.frame)
        self.frame_panier.setObjectName(u"frame_panier")
        self.frame_panier.setMinimumSize(QSize(0, 0))
        self.frame_panier.setMaximumSize(QSize(475, 16777215))
        self.frame_panier.setFrameShape(QFrame.StyledPanel)
        self.frame_panier.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_panier)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_panier_nb = QLabel(self.frame_panier)
        self.label_panier_nb.setObjectName(u"label_panier_nb")
        self.label_panier_nb.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setPointSize(19)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_panier_nb.setFont(font5)
        self.label_panier_nb.setStyleSheet(u"padding-left:30px;")

        self.verticalLayout_9.addWidget(self.label_panier_nb)

        self.frame_line_cont = QFrame(self.frame_panier)
        self.frame_line_cont.setObjectName(u"frame_line_cont")
        self.frame_line_cont.setMaximumSize(QSize(16777215, 10))
        self.frame_line_cont.setFrameShape(QFrame.NoFrame)
        self.frame_line_cont.setFrameShadow(QFrame.Raised)
        self.Layout_line = QVBoxLayout(self.frame_line_cont)
        self.Layout_line.setSpacing(0)
        self.Layout_line.setObjectName(u"Layout_line")
        self.Layout_line.setContentsMargins(15, 0, 15, 0)
        self.frame_line_2 = QFrame(self.frame_line_cont)
        self.frame_line_2.setObjectName(u"frame_line_2")
        self.frame_line_2.setMinimumSize(QSize(0, 10))
        self.frame_line_2.setMaximumSize(QSize(16777215, 10))
        self.frame_line_2.setFrameShape(QFrame.HLine)
        self.frame_line_2.setFrameShadow(QFrame.Raised)

        self.Layout_line.addWidget(self.frame_line_2)


        self.verticalLayout_9.addWidget(self.frame_line_cont)

        self.panier_scroll = QScrollArea(self.frame_panier)
        self.panier_scroll.setObjectName(u"panier_scroll")
        self.panier_scroll.setStyleSheet(u"border:none;\n"
"background: transparent;")
        self.panier_scroll.setWidgetResizable(True)
        self.area_panier_wid = QWidget()
        self.area_panier_wid.setObjectName(u"area_panier_wid")
        self.area_panier_wid.setGeometry(QRect(0, 0, 457, 256))
        self.panier_scroll.setWidget(self.area_panier_wid)

        self.verticalLayout_9.addWidget(self.panier_scroll)


        self.horizontalLayout_2.addWidget(self.frame_panier)

        self.frame_recap = QFrame(self.frame)
        self.frame_recap.setObjectName(u"frame_recap")
        self.frame_recap.setMinimumSize(QSize(0, 330))
        self.frame_recap.setMaximumSize(QSize(500, 340))
        self.frame_recap.setFrameShape(QFrame.StyledPanel)
        self.frame_recap.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_recap)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(11)
        self.gridLayout_6.setContentsMargins(15, 11, 15, 11)
        self.passer_commande_btn = QPushButton(self.frame_recap)
        self.passer_commande_btn.setObjectName(u"passer_commande_btn")
        self.passer_commande_btn.setMinimumSize(QSize(350, 40))
        self.passer_commande_btn.setMaximumSize(QSize(350, 16777215))
        self.passer_commande_btn.setFont(font)

        self.gridLayout_6.addWidget(self.passer_commande_btn, 3, 0, 1, 1, Qt.AlignHCenter)

        self.label_title_recap = QLabel(self.frame_recap)
        self.label_title_recap.setObjectName(u"label_title_recap")
        self.label_title_recap.setMinimumSize(QSize(0, 50))
        self.label_title_recap.setMaximumSize(QSize(16777215, 60))
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        self.label_title_recap.setFont(font6)
        self.label_title_recap.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_title_recap, 0, 0, 1, 1)

        self.recap_facure_frame = QFrame(self.frame_recap)
        self.recap_facure_frame.setObjectName(u"recap_facure_frame")
        self.recap_facure_frame.setMinimumSize(QSize(0, 110))
        self.recap_facure_frame.setMaximumSize(QSize(16777215, 300))
        self.gridLayout_5 = QGridLayout(self.recap_facure_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_livraison_ti = QLabel(self.recap_facure_frame)
        self.label_livraison_ti.setObjectName(u"label_livraison_ti")
        self.label_livraison_ti.setFont(font)
        self.label_livraison_ti.setStyleSheet(u"color: rgba(41, 41, 41, 200);padding-left:12px;")

        self.gridLayout_5.addWidget(self.label_livraison_ti, 2, 0, 1, 1)

        self.label_total_ti = QLabel(self.recap_facure_frame)
        self.label_total_ti.setObjectName(u"label_total_ti")
        self.label_total_ti.setFont(font)
        self.label_total_ti.setStyleSheet(u"color: rgba(41, 41, 41, 200);padding-left:12px;")

        self.gridLayout_5.addWidget(self.label_total_ti, 4, 0, 1, 1)

        self.label_livraison = QLabel(self.recap_facure_frame)
        self.label_livraison.setObjectName(u"label_livraison")
        font7 = QFont()
        font7.setFamilies([u"Sora ExtraLight"])
        self.label_livraison.setFont(font7)

        self.gridLayout_5.addWidget(self.label_livraison, 2, 1, 1, 1)

        self.label_total = QLabel(self.recap_facure_frame)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setFont(font7)

        self.gridLayout_5.addWidget(self.label_total, 4, 1, 1, 1)

        self.label_sous_total = QLabel(self.recap_facure_frame)
        self.label_sous_total.setObjectName(u"label_sous_total")
        self.label_sous_total.setFont(font7)

        self.gridLayout_5.addWidget(self.label_sous_total, 1, 1, 1, 1)

        self.label_soustotal_ti = QLabel(self.recap_facure_frame)
        self.label_soustotal_ti.setObjectName(u"label_soustotal_ti")
        self.label_soustotal_ti.setFont(font)
        self.label_soustotal_ti.setStyleSheet(u"color: rgba(41, 41, 41, 200);padding-left:12px;")

        self.gridLayout_5.addWidget(self.label_soustotal_ti, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.recap_facure_frame, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_recap)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(self.panier_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(264, 104))
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_info = QLabel(self.frame_3)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setMaximumSize(QSize(392, 26))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI Semibold"])
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setItalic(False)
        self.label_info.setFont(font8)

        self.verticalLayout_10.addWidget(self.label_info)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(262, 70))
        self.frame_10.setMaximumSize(QSize(262, 70))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.paye_wave = QPushButton(self.frame_10)
        self.paye_wave.setObjectName(u"paye_wave")
        self.paye_wave.setMinimumSize(QSize(80, 30))
        self.paye_wave.setMaximumSize(QSize(80, 40))
        icon = QIcon()
        icon.addFile(u":/icon/Resources/image/wave-senegal-mobile-money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paye_wave.setIcon(icon)
        self.paye_wave.setIconSize(QSize(80, 60))

        self.horizontalLayout_11.addWidget(self.paye_wave)

        self.paye_orange_money = QPushButton(self.frame_10)
        self.paye_orange_money.setObjectName(u"paye_orange_money")
        self.paye_orange_money.setMinimumSize(QSize(50, 50))
        self.paye_orange_money.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icon/Resources/image/OM_Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paye_orange_money.setIcon(icon1)
        self.paye_orange_money.setIconSize(QSize(50, 50))

        self.horizontalLayout_11.addWidget(self.paye_orange_money)

        self.paye_visa = QPushButton(self.frame_10)
        self.paye_visa.setObjectName(u"paye_visa")
        self.paye_visa.setMinimumSize(QSize(100, 30))
        self.paye_visa.setMaximumSize(QSize(120, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icon/Resources/image/Visa_Inc._logo.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paye_visa.setIcon(icon2)
        self.paye_visa.setIconSize(QSize(50, 50))

        self.horizontalLayout_11.addWidget(self.paye_visa)


        self.verticalLayout_10.addWidget(self.frame_10)


        self.verticalLayout_2.addWidget(self.frame_3)

        StackedWidget.addWidget(self.panier_page)
        self.space_client_page = QWidget()
        self.space_client_page.setObjectName(u"space_client_page")
        StackedWidget.addWidget(self.space_client_page)
        self.space_admin_page = QWidget()
        self.space_admin_page.setObjectName(u"space_admin_page")
        self.space_admin_page.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.space_admin_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_lay_sa = QFrame(self.space_admin_page)
        self.frame_lay_sa.setObjectName(u"frame_lay_sa")
        self.frame_lay_sa.setStyleSheet(u"#frame_lay_sa{\n"
"	\n"
"	background-color: rgba(177, 173, 170, 35);\n"
"}\n"
"#space_admin_page {\n"
"	background-color: rgb(255, 255, 255);\n"
"    background-color: #f0f0f0;\n"
"    padding: 50px;\n"
"}\n"
"\n"
"#label_title {\n"
"    font-size: 34px;\n"
"    text-align: center;\n"
"    margin-bottom: 20px;\n"
"}\n"
"\n"
"#come_back_home {\n"
"    background-color: transparent;\n"
"    border: 2px solid #f18b0e;\n"
"    color: #f18b0e;\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    margin-top: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.2s, color 0.2s;\n"
"}\n"
"\n"
"#come_back_home:hover {\n"
"    background-color: #f18b0e;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#widget {\n"
"    background-color: #fff;\n"
"    border-radius: 10px;\n"
"    padding: 20px;\n"
"    margin-top: 50px;\n"
"}\n"
"\n"
"#gest_prod_btn, #gest_client_btn, #gest_compt_admin_btn {\n"
"    background-color: transparent;\n"
"    border: 2px solid #f18b0e;\n"
"    color: #f18b0e;\n"
"    font-size: 1"
                        "6px;\n"
"    padding: 10px 20px;\n"
"    border-radius: 8px;\n"
"    margin-top: 20px;\n"
"    text-align: center;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.2s, color 0.2s;\n"
"}\n"
"\n"
"#gest_prod_btn:hover, #gest_client_btn:hover, #gest_compt_admin_btn:hover {\n"
"    background-color: #f18b0e;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#gest_prod_btn:pressed, #gest_client_btn:pressed, #gest_compt_admin_btn:pressed ,#come_back_home:pressed{\n"
"    background-color: #d06e0c;\n"
"    border-color: #d06e0c;\n"
"}\n"
"")
        self.frame_lay_sa.setFrameShape(QFrame.StyledPanel)
        self.frame_lay_sa.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_lay_sa)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(150, -1, 0, 110)
        self.frame_sa = QFrame(self.frame_lay_sa)
        self.frame_sa.setObjectName(u"frame_sa")
        self.frame_sa.setStyleSheet(u"")
        self.layout_contain = QVBoxLayout(self.frame_sa)
        self.layout_contain.setObjectName(u"layout_contain")
        self.label_title = QLabel(self.frame_sa)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 80))
        font9 = QFont()
        self.label_title.setFont(font9)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.layout_contain.addWidget(self.label_title, 0, Qt.AlignTop)

        self.sub_frame_sa = QFrame(self.frame_sa)
        self.sub_frame_sa.setObjectName(u"sub_frame_sa")
        self.space_ad_layout = QVBoxLayout(self.sub_frame_sa)
        self.space_ad_layout.setObjectName(u"space_ad_layout")
        self.gest_prod_btn = QPushButton(self.sub_frame_sa)
        self.gest_prod_btn.setObjectName(u"gest_prod_btn")
        self.gest_prod_btn.setMinimumSize(QSize(0, 60))

        self.space_ad_layout.addWidget(self.gest_prod_btn)

        self.gest_client_btn = QPushButton(self.sub_frame_sa)
        self.gest_client_btn.setObjectName(u"gest_client_btn")
        self.gest_client_btn.setMinimumSize(QSize(0, 60))

        self.space_ad_layout.addWidget(self.gest_client_btn)

        self.gest_compt_admin_btn = QPushButton(self.sub_frame_sa)
        self.gest_compt_admin_btn.setObjectName(u"gest_compt_admin_btn")
        self.gest_compt_admin_btn.setMinimumSize(QSize(0, 60))

        self.space_ad_layout.addWidget(self.gest_compt_admin_btn)


        self.layout_contain.addWidget(self.sub_frame_sa)


        self.horizontalLayout.addWidget(self.frame_sa)

        self.frame_2 = QFrame(self.frame_lay_sa)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(150, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.come_back_home = QPushButton(self.frame_2)
        self.come_back_home.setObjectName(u"come_back_home")
        self.come_back_home.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.come_back_home)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_lay_sa)

        StackedWidget.addWidget(self.space_admin_page)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label_title_gestprod.setText(QCoreApplication.translate("StackedWidget", u"Gestion des Produits", None))
        self.label_nom_prod.setText(QCoreApplication.translate("StackedWidget", u"Nom du Produits :", None))
        self.label_catergeorie.setText(QCoreApplication.translate("StackedWidget", u"Categorie :", None))
        self.label_prix.setText(QCoreApplication.translate("StackedWidget", u"Prix :", None))
        self.bouton_ajouter.setText(QCoreApplication.translate("StackedWidget", u"Ajouter", None))
        self.label_descr.setText(QCoreApplication.translate("StackedWidget", u"Description :", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("StackedWidget", u"<b>Photo<b/>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton.setText(QCoreApplication.translate("StackedWidget", u"...", None))
        self.bouton_modifier.setText(QCoreApplication.translate("StackedWidget", u"Modifier", None))
        self.option_stockage.setTitle("")
#if QT_CONFIG(tooltip)
        self.ajouter_produit_btn.setToolTip(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-weight:700;\">Ajouter au Stock</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ajouter_produit_btn.setText(QCoreApplication.translate("StackedWidget", u"Ajouter", None))
#if QT_CONFIG(tooltip)
        self.retirer_produit_btn.setToolTip(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-weight:700;\">Retrancher du Stock</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.retirer_produit_btn.setText(QCoreApplication.translate("StackedWidget", u"Retirer", None))
        self.liste_prod_combo_box.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"liste des produits", None))
#if QT_CONFIG(tooltip)
        self.quantite_spin_box.setToolTip(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-weight:700;\">Quantit\u00e9</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.supprimer_produit_btn.setToolTip(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Supprimer d\u00e9finitivement le produit</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.supprimer_produit_btn.setText(QCoreApplication.translate("StackedWidget", u"Supprimer le produit", None))
        self.label_9.setText(QCoreApplication.translate("StackedWidget", u"STOCKAGE", None))
        ___qtablewidgetitem = self.stock_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StackedWidget", u"produits", None));
        ___qtablewidgetitem1 = self.stock_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StackedWidget", u"Stock", None));
        self.label_title_list_clients.setText(QCoreApplication.translate("StackedWidget", u"Liste des clients", None))
        self.label_10.setText(QCoreApplication.translate("StackedWidget", u"Nom", None))
        self.label_11.setText(QCoreApplication.translate("StackedWidget", u"Email", None))
        self.label_12.setText(QCoreApplication.translate("StackedWidget", u"Numero de telephone", None))
        self.label_13.setText(QCoreApplication.translate("StackedWidget", u"Action", None))
        self.label_logo_panier_2.setText("")
        self.label_panier_ti_2.setText(QCoreApplication.translate("StackedWidget", u"Panier", None))
        self.label_panier_nb.setText(QCoreApplication.translate("StackedWidget", u"Panier (0)", None))
        self.passer_commande_btn.setText(QCoreApplication.translate("StackedWidget", u"Passez la commande", None))
        self.label_title_recap.setText(QCoreApplication.translate("StackedWidget", u"R\u00e9capitulatif de la commande", None))
        self.label_livraison_ti.setText(QCoreApplication.translate("StackedWidget", u"Livraison :", None))
        self.label_total_ti.setText(QCoreApplication.translate("StackedWidget", u"Total \u00e0 payer :", None))
        self.label_livraison.setText(QCoreApplication.translate("StackedWidget", u"5f", None))
        self.label_total.setText(QCoreApplication.translate("StackedWidget", u"0f", None))
        self.label_sous_total.setText(QCoreApplication.translate("StackedWidget", u"0 f", None))
        self.label_soustotal_ti.setText(QCoreApplication.translate("StackedWidget", u"Sous-Total", None))
        self.label_info.setText(QCoreApplication.translate("StackedWidget", u"Nous acceptons", None))
        self.paye_wave.setText("")
        self.paye_orange_money.setText("")
        self.paye_visa.setText("")
        self.label_title.setText(QCoreApplication.translate("StackedWidget", u"Espace Administrateur", None))
        self.gest_prod_btn.setText(QCoreApplication.translate("StackedWidget", u"Gestion des Produits", None))
        self.gest_client_btn.setText(QCoreApplication.translate("StackedWidget", u"Gestion des Client", None))
        self.gest_compt_admin_btn.setText(QCoreApplication.translate("StackedWidget", u"Gesstion du compte Admin", None))
        self.come_back_home.setText(QCoreApplication.translate("StackedWidget", u"Retour \u00e0 l'accueil", None))
    # retranslateUi

