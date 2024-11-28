import requests
# Best test comment ¯\_(ツ)_/¯
def get_weather():    
    x = requests.get('https://wttr.in/')
    print(x)

if __name__ == "__main__":    
    get_weather()

