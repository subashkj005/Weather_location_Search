import json         
  
from random import uniform, randint
from faker import Faker      
  
fake = Faker()  


description = ["Clear Sky", "Rainy", "Cloudy", "Sunny", "Storm"]
    
def input_data(x):  
    
    weather_data = []  
    idx = 0 
    while idx != x:
        city_name = fake.city() 
        if city_name not in weather_data:
            data={}  
            data['location']= city_name
            data['timestamp']= "2022-01-01T00:00:00Z"
            data['temperature']= str(round(uniform(10, 85), 1) ) 
            data['humidity']= str(round(uniform(10, 85), 1) )   
            data['description']= description[randint(0, len(description)-1)]
            weather_data.append(data)
            idx += 1
            
    with open('./weather_data.txt', 'w') as fp:  
        json.dump(weather_data, fp) 
     
    return True
    
