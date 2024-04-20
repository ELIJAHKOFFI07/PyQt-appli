from qt_core import *


class table_info(QFrame):
    def __init__(self, nom="John Doe", email="JohnDoe@gmail.com", numero="+0052555556",
                 ):
        super().__init__()

        # Création des widgets
        self.label_layout = QHBoxLayout()
        self.bouton_layout = QHBoxLayout()

        self.label_2 = QLabel(nom)
        self.label_3 = QLabel(email)
        self.label_4 = QLabel(numero)

        # self.bouton_info = QPushButton("Information")
        self.bouton_modifier = QPushButton("Modifier")
        self.bouton_supprimer = QPushButton("Supprimer")

        # Ajout des widgets aux layouts
        # self.label_layout.addWidget(self.label_1)
        self.label_layout.addWidget(self.label_2)
        self.label_layout.addWidget(self.label_3)
        self.label_layout.addWidget(self.label_4)

        # self.bouton_info.setFixedSize(QSize(160, 35))
        self.bouton_supprimer.setFixedSize(QSize(160, 35))
        self.bouton_modifier.setFixedSize(QSize(160, 35))

        # le nom des objets
        self.bouton_modifier.setObjectName("Modifier-Information")
        self.bouton_supprimer.setObjectName("Supprimer-Information")

        # self.bouton_layout.addWidget(self.bouton_info)
        self.bouton_layout.addWidget(self.bouton_modifier)
        self.bouton_layout.addWidget(self.bouton_supprimer)

        # Ajout des layouts au layout principal de la frame
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.label_layout)
        self.layout.addLayout(self.bouton_layout)

        # Configuration du layout de la frame
        self.setLayout(self.layout)

        # Appliquer les styles aux labels
        # self.label_1.setStyleSheet("""
        #     QLabel {
        #         color: #212529; /* Couleur du texte */
        #         font-size: 20px; /* Taille de la police */
        #         font-weight: bold; /* Police en gras */
        #         margin-right: 10px; /* Marge à droite pour espacer les labels */
        #     }
        # """)
        self.setStyleSheet("""
            QLabel {
                color: #212529; /* Couleur du texte */
                font-size: 18px; /* Taille de la police */
                margin-right: 10px; /* Marge à droite pour espacer les labels */
            }
            #info_frame{
            border:1px solid #dee2e6;
            border-radius:8px;
            }
        """
                           )
        self.setObjectName("info_frame")

        # Appliquer les styles aux boutons
        self.bouton_supprimer.setStyleSheet("""
            QPushButton {
                background-color: #dc3545; /* Couleur rouge */
                border: 1px solid #dc3545; /* Bordure rouge */
                color: #FFFFFF; /* Couleur du texte par défaut */
                border-radius: 5px; /* Bords arrondis */
                padding: 5px 10px; /* Espacement interne du bouton */
                font-size: 16px; /* Taille de la police */
                font-weight: bold; /* Police en gras */
            }
            QPushButton:hover {
                background-color: #c82333; /* Couleur rouge foncée */
                border: 1px solid #c82333; /* Bordure rouge foncée */
            }
            QPushButton:pressed {
                background-color: #b21f2d; /* Couleur rouge foncée lorsque le bouton est enfoncé */
                border: 1px solid #b21f2d; /* Bordure rouge foncée lorsque le bouton est enfoncé */
            }
        """)

        self.bouton_modifier.setStyleSheet("""
            QPushButton {
                background-color: #ffc107; /* Couleur jaune */
                border: 1px solid #ffc107; /* Bordure jaune */
                color: #FFFFFF; /* Couleur du texte par défaut */
                border-radius: 5px; /* Bords arrondis */
                padding: 5px 10px; /* Espacement interne du bouton */
                font-size: 16px; /* Taille de la police */
                font-weight: bold; /* Police en gras */
            }
            QPushButton:hover {
                background-color: #e0a800; /* Couleur jaune foncée */
                border: 1px solid #e0a800; /* Bordure jaune foncée */
            }
            QPushButton:pressed {
                background-color: #b58905; /* Couleur jaune foncée lorsque le bouton est enfoncé */
                border: 1px solid #b58905; /* Bordure jaune foncée lorsque le bouton est enfoncé */
            }
        """)

        # self.bouton_info.setStyleSheet("""
        #     QPushButton {
        #         background-color: #17a2b8; /* Couleur bleue */
        #         border: 1px solid #17a2b8; /* Bordure bleue */
        #         color: #FFFFFF; /* Couleur du texte par défaut */
        #         border-radius: 5px; /* Bords arrondis */
        #         padding: 5px 10px; /* Espacement interne du bouton */
        #         font-size: 16px; /* Taille de la police */
        #         font-weight: bold; /* Police en gras */
        #     }
        #     QPushButton:hover {
        #         background-color: #138496; /* Couleur bleue foncée */
        #         border: 1px solid #138496; /* Bordure bleue foncée */
        #     }
        #     QPushButton:pressed {
        #         background-color: #0c6b7c; /* Couleur bleue foncée lorsque le bouton est enfoncé */
        #         border: 1px solid #0c6b7c; /* Bordure bleue foncée lorsque le bouton est enfoncé */
        #     }
        # """)

    def get_bouton_modifier(self):
        return self.bouton_modifier

    def get_bouton_supprimer(self):
        return self.bouton_supprimer


if __name__ == "__main__":
    app = QApplication([])

    # Création d'une instance de la classe table_info et affichage de la fenêtre
    window = table_info()
    window.show()

    app.exec()
