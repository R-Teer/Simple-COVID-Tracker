import json
import requests

print("--------------------------------------------")
print("COVID WORLD TRACKER")
print("You can use this tool to generate automatic statistics for COVID-19 infected countries")
print("--------------------------------------------")

def covidstat():
    countryinput = input("Enter Country Name : ")
    url = "https://covid-19-data.p.rapidapi.com/country"
    querystring = {"format":"json","name":countryinput}
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "e27441159cmsh60575a0ae0011c1p19e664jsn0c2d2894f5ac"
         }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print("--------------------------------------------")
    print("analysing data...")
    print("--------------------------------------------")


    data = json.loads(response.text)
    for cou in data:
        print("Name of Country: " + (cou['country']))
        print(str(cou['confirmed']) + (" Total Cases"))
        print("Number of recoveries: " + (str(cou['recovered'])))
        print("Number of critical patients: " + (str(cou['critical'])))
        print("Number of fatalities: " + (str(cou['deaths'])))
        print("--------------------------------------------")
        restart = input("Would you like to restart this program?")
        if restart == "yes" or restart == "y":
            print("--------------------------------------------")
            print("Restarting Application")
            print("--------------------------------------------")
            covidstat()
        if restart == "no" or restart == "n":
            print("--------------------------------------------")
            print ("Application terminating. Goodbye.")

covidstat()
print("--------------------------------------------")
print ("Thank You For Using")



