from data.repositories import zivotinje_repo, zahtevi_repo, udomitelji_repo, notifikacije_repo
from model import ZahtevZaUdomljavanje, StatusZivotinje, Udomitelj, Notifikacija


class ZahtevController:

    def posalji_zahtev(self, zivotinja_id, ime_podnosioca, kontakt_podnosioca):
        zahtev = ZahtevZaUdomljavanje(
            id=zahtevi_repo.sledeci_id(),
            zivotinja_id=zivotinja_id,
            ime_podnosioca=ime_podnosioca,
            kontakt_podnosioca=kontakt_podnosioca,
        )
        zahtevi_repo.dodaj(zahtev)

        zivotinja = zivotinje_repo.nadji_po_id(zivotinja_id)
        zivotinja.promeni_status(StatusZivotinje.NA_CEKANJU)
        zivotinje_repo.azuriraj(zivotinja)
        return zahtev

    def pregled_zahteva(self):
        from model import StatusZahteva
        return [z for z in zahtevi_repo.svi() if z.status == StatusZahteva.NA_CEKANJU]

    def odobri_zahtev(self, zahtev_id):
        zahtev = zahtevi_repo.nadji_po_id(zahtev_id)
        zahtev.odobri()
        zahtevi_repo.azuriraj(zahtev)

        postojeci = [u for u in udomitelji_repo.svi()
                     if u.kontakt == zahtev.kontakt_podnosioca]
        if postojeci:
            udomitelj = postojeci[0]
            udomitelj.dodaj_zivotinju(zahtev.zivotinja_id)
            udomitelji_repo.azuriraj(udomitelj)
        else:
            ime_delovi = zahtev.ime_podnosioca.split(" ", 1)
            udomitelj = Udomitelj(
                id=udomitelji_repo.sledeci_id(),
                ime=ime_delovi[0],
                prezime=ime_delovi[1] if len(ime_delovi) > 1 else "",
                adresa="",
                kontakt=zahtev.kontakt_podnosioca,
                zivotinje_ids=[zahtev.zivotinja_id],
            )
            udomitelji_repo.dodaj(udomitelj)

        zivotinja = zivotinje_repo.nadji_po_id(zahtev.zivotinja_id)
        zivotinja.promeni_status(StatusZivotinje.UDOMLJENA)
        zivotinje_repo.azuriraj(zivotinja)

        notifikacije_repo.dodaj(Notifikacija(
            id=notifikacije_repo.sledeci_id(),
            sadrzaj=f"Zahtev za udomljavanje životinje '{zivotinja.ime}' je odobren.",
        ))
        return zahtev

    def odbij_zahtev(self, zahtev_id):
        zahtev = zahtevi_repo.nadji_po_id(zahtev_id)
        zahtev.odbij()
        zahtevi_repo.azuriraj(zahtev)

        zivotinja = zivotinje_repo.nadji_po_id(zahtev.zivotinja_id)
        zivotinja.promeni_status(StatusZivotinje.DOSTUPNA)
        zivotinje_repo.azuriraj(zivotinja)
        return zahtev