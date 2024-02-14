from screeninfo import get_monitors
import tkinter as tk


class ScreenApp:
    """
    Utilisée par avoir le bord gauche, haut de l'écran ayant le curseur souris ainsi que la taille de ce dernier.
    """

    def __init__(self):
        # On récupère la position courante du curseur de la souris
        root = tk.Tk()
        root.update()
        x_mouse = root.winfo_pointerx()
        y_mouse = root.winfo_pointery()
        root.destroy()

        # Et on regarde les écrans
        monitors = get_monitors()
        for monitor in monitors:
            if monitor.x <= x_mouse <= monitor.x + monitor.width and monitor.y <= y_mouse <= monitor.y + monitor.height:
                self.__x = monitor.x
                self.__y = monitor.y
                self.__width = monitor.width
                self.__height = monitor.height

    def get_left(self) -> int:
        """
        Donne le coin gauche de l'écran

        :return: X haut de l'écran en pixels
        """
        return self.__x

    def get_top(self) -> int:
        """
        Donne le coin haut de l'écran

        :return: Y haut de l'écran en pixels
        """
        return self.__y

    def get_width(self) -> int:
        """
        Donne la largeur de l'écran

        :return: Donne la largeur de l'écran en pixels
        """
        return self.__width

    def get_height(self) -> int:
        """
        Donne la hauteur de l'écran

        :return: Donne la hauteur de l'écran en pixels
        """
        return self.__height
