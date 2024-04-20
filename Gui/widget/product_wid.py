from qt_core import *
# from resources_rc import *


class ProductWidget(QWidget):
    def __init__(self, nom="Grain de mais", des="ce sont des graines qui changent", prix="155$"):
        super().__init__()
        self.setFixedSize(600, 200)

        # Style du widget lui-même
        self.setStyleSheet('''
            ProductWidget {
                background-color: #f8f9fa;
                border: 1px solid #ced4da;
                border-radius: 5px;
                padding: 10px;
            }
        ''')

        # Style des boutons
        button_style = '''
            QPushButton {
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        '''

        # Style du SpinBox
        spinbox_style = '''
            QSpinBox {
                border: 1px solid #ced4da;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                subcontrol-origin: border;
                subcontrol-position: top right;
                width: 0px;
            }
        '''

        self.bouton_add = QPushButton()
        icon_add = QIcon(
            "../image/add_FILL0_wght400_GRAD0_opsz40.svg")  # Remplacez "chemin/vers/icon_add.png" par le chemin de votre icône d'ajout
        self.bouton_add.setIcon(icon_add)
        self.bouton_add.setIconSize(QSize(25, 25))

        self.bouton_add.setFixedSize(35, 35)
        self.bouton_add.setStyleSheet(button_style)

        self.bouton_rem = QPushButton()
        icon_rem = QIcon(
            ":/img/image/remove_FILL0_wght400_GRAD0_opsz48.svg")  # Remplacez "chemin/vers/icon_rem.png" par le chemin de votre icône de suppression
        self.bouton_rem.setIcon(icon_rem)
        self.bouton_rem.setIconSize(QSize(25, 25))
        self.bouton_rem.setFixedSize(35, 35)
        self.bouton_rem.setStyleSheet(button_style)

        self.bouton_delete = QPushButton()
        icon_delete = QIcon(
            "../image/delete_FILL0_wght400_GRAD0_opsz40.svg")  # Remplacez "chemin/vers/icon_delete.png" par le chemin de votre icône de suppression de produit
        self.bouton_delete.setIcon(icon_delete)
        self.bouton_delete.setIconSize(QSize(40, 40))
        self.bouton_delete.setFixedSize(40, 40)
        self.bouton_delete.setStyleSheet('''
            QPushButton {
                border: none;
                background-color:#ccc;
            }
        ''')

        self.bouton_im_prod = QPushButton()
        icon_prod = QIcon(
            "chemin/vers/icon_prod.png")  # Remplacez "chemin/vers/icon_prod.png" par le chemin de votre icône d'image de produit
        self.bouton_im_prod.setIcon(icon_prod)
        self.bouton_im_prod.setFixedSize(101, 101)

        self.quantite = QSpinBox()
        self.quantite.setFixedSize(50, 35)
        self.quantite.setStyleSheet(spinbox_style)

        self.label_prix = QLabel(prix)
        self.label_prix.setStyleSheet('''
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
        ''')

        self.label_desc = QLabel(des)
        self.label_desc.setStyleSheet('''
            QLabel {
                font-size: 14px;
            }
        ''')

        self.label_name = QLabel(nom)
        self.label_name.setStyleSheet('''
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
        ''')

        layout = QVBoxLayout()
        layout_add = QHBoxLayout()
        layout_quantite = QHBoxLayout()
        layout_quantite.addWidget(self.bouton_rem)
        layout_quantite.addWidget(self.quantite)
        layout_quantite.addWidget(self.bouton_add)

        layout_label = QVBoxLayout()
        layout_label.addWidget(self.label_name)
        layout_label.addWidget(self.label_desc)
        layout_label.addWidget(self.label_prix)

        frame_info_prod = QFrame()
        frame_info_prod.setLayout(layout_label)

        bottom_frame = QFrame()
        bottom_frame.setLayout(layout_quantite)

        nex_frame = QFrame()

        layout_add.addWidget(self.bouton_im_prod)
        layout_add.addWidget(frame_info_prod)
        layout_add.addWidget(self.bouton_delete, alignment=Qt.AlignTop | Qt.AlignRight)
        nex_frame.setLayout(layout_add)

        layout.addWidget(nex_frame)
        layout.addWidget(bottom_frame, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.bouton_add.clicked.connect(lambda: self.move_quantite(1))
        self.bouton_rem.clicked.connect(lambda: self.move_quantite(-1))

    def move_quantite(self, step):
        qte = self.quantite.value()
        qte += step
        # Vérifier que la quantité ne devient pas négative ou nulle
        qte = max(0, qte)
        self.quantite.setValue(qte)


if __name__ == "__main__":
    app = QApplication([])
    win = ProductWidget()
    win.show()
    app.exec()
