

class Etat(object):
        
        def __init__(self, nom=None, transitions=[], initial = False, final = False):
                """
                :param set nom: Identifiant de l'etat.
                :param list transitions: c'est la liste(de tuples) des transitions qui associe a chaque etiquette, un etat de destination
                :param bool initial: True si l'object est un etat initial
                :param bool final: True si l'objet est un etat final
                :raise TyperError: SI nom n'est pas de type set

                :example
                
                >>>q1 = Etat(set(["q1"]))
                >>>q0 = Etat(set(["q0"]), [("a", q1), ("b", q0)])
                """
                if not isinstance(nom, set):
                        raise TypeError("Le premier paramatre doit etre un set")
                else :      
                        self.nom = nom
                self.transitions = transitions
                self.initial = initial
                self.final = final
                
        def destination(self, etiquette):
                """
                Methode qui determine une transition pour une etiquette donnee.
                :param etiquette: Lettre de l'alphabet servant d'etiquette a la transition.
                :return list: La liste des etats auquelles aboutissent la transition.
                
                :example:
                
                >>>q0.destinantion("a").symbole
                >>>'q1'
                
                """
                dests = set()
                for e in self.transitions:
                        try:
                                if e[0] == etiquette:
                                        dests.add(e[1])
                        except Exception as e:
                                #if e is AttributeError:
                                        #raise ValueError("Il n'existe pas de transition {}-{}->".format(self, etiquette))
                                print(e)
                                
                return dests
        
        
        def __str__(self):
                chaine = ""
                for i in self.nom:
                        chaine = chaine + i +", "
                chaine = chaine[:-2]
                return "({})".format(chaine)
        
        def __repr__(self):
                return self.__str__()
                
                

class Automate(object):
        
                
        def __init__(self, alphabet=None, etats=[]):
                """
                :param set alphabet: Ensemble des caracteres de l'alphabet de l'automate.
                :param list etats: Liste des etats de l'automate.
                """
                self.alphabet = alphabet
                self.etats = etats
                self.etat_i = None
                self.etats_f = []
                
                for e in etats:
                        if e.final == True:
                                self.etats_f.append(e)
                        if e.initial == True:
                                self.etat_i = e
                
                
        
        
        def transition(self, nom, etiquette):
                """
                Methode qui represente la fonction de transition de l'automate
                :param set nom: Identifiant de l'etat source de la transition.
                :param str etiquette: Etiquette de la transition.
                :return Etat: Etat destination de la transition
                """
                etat = None
                for e in self.etats:
                        if nom == e.nom:
                                etat = e.destination(etiquette)
                                
                return etat
        
        
        
        
        
        def is_deterministe(self):
                for a in self.alphabet:
                        for e in self.etats:
                                if len(self.transition(e.nom, a)) > 1:
                                        return False
                return True
        
        
        
        
        
        def is_deterministe_complet(self):
                for e in self.etats:
                        for a in self.alphabet:
                                if len(e.destination(a))<1:
                                        return False
                return True
        
        
        def verifier_mot(self, mot):
                mot = list(mot)
                q0 = self.etat_i
                for m in mot:
                        Q = self.transition(q0.nom, m)
                        for q in Q:
                                pass
                        
                        
        
        
        def __str__(self):
                chaine = "\t\t"
                for a in self.alphabet:
                        chaine = chaine + "{}\t".format(e.nom)
                chaine = chaine + "\n\n"
                
                for e in self.etats:
                        chaine = chaine + "\t{}".format(e.nom)
                        for a in self.alphabet:
                                ch = "  "
                                if len(e.destination(a))>0:
                                        ch = e.__str__()
                                        chaine = chaine + "\t{}".format(ch)
                                        
                                        
        
        
        
        
        
        
if __name__=='__main__':
        
        etats = []
        e = Etat(set(["q2"]), [], False, True)
        etats.append(e)
        e1 = Etat(set(["q1"]))
        e1.transitions = [("b", e), ("a", e1), ("b", e1)]
        etats.append(e1)
        e = Etat(set(["q0"]), [("a", e1)], True)
        etats.append(e)
        
        automate = Automate(["a", "b"], etats)
        
        print(automate.transition(set(['q0']), 'a'))
        print(automate.is_deterministe())
        print(automate.etats_f)