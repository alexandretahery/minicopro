import os
import sys
import csv
import django
from datetime import datetime

def safe_float(value):
    try:
        return float(value)
    except:
        return None

def get_django_settings():
    print("Setting up Django environment...")
    root_dir = os.path.dirname(os.path.dirname(__file__))
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if dirpath not in sys.path:
            sys.path.append(dirpath)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()

def read_csv_and_import_data(path):
    from MiniCopro.models import Annonce
    with open(path, newline='', encoding="utf-8", errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                Annonce.objects.create(
                    dept_code=row["DEPT_CODE"],
                    zip_code=row["ZIP_CODE"],
                    city=row["CITY"],
                    condominium_expenses=safe_float(row["CONDOMINIUM_EXPENSES"]),
                )
            except Exception as e:
                print(f"Erreur ligne ignorée : {e}")

def main():
    get_django_settings()
    read_csv_and_import_data("scripts/data.csv")

if __name__ == "__main__":
    main()





