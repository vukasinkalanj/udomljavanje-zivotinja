from datetime import datetime


class Notifikacija:
    def __init__(self, id, sadrzaj, datum_slanja=None, procitana=False):
        self.id = id
        self.sadrzaj = sadrzaj
        self.datum_slanja = datum_slanja or datetime.now().isoformat()
        self.procitana = procitana

    def to_dict(self):
        return {
            "id": self.id,
            "sadrzaj": self.sadrzaj,
            "datumSlanja": self.datum_slanja,
            "procitana": self.procitana,
        }

    @staticmethod
    def from_dict(d):
        return Notifikacija(id=d["id"], sadrzaj=d["sadrzaj"],
                             datum_slanja=d.get("datumSlanja"),
                             procitana=d.get("procitana", False))

    def __repr__(self):
        return f"Notifikacija({self.sadrzaj[:30]!r})"


class Udruzenje:
    def __init__(self, id, ime, misija="", ziro_racun=""):
        self.id = id
        self.ime = ime
        self.misija = misija
        self.ziro_racun = ziro_racun

    def to_dict(self):
        return {"id": self.id, "ime": self.ime, "misija": self.misija,
                "ziroRacun": self.ziro_racun}

    @staticmethod
    def from_dict(d):
        return Udruzenje(id=d["id"], ime=d["ime"], misija=d.get("misija", ""),
                          ziro_racun=d.get("ziroRacun", ""))

    def __repr__(self):
        return f"Udruzenje({self.ime})"