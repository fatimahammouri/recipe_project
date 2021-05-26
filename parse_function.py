"""creat a helping function parse the complex API response 
    then forms a simpler dictionary of only the data needed 
    from the API response"""

def parse_api_results(complex_results):

    recipe_details = {}
    ingredients = []

    recipe_details['title'] = complex_results['title']
    recipe_details['image'] = complex_results['image']
    recipe_details['servings'] = complex_results['servings']
    recipe_details['readyInMinutes'] = complex_results['readyInMinutes']
    recipe_details['sourceUrl'] = complex_results['sourceUrl']
    # recipe_details['instructions'] = complex_results['instructions']..we need a different way to get the steps
    
    for each_step in complex_results['analyzedInstructions'][0]['steps']:
        instructions = each_step['step']
    recipe_details['instructions'] = instructions

    
    for each_ingredient in complex_results["extendedIngredients"]:
        ingredient = each_ingredient["originalString"]
        ingredients.append(ingredient)
    # print(ingredients)   
    recipe_details["ingredients"] = ingredients

    return recipe_details