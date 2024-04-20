from qt_core import *
# from resources_rc import *


class FrameProduit(QFrame):
    def __init__(self, product):
        super().__init__()

        self.setFixedSize(250, 300)  # Définir la taille de la frame à 250*300 pixels

        layout_frame = QVBoxLayout()
        layout_frame.setContentsMargins(10, 10, 10, 10)  # Ajouter des marges au layout

        self.button_image = QPushButton()
        self.button_image.setFixedSize(150, 150)
        self.button_image.setIconSize(self.button_image.size())  # Redimensionner l'icône pour remplir le bouton
        self.button_image.setIcon(QIcon(product['image']))  # Définir l'icône du bouton à partir de l'image

        self.label_nom = QLabel(product['name'])
        self.label_des = QLabel(product['description'])
        self.label_prix = QLabel(f"Prix : {product['price']}€")
        self.bouton_ajouter = QPushButton("Ajouter au panier")
        self.bouton_ajouter.setMinimumHeight(40)

        # Appliquer le style inspiré de Bootstrap aux widgets
        self.button_image.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; background-color: #fff;")
        self.label_nom.setStyleSheet("font-weight: bold; font-size: 16px; margin-top: 10px;")
        self.label_des.setStyleSheet("color: #777; font-size: 14px;")
        self.label_prix.setStyleSheet("color: #337ab7; font-size: 16px; margin-top: 5px;")
        self.bouton_ajouter.setStyleSheet(
            "background-color: #337ab7; color: #fff; font-size: 14px; border: none; border-radius: 5px; padding: 5px 10px;")

        # Ajouter les widgets au layout vertical
        layout_frame.addWidget(self.button_image, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_frame.addWidget(self.label_nom)
        layout_frame.addWidget(self.label_des)
        layout_frame.addWidget(self.label_prix)
        layout_frame.addWidget(self.bouton_ajouter)

        # Définir le layout vertical comme layout principal du QFrame
        self.setLayout(layout_frame)
        self.setObjectName("products")
        self.setStyleSheet("""
        /* Style de la frame produit */
#products {
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 5px;

}

/* Style du bouton d'image */
QPushButton#button_image {
    border: none;
    background-color: transparent;
    padding: 0;
}
        """)


if __name__ == "__main__":
    # Exemple d'utilisation de la classe FrameProduit
    app = QApplication([])

    # Créer une fenêtre principale pour afficher les produits
    fenetre = QWidget()
    fenetre.setWindowTitle("Liste des Produits")
    fenetre_layout = QHBoxLayout()

    # Exemple de données de deux produits sous forme de dictionnaire
    produit1 = {
        'name': 'Graines de Nigel',
        'description': 'Description du produit 1',
        'price': '20',
        'image': ':img/image/038acda7c1016b01ef5ce7969df37853-removebg-preview.png'  # Remplacez par le chemin de votre image
    }

    produit2 = {
        'name': 'Pulpe d\'aloès',
        'description': 'Description du produit 2',
        'price': '15',
        'image': 'chemin/vers/votre/image2.jpg'  # Remplacez par le chemin de votre image
    }

    # Créer deux instances de FrameProduit en leur passant les données des produits
    frame_produit1 = FrameProduit(produit1)
    frame_produit2 = FrameProduit(produit2)

    # Ajouter les frames produits au layout horizontal
    fenetre_layout.addWidget(frame_produit1)
    fenetre_layout.addWidget(frame_produit2)

    # Définir le layout horizontal comme layout principal de la fenêtre
    fenetre.setLayout(fenetre_layout)

    fenetre.show()
    app.exec()
