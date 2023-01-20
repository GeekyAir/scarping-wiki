from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
import pandas as pd
import os


def get_excel_data_or_none(path):
    try:
        excel_data = pd.read_excel(path)
        excel_data = excel_data.fillna(value="Empty")
        records = excel_data.to_dict("index")
        keys = [key for key in records][1:]

        for key in keys:
            records[key]["index"] = key
            records[key]["details"] = reverse_lazy("api:ExcelDetailAPIView", args=[key])

        excel_data = records
        return excel_data

    except Exception as e:
        print(e)
        excel_data = None
        return excel_data


def search_value_in_column(ws, search_string, column="A"):
    row_index = ''
    for row in range(1, ws.max_row + 1):
        coordinate = "{}{}".format(column, row)
        if ws[coordinate].value == search_string:
            row_index = row
            return row_index
            # return column, row
    return None
    # return column, None






