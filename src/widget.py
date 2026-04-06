# This Python file uses the following encoding: utf-8
import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidget, QTableWidgetItem, QInputDialog
import sqlite3
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import QMenu
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pysidpyside6-uic form.ui -o ui_form.pye2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from datetime import datetime

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Weather Diary  - Fedora 43 Edition")
        #Connect le bouton obtenir a l'action
        self.ui.btn_obtenir.clicked.connect(self.fetch_weather)
        self.ui.tableWeather.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableWeather.customContextMenuRequested.connect(self.ouvrir_menu_contexte)
        #desactiver les verticales headers
        self.ui.table_historique.verticalHeader().setVisible(False)
        self.setFixedSize(self.size())
        self.ui.table_historique.setColumnCount(4)
        self.ui.table_historique.setHorizontalHeaderLabels(["Ville", "Temp.", "Météo", "Recherche"])

        self.villes_suivies = []
        #config du tableau de gauche
        self.ui.tableWeather.setColumnCount(4)
        self.ui.tableWeather.setHorizontalHeaderLabels(["Ville", "Heure", "Temp.", "Ciel"])
        self.ui.tableWeather.verticalHeader().setVisible(False)

        #connexion des boutons
        self.ui.btn_ajouter.clicked.connect(self.ajouter_ville)
        self.ui.btn_rafraichir.clicked.connect(self.update_weather_table)
        self.init_db()
        self.charger_villes_sauvegardees()
        self.ui.table_historique.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Empêcher la modification directe des cellules (lecture seule)
        self.ui.table_historique.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.ui.tableWeather.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWeather.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWeather.setSelectionMode(QAbstractItemView.SingleSelection)


    def init_db(self):
        self.conn = sqlite3.connect("/home/lcdelcroix/Documents/j_ai_grandi_12.11.2025/Project/Python/weather/data/meteo_master.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            temperature REAL NOT NULL,
            meteo TEXT NOT NULL,
            time_search TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_followed (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        last_temp REAL,
        last_meteo TEXT
        )
        """)
        self.conn.commit()


    def sauvergarder_historique_db(self, nom, temp, meteo):
        try:
            self.cursor.execute(
                "INSERT INTO history (name, temperature, meteo) VALUES (?, ?, ?)",
                (nom, temp, meteo)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Erreur SQL historique : {e}")



    def sauvergarder_ville_db(self, nom_ville):
        try:
            self.cursor.execute("INSERT OR IGNORE INTO weather_followed (name) VALUES (?)", (nom_ville,))
            self.conn.commit()
        except Exception as e:
            print(f"Erreur SQL sauvegarde : {e}")



    def charger_villes_sauvegardees(self):
        try:
            self.cursor.execute("SELECT name FROM weather_followed")
            lignes = self.cursor.fetchall()

            self.villes_suivies = [row[0] for row in lignes]

            if self.villes_suivies:
                self.update_weather_table()
        except Exception as e:
            print(f"Erreur lors du chargement : {e}")


    def fetch_weather(self):
        ville = self.ui.lineEdit_ville.text()
        api_key = "ff2ee90bff20d7c836254e223804fd0a"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric&lang=fr"

        try:
            reponse = requests.get(url)
            data = reponse.json()

            if data["cod"] == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                info = f"Meteo a {ville}: {temp} °C, {desc}"

                QMessageBox.information(self, "Résultat Météo", info)

                self.ajouter_a_l_historique(ville, temp, desc)
                self.ui.lineEdit_ville.clear();
            else:
                QMessageBox.warning(self, "Erreur", "Ville non trouvée !")
        except Exception as e:
            print(f"Erreur de connexion : {e}")


    def ajouter_a_l_historique(self, ville, temp, desc):
        heure_recherche = datetime.now().strftime("%H:%M:%S")

        row = self.ui.table_historique.rowCount()
        self.ui.table_historique.insertRow(row)

        self.ui.table_historique.setItem(row, 0, QTableWidgetItem(ville))
        self.ui.table_historique.setItem(row, 1, QTableWidgetItem(f"{temp}C"))
        self.ui.table_historique.setItem(row, 2, QTableWidgetItem(desc))
        self.ui.table_historique.setItem(row, 3, QTableWidgetItem(heure_recherche))
        self.sauvergarder_historique_db(ville, temp, desc)



    def ajouter_ville(self):
        ville , ok = QInputDialog.getText(self, "Ajouter une ville", "Nom de la ville :")

        if ok and ville:
            ville  = ville.strip().capitalize()
            self.sauvergarder_ville_db(ville)

            if ville in self.villes_suivies:
                QMessageBox.information(self, "Info", "Cette ville est déjà suivie.")
                return

            api_key = "ff2ee90bff20d7c836254e223804fd0a"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric&lang=fr"

            try:
                reponse = requests.get(url)
                if reponse.status_code == 200:
                    self.villes_suivies.append(ville)
                    self.update_weather_table()
                else:
                    QMessageBox.warning(self, "Erreur", f"La ville '{ville}' n'a pas été trouvée.")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur réseau : {e}")

    def update_weather_table(self):
        self.ui.tableWeather.setRowCount(0)
        api_key = "ff2ee90bff20d7c836254e223804fd0a"

        for ville in self.villes_suivies:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric&lang=fr"
            try:
                data = requests.get(url).json()
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]

                self.cursor.execute("""
                    UPDATE weather_followed
                    SET last_temp = ?, last_meteo = ?
                    WHERE name = ?
                """, (temp, desc, ville))
                self.conn.commit()

                import time
                utc_now = time.time()
                local_time = time.strftime('%H:%M', time.gmtime(utc_now + data['timezone']))

                row = self.ui.tableWeather.rowCount()
                self.ui.tableWeather.insertRow(row)
                self.ui.tableWeather.setItem(row, 0, QTableWidgetItem(ville))
                self.ui.tableWeather.setItem(row, 1, QTableWidgetItem(local_time))
                self.ui.tableWeather.setItem(row, 2, QTableWidgetItem(f"{temp}°C"))
                self.ui.tableWeather.setItem(row, 3, QTableWidgetItem(desc))
            except Exception as e:
                print(f"Erreur lors de l'update de {ville}: {e}")
    
    def ouvrir_menu_contexte(self, position):
        # On crée le menu
        menu = QMenu()
        action_supprimer = QAction("Supprimer cette ville", self)
        action_supprimer.triggered.connect(self.supprimer_ville_selectionnee)
        menu.addAction(action_supprimer)
    
        # On l'affiche à l'endroit de la souris
        menu.exec(QCursor.pos())

    def supprimer_ville_selectionnee(self):
        # 1. Récupérer la ligne sélectionnée
        current_row = self.ui.tableWeather.currentRow()
    
        if current_row != -1: # Si une ligne est bien sélectionnée
            # 2. Récupérer le nom de la ville (colonne 0)
            nom_ville = self.ui.tableWeather.item(current_row, 0).text()
        
            # 3. Supprimer de la Base de Données
            try:
                self.cursor.execute("DELETE FROM weather_followed WHERE name = ?", (nom_ville,))
                self.conn.commit()
            
                # 4. Supprimer de la liste Python
                if nom_ville in self.villes_suivies:
                    self.villes_suivies.remove(nom_ville)
            
                # 5. Supprimer la ligne de l'interface
                self.ui.tableWeather.removeRow(current_row)
            
                print(f"{nom_ville} supprimée avec succès.")
            except Exception as e:
                QMessageBox.critical(self, "Erreur SQL", f"Impossible de supprimer : {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    style_principal = """
        QWidget {
            background-color: #f5f5f5;
            font-family: 'Segoe UI', Arial;
            font-size: 14px;
        }

        QFrame#frameHistory, QFrame#frameInput, QFrame#frameTableWeather {
            border: 2px solid #2980b9;
            border-radius: 8px;
            margin-top: 10px;
            font-weight: bold;
            color: #2c3e50;
        }

        QFrame::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 3px 0 3px;
        }

        QPushButton {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 8px;
            min-width: 80px;
        }

        QPushButton:hover {
            background-color: #2980b9;
        }

        QLineEdit {
            border: 1px solid #bdc3c7;
            border-radius: 4px;
            padding: 5px;
        }

        QTableWidget {
            gridline-color: #dcdde1;
            background-color: white;
            selection-background-color: #3498db;
            border: 2px solid #0A1214;
            border-radius: 8px;
        }

        QHeaderView::section {
            background-color: #3498db;
            color: white;
            padding: 4px;
            border: 1px solid #2980b9;
            font-weight: bold;
        }

        QTableWidget::item:selected {
            background-color: #3498db;
            color: white;
            border: none;
        }

        QTableWidget {
            outline: 0;
        }
    """
    app.setStyleSheet(style_principal)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
