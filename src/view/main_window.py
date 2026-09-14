import tkinter as tk
from tkinter import ttk
from view.pregled_zivotinja_view import PregledZivotinjaView
from view.volonter_zahtevi_view import VolonterZahteviView


class GlavniProzor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Udomljavanje i zaštita životinja — prototip")
        self.geometry("900x600")

        traka = ttk.Frame(self, padding=8)
        traka.pack(side="top", fill="x")
        ttk.Label(traka, text="Režim:", font=("Segoe UI", 10, "bold")).pack(side="left", padx=(0, 8))
        ttk.Button(traka, text="Neregistrovani korisnik",
                   command=self.prikazi_gosta).pack(side="left", padx=4)
        ttk.Button(traka, text="Volonter — zahtevi",
                   command=self.prikazi_volontera).pack(side="left", padx=4)

        self.sadrzaj = ttk.Frame(self)
        self.sadrzaj.pack(side="top", fill="both", expand=True)

        self.prikazi_gosta()

    def _ocisti_sadrzaj(self):
        for widget in self.sadrzaj.winfo_children():
            widget.destroy()

    def prikazi_gosta(self):
        self._ocisti_sadrzaj()
        PregledZivotinjaView(self.sadrzaj).pack(fill="both", expand=True)

    def prikazi_volontera(self):
        self._ocisti_sadrzaj()
        VolonterZahteviView(self.sadrzaj).pack(fill="both", expand=True)


if __name__ == "__main__":
    app = GlavniProzor()
    app.mainloop()