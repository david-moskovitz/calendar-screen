import csv
from luach.models import MyDate

def run():
    dates = open('scripts/dates_bbb.csv', encoding="utf8")
    reader = csv.reader(dates)

    for row in reader:
        

        d, created = MyDate.objects.get_or_create(english_date=row[0],hebrew_date=row[1],hebrew_year=row[2],sof_zman_1=row[3],sof_zman_2=row[4],sof_zman_tefila=row[5])

        d.save()

        print(row)