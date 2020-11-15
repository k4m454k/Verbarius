

hours_temps = {
    0: {'current_hour': 'ноль', 'future_hour': 'первого', 'future_hour_std': 'час', "declension": "часов"},
    1: {'current_hour': 'один час', 'future_hour': 'второго', 'future_hour_std': 'два', "declension": "и"},
    2: {'current_hour': 'два', 'future_hour': 'третьего', 'future_hour_std': 'три', "declension": "часа"},
    3: {'current_hour': 'три', 'future_hour': 'четвёртого', 'future_hour_std': 'четыре', "declension": "часа"},
    4: {'current_hour': 'четыре', 'future_hour': 'пятого', 'future_hour_std': 'пять', "declension": "часа"},
    5: {'current_hour': 'пять', 'future_hour': 'шестого', 'future_hour_std': 'шесть', "declension": "часов"},
    6: {'current_hour': 'шесть', 'future_hour': 'седьмого', 'future_hour_std': 'семь', "declension": "часов"},
    7: {'current_hour': 'семь', 'future_hour': 'восьмого', 'future_hour_std': 'восемь', "declension": "часов"},
    8: {'current_hour': 'восемь', 'future_hour': 'девятого', 'future_hour_std': 'девять', "declension": "часов"},
    9: {'current_hour': 'девять', 'future_hour': 'десятого', 'future_hour_std': 'десять', "declension": "часов"},
    10: {'current_hour': 'десять', 'future_hour': 'одиннадцатого', 'future_hour_std': 'одиннадцать', "declension": "часов"},
    11: {'current_hour': 'одиннадцать', 'future_hour': 'двенадцатого', 'future_hour_std': 'полдень', "declension": "часов"},
    12: {'current_hour': 'двенадцать', 'future_hour': 'первого', 'future_hour_std': 'час', "declension": "часов"},
    13: {'current_hour': 'один час', 'future_hour': 'второго', 'future_hour_std': 'два', "declension": "и"},
    14: {'current_hour': 'два', 'future_hour': 'третьего', 'future_hour_std': 'три', "declension": "часа"},
    15: {'current_hour': 'три', 'future_hour': 'четвёртого', 'future_hour_std': 'четыре', "declension": "часа"},
    16: {'current_hour': 'четыре', 'future_hour': 'пятого', 'future_hour_std': 'пять', "declension": "часа"},
    17: {'current_hour': 'пять', 'future_hour': 'шестого', 'future_hour_std': 'шесть', "declension": "часов"},
    18: {'current_hour': 'шесть', 'future_hour': 'седьмого', 'future_hour_std': 'семь', "declension": "часов"},
    19: {'current_hour': 'семь', 'future_hour': 'восьмого', 'future_hour_std': 'восемь', "declension": "часов"},
    20: {'current_hour': 'восемь', 'future_hour': 'девятого', 'future_hour_std': 'девять', "declension": "часов"},
    21: {'current_hour': 'девять', 'future_hour': 'десятого', 'future_hour_std': 'десять', "declension": "часов"},
    22: {'current_hour': 'десять', 'future_hour': 'одиннадцатого', 'future_hour_std': 'одиннадцать', "declension": "часов"},
    23: {'current_hour': 'одиннадцать', 'future_hour': 'до полуночи', 'future_hour_std': 'полночь', "declension": "часов"}
}


base_temps = {
    0: ["$current_hour", "$current_hour ровно"],
    1: ["одна минута $future_hour", "$current_hour $declension одна минута", "без пятидесяти девяти $future_hour_std"],
    2: ["две минуты $future_hour", "$current_hour $declension две минуты"],
    3: ["три минуты $future_hour", "$current_hour $declension три минуты"],
    4: ["четыре минуты $future_hour", "$current_hour $declension четыре минуты"],
    5: ["пять минут $future_hour", "$current_hour $declension пять минут"],
    6: ["шесть минут $future_hour", "$current_hour $declension шесть минут"],
    7: ["семь минут $future_hour", "$current_hour $declension семь минут"],
    8: ["восемь минут $future_hour", "$current_hour $declension восемь минут"],
    9: ["девять минут $future_hour", "$current_hour $declension девять минут"],
    10: ["десять минут $future_hour", "$current_hour $declension десять минут", "$current_hour десять"],
    11: ["одиннадцать минут $future_hour", "$current_hour $declension одиннадцать минут"],
    12: ["двенадцать минут $future_hour", "$current_hour $declension двенадцать минут"],
    13: ["тринадцать минут $future_hour", "$current_hour $declension тринадцать минут"],
    14: ["четырнадцать минут $future_hour", "$current_hour $declension четырнадцать минут"],
    15: ["пятнадцать минут $future_hour", "$current_hour $declension пятнадцать минут",
         "четверть $future_hour", "$current_hour с четвертью"],
    16: ["шестнадцать минут $future_hour", "$current_hour $declension шестнадцать минут"],
    17: ["семнадцать минут $future_hour", "$current_hour $declension семнадцать минут"],
    18: ["восемнадцать минут $future_hour", "$current_hour $declension восемнадцать минут"],
    19: ["девятнадцать минут $future_hour", "$current_hour $declension девятнадцать минут"],
    20: ["двадцать минут $future_hour", "$current_hour $declension двадцать минут", "$current_hour двадцать"],
    21: ["двадцать одна минута $future_hour", "$current_hour $declension двадцать одна минута"],
    22: ["двадцать две минуты $future_hour", "$current_hour $declension двадцать две минуты"],
    23: ["двадцать три минуты $future_hour", "$current_hour $declension двадцать три минуты"],
    24: ["двадцать четыре минуты $future_hour", "$current_hour $declension двадцать четыре минуты"],
    25: ["двадцать пять минут $future_hour", "$current_hour $declension двадцать пять минут", "без пять пол $future_hour"],
    26: ["двадцать шесть минут $future_hour", "$current_hour $declension двадцать шесть минут"],
    27: ["двадцать семь минут $future_hour", "$current_hour $declension двадцать семь минут"],
    28: ["двадцать восемь минут $future_hour", "$current_hour $declension двадцать восемь минут"],
    29: ["двадцать девять минут $future_hour", "$current_hour $declension двадцать девять минут"],
    30: ["половина $future_hour", "$current_hour $declension тридцать минут", "$current_hour тридцать"],
    31: ["тридцать одна минута $future_hour", "$current_hour $declension тридцать одна минута"],
    32: ["тридцать две минуты $future_hour", "$current_hour $declension тридцать две минуты"],
    33: ["тридцать три минуты $future_hour", "$current_hour $declension тридцать три минуты"],
    34: ["тридцать четыре минуты $future_hour", "$current_hour $declension тридцать четыре минуты"],
    35: ["тридцать пять минут $future_hour", "$current_hour $declension тридцать пять минут"],
    36: ["тридцать шесть минут $future_hour", "$current_hour $declension тридцать шесть минут"],
    37: ["тридцать семь минут $future_hour", "$current_hour $declension тридцать семь минут"],
    38: ["тридцать восемь минут $future_hour", "$current_hour $declension тридцать восемь минут"],
    39: ["тридцать девять минут $future_hour", "$current_hour $declension тридцать девять минут"],
    40: ["$current_hour $declension сорок минут", "без двадцати $future_hour_std", "$current_hour сорок"],
    41: ["сорок одна минута $future_hour", "$current_hour $declension сорок одна минута"],
    42: ["сорок две минуты $future_hour", "$current_hour $declension сорок две минуты"],
    43: ["сорок три минуты $future_hour", "$current_hour $declension сорок три минуты"],
    44: ["сорок четыре минуты $future_hour", "$current_hour $declension сорок четыре минуты"],
    45: ["$current_hour $declension сорок пять минут", "без пятнадцати $future_hour_std", "$current_hour сорок пять"],
    46: ["сорок шесть минут $future_hour", "$current_hour $declension сорок шесть минут"],
    47: ["сорок семь минут $future_hour", "$current_hour $declension сорок семь минут"],
    48: ["сорок восемь минут $future_hour", "$current_hour $declension сорок восемь минут"],
    49: ["сорок девять минут $future_hour", "$current_hour $declension сорок девять минут"],
    50: ["пятьдесят минут $future_hour", "без десяти $future_hour_std", "$current_hour $declension пятьдесят минут"],
    51: ["пятьдесят одна минута $future_hour", "$current_hour $declension пятьдесят одна минута"],
    52: ["пятьдесят две минуты $future_hour", "$current_hour $declension пятьдесят две минуты"],
    53: ["пятьдесят три минуты $future_hour", "$current_hour $declension пятьдесят три минуты"],
    54: ["пятьдесят четыре минуты $future_hour", "$current_hour $declension пятьдесят четыре минуты"],
    55: ["$current_hour $declension пятьдесят пять минут", "без пяти $future_hour_std", "$current_hour сорок пять"],
    56: ["пятьдесят шесть минут $future_hour", "$current_hour $declension пятьдесят шесть минут"],
    57: ["пятьдесят семь минут $future_hour", "$current_hour $declension пятьдесят семь минут"],
    58: ["пятьдесят восемь минут $future_hour", "$current_hour $declension пятьдесят восемь минут"],
    59: ["пятьдесят девять минут $future_hour", "$current_hour $declension пятьдесят девять минут",
         "без минуты $future_hour_std"]
}
