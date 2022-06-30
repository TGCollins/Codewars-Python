def cakes(recipe, available):
    if(set(recipe).issubset(set(available))):
        proportion = []
        for ingredient in recipe:   
            proportion.append(available[ingredient]//recipe[ingredient])
        return min(proportion)
    else:
        return 0
