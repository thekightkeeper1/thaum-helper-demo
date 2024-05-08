ESSEN_DATA = "essentia.json"


import json


def getEssentiaList():
    with open(ESSEN_DATA) as fp:
        essentialList = json.load(fp)
    return essentialList

def saveAspectList(aspectGraph):
    aspectList = []
    for aspectName in aspectGraph.getAspectList():
        aspect = aspectGraph.searchAspect(aspectName)
        jsonAspect = {
            "name": aspect.name,
            "components": aspect.components,
            "combos": [],
            "tier": aspect.tier
        }
        for combo in aspect.combos:
            jsonCombo = {
                "reactant": combo.reactant,
                "product": combo.product
            }
            jsonAspect["combos"].append((jsonCombo))
        aspectList.append(jsonAspect)

    with open(ESSEN_DATA, "w") as fp:
        json.dump(aspectList, fp, indent=3)

    print("Hopefully successful")
