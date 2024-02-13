import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton
from PySide6 import QtCore
from PySide6.QtCore import Slot


class Form(QDialog):
    """
    Pour jouer avec une boite de dialogue simple
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ma boite de dialogue")

        # Création du LineEdit
        self.__l = QLineEdit(self)
        self.__l.setGeometry(0, 0, 400, 200)
        self.__l.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Les boutons
        # b1 : compteur
        self.__b1 = QPushButton("0", self)
        self.__b1.setGeometry(0, 200, 100, 50)

        # b2 : pour effacer la pub
        self.__b2 = QPushButton("Effacer pub", self)
        self.__b2.setGeometry(300, 200, 100, 50)

        # b3 : pour remettre la pub
        self.__b3 = QPushButton("Remettre pub", self)
        self.__b3.setGeometry(300, 200, 100, 50)

        # Init
        self.__nb = 0
        self.__mettre_pub()

        # Au départ le bouton 3 est invisible
        self.__b3.hide()

        # Les connects
        self.__b1.clicked.connect(self.__cpt)
        self.__b2.pressed.connect(self.__l.clear)
        self.__b3.pressed.connect(self.__mettre_pub)

        # Et la gestion mêlée des boutons 2 ... 3

        self.__b2.clicked.connect(self.__b3.show)
        self.__b2.released.connect(self.__b2.hide)

        self.__b3.clicked.connect(self.__b2.show)
        self.__b3.released.connect(self.__b3.hide)

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
        self.__l.setText("Achetez des pommes !\nC'est bon pour vous.")


if __name__ == '__main__':
    # On crée l'application
    app = QApplication(sys.argv)
    # Création et affichage de la boite de dialogue
    form = Form()
    form.show()
    # On lance QT
    sys.exit(app.exec())
