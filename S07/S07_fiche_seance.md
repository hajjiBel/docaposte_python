# Fiche séance S7 – Classes et instances (2)

**Durée** : 2 h · **Type** : théorie + pratique · **Projet fil rouge** : GestParc, étape 5 (`Equipment` complète, `Employee`, `Inventory`)

## Objectifs
- Distinguer attributs de classe et d'instance ; éviter les attributs de classe mutables
- Écrire des `@classmethod` (constructeurs alternatifs) et des `@staticmethod` (utilitaires)
- Implémenter `__str__`, `__repr__`, `__eq__`, `__lt__`, `__len__`, `__contains__`, `__getitem__`, `__add__`
- Encapsuler avec `_`, `__` (name mangling) et `@property` (lecture seule, setter avec validation)

## Déroulé détaillé
| Horaire | Durée | Activité | Support |
|---|---|---|---|
| 0:00 | 10 min | Quiz flash S6 | Slide 2 |
| 0:10 | 20 min | Attributs de classe et pièges, `@classmethod`, `@staticmethod` | Slides 4–7 |
| 0:30 | 30 min | Lab partie 1 : ex. 1 à 4 | Slide 8 |
| 1:00 | 5 min | Pause | |
| 1:05 | 20 min | Méthodes spéciales, `__str__`/`__repr__`, comparaison et tri, opérateurs et conteneurs, `_`/`__`, `@property`, pièges | Slides 9–15 |
| 1:25 | 30 min | Lab partie 2 : ex. 5 à 9, synthèse `IPv4Address`, GestParc étape 5 | Slide 16 |
| 1:55 | 5 min | Récapitulatif, annonce du TP S8 | Slide 17 |

## Matériel
- `S07_lab_enonce.ipynb`, `S07_lab_corrige.ipynb`, `img/` (diagramme UML de l'étape 5 + source Mermaid)
- `scripts/gestparc/main.py` : version de référence de l'étape 5

## Points de vigilance
- **Séance très dense.** Priorités : ex. 1, 3, 5, 6, 9 et l'étape 5. Les ex. 4, 7, 8 et la synthèse peuvent être terminés à la maison.
- Les setters « refusent » une valeur invalide par un message : c'est provisoire. En S10, on lèvera `ValueError` (annoncer ce refactoring).
- Piège classique du setter : `self.price = value` dans le setter de `price` provoque une récursion infinie. Le montrer.
- `all()` / `any()` apparaissent (fonctions intégrées) : les présenter en 30 secondes.
- `try/except AttributeError` dans les cellules de vérification : aperçu de S10, rien à expliquer en détail.
- L'étape 5 est longue : distribuer le diagramme UML et faire implémenter `Equipment` d'abord (indispensable), puis `Inventory`.

## Adaptation selon les profils
| Profil | Accent | Exemples |
|---|---|---|
| Développeurs | Protocoles Python (dunder), `total_ordering`, `__hash__` | Ex. 6, 8, bonus |
| Chefs de projet | Durées et montants manipulés comme des valeurs métier | Ex. 4 (`Duration`), ex. 7 (`Money`) |
| Data | Comparaisons et tri d'objets, conversions | Ex. 6 (versions), synthèse |
| Admins sys / réseau | IP, versions OpenSSL, pools de serveurs, onduleur | Ex. 3, 6, 8, 9, synthèse `IPv4Address` |

## Différenciation
- **Rapides** : synthèse `IPv4Address`, bonus (`total_ordering`, `__hash__`, `__iter__`, module `ipaddress`).
- **En difficulté** : partir de la version de référence de l'étape 4 ; implémenter seulement `__str__`, `__eq__`, `from_dict` et la propriété `price` pour l'étape 5.
