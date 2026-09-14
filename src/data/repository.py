import json
import os


class JsonRepository:
    def __init__(self, putanja, klasa):
        self.putanja = putanja
        self.klasa = klasa
        os.makedirs(os.path.dirname(putanja), exist_ok=True)
        if not os.path.exists(putanja):
            with open(putanja, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _ucitaj_sirovo(self):
        with open(self.putanja, "r", encoding="utf-8") as f:
            return json.load(f)

    def _sacuvaj_sirovo(self, lista_recnika):
        with open(self.putanja, "w", encoding="utf-8") as f:
            json.dump(lista_recnika, f, ensure_ascii=False, indent=2)

    def svi(self):
        return [self.klasa.from_dict(d) for d in self._ucitaj_sirovo()]

    def nadji_po_id(self, id):
        for obj in self.svi():
            if obj.id == id:
                return obj
        return None

    def sledeci_id(self):
        podaci = self._ucitaj_sirovo()
        if not podaci:
            return 1
        return max(d["id"] for d in podaci) + 1

    def dodaj(self, objekat):
        podaci = self._ucitaj_sirovo()
        podaci.append(objekat.to_dict())
        self._sacuvaj_sirovo(podaci)
        return objekat

    def azuriraj(self, objekat):
        podaci = self._ucitaj_sirovo()
        for i, d in enumerate(podaci):
            if d["id"] == objekat.id:
                podaci[i] = objekat.to_dict()
                break
        self._sacuvaj_sirovo(podaci)
        return objekat