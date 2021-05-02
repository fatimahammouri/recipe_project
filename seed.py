import os 
import crud 
import model
import server
import requests 

os.system('dropdb recipe')
os.system('createdb recipe')


cuisines_list = ['american', 'african', 'caribbean', 'chinese', 
                'european', 'cajun', 'french', 'greek', 'indian',
                'italian', 'mediterranean', 'mexican', 'thai'] 

for cuisine in cuisines_list:
    cuisine = crud.create_cuisine(cuisine)



