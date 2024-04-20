from PySide6 import QtCore

from Gui.widget import table_info
from qt_core import *

styles = """
                QMessageBox {
                    background-color: #f8f8f8;
                    border: 2px solid #c3c3c3;
                    border-radius: 5px;
                    font-size: 14px;
                    padding: 10px;
                }

                QMessageBox QLabel {
                    color: #000000;
                    font-weight: bold;
                }

                QMessageBox QPushButton {
                    background-color: #f0f0f0;
                    border: 2px solid #c3c3c3;
                    border-radius: 5px;
                    font-size: 12px;
                    padding: 5px;
                    min-width: 80px;
                }

                QMessageBox QPushButton:hover {
                    background-color: #d0d0d0;
                }
            """


def setup_user_info_layout(self):
    # Création du layout pour les informations des utilisateurs
    layout_utilisateurs = QVBoxLayout()
    layout_utilisateurs.setContentsMargins(7, 0, 7, 0)

    # Récupération des clients dans la base de données en utilisant la classe de gestion de la BDD
    query = "SELECT * FROM clients"
    list_clients = self.gestionnaire_db.executer_requete_fetchall(query)

    # Ajout des utilisateurs
    for client in list_clients:
        utilisateur = table_info(nom=client[1], email=client[2], numero=client[4])
        layout_utilisateurs.addWidget(utilisateur)

        # Récupération des boutons "Modifier" et "Supprimer" de chaque utilisateur
        bouton_supprimer = utilisateur.get_bouton_supprimer()

        # Connexion des signaux des boutons aux slots correspondants
        bouton_supprimer.clicked.connect(on_supprimer_clicked)

    # Ajout du layout des utilisateurs à la zone de défilement
    self.pages.scroll_area_content.setLayout(layout_utilisateurs)


def display_tab(self):
    # Récupération des produits dans la base de données en utilisant la classe de gestion de la BDD
    query = "SELECT * FROM produits"
    list_produits = self.gestionnaire_db.executer_requete_fetchall(query)
    print(list_produits)

    result = [(produit[1], produit[3]) for produit in list_produits]  # Création de la liste des tuples (nom, qte)

    self.pages.stock_tab.setRowCount(0)

    for row_number, row_data in enumerate(result):
        self.pages.stock_tab.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            item = QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)  # Centrer le texte
            self.pages.stock_tab.setItem(row_number, column_number, item)


def display_prod(self):
    # Récupération des produits dans la base de données en utilisant la classe de gestion de la BDD
    query = "SELECT * FROM produits"
    list_produits = self.gestionnaire_db.executer_requete_fetchall(query)

    result1 = [produit[1] for produit in list_produits]  # Création de la liste des noms de produits

    # Nettoyer et mettre à jour la combobox avec les noms des produits
    self.pages.liste_prod_combo_box.clear()
    self.pages.liste_prod_combo_box.addItems(result1)


def ajouter_Produit(self):
    nom_prod = self.pages.nom_prod_le.text()
    categorie_prod = self.pages.categorie_prod_le.text()
    prix_prod = self.pages.prix_prod_le.text()
    des = self.pages.textEdit.toPlainText()

    # Utilisation de votre classe de gestion de la base de données pour exécuter la requête
    insert_query = "INSERT INTO produits (libelle, prixvente,categorie, description) VALUES (%s, %s, %s, %s);"
    valeurs = (nom_prod, prix_prod, categorie_prod, des)
    if self.gestionnaire_db.executer_requete(insert_query, valeurs):
        print("Produit ajouté avec succès.")
        message_info("Info", "Produit ajouté avec succès.")


def supprimer_Produit(self):
    nom_prod = self.pages.liste_prod_combo_box.currentText()
    delete_query = "DELETE FROM produits WHERE libelle=%s;"
    if self.gestionnaire_db.executer_requete(delete_query, (nom_prod,)):
        print("Produit supprimé avec succès.")
        message_info("Info", "Produit supprimé avec succès.")


def on_supprimer_clicked(self):
    try:
        # Récupère l'objet bouton qui a émis le signal
        sender_button = self.sender()
        client_id_to_delete = int(sender_button.objectName())  # Convertir en entier si nécessaire

        # Utilisation de la classe de gestion de la BDD pour exécuter la requête de suppression
        delete_query = "DELETE FROM clients WHERE noclient = %s;"
        if self.gestionnaire_db.executer_requete(delete_query, (client_id_to_delete,)):
            print("Client avec ID {} supprimé avec succès.".format(client_id_to_delete))
            message_info("Succès", f"Client avec ID {client_id_to_delete} supprimé avec succès.")
        else:
            message_error("Error", "Erreur lors de la suppression du client.")
            print("Erreur lors de la suppression du client.")

    except Exception as e:
        message_error("Erreur", f"Erreur lors de la suppression: {e}")
        print("Erreur lors de la suppression:", e)

    print("Bouton Supprimer cliqué !")


def message_info(title: str, message: str):
    success_self = QMessageBox()
    success_self.setIcon(QMessageBox.Information)
    success_self.setText(message)
    success_self.setWindowTitle(title)
    success_self.setStandardButtons(QMessageBox.Ok)
    success_self.setStyleSheet(styles)
    # success_self.setWindowIcon(QIcon("images/image/btp.ico"))
    success_self.exec()


def message_error(title: str, self: str):
    message = QMessageBox()
    message.setIcon(QMessageBox.Warning)
    message.setText(self)
    message.setWindowTitle(title)
    # message.setWindowIcon(QIcon("images/image/btp.ico"))
    message.setStyleSheet(styles)
    message.exec()


def show_confirmation_dialog(title: str, message: str):
    # Créer une instance de la boîte de message
    selfBox = QMessageBox()

    # Configurer le titre de la boîte de message
    selfBox.setWindowTitle(title)

    # Configurer le texte du message
    selfBox.setText(message)
    icone = QIcon("images/image/btp.ico")
    selfBox.setWindowIcon(icone)

    # Configurer les boutons de la boîte de message
    selfBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    selfBox.button(QMessageBox.Yes).setText("Oui")
    selfBox.button(QMessageBox.No).setText("Non")
    # Utiliser une feuille de style pour personnaliser l'apparence de la boîte de message
    selfBox.setStyleSheet("""QMessageBox {
                            background-color: #f5f5f5;
                            border: 2px solid #ddd;
                            font-size: 16px;
                            color: #333;
                        }
                        
                        QMessageBox QPushButton {
                            background-color: #0074D9;
                            color: #fff;
                            border-radius: 4px;
                            padding: 8px 16px;
                            min-width: 80px;
                        }
                        
                        QMessageBox QPushButton:hover {
                            background-color: #005cb2;
                        }
                        """)

    return selfBox.exec()


def toggleMenu(self, maxWidth):
    # GET WIDTH
    width = self.ui.frame_left_menu.width()
    max_extend = maxWidth
    standard = 0
    if width == 0:
        width_extended = max_extend
        # self.ui.toogleSildeBtn.setIcon(QIcon("images/icon_svg/arrow_back_ios_FILL0_wght400_GRAD0_opsz48.svg"))
    else:
        width_extended = standard
        # self.ui.toogleSildeBtn.setIcon(QIcon("images/icon_svg/menu_FILL0_wght400_GRAD0_opsz40.svg"))
    # ANIMATION
    self.animation = QPropertyAnimation(
        self.ui.frame_left_menu, b"minimumWidth")
    self.animation.setDuration(400)
    self.animation.setStartValue(width)
    self.animation.setEndValue(width_extended)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()


def close_page(self):
    # GET WIDTH
    width = self.ui.self.ui.frame_left_menu.width()
    max_extend = self.ui.self.ui.frame_left_menu.maximumWidth()
    standard = 0
    # SET MAX WIDTH
    width_extended = standard if width == max_extend else max_extend
    # ANIMATION
    self.animation = QPropertyAnimation(self.ui.self.ui.frame_left_menu, b"minimumWidth")
    self.animation.setDuration(500)
    self.animation.setStartValue(width)
    self.animation.setEndValue(width_extended)
    self.animation.setEasingCurve(QEasingCurve.InOutQuart)
    self.animation.start()


def setup_ui(self):
    self.pages.gest_prod_btn.clicked.connect(
        lambda: self.ui.page.setCurrentWidget(self.pages.gest_prod_page))
    self.pages.gest_client_btn.clicked.connect(
        lambda: self.ui.page.setCurrentWidget(self.pages.gest_client_btn))
    self.ui.panier_btn.clicked.connect(lambda: self.ui.page.setCurrentWidget(self.pages.panier_page))
    self.ui.accueil_btn.clicked.connect(lambda: self.ui.page.setCurrentWidget(self.pages.home_page))
    self.ui.space_admin_btn.clicked.connect(lambda: self.ui.page.setCurrentWidget(self.pages.space_admin_page))
    self.pages.gest_client_btn.clicked.connect(lambda: self.ui.page.setCurrentWidget(self.pages.gest_client_page))
    self.pages.stock_tab.horizontalHeader().resizeSection(0, 400)
    self.pages.stock_tab.horizontalHeader().resizeSection(1, 180)


def modif_info_user(self):
    nom = self.pages.modif_nom_le.text()
    prenom = self.pages.modif_prenom_le.text()
    adresse = self.pages.modif_adress_le.text()
    contact = self.pages.modif_contact_le.text()
    # Supposons que vous ayez un objet gestionnaire_db de la classe ManageData
    nom_client = self.pages.label_nom.text()
    prenom_client = self.pages.label_prenom.text()

    requete_id_client = "SELECT id_client FROM clients WHERE nom = %s AND prenom = %s"
    valeurs = (nom_client, prenom_client)

    resultat = self.gestionnaire_db.executer_requete_fetchone(requete_id_client, valeurs)

    if resultat:
        id_client = resultat[0]
        print("L'ID du client {} {} est : {}".format(nom_client, prenom_client, id_client))
        query = "UPDATE clients SET nom = %s, prenom = %s, adresse = %s, contact = %s WHERE id_client = %s;"
        valeur = (nom, prenom, adresse, contact, id_client)

        self.gestionnaire_db.executer_requete(query, valeur)
        message_info("Information", "Information modifier avec succès")
    else:
        print("Aucun client trouvé avec le nom {} {}.".format(nom_client, prenom_client))


def display_info_user(self):
    # Supposons que vous ayez un objet gestionnaire_db de la classe ManageData
    nom_client = "Nom du client"
    prenom_client = "Prénom du client"

    requete_info_client = "SELECT * FROM clients WHERE nom = %s AND prenom = %s"
    valeurs = (nom_client, prenom_client)

    resultat = self.gestionnaire_db.executer_requete_fetchone(requete_info_client, valeurs)

    if resultat:
        id_client = resultat[0]
        nom = resultat[1]
        prenom = resultat[2]
        email = resultat[3]
        numero = resultat[4]

        self.pages.label_nom.setText(nom)
        self.pages.label_prenom.setText(prenom)
        self.pages.label_adress.setText(email)
        self.pages.label_contact.setText(numero)
    else:
        print("Aucun client trouvé avec le nom {} {}.".format(nom_client, prenom_client))
