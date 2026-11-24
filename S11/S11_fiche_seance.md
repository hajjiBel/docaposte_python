# Fiche séance S11 – Fichiers et modules de base

**Durée** : 2 h · **Type** : théorie + pratique · **Projet fil rouge** : GestParc, étape 8 (garanties, rapport texte, journal de maintenance)

## Objectifs
- Lire et écrire des fichiers texte avec `with`, les modes et l'encodage adaptés
- Manipuler chemins et dossiers avec `pathlib`
- Utiliser `math`, `random` (graine), `datetime` (dates, durées, formats) et `time`
- Valider et extraire des informations avec le module `re`

## Déroulé détaillé
| Horaire | Durée | Activité | Support |
|---|---|---|---|
| 0:00 | 10 min | Quiz flash S11 | Slide 2 |
| 0:10 | 20 min | `open` et modes, `with`, lecture, encodage, `pathlib` | Slides 4–8 |
| 0:30 | 30 min | Lab partie 1 : ex. 1 à 5 | Slide 9 |
| 1:00 | 5 min | Pause | |
| 1:05 | 20 min | `import`, `math`, `random`, `datetime`, `time`, `re`, groupes nommés, pièges | Slides 10–16 |
| 1:25 | 30 min | Lab partie 2 : ex. 6 à 10, synthèse journal web, GestParc étape 8 | Slide 17 |
| 1:55 | 5 min | Récapitulatif | Slide 18 |

## Matériel
- `S12_lab_enonce.ipynb`, `S12_lab_corrige.ipynb`
- `scripts/gestparc/gestparc_modele.py` : modèle étape 7 + garanties, chargé dans le notebook par `%run`
- `scripts/gestparc/main.py` (étape 8 complète) et `sample_maintenance.log`
- Le notebook crée ses fichiers dans `lab_s12/` (à côté du notebook)

## Points de vigilance
- Le notebook doit être ouvert **depuis le dossier de la séance** (chemins relatifs `scripts/...` et `lab_s12/`).
- `import` est utilisé officiellement à partir de cette séance (forme simple) ; les détails viennent en S14. `%run` est une commande Jupyter, pas du Python : le préciser.
- Windows : l'encodage par défaut peut être `cp1252` → toujours `encoding="utf-8"`.
- Les tests de dates n'utilisent jamais `date.today()` : la date du jour est passée en paramètre (bonne pratique de testabilité, reprise en S15).
- Regex : faire tester les motifs sur regex101.com ; ne pas viser l'exhaustivité (une regex d'e-mail « parfaite » n'existe pas).
- Le module `random` n'est pas fait pour la sécurité : mentionner `secrets` (bonus).

## Adaptation selon les profils
| Profil | Accent | Exemples |
|---|---|---|
| Développeurs | `with` comme gestionnaire de contexte, regex compilées, testabilité des dates | Ex. 10, bonus `timeit` |
| Chefs de projet | Délais, SLA, rapports texte | Ex. 8 (SLA), étape 8 (rapport) |
| Data | Lecture robuste, encodages, statistiques sur journaux | Ex. 5, synthèse |
| Admins sys / réseau | Configuration, rotation de journaux, journaux Apache, sous-réseaux | Ex. 2, 4, 6, synthèse |

## Différenciation
- **Rapides** : bonus (`secrets`, `timeit`, `shutil`, `zoneinfo`), ajouter au rapport GestParc une section « garanties à échéance ».
- **En difficulté** : ex. 1, 2, 3, 6, 8 et l'étape 8 sans `log_summary` ; fournir le motif `LOG_PATTERN`.
