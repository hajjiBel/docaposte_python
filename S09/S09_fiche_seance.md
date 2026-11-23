# Fiche séance S9 – Héritage et polymorphisme

**Durée** : 2 h · **Type** : théorie + pratique · **Projet fil rouge** : GestParc, étape 6 (hiérarchie d'équipements)

## Objectifs
- Créer des sous-classes, utiliser `super()`, redéfinir et étendre des méthodes
- Tester les relations avec `isinstance` / `issubclass`
- Comprendre l'héritage multiple, le MRO et les mixins
- Exploiter le polymorphisme et le duck typing
- Définir des classes abstraites avec `abc`

## Déroulé détaillé
| Horaire | Durée | Activité | Support |
|---|---|---|---|
| 0:00 | 10 min | Quiz flash S8 | Slide 2 |
| 0:10 | 20 min | Principe, héritage simple, `super()`, redéfinition/extension, `isinstance` | Slides 4–7 |
| 0:30 | 30 min | Lab partie 1 : ex. 1 à 4 (dont la hiérarchie du moteur de jeu) | Slide 8 |
| 1:00 | 5 min | Pause | |
| 1:05 | 20 min | Héritage multiple et MRO, mixins, polymorphisme, duck typing, `abc`, pièges | Slides 9–13 |
| 1:25 | 30 min | Lab partie 2 : ex. 5 à 8, synthèse supervision, GestParc étape 6 | Slide 14 |
| 1:55 | 5 min | Récapitulatif | Slide 15 |

## Matériel
- `S09_lab_enonce.ipynb`, `S09_lab_corrige.ipynb`, `img/` (diagrammes des personnages et de GestParc)
- `scripts/gestparc/main.py` : étape 6 (menu avec plan de maintenance et plan IP)

## Points de vigilance
- Ex. 3 : réalise la « pratique » du programme (hiérarchie de personnages du moteur de jeu de S8).
- Rappeler le test « est un » / « a un » pour choisir entre héritage et composition.
- Le MRO surprend : faire prédire avant d'exécuter (ex. 5).
- `raise NotImplementedError` (ex. 7) et le `TypeError` des classes abstraites sont des avant-goûts de S10.
- Étape 6 : les signatures des sous-classes utilisent `*` (arguments nommés obligatoires, vus en S5). `Laptop` est fournie comme modèle.
- Les propriétés `price` et `ip_address` « refusent avec un message » : en S10, elles lèveront `ValueError`.

## Adaptation selon les profils
| Profil | Accent | Exemples |
|---|---|---|
| Développeurs | MRO, mixins, *Template Method*, `__init_subclass__`, dataclasses | Ex. 5, 6, 7, bonus |
| Chefs de projet | Hiérarchies métier lisibles, polymorphisme comme « même question, réponses adaptées » | Ex. 1 (Manager), plan de maintenance |
| Data | Exports polymorphes (CSV, Markdown) | Ex. 7 |
| Admins sys / réseau | Sauvegardes, supervision, équipements réseau avec IP | Ex. 8, synthèse, étape 6 |

## Différenciation
- **Rapides** : bonus (`__init_subclass__`, propriété abstraite, `@dataclass`), ajouter une sous-classe `Monitor` sans IP.
- **En difficulté** : ex. 1, 2, 3, 7 et, pour l'étape 6, implémenter seulement `Server` sur le modèle de `Laptop`.
