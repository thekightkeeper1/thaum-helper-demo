PRIMALS = ["ignis",
           "aqua",
           "terra",
           "ordo",
           "perditio",
           "aer"]


def print_formatted_data(column_width, *strings):
    # Calculate the number of columns
    num_columns = len(strings)

    # Calculate the number of rows required to print all strings
    max_length = max(len(s) for s in strings)
    num_rows = (max_length + column_width - 1) // column_width

    # Print the data
    for row in range(num_rows):
        row_data = []
        for col in range(num_columns):
            start_index = row * column_width
            end_index = min((row + 1) * column_width, len(strings[col]))
            cell_data = strings[col][start_index:end_index]
            cell_data = cell_data.ljust(column_width)  # Pad with spaces if necessary
            row_data.append(cell_data)
        print('| ' + ' | '.join(row_data) + ' |')


class Aspect:

    def __init__(self, name, components, combos, tier):
        self.name = name
        self.components = components
        self.combos = []
        for pair in combos:
            self.addCombo(pair["reactant"], pair["product"])
        self.tier = tier

    def isPrimal(self):
        if self.name in PRIMALS:
            return True
        return False

    def addCombo(self, reactant, product):
        self.combos.append(Combo(self.name, reactant, product))

    def getProductNames(self):
        names = list()
        for trio in self.combos:
            names.append(trio.product)
        return names

    def getReactantNames(self):
        names = list()
        for e in self.combos:
            if e.product != "":
                names.append(e.reactant)
        return names

    def getNoProductReactantNames(self):
        names = list()
        for e in self.combos:
            names.append(e.reactant)
        return names

    def display(self):
        name = str(self.name)
        components = "primal" if self.isPrimal() else f"{self.components[0]} + {self.components[1]}"
        products = filter(lambda s: s != "", self.getProductNames())
        products = ", ".join(products)
        combinesWith = ", ".join(self.getReactantNames())
        print_formatted_data(
            20,
            name,
            components,
            products,
            combinesWith,
        )


class Combo:
    def __init__(self, base, reactant, product):
        self.base = base
        self.reactant = reactant
        self.product = product


class EssentiaGraph:

    def __init__(self):
        self.essentiaLibrary = {}

    def calcTier(self, components):
        tier1 = self.essentiaLibrary[components[0]].tier
        tier2 = self.essentiaLibrary[components[1]].tier
        return tier1 + 1 if tier1 > tier2 else tier2 + 1

    def  addAspect(self, name, components, combos, tier):
        if tier == -1:
            tier = self.calcTier(components)
        e = Aspect(name, components, combos, tier)
        self.essentiaLibrary[name] = e

    def addCombo(self, baseName, reactant, product):
        aspects = self.essentiaLibrary.keys()
        if (reactant not in aspects):
            print("Can not use an aspect that does not exist in a combo")
            print(reactant)
        if( product not in aspects and product != ""):
            print("Can not use an aspect that does not exist in a combo")
            print(product)
        self.essentiaLibrary[baseName].addCombo(reactant, product)
        self.essentiaLibrary[reactant].addCombo(baseName, product)

    def getCopy(self):
        return self.essentiaLibrary.copy()

    def searchAspect(self, aspectName):
        return self.essentiaLibrary[aspectName]

    def getAspectList(self):
        return list(self.essentiaLibrary.keys())

    def getUntestedReactantNames(self, baseName):

        if baseName not in self.essentiaLibrary.keys():
            print("Base aspect does not exist")
            return []

        baseAspect = self.essentiaLibrary[baseName]
        testedReactants = baseAspect.getNoProductReactantNames()
        untestedReactants = []
        for aspect in self.essentiaLibrary.keys():
            if aspect in testedReactants:
                pass
            else:
                untestedReactants.append(aspect)

        return untestedReactants

    def getAllUntestedReactants(self):  # Gets ALL combos which have not been tested

        reactants = {}
        aspectNames = list(self.essentiaLibrary.keys())

        for i in range(len(aspectNames)):
            baseAspect = self.essentiaLibrary[aspectNames[i]]
            testedReactants = baseAspect.getReactantNames()
            reactants[baseAspect.name] = []

            # Iterating from i+1 for the reactant
            for j in range(i + 1, len(aspectNames)):
                secondEssentia = self.essentiaLibrary[aspectNames[j]]

                # Checks if item 2 is in item 1's checked list
                if secondEssentia.name in testedReactants:
                    pass
                else:
                    reactants[baseAspect.name].append(secondEssentia.name)
        return reactants

    def display(self):
        for k in self.essentiaLibrary.keys():
            essentia = self.essentiaLibrary[k]
            essentia.display()
