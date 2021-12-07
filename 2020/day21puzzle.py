
import copy

class Food():
    def __init__(self, line):
        ingredients = []
        allergens = []
        [ingredients, allergens] = line.split(" (")
        allergens = allergens[9:-1]
        allergens = allergens.split(", ")
        self.allergens = allergens
#        for allergen in allergens:
#            self.allergens += [Allergen(allergen)]
            
        ingredients = ingredients.split(" ")
        self.ingredients = ingredients
#        for ingredient in ingredients:
#            self.ingredients += [Ingredient(ingredient)]
            
        self.allergensNotContained = 0 # this is the good stuff


    def printAll(self):
        print("Ingredients: ",end='')
        for ingredient in self.ingredients:
            print(ingredient,end=' ')
        print(". Allergens: ",end='')
        for allergen in self.allergens:
            print(allergen,end=' ')
        print()


def printAll(things):
    for thing in things:
        print(thing)
    return

def getNonIntersection( foods, allergen ):
    foodsWithAllergen = []
    print("Getting foods which contain",allergen)
    for food in foods:
        if allergen in food.allergens:
            foodsWithAllergen += [food]
            
#    print("They are:")
#    print(foodsWithAllergen)

    ingredientsInFood = []
    for food in foodsWithAllergen:
        for ingredient in food.ingredients:
            if ingredient not in ingredientsInFood:
                ingredientsInFood += [ingredient]
                
##    for food in foodsWithAllergen:
##        for ingredient in food.ingredients:
##            addit = True
##            for anIngredient in ingredientsInFood:
##                if anIngredient.name == ingredient.name:
##                    addit = False
##                    break
##            if(addit):
##                ingredientsInFood += [ingredient]
##    # now ingredients in food is all ingredients in the intersecting foods
#    for ingredient in ingredientsInFood:
#        print(ingredient)

    # need to remove any ingredient from ingredientsInFood which
    # is in all food in foodsWithAllergen
    nonIntersection = copy.deepcopy(ingredientsInFood)
    for ingredient in ingredientsInFood:
        remove = True
        for food in foodsWithAllergen:
            if ingredient not in food.ingredients:
                remove = False
                break
        if(remove):
            nonIntersection.remove(ingredient)

    intersectingIngredients = []
    for ingredient in ingredientsInFood:
        addit = True
        for food in foodsWithAllergen:
            if ingredient not in food.ingredients:
                addit = False
                break
        if(addit):
            intersectingIngredients += [ingredient]
    return intersectingIngredients

        
#    print("Non intersecting ingredients:")
#    for ingredient in nonIntersection:
#        print(ingredient)
    return nonIntersection


def notOver( alls ):
    for allergen in alls.keys():
        if len(alls[allergen]) != 1:
            return True
    return False


f = open("day21.txt")
data = f.readlines()
data = [line.strip() for line in data]

foods = []
for line in data:
    foods += [Food(line)]

#for food in foods:
#    food.printAll()

allIngredients = []
for food in foods:
    for ingredient in food.ingredients:
        if ingredient not in allIngredients:
            allIngredients += [ingredient]
            
allAllergens = []
for food in foods:
    for allergen in food.allergens:
        if allergen not in allAllergens:
            allAllergens += [allergen]


#print("All ingredients:")
#printAll(allIngredients)

#print()
#print("All allergens:")
#printAll(allAllergens)


alls = {}
for allergen in allAllergens:
#    print()
#    print("For allergen",allergen,"the following ingredients intersect all foods with it")
    nonIntersection = getNonIntersection( foods, allergen )
#    print(nonIntersection)
    alls[allergen] = nonIntersection
##    for ingredient in nonIntersection:
##        allIngredients[ingredient] += 1
    

print("done")
print(alls)


while notOver(alls):
    for allergen in alls.keys():
        if len(alls[allergen]) == 1:
            removal = alls[allergen][0]
#            print("Value to remove:",removal)
            for otherAllergen in alls.keys():
                if allergen == otherAllergen:
#                    print(allergen,"==",otherAllergen)
#                    print("NOT removing the ingredient")
                    continue
                else:
#                    print(allergen,"!=",otherAllergen)
                    if removal in alls[otherAllergen]:
#                        print("Removing the ingredient")
                        alls[otherAllergen].remove(removal)
    print(alls)

for allergen in alls.keys():
    allIngredients.remove(alls[allergen][0])

#print(allIngredients)

total = 0
for ingredient in allIngredients:
    for food in foods:
        if ingredient in food.ingredients:
            total += 1
print(total)

#print(alls)
allergens = []
for allergen in alls.keys():
    allergens += [allergen]

#print(allergens)
allergens.sort()
#print(allergens)

final = []
for allergen in allergens:
    final += alls[allergen]
#print(final)

output = ','.join(final)
print(output)
