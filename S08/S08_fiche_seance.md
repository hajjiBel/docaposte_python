# Fiche séance S8 – TP : simulation d'un moteur de jeu

**Durée** : 2 h · **Type** : TP (15 min de théorie maximum) · **Projet fil rouge** : pas de nouvelle étape (moteur repris en S9)

## Objectifs
- Implémenter un diagramme de classes UML complet (5 classes)
- Faire collaborer des objets par composition et agrégation
- Utiliser propriétés, méthodes spéciales, dictionnaires et ensembles dans une application
- Écrire une boucle de jeu dont la logique est testable sans clavier

## Déroulé détaillé
| Horaire | Durée | Activité | Support |
|---|---|---|---|
| 0:00 | 10 min | Quiz flash S7 | Slide 2 |
| 0:10 | 10 min | Démo d'une partie (`scripts/game_engine.py`), cahier des charges, UML, règles | Slides 4–6 |
| 0:20 | 40 min | Partie 1 : ex. 1 à 4 (`Item`, `Entity`, `Player`, `Enemy`) | Slide 7 |
| 1:00 | 5 min | Pause | |
| 1:05 | 5 min | Boucle de jeu, séparation logique / affichage | Slide 8 |
| 1:10 | 45 min | Partie 2 : ex. 5, 6 et synthèse (`World`, partie scénarisée) | Slide 9 |
| 1:55 | 5 min | Bilan : lister les duplications Player / Enemy | Slide 10 |

## Matériel
- `S08_lab_enonce.ipynb` (signatures et docstrings fournies), `S08_lab_corrige.ipynb`
- `scripts/game_engine.py` : moteur complet, jouable dans un terminal (`python game_engine.py`)
- `img/s08_game.svg` (diagramme UML) et sa source Mermaid

## Points de vigilance
- Les exercices sont **chaînés** : un stagiaire bloqué sur `Entity` bloque la suite. Après 15 min de blocage, lui donner la classe du corrigé.
- Les ex. 5, 6 et la synthèse se codent tous dans la cellule de la classe `World` (ex. 5) : le préciser à l'oral.
- Pas d'héritage volontairement (composition `Player.entity`) : ne pas répondre « on pourrait hériter » en détail, c'est l'objet de S9.
- Pas de hasard (module `random` en S12) : les parties sont reproductibles, ce qui permet les vérifications automatiques.
- Les messages renvoyés au lieu d'être affichés préparent les tests (S15) et l'IHM (S17).

## Adaptation selon les profils
| Profil | Accent | Exemples |
|---|---|---|
| Développeurs | Responsabilités des classes, testabilité, séparation logique / affichage | Bonus ennemis mobiles, niveaux |
| Chefs de projet | Lecture du diagramme UML, découpage en lots | Faire planifier l'ordre d'implémentation |
| Data | Structures de données de la carte (`set`, `dict` de positions) | `render`, bonus brouillard |
| Admins sys / réseau | Boucle d'événements, commandes textuelles (analogie avec un shell) | `play_turn` |

## Différenciation
- **Rapides** : bonus (brouillard de guerre, ennemis mobiles, niveaux), puis nouvelles commandes (`look`, `drop`).
- **En difficulté** : ex. 1 à 4 et ex. 5 (affichage) constituent l'objectif minimal ; donner le corrigé de `move_player` pour pouvoir jouer.
