import os 
import crud 
import model
import server
import requests 

os.system('dropdb recipe')
os.system('createdb recipe')

model.connect_to_db(server.app)
model.db.create_all()

cuisines_list = ['american', 'african', 'caribbean', 'chinese', 
                 'cajun', 'european', 'greek', 'indian',
                'italian', 'japanese', 'korean', 'latin american',
                'middle eastern', 'mexican', 
                'spanish', 'thai', 'vietnamese'] 

for cuisine in cuisines_list:
    cuisine = crud.create_cuisine(cuisine)

##########################################################################



