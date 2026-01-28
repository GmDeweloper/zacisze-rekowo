import pandas as pd
from datetime import date

INPUT = "ZACISZE_REKOWO_ceny.csv"
OUTPUT = "ceny.csv"

df = pd.read_csv(INPUT, sep=";", encoding="utf-8-sig")

# cena obowiązuje od wejścia obowiązku
df["price_valid_from"] = "2025-07-11"

# codziennie aktualna data wygenerowania pliku
df["last_update"] = date.today().isoformat()

df.to_csv(OUTPUT, sep=";", index=False, encoding="utf-8-sig", float_format="%.2f")
print("OK wygenerowano:", OUTPUT)
