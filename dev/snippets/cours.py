"""Ce module contient les codes necessaires au suivi des cours"""
from pprint import pprint

COURSE_INDEX = {
    "cours": [{
        "nom": "Apprendre Python 3.6",
        "hash": "5e4aze4az5e4aze4aze4az24eaze",
        "file": "apprendre_py36/intro.mp4",
        "chapitres":[{
                "numero": 1,
                "nom: ": "Les variables",
                "hash": "aze54az5az4ea5z4e5az4e5a4",
                "file": "apprendre_py36/variables.mp4"
            } , {
                "numero": 2,
                "nom": "Les fonctions",
                "hash": "zaz54z455a4z54ef4z5e4f54zf",
                "file": "apprendre_py36/fonctions.mp4"
            }]
        } , {
        "nom": "Apprendre Django 2.2",
        "hash": "2sd4fsd4fs5d4f2sdf4s5d4fs2df4",
        "file": "apprendre_django/intro.mp4",
        "chapitres": [{
                "numero": 1,
                "nom": "Demarrage d'un projet",
                "hash": "az2eaz4e5aze4az2e4az54eaze4",
                "file": "apprendre_django/demarrer.mp4"
            } , {
                "number": 2,
                "nom": "Vues",
                "hash": "sd24fs54fs2d4f5sd4f2sdfsdf4s",
                "file": "apprendre_django/vues.mp4"
            }]
        }],
    
    "last": {
        "cours": "5e4aze4az5e4aze4aze4az24eaze",
        "chapitre": 2,
        "position": 80
        }
    }

pprint(COURSE_INDEX)
with open("cours.json", "w") as fp:
    import json
    fp.write(json.dumps(COURSE_INDEX, indent=4))


class Chapitre:
    """Cette classe represente un chapitre"""

    def __init__(self, cours, numero, hashe, fichier):
        """Cette classe doit initialise avec ces parametres:
        cours: une instance de la classe Cours ou le hash d'un cours
        numero: numero du chapitre dans le cours
        hashe: hash du chapitre
        fichier: nom du fichier video sur le disque"""


class Cours:
    """Cette classe represente un cours"""

    def __init__(self, nom, hashe, fichier):
        """On initialise la classe avec ses attributs,
        nom, hash et fichier. notez hash au lieu de hash parce que
        hash est une fonction incluse.
        nom: le nom du cours
        hashe: le hash du fichier d'introducation
        fichier: le fichier video d'introduction"""

    def ajouter_chapitre(self, numero, nom, hash, fichier):
        """Cette method permet d'ajouter un chapitre à un cours
        numero: numero du chapitre dans le cours,
        nom: nom du chapitre dans un cours
        hashe: hash du fichier du cours
        fichier: ficher video sur le disque"""

    def liste_chapitres(self):
        """Retourne la liste des chapitres de ce cours"""

    def charger_chapitres(self, chapitres):
        """Charge une liste contenant les chapitres et les ajoute
        au cours
        chapitres: liste de chapitres"""


class IndexCours:
    """Cette classe represente l'index de cours"""

    @classmethod
    def load_from_dict(self, index):
        """charge l'index a partir d'un dictionnaire
        index: dictionnaire contenant l'index"""

    @classmethod
    def load_from_file(self, fichier):
        """Charge l'index a partir d'un fichier json.
        index: fichier json"""

    def get_cours(self, hashe=None, nom=None):
        """Cette methode permet d'avoir un objet Cours a partir
        de son hash ou de son nom"""




