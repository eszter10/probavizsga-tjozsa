## 4 Feladat: Számfordító

Adott egy petofi.txt nevű file (megtalálhatod a feladat mellett).
Készíts egy Python python applikációt (egy darab python file) ami minden második szót a petofi.txt file-ból átírja egy res.csv nevű fileba. Az eredmény legyen vesszővel elválasztott fomrátumű a következő módon:
```
2, borocska
4, Vígan
6, életem
...
```
Tehát az első oszlop tartalmazza az, hogy az eredeti file-ban hanyadik volt a szó (az első szó az 1-es indexet kapja).


### Tanácsok a megoldáshoz:
* Fontos, hogy függvényt adjál be
* Fontos, hogy ne triviális megoldást adj be (a felnti számokra működik csak de ha egy másik tesztadattal próbáljuk arra nem műküdik)
* Ne gondold túl!
* Bérmilyen megodás ami a fenti teszt adatokra (és hasonló tesztadatokra) a helyes megoldást adja tökéletesen megfelel
* Nincs pontlevonás ha `lehetne ezt egyszerűbben is`
* Nincs plusz pont ha `kevesebb sorból oldod meg`


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `rev_num.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(