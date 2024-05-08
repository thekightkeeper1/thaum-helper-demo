def combos(aspectGraph, tokens):

    update = False
    baseAspect = ""
    while (len(tokens) > 0):

        tkn = tokens.pop(0)
        if tkn == "-u":
            update = True
        else:
            baseAspect = tkn

    if baseAspect == "" and not update:
        print("Did not specify a base aspect, showing all")
        print(aspectGraph.getAllUntestedReactants())
        return

    if update and baseAspect == "":
        print("Did not specify a base aspect, testing all")
        print("not implemented")
        return
    untested = aspectGraph.getUntestedReactantNames(baseAspect)
    print(untested)

    if update:
        print("Enter nothing if the result is unknown, 1 for no result, or the product reactantName")
        for reactantName in untested:
            print(f"{baseAspect} + {reactantName} = ?")

            product = input()
            if product == "":  # Basically just skipping this reactant
                continue
            if product == "1":
                product = ""

            else:
                aspectGraph.addAspect(
                    name = product,
                    components = (baseAspect, reactantName),
                    combos = [],
                    tier = -1
                )
            aspectGraph.addCombo(baseAspect, reactantName, product)

        print("Finished Updating")

def display(aspectGraph, tokens):

    if (len(tokens) > 0):
        aspectName = tokens.pop(0)
        aspectGraph.getAspect(aspectName).display()

    else :
        aspectGraph.display()



