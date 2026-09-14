from enum import Enum
from datetime import datetime


class StatusZahteva(str, Enum):
    NA_CEKANJU = "NA_CEKANJU"
    PRIHVACEN = "PRIHVACEN"
    ODBIJEN = "ODBIJEN"


class ZahtevZaUdomljavanje:
    def __init__(self, id, zivotinja_id, ime_podnosioca, kontakt_podnosioca,
                 datum_podnosenja=None, status=StatusZahteva.NA_CEKANJU):
        self.id = id
        self.zivotinja_id = zivotinja_id
        self.ime_podnosioca = ime_podnosioca
        self.kontakt_podnosioca = kontakt_podnosioca
        self.datum_podnosenja = datum_podnosenja or datetime.now().isoformat()
        self.status = StatusZahteva(status) if not isinstance(status, StatusZahteva) else status

    def odobri(self):
        self.status = StatusZahteva.PRIHVACEN

    def odbij(self):
        self.status = StatusZahteva.ODBIJEN

    def to_dict(self):
        return {
            "id": self.id,
            "zivotinjaId": self.zivotinja_id,
            "imePodnosioca": self.ime_podnosioca,
            "kontaktPodnosioca": self.kontakt_podnosioca,
            "datumPodnosenja": self.datum_podnosenja,
            "status": self.status.value,
        }

    @staticmethod
    def from_dict(d):
        return ZahtevZaUdomljavanje(
            id=d["id"], zivotinja_id=d["zivotinjaId"],
            ime_podnosioca=d["imePodnosioca"],
            kontakt_podnosioca=d["kontaktPodnosioca"],
            datum_podnosenja=d.get("datumPodnosenja"),
            status=StatusZahteva(d.get("status", "NA_CEKANJU")),
        )

    def __repr__(self):
        return f"ZahtevZaUdomljavanje(#{self.id}, {self.status.value})"