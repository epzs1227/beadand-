from datetime import datetime, timedelta

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=5000, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=8000, szobaszam=szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def foglalas_felvetel(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                print("A megadott szoba már foglalt ezen a napon.")
                return False
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = {'szobaszam': szobaszam, 'datum': datum, 'ar': szoba.ar}
                self.foglalasok.append(foglalas)
                print(f"A(z) {szobaszam}. számú szoba foglalása sikeres.")
                return True
        print("A megadott szobaszám nem létezik.")
        return False

    def foglalas_lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                self.foglalasok.remove(foglalas)
                print("A foglalás sikeresen lemondva.")
                return True
        print("Nem található foglalás a megadott paraméterekkel.")
        return False

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincs egyetlen foglalás sem.")
        else:
            print("Foglalások listája:")
            for i, foglalas in enumerate(self.foglalasok, start=1):
                print(f"{i}. Szobaszám: {foglalas['szobaszam']}, Dátum: {foglalas['datum']}, Ár: {foglalas['ar']} Ft")

def main():
    szalloda = Szalloda("Pihenő Hotel")
    szalloda.szoba_hozzaad(EgyagyasSzoba(101))
    szalloda.szoba_hozzaad(EgyagyasSzoba(102))
    szalloda.szoba_hozzaad(KetagyasSzoba(201))
    szalloda.szoba_hozzaad(KetagyasSzoba(202))
    szalloda.szoba_hozzaad(KetagyasSzoba(203))

    szalloda.foglalas_felvetel(101, datetime.now() + timedelta(days=2))
    szalloda.foglalas_felvetel(201, datetime.now() + timedelta(days=4))
    szalloda.foglalas_felvetel(201, datetime.now() + timedelta(days=6))
    szalloda.foglalas_felvetel(203, datetime.now() + timedelta(days=8))
    szalloda.foglalas_felvetel(101, datetime.now() + timedelta(days=10))

    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Művelet sorszáma: ")

        if valasztas == "1":
            szobaszam = int(input("Kérem adja meg a szobaszámot: "))
            datum = input("Kérem adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum, "%Y-%m-%d")
            except ValueError:
                print("Érvénytelen dátum formátum.")
                continue
            if datum < datetime.now():
                print("A foglalás dátuma nem lehet múltbeli.")
                continue
            szalloda.foglalas_felvetel(szobaszam, datum)
        elif valasztas == "2":
            szobaszam = int(input("Kérem adja meg a szobaszámot: "))
            datum = input("Kérem adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum, "%Y-%m-%d")
            except ValueError:
                print("Érvénytelen dátum formátum.")
                continue
            szalloda.foglalas_lemondas(szobaszam, datum)
        elif valasztas == "3":
            szalloda.foglalasok_listazasa()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen művelet.")

if __name__ == "__main__":
    main()
