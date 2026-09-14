from abc import ABC
from datetime import datetime


class Korisnik(ABC):
    def __init__(self, id, ime, prezime, email, telefon, lozinka_hash="",
                 datum_kreiranja=None):
        self.id = id
        self.ime = ime
        self.prezime = prezime
        self.email = email
        self.telefon = telefon
        self.lozinka_hash = lozinka_hash
        self.datum_kreiranja = datum_kreiranja or datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "ime": self.ime,
            "prezime": self.prezime,
            "email": self.email,
            "telefon": self.telefon,
            "lozinkaHash": self.lozinka_hash,
            "datumKreiranja": self.datum_kreiranja,
        }


class Volonter(Korisnik):
    def __init__(self, id, ime, prezime, email, telefon, lozinka_hash="",
                 datum_kreiranja=None, datum_pridruzivanja=None, aktivan=True):
        super().__init__(id, ime, prezime, email, telefon, lozinka_hash, datum_kreiranja)
        self.datum_pridruzivanja = datum_pridruzivanja or datetime.now().isoformat()
        self.aktivan = aktivan

    def to_dict(self):
        d = super().to_dict()
        d.update({
            "datumPridruzivanja": self.datum_pridruzivanja,
            "aktivan": self.aktivan,
        })
        return d

    @staticmethod
    def from_dict(d):
        return Volonter(
            id=d["id"], ime=d["ime"], prezime=d["prezime"], email=d["email"],
            telefon=d["telefon"], lozinka_hash=d.get("lozinkaHash", ""),
            datum_kreiranja=d.get("datumKreiranja"),
            datum_pridruzivanja=d.get("datumPridruzivanja"),
            aktivan=d.get("aktivan", True),
        )

    def __repr__(self):
        return f"Volonter({self.ime} {self.prezime})"