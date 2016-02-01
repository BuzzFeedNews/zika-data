#!/usr/bin/env python
import pdfplumber
import pdfplumber.utils
import pandas as pd
from collections import OrderedDict

def get_column(chars, x_start, x_end, dtype):
    return chars[
        (chars["x0"] >= x_start) &
        (chars["x0"] < x_end)
    ].groupby("doctop")\
        .apply(pdfplumber.utils.collate_chars)\
        .str.strip()\
        .astype(dtype)\
        .values

def parse(pdf):
    chars = pd.DataFrame(pdf.chars)

    data_chars = chars[
        (chars["fontname"] == "QURFPK+ArialNarrow")
    ].sort_values(["doctop", "x0"])

    counts = pd.DataFrame(OrderedDict([
        ("region", get_column(data_chars, 0, 200, str)),
        ("samples_received", get_column(data_chars, 200, 283, int)),
        ("samples_testable", get_column(data_chars, 283, 366, int)),
        ("samples_tested", get_column(data_chars, 366, 452, int)),
        ("samples_in_progress", get_column(data_chars, 452, 512, int)),
    ]))

    return counts

if __name__ == "__main__":
    import sys
    if hasattr(sys.stdin, "buffer"):
        buf = sys.stdin.buffer
    else:
        buf = sys.stdin
    pdf = pdfplumber.load(buf)
    data = parse(pdf)
    data.to_csv(sys.stdout, index=False, encoding="utf-8")
    
