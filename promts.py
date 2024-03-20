"""
promt.py generates the user promts for the message varibles
author @sabber1
"""

def generateEnglish(item_name, item_attr1, item_attr2, length, item_material):
    length_tmp = "50 word"
    if length == "medium":
        length_tmp = "150 word"

    content = f"Create a {length_tmp} item description for a {item_name} with these atributes: {item_attr1}, {item_attr2}. "
    if (item_material != ""):
        content += f"The {item_name} is made out of {item_material}."

    return content

def generateHungarian(item_name, item_attr1, item_attr2, length, item_material):
    length_tmp = "50"
    if length == "medium":
        length_tmp = "150"

    content = f"Készíts egy {length_tmp} szavas cikk leírást a(z) {item_name} nevű termékről, ezekkel a tulajdonságokkal: {item_attr1}, {item_attr2}. "
    if (item_material != ""):
        content += f"A(z) {item_name} anyaga: {item_material}."

    return content