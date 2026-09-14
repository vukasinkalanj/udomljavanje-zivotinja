from data.repositories import zivotinje_repo, volonteri_repo, udruzenja_repo
from model import Zivotinja, Volonter, Udruzenje, StatusZivotinje


def pokreni():
    if not udruzenja_repo.svi():
        udruzenja_repo.dodaj(Udruzenje(
            id=udruzenja_repo.sledeci_id(),
            ime="Udruženje Šapica",
            misija="Zbrinjavanje napuštenih životinja",
            ziro_racun="160-0000000001-11",
        ))

    if not volonteri_repo.svi():
        volonteri_repo.dodaj(Volonter(
            id=volonteri_repo.sledeci_id(),
            ime="Ana", prezime="Anić", email="ana@sapica.rs", telefon="0601111111",
        ))

    if not zivotinje_repo.svi():
        demo = [
            ("Reks", 3, "M", "", "Druželjubiv pas, voli decu."),
            ("Mica", 2, "Ž", "", "Mačka, pomalo plašljiva u početku."),
            ("Luna", 1, "Ž", "Alergija na određenu hranu", "Energičan štenac."),
        ]
        for ime, starost, pol, zdravlje, opis in demo:
            zivotinje_repo.dodaj(Zivotinja(
                id=zivotinje_repo.sledeci_id(), ime=ime, starost=starost, pol=pol,
                zdravstveni_problem=zdravlje, opis=opis,
                status=StatusZivotinje.DOSTUPNA, vidljiva=True, udruzenje_id=1,
            ))

    print("Seed podaci spremni:")
    print(" -", len(udruzenja_repo.svi()), "udruženje(a)")
    print(" -", len(volonteri_repo.svi()), "volonter(a)")
    print(" -", len(zivotinje_repo.svi()), "životinja")


if __name__ == "__main__":
    pokreni()