# Fiche séance S13 – Système, données et base de données

**Durée** : 2 h · **Type** : théorie + pratique · **Projet fil rouge** : GestParc, étape 9 (CSV, JSON, SQLite, ligne de commande)

## Objectifs
- Utiliser `sys` (arguments, code de sortie, sortie d'erreur) et `os` (variables d'environnement, `os.walk`)
- Lire et écrire du JSON et du CSV, en gérant les types et les encodages
- Réaliser un CRUD SQLite avec requêtes paramétrées, transactions, jointures et agrégations
- Démontrer puis empêcher une injection SQL

## Déroulé détaillé
| Horaire | Durée | Activité | Support |
|---|---|---|---|
| 0:00 | 10 min | Quiz flash S12 | Slide 2 |
| 0:10 | 20 min | `sys`, `os.environ`, `os.walk`, `json`, `csv` | Slides 4–9 |
| 0:30 | 30 min | Lab partie 1 : ex. 1 à 5 | Slide 10 |
| 1:00 | 5 min | Pause | |
| 1:05 | 20 min | SQLite, CRUD, transactions, injection SQL, agrégations, pièges | Slides 11–16 |
| 1:25 | 30 min | Lab partie 2 : ex. 6 à 9, synthèse, GestParc étape 9 | Slide 17 |
| 1:55 | 5 min | Récapitulatif | Slide 18 |

## Matériel
- `S13_lab_enonce.ipynb`, `S13_lab_corrige.ipynb` ; le notebook écrit dans `lab_s13/`
- `scripts/gestparc/gestparc_modele.py` (modèle de l'étape 8, chargé par `%run`)
- `scripts/gestparc/main.py` : étape 9 complète, utilisable en ligne de commande (`init`, `list`, `export`, `import`) avec la variable `GESTPARC_DB`
- Facultatif : *DB Browser for SQLite* pour visualiser `lab_s13/gestparc.db`

## Points de vigilance
- Faire une démo **en terminal** de `sys.argv`, du code de retour (`echo $?` / `$LASTEXITCODE`) et d'une variable d'environnement (`export` / `$env:`).
- L'injection SQL (ex. 8) se fait sur une base de test en mémoire : rappeler le cadre éthique.
- Les mots de passe en clair de l'ex. 8 sont une simplification : citer `hashlib` / `bcrypt`.
- `executescript` (ex. 9) n'accepte pas de paramètres : réservé aux scripts de création.
- Le stockage des attributs spécifiques en JSON (colonne `specs`) est un compromis pédagogique ; discuter de l'alternative (une table par type, ou un ORM comme SQLAlchemy).
- Le fichier `main.py` dépasse 600 lignes : c'est la motivation directe de S14 (packages).

## Adaptation selon les profils
| Profil | Accent | Exemples |
|---|---|---|
| Développeurs | DB-API, transactions, `ON CONFLICT`, couche « repository » | Ex. 7, 9, étape 9 |
| Chefs de projet | Synthèses CSV pour le pilotage (heures, coûts, fournisseurs) | Ex. 5, synthèse |
| Data | CSV/JSON, agrégations SQL (`GROUP BY`, `JOIN`) | Ex. 5, 9, synthèse |
| Admins sys / réseau | Arguments de scripts, codes de retour, variables d'environnement, audit de disque | Ex. 1, 2, 3, CLI de GestParc |

## Différenciation
- **Rapides** : bonus (`argparse`, `utf-8-sig`, `subprocess`, historique des affectations).
- **En difficulté** : ex. 1, 4, 5, 6, 7, 8 ; pour l'étape 9, se limiter à CSV + JSON et utiliser le dépôt SQLite fourni dans `main.py`.
