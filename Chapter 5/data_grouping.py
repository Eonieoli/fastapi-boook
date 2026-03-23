tuple_thing = ("yeti", "CN", "Himalayas", "Hirsute Himalayan", "Abominable Snowman")
print("Name is", tuple_thing[0])


list_thing = ["yeti", "CN", "Himalayas", "Hirsute Himalayan", "Abominable Snowman"]
print("Name is", list_thing[0])


NAME = 0
COUNTRY = 1
AREA = 2
DESCRIPTION = 3
AKA = 4
touple_thing = ("yeti", "CN", "Himalayas", "Hirsute Himalayan", "Abominable Snowman")
print("Name is", tuple_thing[NAME])


dict_thing = {
    "name": "yeti",
    "country": "CN",
    "area": "Himalayas",
    "description": "Hirsute Himalayan",
    "aka": "Abominable Snowman"
}
print("Name is", dict_thing["name"])


from collections import namedtuple
CreatureNamedTuple = namedtuple("CreatureNamedTuple", "name, country, area, description, aka")
namedtuple_thing = CreatureNamedTuple("yeti", "CN", "Himalaya", "Hirsute Himalayan", "Abominable Snowman")
print("Name is", namedtuple_thing[0])
print("Name is", namedtuple_thing.name)


class CreatureClass():
    def __init__(
            self,
            name: str,
            country: str,
            area: str,
            description: str,
            aka: str
            ):
        self.name = name
        self.country = country
        self.area = area
        self.description = description
        self.aka = aka

class_thing = CreatureClass(
    "yeti",
    "CN",
    "Himalayas",
    "Hirsute Himalayan",
    "Abominable Snowman")
print("Name is", class_thing.name)


from dataclasses import dataclass

@dataclass
class CreatureDataClass():
    name: str
    country: str
    area: str
    description: str
    aka: str

dataclass_thing = CreatureDataClass(
    "yeti",
    "CN",
    "Himalayas",
    "Hirsute Himalayan",
    "Abominable Snowman"
)
print("Name is", dataclass_thing.name)