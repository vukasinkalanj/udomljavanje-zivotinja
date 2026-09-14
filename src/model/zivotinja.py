from enum import Enum


class StatusZivotinje(str, Enum):
    DOSTUPNA = "DOSTUPNA"
    NA_CEKANJU = "NA_CEKANJU"
    PRIVREMENO_ZBRINUTA = "PRIVREMENO_ZBRINUTA"
    UDOMLJENA = "UDOMLJENA"


class Zivotinja:
    def __init__(self, id, ime, starost, pol, zdravstveni_problem="", opis="",
                 status=StatusZivotinje.DOSTUPNA, vidljiva=True, udruzenje_id=None):
        self.id = id
        self.ime = ime
        self.starost = starost
        self.pol = pol
        self.zdravstveni_problem = zdravstveni_problem
        self.opis = opis
        self.status = StatusZivotinje(status) if not isinstance(status, StatusZivotinje) else status
        self.vidljiva = vidljiva
        self.udruzenje_id = udruzenje_id

    def promeni_status(self, nov_status: StatusZivotinje):
        self.status = StatusZivotinje(nov_status)

    def promeni_vidljivost(self, vidljivo: bool):
        self.vidljiva = vidljivo

    def to_dict(self):
        return {
            "id": self.id,
            "ime": self.ime,
            "starost": self.starost,
            "pol": self.pol,
            "zdravstveniProblem": self.zdravstveni_problem,
            "opis": self.opis,
            "status": self.status.value,
            "vidljiva": self.vidljiva,
            "udruzenjeId": self.udruzenje_id,
        }

    @staticmethod
    def from_dict(d):
        return Zivotinja(
            id=d["id"], ime=d["ime"], starost=d["starost"], pol=d["pol"],
            zdravstveni_problem=d.get("zdravstveniProblem", ""),
            opis=d.get("opis", ""),
            status=StatusZivotinje(d.get("status", "DOSTUPNA")),
            vidljiva=d.get("vidljiva", True),
            udruzenje_id=d.get("udruzenjeId"),
        )

    def __repr__(self):
        return f"Zivotinja({self.ime}, {self.status.value})"