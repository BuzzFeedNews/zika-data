#!/usr/bin/env python
import pdfplumber
import pdfplumber.utils
import pandas as pd

DEPT_FIXES = {
    "N. DE SANTANDER": "NORTE SANTANDER",
    "SANTA MARTA": "STA MARTA D.E.",
    "LA GUAJIRA": "GUAJIRA",
    "VALLE": "VALLE DEL CAUCA",
}

MUNI_FIXES = {
    "CHACHAGSI": "CHACHAGUI",
    "GSICAN": "GUICAN",
    "TOGSI": "TOGUÍ",
    "SAN MIGUEL (LA DORADA)": "SAN MIGUEL"
}

INT_COLS = [
    "zika_confirmed_laboratory",
    "zika_confirmed_clinic",
    "zika_suspected",
    "zika_total"
]

COLUMNS = [
    "department",
    "municipality"
] + INT_COLS

def parse(pdf):
    chars = pd.DataFrame(pdf.chars)

    data_chars = chars[
        ((chars["fontname"] == "ABCDEE+Calibri") &
        (chars["size"] == 6)) |
        ((chars["fontname"] == "Arial") &
        (chars["size"] == 5.628))
    ].copy()

    data = pdfplumber.utils.extract_columns(data_chars, x_tolerance=1, y_tolerance=1)

    if len(data.columns) == 6:
        data.columns = COLUMNS
    else:
        data.columns = [ "sivigila_code" ] + COLUMNS
    data = data.drop_duplicates().reset_index(drop=True)
    data[INT_COLS] = data[INT_COLS].astype(int)
    data["department"] = data["department"].str.strip().str.upper().apply(lambda x: DEPT_FIXES.get(x, x))
    data["sivigila_code"] = data["sivigila_code"].str.strip()
    data["municipality"] = data["municipality"].str.strip().str.upper().apply(lambda x: MUNI_FIXES.get(x, x))

    sums = data[INT_COLS].sum(axis=1)
    equalities = (sums == (data["zika_total"] * 2)).unique().tolist()
    assert(equalities == [ True ])
    return data

if __name__ == "__main__":
    import sys
    if hasattr(sys.stdin, "buffer"):
        buf = sys.stdin.buffer
    else:
        buf = sys.stdin
    pdf = pdfplumber.load(buf)
    data = parse(pdf)
    data.to_csv(sys.stdout, index=False, encoding="utf-8")
    
