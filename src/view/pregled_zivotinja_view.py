import tkinter as tk
from tkinter import ttk, messagebox
from controller.zivotinja_controller import ZivotinjaController
from controller.zahtev_controller import ZahtevController


class PregledZivotinjaView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.zc = ZivotinjaController()
        self.kc = ZahtevController()

        ttk.Label(self, text="Životinje dostupne za udomljavanje",
                  font=("Segoe UI", 13, "bold")).pack(anchor="w")

        traka = ttk.Frame(self)
        traka.pack(fill="x", pady=8)
        ttk.Label(traka, text="Pretraga:").pack(side="left")
        self.tekst_var = tk.StringVar()
        ttk.Entry(traka, textvariable=self.tekst_var, width=25).pack(side="left", padx=6)

        ttk.Label(traka, text="Pol:").pack(side="left", padx=(12, 0))
        self.pol_var = tk.StringVar(value="Svi")
        ttk.Combobox(traka, textvariable=self.pol_var, values=["Svi", "M", "Ž"],
                     width=6, state="readonly").pack(side="left", padx=6)

        ttk.Button(traka, text="Pretraži", command=self._pretrazi).pack(side="left", padx=8)
        ttk.Button(traka, text="Prikaži sve", command=self._ucitaj_sve).pack(side="left")

        kolone = ("ime", "starost", "pol", "opis")
        self.stablo = ttk.Treeview(self, columns=kolone, show="headings", height=12)
        for kol, naslov, sirina in [("ime", "Ime", 120), ("starost", "Starost", 70),
                                     ("pol", "Pol", 50), ("opis", "Opis", 400)]:
            self.stablo.heading(kol, text=naslov)
            self.stablo.column(kol, width=sirina)
        self.stablo.pack(fill="both", expand=True, pady=8)
        self.stablo.bind("<Double-1>", lambda e: self._otvori_detalje())

        ttk.Button(self, text="Detalji / Pošalji zahtev za udomljavanje",
                   command=self._otvori_detalje).pack(anchor="e")

        self._id_po_redu = {}
        self._ucitaj_sve()

    def _popuni_stablo(self, zivotinje):
        self.stablo.delete(*self.stablo.get_children())
        self._id_po_redu.clear()
        for z in zivotinje:
            red = self.stablo.insert("", "end", values=(z.ime, z.starost, z.pol, z.opis))
            self._id_po_redu[red] = z.id

    def _ucitaj_sve(self):
        self.tekst_var.set("")
        self.pol_var.set("Svi")
        self._popuni_stablo(self.zc.pregled_svih())

    def _pretrazi(self):
        pol = None if self.pol_var.get() == "Svi" else self.pol_var.get()
        self._popuni_stablo(self.zc.pretraga(tekst=self.tekst_var.get(), pol=pol))

    def _otvori_detalje(self):
        izbor = self.stablo.selection()
        if not izbor:
            messagebox.showinfo("Info", "Prvo izaberi životinju iz liste.")
            return
        zivotinja_id = self._id_po_redu[izbor[0]]
        zivotinja = self.zc.detalji(zivotinja_id)
        DetaljiZivotinjeDialog(self, zivotinja, self.kc, on_poslato=self._ucitaj_sve)


class DetaljiZivotinjeDialog(tk.Toplevel):
    def __init__(self, parent, zivotinja, zahtev_controller, on_poslato):
        super().__init__(parent)
        self.title(f"Detalji — {zivotinja.ime}")
        self.geometry("380x420")
        self.zivotinja = zivotinja
        self.kc = zahtev_controller
        self.on_poslato = on_poslato

        okvir = ttk.Frame(self, padding=12)
        okvir.pack(fill="both", expand=True)

        for naslov, vrednost in [
            ("Ime", zivotinja.ime), ("Starost", zivotinja.starost), ("Pol", zivotinja.pol),
            ("Zdravstveni problem", zivotinja.zdravstveni_problem or "—"),
            ("Opis", zivotinja.opis), ("Status", zivotinja.status.value),
        ]:
            red = ttk.Frame(okvir)
            red.pack(fill="x", pady=2)
            ttk.Label(red, text=f"{naslov}:", font=("Segoe UI", 9, "bold"),
                      width=18, anchor="w").pack(side="left")
            ttk.Label(red, text=str(vrednost), wraplength=200, justify="left").pack(side="left")

        ttk.Separator(okvir).pack(fill="x", pady=10)
        ttk.Label(okvir, text="Zahtev za udomljavanje (FR6)",
                  font=("Segoe UI", 10, "bold")).pack(anchor="w")

        ttk.Label(okvir, text="Ime i prezime:").pack(anchor="w", pady=(8, 0))
        self.ime_var = tk.StringVar()
        ttk.Entry(okvir, textvariable=self.ime_var).pack(fill="x")

        ttk.Label(okvir, text="Kontakt (telefon/email):").pack(anchor="w", pady=(8, 0))
        self.kontakt_var = tk.StringVar()
        ttk.Entry(okvir, textvariable=self.kontakt_var).pack(fill="x")

        self.dugme_posalji = ttk.Button(okvir, text="Pošalji zahtev", command=self._posalji)
        self.dugme_posalji.pack(pady=14)

        if zivotinja.status.value != "DOSTUPNA":
            self.dugme_posalji.state(["disabled"])
            ttk.Label(okvir, text="Ova životinja trenutno nije dostupna za zahtev.",
                      foreground="#b00").pack()

    def _posalji(self):
        if not self.ime_var.get().strip() or not self.kontakt_var.get().strip():
            messagebox.showwarning("Nedostaju podaci", "Unesi ime i kontakt.")
            return
        self.kc.posalji_zahtev(self.zivotinja.id, self.ime_var.get().strip(),
                                self.kontakt_var.get().strip())
        messagebox.showinfo("Poslato", "Zahtev za udomljavanje je poslat udruženju.")
        self.on_poslato()
        self.destroy()