from fuzzywuzzy import fuzz

def fuzzy_match(ingredient, ingredient_list):
    best_match = None
    highest_score = 0
    for item in ingredient_list:
        score = fuzz.ratio(ingredient.lower(), item.lower())
        if score > highest_score:
            highest_score = score
            best_match = item
    return best_match

print(fuzzy_match("apple", ["honeycrisp aples", "orange", "watermelon", "pomme"]))
print(fuzzy_match("cornstarch", ["F�cule de ma�s", "potato starch"]))