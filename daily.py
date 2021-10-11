import pandas as pd

def get_quantity_sales():  #filtert die Anzahl der versandten Artikel (eventuell etwas umständlich, aber funktioniert)
    df = pd.read_excel("Del_today_28.08.2021-4_35_20.xlsx")
    dff = df.dropna(subset=['ColorName'])
    quantity_textiles = dff.Quantity.sum()
    newdf = df[(df.ItemNo == '1111000000')]
    katalog = newdf.drop(['DelDate', 'Description', 'ColorName', 'SizeName', 'StorageBin', 'HL', 'Weight', 'IpB', 'ItemNo'],axis=1)
    quantity_catalog = katalog['Quantity'].values[0]
    quantitySum = quantity_textiles+quantity_catalog
    return quantitySum