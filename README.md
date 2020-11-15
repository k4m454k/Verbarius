# Verbarius Clock Russian prototype algorithm

## Example:

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

## Install:

`pip install verbarius`


## Usage:

```
>>> from verbarius import Verbarius
>>> v = Verbarius()
>>> v.get_time_string(hour=3, minute=10)
'десять минут четвёртого'
```
