
class Personne(object):

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @nom.setter
    def nom(self, nom):
        if not isinstance(nom, str):
            raise TypeError("Type de nom invalide")
        elif len(nom) == 0:
            raise AttributeError("Le nom ne doit pas etre vide")
        elif len(nom) > 15:
            raise AttributeError("Le nom ne doit pas avoir plus de quinze caracteres")
        else:
            self.__nom = nom

    @prenom.setter
    def prenom(self, prenoms):
        sep = prenoms.split(' ')
        if len(sep) > 3:
            raise AttributeError("Trop grand nombre de prenoms")
        for p in sep:
            if len(p) > 15:
                raise AttributeError("Le prenom %s est trop long" % (p))
        self.__prenom = prenoms

    def __separer(self, prenoms):
        return prenoms.split(' ')

if __name__ == '__main__':
    a = Personne("Maman", "Alice")
