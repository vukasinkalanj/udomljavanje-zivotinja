import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data.seed_data import pokreni as ucitaj_seed_podatke
from view.main_window import GlavniProzor

if __name__ == "__main__":
    ucitaj_seed_podatke()
    app = GlavniProzor()
    app.mainloop()