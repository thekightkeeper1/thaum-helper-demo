from EssentiaLoader import *
from EssentiaResearch import EssentiaGraph
import MenuCommands as Menu

ESSEN_PROPS = ["name", "components", "products", "tier"]


def loadEssentiaGraph():
    essentiaGraph = EssentiaGraph()
    aspects = getEssentiaList()

    for e in aspects:
        essentiaGraph.addAspect(
            e["name"],
            e["components"],
            e["combos"],
            e["tier"]
        )

    return essentiaGraph


def loop(aspectGraph):
    menu = """
    combos [aspect] [-u]
    display [aspect]
    exit
    """
    while True:

        cmdline = input()
        if cmdline == "help":
            print(menu)

        arguments = cmdline.split()
        if (len(arguments) < 1):
            continue

        token = arguments.pop(0)
        if token == "combos":
            Menu.combos(aspectGraph, arguments)
        elif token == "display":
            Menu.display(aspectGraph, arguments)
        elif token == "exit":
            break


def main():
    researchTable = loadEssentiaGraph()
    # researchTable.display()
    # print(researchTable.getAllUntriedCombos()
    loop(researchTable)
    saveAspectList(researchTable)


if __name__  == "__main__":
     main()
