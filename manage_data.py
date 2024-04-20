import MySQLdb


class ManageData:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def se_connecter(self):
        self.conn = MySQLdb.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()

    def se_deconnecter(self):
        if self.conn:
            self.conn.close()
            self.cursor = None

    def executer_requete(self, requete, valeurs=None):
        try:
            self.cursor.execute(requete, valeurs)
            self.conn.commit()
            return True
        except Exception as e:
            print("Erreur lors de l'exécution de la requête :", e)
            self.conn.rollback()
            return False

    def executer_requete_fetchone(self, requete, valeurs=None):
        self.cursor.execute(requete, valeurs)
        resultat = self.cursor.fetchone()
        return resultat

    def executer_requete_fetchall(self, requete, valeurs=None):
        self.cursor.execute(requete, valeurs)
        resultat = self.cursor.fetchall()
        return resultat

# Exemple d'utilisation
# if __name__ == "__main__":
#     gestionnaire_db = GestionnaireBaseDeDonnees(
#         host="localhost",
#         user="root",
#         password="",
#         database="projetgl"
#     )
#
#     gestionnaire_db.se_connecter()
#
#     requete_select = "SELECT COUNT(*) FROM client_courant"
#     row_count = gestionnaire_db.executer_requete_fetchone(requete_select)[0]
#
#     if row_count == 0:
#         print("La table Client est vide.")
#     else:
#         requete_role = "SELECT role FROM votre_table WHERE condition = %s"
#         condition = ("admin",)  # Exemple de condition
#         resultat = gestionnaire_db.executer_requete_fetchone(requete_role, condition)
#
#         if resultat and resultat[0] == "admin":
#             print("L'utilisateur est un admin.")
#         else:
#             print("L'utilisateur n'est pas un admin.")
#
#     gestionnaire_db.se_deconnecter()
