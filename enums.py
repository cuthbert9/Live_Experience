from enum import Enum


class UserRoleEnum(str,Enum):
    USER="user"
    ORGANIZER="organizer"
    ADMIN="admin"



class VenuetypeEnum(str,Enum):
    CLUB="club"
    BAR="bar"
    ARENA="arena"
    HALL="hall"
    INDOOR="indoor"

class GenreEnum(str,Enum):
    JAZZ="jazz"
    AFRO="afro"
    AFRO_FUSION="afro-fusion"
    ROCK="rock"
    POP="pop"    
    TRADITIONAL="traditional"
    GOSPEL="gospel"
    BONGOFLEVA="bongo_fleva"
    HIPHOP="hiphop"


    
    