from PySide6.QtWebEngineWidgets import QWebEngineView

from qt_core import *


class FactureWidget(QMainWindow):
    def __init__(self, numero_facture, date_facture, mode_paiement, produits, sous_total, taxes, total, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Facture")
        self.setGeometry(100, 100, 800, 600)

        # Générer le contenu HTML de la facture
        content = self.generate_html_content(numero_facture, date_facture, mode_paiement, produits, sous_total, taxes,
                                             total)

        # Afficher le contenu HTML dans le WebView
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)
        self.web_view.setHtml(content)

    def generate_html_content(self, numero_facture, date_facture, mode_paiement, produits, sous_total, taxes, total):
        # Générer le contenu HTML avec les données de la facture
        content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Facture</title>
            <style>
                /* Styles pour rendre la facture responsive */
        body {{
            font-family: "Montserrat", sans-serif;
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-image: url("image/photo_2023-08-04_13-32-33-removebg-preview.png");
            background-repeat: no-repeat;
            background-position: center;
            /*background-color: rgba(255, 255, 255, 0.3); /* Blanc semi-transparent */


        }}

        table {{
            width: 100%;
            border-collapse: collapse;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}

        th {{
            background-color: #f2f2f2;
        }}

        .total {{
            font-weight: bold;
        }}

        .en-tete {{
            font-weight: bold;
            font-size: 16px;
            text-align: center;
            margin-bottom: 20px;
        }}

        .adresse {{
            text-align: center;
            margin-bottom: 20px;
        }}

        .footer {{
            font-weight: bold;
            font-size: 12px;
            text-align: center;
            margin-top: 20px;
        }}
            </style>
        </head>
        <body>
            <div class="en-tete">
                COMBIO SARL<br>
                428, rue des jardins deux plateaux vallon<br>
                Abidjan, Côte d'Ivoire<br>
                Tél: +225 01 234 567<br>
                Email: info@combio.com
            </div>

            <p>Date: {date_facture}</p>
            <p>Facture No: {numero_facture}</p>

            <table>
                <thead>
                    <tr>
                        <th>Description</th>
                        <th>Quantité</th>
                        <th>Prix</th>
                    </tr>
                </thead>
                <tbody>
        """
        for produit in produits:
            content += f"""
                    <tr>
                        <td>{produit['nom']}</td>
                        <td>{produit['quantite']}</td>
                        <td>{produit['prix']}$</td>
                    </tr>
            """
        content += f"""
                </tbody>
            </table>

            <p class="total">{sous_total}</p>
            <p class="total">{taxes}</p>

            <table>
                <tfoot>
                    <tr>
                        <th>Total à payer:</th>
                        <td colspan="2">{total}</td>
                    </tr>
                </tfoot>
            </table>

            <p class="footer">Mode de paiement : {mode_paiement}</p>
            <p class="footer">Merci de votre achat chez COMBIO !</p>
        </body>
        </html>
        """
        return content


if __name__ == "__main__":
    app = QApplication([])

    # Exemple d'utilisation de la classe FactureWidget avec des paramètres personnalisables
    numero_facture = "001"
    date_facture = "05/08/2023"
    mode_paiement = "Espèces"
    produits = [
        {"nom": "Graines de Nigel", "quantite": "2", "prix": "20"},
        {"nom": "Pulpe d'aloès", "quantite": "1", "prix": "15"},
        {"nom": "Ail sans odeur", "quantite": "3", "prix": "8"},
        {"nom": "Panax Ginseng", "quantite": "2", "prix": "25"}
    ]
    sous_total = "Sous-total: 130$"
    taxes = "Taxes (TVA 18%): 23.40$"
    total = "Total à payer: 153.40$"

    fenetre = FactureWidget(numero_facture, date_facture, mode_paiement, produits, sous_total, taxes, total)
    fenetre.show()
    app.exec()


