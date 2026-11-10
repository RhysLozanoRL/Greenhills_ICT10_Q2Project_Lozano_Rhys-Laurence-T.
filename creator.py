# About the creator
from pyscript import display, document # pyright: ignore[reportMissingImports]

# Creates a dictionary of things about me such as my name, hobbies, and etc
creator = {
    "Name": "Rhys Laurence T. Lozano",
    "Nickname": "Kuch",
    "Grade & Section": "10 - Topaz",
    "Hobbies": "Reading, Writing",
    "Dreams": "To work in law",
    "Favourite Game" : "Persona 5",
    "Favourite Book" : "Human Acts by Han Kang"
 }

def show_creator(e):
    document.getElementById("output").innerHTML = ""
# Displays each key and value
    display(f"Name: {creator['Name']}", target="output")
    display(f"Nickname: {creator['Nickname']}", target="output")
    display(f"Grade & Section: {creator['Grade & Section']}", target="output")
    display(f"Hobbies: {creator['Hobbies']}", target="output")
    display(f"Dreams: {creator['Dreams']}", target="output")
    display(f"Favourite Game: {creator['Favourite Game']}", target="output")
    display(f"Favourite Book: {creator['Favourite Book']}", target="output")