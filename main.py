import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtGui import QScreen
from screen_app import ScreenApp


class Form(QDialog):
    """
    Pour jouer avec une boite de dialogue simple
    """

    def __init__(self, application: QApplication, parent=None):
        super().__init__(parent)
        self.__app = application
        self.setWindowTitle("Ma boite de dialogue")
        self.__app.primaryScreenChanged.connect(self.__cpt)

        # Pour organiser la présentation de la boite de dialogue
        self.__layout = QVBoxLayout(self)

        # Création pour les dimensions de l'écran
        self.__label_principal = QLabel("Taille de l'écran")
        self.__label_principal.setStyleSheet("font-weight: bold;")
        self.__label_pixels = QLabel("Pixels")
        self.__label_pixels.setStyleSheet("font-weight: bold;")
        self.__label_physique = QLabel("mm")
        self.__label_physique.setStyleSheet("font-weight: bold;")
        self.__le_pixels = QLabel()
        self.__le_physique = QLabel()

        # Création de la pub
        self.__l = QLabel()
        self.__l.setText("Achetez des pommes !\nC'est bon pour vous.")
        self.__l.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.__l.setStyleSheet("color: blue; font-weight: bold;")
        gros = self.__l.font()
        gros.setPointSize(gros.pointSize() * 4)
        self.__l.setFont(gros)

        # Les boutons
        # b1 : compteur
        self.__b1 = QPushButton("0")
        self.__b1.setStyleSheet("font-weight: bold;")

        # b2 : pour effacer la pub
        self.__b2 = QPushButton("Effacer pub")
        self.__b2.setStyleSheet("font-weight: bold;")

        # b3 : pour remettre la pub
        self.__b3 = QPushButton("Remettre pub", self)
        self.__b3.setStyleSheet("font-weight: bold;")

        # Init
        self.__nb = 0
        self.__screen()
        self.__mettre_pub()
        self.__affiche_screen()

        # Les connects
        self.__b1.clicked.connect(self.__cpt)
        self.__b2.pressed.connect(self.__effacer_pub)
        self.__b3.pressed.connect(self.__mettre_pub)

        self.__organiser_widgets()

        # Taille de la dialog box
        self.resize(self.__pixels_w / 3, self.__pixels_h / 3)

    def __screen(self):
        """
        Pour récupérer les tailles physiques (mm) et pixels de l'écran primaire
        :return:
        """
        screen = self.__app.primaryScreen()
        sc = ScreenApp()

        self.__pixels_w = sc.get_width()
        self.__pixels_h = sc.get_height()
        self.__taille = screen.physicalSize()

    def __affiche_screen(self):
        """
        Pour afficher les tailles de l'écran primaire
        :return:
        """
        self.__le_pixels.setText(str(self.__pixels_w) + " x " + str(self.__pixels_h))
        screens = self.__app.screens()
        mess = ""
        for screen in screens:
            w = screen.physicalSize().width()
            h = screen.physicalSize().height()
            p = ((w / 25.4) ** 2 + ((h / 25.4) ** 2)) ** 0.5
            if mess != "":
                mess += " & "
            mess += str(w) + " x " + str(h)
            mess += " (" + str(round(p)) + " pouces)"

        self.__le_physique.setText(mess)

    def __organiser_widgets(self):
        """
        Dans self.__layout on a un QVBoxLayout dans lequel on va construire notre fenêtre de dialogue
        :return:
        """
        self.__layout.addWidget(self.__label_principal)

        vlayout1 = QVBoxLayout()
        vlayout1.addWidget(self.__label_pixels)
        vlayout1.addWidget(self.__le_pixels)

        vlayout2 = QVBoxLayout()
        vlayout2.addWidget(self.__label_physique)
        vlayout2.addWidget(self.__le_physique)

        hlayout1 = QHBoxLayout()
        hlayout1.addLayout(vlayout1)
        hlayout1.addLayout(vlayout2)

        # ---------------------

        vlayout3 = QVBoxLayout()
        vlayout3.addStretch()
        vlayout3.addWidget(self.__l)
        vlayout3.addStretch()

        # ---------------------

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(self.__b1)
        hlayout2.addWidget(self.__b2)
        hlayout2.addWidget(self.__b3)

        # ---------------------

        self.__layout.addLayout(hlayout1)
        self.__layout.addLayout(vlayout3)
        self.__layout.addLayout(hlayout2)

        self.setLayout(self.__layout)

    @Slot()
    def __cpt(self):
        """
        Slot qui incrémente l'intitulé du bouton 1
        :return:
        """
        self.__nb += 1
        self.__b1.setText(str(self.__nb))

    @Slot()
    def __mettre_pub(self):
        """
        Slot pour afficher le message de pub dans le QLineEdit
        :return:
        """
        self.__l.show()
        self.__b2.setEnabled(True)
        self.__b3.setEnabled(False)

    @Slot()
    def __effacer_pub(self):
        """
        Slot pour afficher le message de pub dans le QLineEdit
        :return:
        """
        self.__l.hide()
        self.__b2.setEnabled(False)
        self.__b3.setEnabled(True)


if __name__ == '__main__':
    # On crée l'application
    app = QApplication(sys.argv)
    # Création et affichage de la boite de dialogue
    form = Form(app)
    form.show()
    # On lance QT
    sys.exit(app.exec())
