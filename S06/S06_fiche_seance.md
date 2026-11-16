# Fiche séance S6 – Classes et instances (1)

**Durée** : 2 h · **Type** : théorie + pratique · **Projet fil rouge** : GestParc, étape 4 (classe `Equipment`)

## Objectifs
- Expliquer classe, instance, attribut, méthode ; lire et produire un diagramme de classes UML
- Écrire une classe avec `__init__`, `self`, attributs d'instance et méthodes
- Instancier, accéder aux attributs, appeler des méthodes, faire collaborer des objets

## Déroulé détaillé
| Horaire | Durée | Activité | Support |
|---|---|---|---|
| 0:00 | 10 min | Quiz flash S5 | Slide 2 |
| 0:10 | 20 min | Procédural vs objet, classe/instance, UML, première classe, `self`, attributs | Slides 4–9 |
| 0:30 | 30 min | Lab partie 1 : ex. 1 à 4 | Slide 10 |
| 1:00 | 5 min | Pause | |
| 1:05 | 20 min | Méthodes, appels, objets qui collaborent, pièges | Slides 11–14 |
| 1:25 | 30 min | Lab partie 2 : ex. 5 à 7, synthèse Kanban, GestParc étape 4 | Slide 15 |
| 1:55 | 5 min | Récapitulatif | Slide 16 |

## Matériel
- `S06_lab_enonce.ipynb`, `S06_lab_corrige.ipynb`, dossier `img/` (diagrammes UML en SVG + sources Mermaid `.mmd`)
- `scripts/gestparc/main.py` : version de référence de l'étape 4
- Tableau blanc : dessiner « étiquettes → objets » pour `self`

## Points de vigilance
- Les notebooks affichent des images du dossier `img/` : distribuer **le dossier complet** de la séance.
- `self` est la principale difficulté : dérouler à la main `lt1.age(2026)` → `Equipment.age(lt1, 2026)`.
- Pas de `__str__` avant S7 : on utilise `describe()`. L'affichage `<__main__.Equipment object at ...>` sert de transition vers S7.
- Pas d'héritage ni de propriétés : les attributs restent publics et modifiables (le piège de la faute de frappe motive l'encapsulation en S7).
- Rappeler le piège de la liste par défaut (S5) dans `__init__`.
- L'attribut `COLUMNS` de la synthèse est un attribut de classe, présenté brièvement : il sera expliqué en S7.

## Adaptation selon les profils
| Profil | Accent | Exemples |
|---|---|---|
| Développeurs | Conception UML avant le code, responsabilités des objets | Ex. 4 (UML → code), synthèse Kanban |
| Chefs de projet | UML comme langage commun, objets métier | Ex. 5 (budget de projet), Kanban |
| Data | Objets qui encapsulent des séries de mesures | Ex. 7 (sonde de température) |
| Admins sys / réseau | Modélisation d'équipements | Ex. 3 (volume disque), ex. 6 (switch) |

## Différenciation
- **Rapides** : bonus (`getattr`/`setattr`, `vars`, diagramme Mermaid avec association), ajouter `Employee` au fil rouge.
- **En difficulté** : ex. 1, 2, 3, 5 et l'étape 4 ; s'appuyer sur l'exemple guidé `Server`.
