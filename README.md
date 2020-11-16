# Verbarius Clock prototype algorithm

Inspired by [Verbarius clock](https://store.artlebedev.ru/electronics/devices/verbarius/)

## Example:

### Russian

```
    половина двенадцатого
    тридцать одна минута двенадцатого
    одиннадцать часов тридцать пять минут
    без двадцати полдень
    одиннадцать сорок пять
    без минуты полдень
    двенадцать
    два ровно
    пятнадцать минут третьего
    без пяти три
    без пятидесяти девяти пять =)
    четыре с четвертью
    одна минута шестого
```

### Ukrainian

```
    двадцять шість хвилин по дванадцятій
    двадцять сім хвилин по дванадцятій
    дванадцята година двадцять вісім хвилин
    дванадцята година двадцять дев'ять хвилин
    пів на першу
    дванадцята година тридцять одна хвилина
    двадцять вісім хвилин до першої
    дванадцята година тридцять три хвилини
    двадцять шість хвилин до першої
```

## Support languages:
- Russian (ru)
- Ukrainian (ua)


## Install:

`pip install verbarius`


## Usage:

```
>>> from verbarius import Verbarius, ru
>>> v = Verbarius(language=ru)
>>> v.get_time_string(hour=3, minute=10)
'десять минут четвёртого'
```

