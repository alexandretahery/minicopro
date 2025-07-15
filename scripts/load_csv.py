import os
import sys
import csv
import django
from datetime import datetime


def parse_bool(value):
    return value.lower() == "true" if isinstance(value, str) else None

def safe_float(value):
    try:
        return float(value)
    except:
        return None

def safe_int(value):
    try:
        return int(value)
    except:
        return None

def safe_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except:
        return None


def get_django_settings():
    print("Setting up Django environment...")
    # Set current folder as the working directory
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
                    ad_urls=row["AD_URLS"],
                    property_type=row["PROPERTY_TYPE"],
                    dept_code=row["DEPT_CODE"],
                    zip_code=row["ZIP_CODE"],
                    city=row["CITY"],
                    insee_code=row["INSEE_CODE"],
                    latitude=safe_float(row["LATITUDE"]),
                    longitude=safe_float(row["LONGITUDE"]),
                    blur_radius=safe_float(row["BLUR_RADIUS"]),
                    marketing_type=row["MARKETING_TYPE"],
                    price=safe_float(row["PRICE"]),
                    description=row["DESCRIPTION"],
                    surface=safe_float(row["SURFACE"]),
                    condominium_expenses=safe_float(row["CONDOMINIUM_EXPENSES"]),
                    caretaker=parse_bool(row["CARETAKER"]),
                    heating_mode=row["HEATING_MODE"],
                    water_heating_mode=row["WATER_HEATING_MODE"],
                    elevator=parse_bool(row["ELEVATOR"]),
                    floor=safe_int(row["FLOOR"]),
                    floor_count=safe_int(row["FLOOR_COUNT"]),
                    lot_count=safe_int(row["LOT_COUNT"]),
                    construction_year=safe_int(row["CONSTRUCTION_YEAR"]),
                    building_type=row["BUILDING_TYPE"],
                    parking=parse_bool(row["PARKING"]),
                    parking_count=safe_int(row["PARKING_COUNT"]),
                    terrace=parse_bool(row["TERRACE"]),
                    terrace_surface=safe_float(row["TERRACE_SURFACE"]),
                    swimming_pool=parse_bool(row["SWIMMING_POOL"]),
                    garden=parse_bool(row["GARDEN"]),
                    standing=row["STANDING"],
                    new_build=parse_bool(row["NEW_BUILD"]),
                    small_building=parse_bool(row["SMALL_BUILDING"]),
                    corner_building=parse_bool(row["CORNER_BUILDING"]),
                    publication_start_date=safe_date(row["PUBLICATION_START_DATE"]),
                    dealer_name=row["DEALER_NAME"],
                    dealer_type=row["DEALER_TYPE"],
                    reference_number=row["REFERENCE_NUMBER"],
                    energy_classification=row["ENERGY_CLASSIFICATION"]
                )
            except Exception as e:
                print(f"Erreur ligne ignorée : {e}")

def main():
    get_django_settings()
    read_csv_and_import_data("scripts/split_1 - Copie.csv")

if __name__ == "__main__":
    main()





