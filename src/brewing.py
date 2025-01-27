import csv

from object_factory import HTML


def create_brewing():
    brewing_tab = HTML(
        "div",
        None,
        {
            "id": "brewing",
            "class": "canvas",
            "hidden": True,
        },
    )

    with open("./config/brewing_imgs_coords.csv", encoding="utf-8") as csv_file:
        reader = csv.DictReader(
            csv_file,
            delimiter=";",
        )

        elements = [
            {key.strip(): value.strip() for key, value in row.items() if value.strip()}
            for row in reader
        ]

    for element in elements:
        HTML(
            element["tag"],
            brewing_tab.element,
            element,
        )
