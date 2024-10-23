#!/usr/bin/env python3

class Bojovnik:
    """
    Trida reprezentujici bojovnika.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self.jmeno = jmeno
        self.zivot = zivot
        self.max_zivot = zivot
        self.utok = utok
        self.obrana = obrana
        self.kostka = kostka
        self._zprava = ''

    def __str__(self):
        return str(self.jmeno)
    
    @property
    def nazivu(self):
        return self.zivot > 0


    
    def utoc(self, souper):
        uder = self.utok + self.kostka.hod()
        souper.bran_se(uder)
    

    def graficky_zivot(self):
        return self.graficky_ukazatel(self.zivot, self.max_zivot)


    def graficky_ukazatel(self, aktualni, maximalni):
        celkem = 20
        pocet = int(aktualni / maximalni * celkem)
        if pocet == 0 and self.nazivu:
            pocet == 1
        return f'[{"#" * pocet}{" " * (celkem-pocet)}]'



    def bran_se(self, uder):
        zraneni = uder - (self.obrana + self.kostka.hod())
        if zraneni > 0:
            self.zivot = self.zivot - zraneni
            zprava = f'{self.jmeno} utrpel zraneni o sile {zraneni}'
            if self.zivot <= 0:
                self.zivot = 0
                zprava = zprava + ' a zemrel.'
        else:
            zprava = f'{self.jmeno} zcela odrazil utok.'
        self.__set_zprava(zprava)


    def __set_zprava(self, zprava):
        self._zprava = zprava
    
    def get_zprava(self):
        return self._zprava

class Mag(Bojovnik):
    def _init__(self, jmeno, zivot, utok, obrana, kostka, mana, magicky_utok):
        super.__init__(jmeno, zivot, utok, obrana, kostka)
        self.mana = mana
        self.max_mana = mana
        self.magicky_utok = magicky_utok

    def utok(self,souper):
        if self.mana < self.max_mana: self.mana += 10
        if self.mana > self.max__mana: 
            self.mana = self.max_mana
            super().utoc(souper)

        else:
            uder = self.magicky_utok + self.kostka.hod()
            self.__set_zprava = f"{self.jmeno} utoci magii za {uder}"
            self.mana = 0
            souper.bran_se(uder)

            
    def graficka_mana(self):
        return self.graficky_ukazatel(self._mana, self._max_mana)
