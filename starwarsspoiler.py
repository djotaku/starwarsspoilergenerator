#!/usr/bin/python3

import random

new_villain = ["Kyle Ren", "Malloc", "Darth Sebelius", "Theranos", "Lord Juul"]

new_friend = ["Kim Spacemeasurer", "Teen Yoda", "Dab Tweetdeck",
              "Yaz Progestin", "Ti-83"]

lightsaber_color = ["Beige", "Ochre", "Mauve", "Aquamarine", "Taupe"]

super_weapon = ["Sun Obliterator", "Moonsquisher", "World Eater",
                "Planet Zester", "Superconducting Supercollider"]

weapon_capability = ["Blowing up a planet with a bunch of beams of energy that combine into one",
                     "Blowing up a bunch of planets with one beam of energy that splits into many",
                     "Cutting a planet in half and smashing the halves together like cymbals",
                     "Increasing the CO2 levels in a planet's atmosphere, causing rapid heating",
                     "Triggering the end credits before the movie is done"]

enemy = ["Boba Fett", "Salacious Crumb", "The Space Slug", "The Bottoms Half of Dath Maul",
         "Youtube Commenters"]

battle_details = ["A bow that shoots little lightsaber-headed arrows",
                  "X-Wings and tie fighters dodging the giant letters of the opening crawl",
                  "A Sith Educational Display that uses force lightning to demonstrate the dielectric breakdown of air",
                  "Kylo Ren Putting on another helmet over his smaller one",
                  "A Sith car wash where the bristles on the brushes are little lightsabers"]

parent1 = ["Luke", "Leia", "Han", "Obi-Wan", "A Random Junk Trader"]

parent2 = ["Poe", "BB-8", "Amylyn Holdo", "Laura Dern", "A Random Junk Trader", 
           "That one droid Jawa Sandcrawler that says Gonk"]

# randomize

random_villain = random.choice(new_villain)
random_friend = random.choice(new_friend)
random_lightsaber_color = random.choice(lightsaber_color)
random_super_weapon = random.choice(super_weapon)
random_weapon_capability = random.choice(weapon_capability)
random_enemy = random.choice(enemy)
random_battle_details = random.choice(battle_details)
random_parent1 = random.choice(parent1)
random_parent2 = random.choice(parent2)

# Website stuff

print("Content-type: text/html\n\n")

print("<h1>Star Wars Spoiler Generator</h1> Based on <a href='https://xkcd.com/2243/'>this</a> XKCD Comic. Refresh the page to get a new version!<p>")

print(f"In this Star Wars movie, our heroes return to take on the first order and new villain, <b>{random_villain}</b>, with help from their new friend, <b>{random_friend}</b>. Rey builds a new lightsaber with a <b>{random_lightsaber_color}</b> blade, and they head out to confront the first order's new superweapon, the <b>{random_super_weapon}</b>, a space station capable of <b>{random_weapon_capability}</b>. They unexpected join forces with their old enemy, <b>{random_enemy}</b>, and destroy the superweapon in a battle featuring <b>{random_battle_details}</b>. <p>P.S.: Rey's parents are <b>{random_parent1}</b> and <b>{random_parent2}</b>")

print("<p> Get the source code <a href='https://github.com/djotaku/starwarsspoilergenerator'>here</a>.")
