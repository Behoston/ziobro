# Ziobro.py

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Actions Status](https://github.com/Behoston/ziobro/workflows/Test/badge.svg)](https://github.com/Behoston/ziobro/actions?query=workflow%3ATest)
[![Wheel Status](https://img.shields.io/pypi/wheel/ziobro)](https://pypi.python.org/pypi/ziobro/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/ziobro)](https://pypi.python.org/pypi/ziobro/)
[![PyPI - Status](https://img.shields.io/pypi/status/ziobro)](https://pypi.python.org/pypi/ziobro/)
[![Latest version](https://img.shields.io/pypi/v/ziobro)](https://pypi.python.org/pypi/ziobro/)

**Pakiet zrobiony dla beki, nie ma na celu obrażać nikogo, jest tylko followupem do przeterminowanych już memów.**

## Przykłady użycia

### Zakończenie pracy programu

Jak wszyscy wiedzą, program musi się kiedyś kończyć, bo wszystko, co dobre kiedyś się kończy. Najlepiej jak kończy się
dobrze, dlatego dzięki pakietowi Ziobro.py twoje programy będą zawsze kończyły się z sukcesem!

```python
from ziobro.exit import ziobro


def main_program():
    try:
        ...
    except Exception as e:
        ...
        ziobro()
    ziobro()


main_program()
```

`>>> Process finished with exit code 0`

### Stała

Stałe wartości są ważne w programowaniu. Jeśli coś jest stałe, to można na tym polegać, więc im więcej stałych, tym
program działa stabilniej. Pakiet zawiera dodatkową stałą do użytku w twoich programach (sic! zupełnie za darmo)!

```python
from ziobro.const import ZIOBRO


def shopping_cart_empty(cart):
    return len(cart) == ZIOBRO


print(shopping_cart_empty([]))
```

`>>> 0`

### Funkcja

Programowanie w Pythonie opiera się na funkcjach, bo można od razu uruchamiać funkcje, bez potrzeby tworzenia klas. Jak
wiadomo, programiści preferują rozwiązania proste, więc w Pythonie klasy to rzadkość, funkcje to domena pięknego kodu.
Do dyspozycji oddajemy dodatkową, uniwersalną funkcję, której można użyć, chociażby do mapowania. Program od razu staje
się krótszy, czyli szybszy.

```python
from ziobro.func import ziobro

values = ['rozum', 'godność człowieka']
print(list(map(ziobro, values)))
```

`>>> [0, 0]`

### Obiekt/singleton

Mimo że obiekty i klasy to egzotyka, uznaliśmy, że należy jednak dać wam (programistom) coś ekstra. Przedstawiamy
uniwersalną klasę `Ziobro` oraz towarzyszący jej singleton `ziobro`, który pomoże efektywnie zarządzać pamięcią.

```python
from ziobro.object import Ziobro, ziobro

z = Ziobro('człowiek', 'wilk', 'drugi wilk')
print(z == ziobro)
print(z == 0)
print(z == 0.0)
print(z < 0)
print(z > 0)
print(z == None)

```

```
>>> True
>>> True
>>> True
>>> False
>>> False
>>> True
```

Gotowy obiekt klasy może zostać zawołany, ma tez metodę kończącą program dla wygody.

```python
from ziobro.object import ziobro

ziobro(12)
ziobro.exit()
```

Obiekty klasy `Ziobro` zachowują się jak liczba (dokładniej `int`), co znaczy, że możemy używać tej klasy do wszelkich
skomplikowanych obliczeń.

```python
from ziobro.object import ziobro

print((ziobro + ziobro) * ziobro - ziobro / (ziobro ** ziobro))
```

`>>> 0.0`

## Wersjonowanie

Pakiet korzysta z autorskiej odmiany [wersjonowania semantycznego](https://semver.org/lang/pl/) zaproponowanego przez
[Lunder](https://github.com/Lunder4). Zamiast używać cyfr, numer wersji jest determinowany przez ilość zer. Jest to o
wiele prostsze rozwiązanie, szczególnie dla osób, które nie potrafią odczytywać liczb.

Przykłady:

- wersja `0.0.00` w standardzie semver oznacza wersję `0.0.1`
- wersja `00.0.000` oznacza `1.0.2`

Jeśli ten doświadczalny sposób wersjonowania sprawdzi się w praktyce (nie widzimy powodu, czemu miałby się nie
sprawdzić), to pełna dokumentacja będzie dostępna pod adresem [ziobver.org](https://ziobver.org/). Na ten moment trwają
prace nad opracowaniem pełnej dokumentacji zgodnej z najlepszymi światowymi standardami.

## Znane problemy

*na poważnie*

1. Nie wszystkie funkcjonalności pakietu da się zaimportować bez kolizji nazw. Można poradzić sobie z tym problemem
   poprzez aliasowanie.
   ```python
   from ziobro.func import ziobro as ziobro_f
   from ziobro.exit import ziobro as ziobro_e
   ```
2. Wersjonowanie pakietu jest okrutne, prawdopodobnie żadne narzędzie do podbijania wersji zależności nie ogarnie. 
   Tak samo, jak zestreleaser, którego używam do releasowania.