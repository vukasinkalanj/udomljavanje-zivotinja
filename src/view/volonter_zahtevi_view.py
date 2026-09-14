import tkinter as tk
from tkinter import ttk, messagebox
from controller.zahtev_controller import ZahtevController
from controller.zivotinja_controller import ZivotinjaController


class VolonterZahteviView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.kc = ZahtevController()
        self.zc = ZivotinjaController()

        ttk.Label(self, text="Zahtevi za udomljavanje na čekanju",
                  font=("Segoe UI", 13, "bold")).pack(anchor="w")
        ttk.Label(self, text="(Realizacija udomljavanja — pregled, odluka, ažuriranje statusa i notifikacija)",
                  foreground="#666").pack(anchor="w", pady=(0, 8))

        kolone = ("zivotinja", "podnosilac", "kontakt", "datum")
        self.stablo = ttk.Treeview(self, columns=kolone, show="headings", height=14)
        for kol, naslov, sirina in [("zivotinja", "Životinja", 120), ("podnosilac", "Podnosilac", 160),
                                     ("kontakt", "Kontakt", 160), ("datum", "Datum", 160)]:
            self.stablo.heading(kol, text=naslov)
            self.stablo.column(kol, width=sirina)
        self.stablo.pack(fill="both", expand=True, pady=8)

        dugmad = ttk.Frame(self)
        dugmad.pack(fill="x")
        ttk.Button(dugmad, text="✓ Odobri", command=self._odobri).pack(side="left", padx=4)
        ttk.Button(dugmad, text="✗ Odbij", command=self._odbij).pack(side="left", padx=4)
        ttk.Button(dugmad, text="Osveži", command=self._ucitaj).pack(side="right")

        self._id_po_redu = {}
        self._ucitaj()

    def _ucitaj(self):
        self.stablo.delete(*self.stablo.get_children())
        self._id_po_redu.clear()
        for z in self.kc.pregled_zahteva():
            zivotinja = self.zc.detalji(z.zivotinja_id)
            ime_zivotinje = zivotinja.ime if zivotinja else f"#{z.zivotinja_id}"
            red = self.stablo.insert("", "end", values=(
                ime_zivotinje, z.ime_podnosioca, z.kontakt_podnosioca,
                z.datum_podnosenja[:16].replace("T", " "),
            ))
            self._id_po_redu[red] = z.id

    def _izabrani_id(self):
        izbor = self.stablo.selection()
        if not izbor:
            messagebox.showinfo("Info", "Prvo izaberi zahtev iz liste.")
            return None
        return self._id_po_redu[izbor[0]]

    def _odobri(self):
        zid = self._izabrani_id()
        if zid is None:
            return
        self.kc.odobri_zahtev(zid)
        messagebox.showinfo("Odobreno", "Zahtev je odobren — udomitelj je zabeležen, "
                                         "životinja je označena kao udomljena, notifikacija poslata.")
        self._ucitaj()

    def _odbij(self):
        zid = self._izabrani_id()
        if zid is None:
            return
        self.kc.odbij_zahtev(zid)
        messagebox.showinfo("Odbijeno", "Zahtev je odbijen — životinja je ponovo dostupna.")
        self._ucitaj()