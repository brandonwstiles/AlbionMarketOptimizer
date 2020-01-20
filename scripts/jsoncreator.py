import re
import json

itemFile = open("../txt/items.txt", "r")
jsonFile = open("../json/itemList.json", "w")
itemList = {'items': []}
lines = itemFile.readlines()

for line in lines:
    line = line.replace(' ', '')
    line = line.replace(':', ' ')

    values = line.split()

    itemID = values[0]
    itemName = values[1]
    try:
        itemDesc = re.sub(r"(\w)([A-Z])", r"\1 \2", values[2])
    except IndexError:
        itemDesc = itemName

    listItem = {
        "name": itemName,
        "itemID": itemID,
        "description": itemDesc
                }

    itemList['items'].append(listItem)

json.dump(itemList, jsonFile)

itemFile.close()
jsonFile.close()
