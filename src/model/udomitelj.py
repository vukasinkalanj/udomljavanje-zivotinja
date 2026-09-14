class Udomitelj:
    def __init__(self, id, ime, prezime, adresa, kontakt, interna_napomena="",
                 zivotinje_ids=None):
        self.id = id
        self.ime = ime
        self.prezime = prezime
        self.adresa = adresa
        self.kontakt = kontakt
        self.interna_napomena = interna_napomena
        self.zivotinje_ids = zivotinje_ids or []

    def dodaj_zivotinju(self, zivotinja_id):
        if zivotinja_id not in self.zivotinje_ids:
            self.zivotinje_ids.append(zivotinja_id)

    def to_dict(self):
        return {
            "id": self.id,
            "ime": self.ime,
            "prezime": self.prezime,
            "adresa": self.adresa,
            "kontakt": self.kontakt,
            "internaNapomena": self.interna_napomena,
            "zivotinjeIds": self.zivotinje_ids,
        }

    @staticmethod
    def from_dict(d):
        return Udomitelj(
            id=d["id"], ime=d["ime"], prezime=d["prezime"], adresa=d["adresa"],
            kontakt=d["kontakt"], interna_napomena=d.get("internaNapomena", ""),
            zivotinje_ids=d.get("zivotinjeIds", []),
        )

    def __repr__(self):
        return f"Udomitelj({self.ime} {self.prezime})"