import os
from .repository import JsonRepository
from model import Zivotinja, ZahtevZaUdomljavanje, Udomitelj, Volonter, Udruzenje, Notifikacija

_OVDE = os.path.dirname(os.path.abspath(__file__))
_SEED = os.path.join(_OVDE, "seed")

zivotinje_repo = JsonRepository(os.path.join(_SEED, "zivotinje.json"), Zivotinja)
zahtevi_repo = JsonRepository(os.path.join(_SEED, "zahtevi.json"), ZahtevZaUdomljavanje)
udomitelji_repo = JsonRepository(os.path.join(_SEED, "udomitelji.json"), Udomitelj)
volonteri_repo = JsonRepository(os.path.join(_SEED, "volonteri.json"), Volonter)
udruzenja_repo = JsonRepository(os.path.join(_SEED, "udruzenja.json"), Udruzenje)
notifikacije_repo = JsonRepository(os.path.join(_SEED, "notifikacije.json"), Notifikacija)