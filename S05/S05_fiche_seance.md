# Fiche séance S5 – Les fonctions

**Durée** : 2 h · **Type** : théorie + pratique · **Projet fil rouge** : GestParc, étape 3 (découpage en fonctions typées)

## Objectifs
- Définir, appeler et documenter des fonctions ; renvoyer une ou plusieurs valeurs
- Utiliser arguments nommés, valeurs par défaut (et éviter le piège des valeurs mutables), `*args`, `**kwargs`
- Expliquer la portée LEGB, `global` et `nonlocal`
- Utiliser `lambda` avec `sorted`, `min`, `max`, `map`, `filter`
- Écrire des compréhensions de liste, de dictionnaire et d'ensemble
- Ajouter systématiquement docstrings et type hints

## Déroulé détaillé
| Horaire | Durée | Activité | Support |
|---|---|---|---|
| 0:00 | 10 min | Quiz flash S4 | Slide 2 |
| 0:10 | 20 min | Pourquoi des fonctions, `def`/`return`, retour multiple, arguments nommés et par défaut, piège mutable, `*args`/`**kwargs`, LEGB | Slides 4–10 |
| 0:30 | 30 min | Lab partie 1 : ex. 1 à 6 | Slide 11 |
| 1:00 | 5 min | Pause | |
| 1:05 | 20 min | Lambdas, `sorted`/`map`/`filter`, compréhensions, docstrings et type hints, pièges | Slides 12–15 |
| 1:25 | 30 min | Lab partie 2 : ex. 7 à 10, synthèse, GestParc étape 3 | Slide 16 |
| 1:55 | 5 min | Récapitulatif | Slide 17 |

## Matériel
- `S05_lab_enonce.ipynb`, `S05_lab_corrige.ipynb`
- `scripts/gestparc/main.py` : fonctions de l'étape 3 et menu `main()` (à comparer avec la version S3)

## Points de vigilance
- Bien distinguer `print` et `return` : erreur n° 1 des débutants.
- Le piège de la valeur par défaut mutable doit être **montré en direct** : personne ne le croit sinon.
- Les compréhensions ont été ajoutées au programme (validé en début de formation) : elles servent dès l'étape 3 et dans toute la suite.
- `nonlocal` et les fonctions imbriquées (ex. 6) sont difficiles : l'exercice est ⭐⭐⭐, il peut être sauté par les débutants.
- `try/except` apparaît dans une cellule de vérification (ex. 3) : simple aperçu, les exceptions sont vues en S10.
- Comparer le menu de S3 et celui de S5 en fin de séance : la réduction de taille motive les fonctions.

## Adaptation selon les profils
| Profil | Accent | Exemples |
|---|---|---|
| Développeurs | Signatures complètes (`*`, `**`), closures, fonctions comme valeurs | Ex. 3, 6, bonus `actions[choice]()` |
| Chefs de projet | Lisibilité grâce aux noms de fonctions, tri de projets | Ex. 7 (projets), ex. 9 (feuilles de temps) |
| Data | Compréhensions, `map`/`filter`, agrégations | Ex. 8, 9, synthèse |
| Admins sys / réseau | Conversion d'unités, nettoyage d'adresses IP, analyse de logs | Ex. 1, 8, synthèse |

## Différenciation
- **Rapides** : bonus (dispatch par dictionnaire, récursivité, `reduce`), ajouter `unassign_equipment` au fil rouge.
- **En difficulté** : ex. 1, 2, 4, 7, 8 et l'étape 3 suffisent ; l'ex. 10 peut être fait à partir des corrections de S4.
