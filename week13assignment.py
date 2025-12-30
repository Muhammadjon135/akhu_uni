import requests
asking = input("Enter a country name: ")

def get_country_data(country_name):
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country_name.lower()}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("Error: Country not found.")
            return None
        else:
            print(f"Server Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException:
        print("Error: Could not connect to the internet.")
        return None

def write_country_info(data):

    with open("country_description.txt", "w",  encoding="utf-8") as f:
        f.write(f"\nFull information about => {data[0]["name"]["common"]}\n")
        f.write("="*40)
            
        f.write("\n\n[ BASIC INFORMATION ]\n")
        f.write(f"Capital: {data[0]['capital'][0]}\n")
        population = str(data[0]['population'])
        parts = []
        while population:
            parts.insert(0, population[-3:])
            population = population[:-3]
        correct_version = ",".join(parts)
        f.write(f"Population: {correct_version}")
            
        f.write("\n\n[ CULTURE ]\n")
        languages = ", ".join(data[0]['languages'].values())
        f.write(f"Language(s) spoken: {languages}\n")
        currency_info = []
        for code, info in data[0]['currencies'].items():
            currency_info.append(f"{info['name']} ({info['symbol']})")
        f.write(f"Used currencies: {", ".join(currency_info)}")


        f.write("\n\n[ GEOGRAPHY ]\n")
        f.write(f"Continent: {data[0]['continents'][0]}\n")
        f.write(f"Subregion: {data[0]['subregion']}\n")
        borders_list = data[0].get("borders", [])
        if not borders_list:
            borders = "Has no bordering countries"
        else:
            borders = ", ".join(borders_list)
        f.write(f"Bordering countries: {borders}")
        

        f.write("\n\n[ TIME & SYMBOLS ]\n")
        f.write(f"Timezones: {data[0]['timezones'][0]}\n")
        f.write(f"Flag description:\n{data[0]['flags']['alt'].replace(". ", ".\n")}\n")
        f.write(f"Flag image: {data[0]['flags']['svg']}")
            
country_data = get_country_data(asking)
if country_data is not None:
    write_country_info(country_data)
