# Seatwork 1: Nickname Atlas
from pyscript import display, document

def get_nickname(e):
    document.getElementById('output').innerHTML = " " # Clears previous answer

    # Set variables: countries and their corresponding nicknames
    country_nicknames = {
        "germany": "The Land of Poets and Thinkers",
        "france": "The Hexagon",
        "switzerland": "The Land of Milk and Honey",
        "belgium": "The Battlefield of Europe",
        "netherlands": "The Low Countries",
        "austria": "The Land of Beauty and Music",
        "luxembourg": "The Grand Duchy",
        "monaco": "The Billionaire's Playground",
        "liechtenstein": "The Principality"
    }

    country = document.getElementById('country_input').value.lower()

    # Looks up nickname; Default message if not available
    nicknames = country_nicknames.get(country, "Sorry, can't seem to find a nickname for that country. Please try again!")

    display(f"Nickname: {nicknames}", target='output')