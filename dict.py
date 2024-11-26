# START
israel_data: dict[str, object] = {"Name": "Israel", "Birth": 1948, "Population_millions": 9.3, "Capital": "Jerusalem",
                                  "Language": "Hebrew",
                                  "cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva",
                                             "Ashdod"], "Currency": "ILS",
                                  "Area_kilometer": 22_145, "gdp_billion": 450}
print(israel_data.get("Capital"))
print(israel_data.keys())
print(israel_data.values())
print(israel_data.items())
copy_dict = israel_data.copy()
copy_dict.pop("gdp_billion")
print(copy_dict)
dict_data = dict.fromkeys(israel_data.keys())
print(dict_data)
dict_data["Name"] = input("Enter the name of the country: ")
dict_data["Birth"] = input("Enter the country's birth year: ")
dict_data["Population_millions"] = input("Enter the country's population in millions: ")
dict_data["Capital"] = input("Enter the country's capital city: ")
dict_data["Language"] = input("Enter the country's official language: ")
dict_data["cities"]: list[str] = input("Enter three cities in your country using a comma: ").split(",")
dict_data["currency"] = input("Enter the country's currency: ")
dict_data["Area_kilometer"] = input("Enter the country's area kilometer: ")
dict_data["gdp_billion"] = input("Enter the country's gdp in billions: ")

print(dict_data)
