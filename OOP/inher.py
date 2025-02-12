# Inheritance: Creating new classes(sub classes/derived classes) based on base/super

class Country:
    def __init__(self, continent, currency, is_landlocked,):
        self.continent = continent
        self.currency = currency
        self.is_landlocked = is_landlocked


class CountryProfile(Country):

    def __init__(self, continent, currency, is_landlocked, current_population):
        super().__init__(continent, currency, is_landlocked)
        self.current_population = current_population

    def __str__(self):
        return f'Continent: {self.continent}, Currency: {self.currency}, Landlocked: {self.is_landlocked}, Population: {self.current_population}'


kenya = CountryProfile("Africa", "KSH", "Yes", 90000)
usa = CountryProfile("North America", "USD", "Yes", 1000000)

print(kenya.__dict__)
print(usa.__dict__)
