from data.repositories import zivotinje_repo
from model import StatusZivotinje


class ZivotinjaController:
    def pregled_svih(self):
        return [z for z in zivotinje_repo.svi()
                if z.status == StatusZivotinje.DOSTUPNA and z.vidljiva]

    def pretraga(self, tekst="", pol=None, max_starost=None):
        rezultat = self.pregled_svih()
        if tekst:
            tekst = tekst.lower()
            rezultat = [z for z in rezultat if tekst in z.ime.lower()
                        or tekst in (z.opis or "").lower()]
        if pol:
            rezultat = [z for z in rezultat if z.pol == pol]
        if max_starost is not None:
            rezultat = [z for z in rezultat if z.starost <= max_starost]
        return rezultat

    def detalji(self, zivotinja_id):
        return zivotinje_repo.nadji_po_id(zivotinja_id)