# Fiche séance S10 – La gestion des exceptions

**Durée** : 2 h · **Type** : théorie + pratique · **Projet fil rouge** : GestParc, étape 7 (exceptions métier)

## Objectifs
- Lire une trace d'erreur ; capturer des exceptions précises avec `try` / `except` / `else` / `finally`
- Exploiter la hiérarchie des exceptions (capturer une famille)
- Utiliser `assert` pour les invariants et `raise` pour signaler les erreurs
- Créer des exceptions personnalisées et chaîner les erreurs avec `raise ... from`

## Déroulé détaillé
| Horaire | Durée | Activité | Support |
|---|---|---|---|
| 0:00 | 10 min | Quiz flash S9 | Slide 2 |
| 0:10 | 20 min | Traceback, `try`/`except`, exceptions précises, hiérarchie, `else`/`finally` | Slides 4–8 |
| 0:30 | 30 min | Lab partie 1 : ex. 1 à 4 | Slide 9 |
| 1:00 | 5 min | Pause | |
| 1:05 | 20 min | `assert`, `raise`, exceptions personnalisées, `raise ... from`, bonnes pratiques | Slides 10–14 |
| 1:25 | 30 min | Lab partie 2 : ex. 5 à 8, synthèse import RH, GestParc étape 7 | Slide 15 |
| 1:55 | 5 min | Récapitulatif, annonce du TP S11 | Slide 16 |

## Matériel
- `S10_lab_enonce.ipynb`, `S10_lab_corrige.ipynb`, `img/s10_exceptions.svg` (hiérarchie)
- `scripts/gestparc/main.py` : étape 7, menu protégé par un unique `try` (à tester avec des saisies erronées)

## Points de vigilance
- Faire le lien avec les cellules ✅ utilisées depuis S1 : ce sont des `assert`.
- Insister sur l'anti-pattern `except: pass` (avaler les erreurs) et sur l'ordre des `except` (du plus précis au plus général).
- `finally` s'exécute même après un `return` : le montrer avec l'exemple de la slide 8.
- Ex. 4 utilise des `lambda` dans une liste : simple réutilisation de S5.
- Étape 7 : changement d'API (`Equipment.assign` et `Inventory.add` ne renvoient plus de booléen). Le signaler explicitement, c'est un vrai refactoring.
- `with` apparaît dans le bonus (`suppress`) : il sera détaillé en S12.

## Adaptation selon les profils
| Profil | Accent | Exemples |
|---|---|---|
| Développeurs | EAFP vs LBYL, hiérarchie d'exceptions applicative, `raise from`, `ExceptionGroup` | Ex. 7, 8, bonus |
| Chefs de projet | Compte rendu de déploiement lisible, erreurs explicites pour l'utilisateur | Ex. 7 (pipeline) |
| Data | Import robuste qui collecte les lignes en erreur | Ex. 2, synthèse |
| Admins sys / réseau | Connexions, nouvelles tentatives, quotas, `finally` pour libérer les ressources | Ex. 3, 8, exemple quota |

## Différenciation
- **Rapides** : ex. 8 (retry), bonus (`ExceptionGroup`, `add_note`, `suppress`).
- **En difficulté** : ex. 1, 2, 3, 6, 7 et, pour l'étape 7, seulement les exceptions et le setter `price`.
