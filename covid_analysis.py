class City:
    def __init__(self,city_id,state_name,city_name,no_of_tests,no_of_postive):
        self.city_id = city_id 
        self.state_name = state_name
        self.city_name = city_name
        self.no_of_tests = no_of_tests
        self.no_of_postive = no_of_postive
 
class PandemicAnalysis :
    def __init__(self,analysis_name,city_list):
        self.analysis_name = analysis_name
        self.city_list =city_list
    def get_citiesMoreThanPercentage(self,percent):
        c =0
        for city in self.city_list:
            percentage = (city.no_of_postive*100)/city.no_of_tests
            if(percentage>=percent):
                print(city.state_name+" "+city.city_name)
                c=1
        if c==0:
            print("No City recorded with the given percentage")
    def get_StateWithMaxPositiveCases(self):
        state_city = {}
        for city in self.city_list:
            if city.state_name not in state_city:
                state_city[city.state_name] = city.no_of_postive
            elif city.state_name in state_city:
                state_city[city.state_name] = state_city.get(city.state_name)+city.no_of_postive
        
        print(max(state_city,key = state_city.get))
        
n= int(input())
cities=[]
for i in range(n):
    city_id = int(input())
    state = input()
    city = input()
    tests = int(input())
    positives = int(input())
    city = City(city_id,state,city,tests,positives)
    cities.append(city)
percent = int(input())
analysis = PandemicAnalysis("test",cities)
analysis.get_citiesMoreThanPercentage(percent)
analysis.get_StateWithMaxPositiveCases()






