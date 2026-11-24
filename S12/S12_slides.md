---
marp: true
theme: default
paginate: true
size: 16:9
header: 'Python – Programmation, approche objet et bonnes pratiques'
footer: 'S13 · Système, données et base de données'
style: |
  section { font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; font-size: 26px; color: #1f2933; padding: 50px 60px; }
  h1 { color: #1f4e78; font-size: 44px; }
  h2 { color: #1f4e78; font-size: 34px; border-bottom: 3px solid #f2b705; padding-bottom: 6px; }
  code { background: #eef2f7; color: #b3261e; border-radius: 4px; padding: 0 4px; }
  section pre { background: #f4f6f9 !important; border: 1px solid #d9e2ec; border-left: 5px solid #1f4e78; border-radius: 8px; font-size: 20px; }
  section pre code { background: transparent !important; color: #1f2933 !important; }
  table { font-size: 21px; }
  th { background: #1f4e78; color: #fff; }
  header, footer { color: #8a94a3; font-size: 14px; }
  section.title { background: linear-gradient(135deg, #1f4e78 0%, #2f6f9f 100%); color: #fff; }
  section.title h1, section.title h2 { color: #fff; border: none; }
  section.lab { background: #fff8e1; }
  section.lab h2 { border-color: #1f4e78; }
  .small { font-size: 20px; color: #52606d; }
  section.quiz { background: #eef6ff; }
  section.quiz h2 { border-color: #1f4e78; }
  img[alt~="center"] { display: block; margin: 0 auto; }
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
---

<!-- _class: title -->
<!-- _paginate: false -->
<!-- _header: '' -->

# Séance 13
## Système, données et base de données

**Objectifs de la séance**
- Interagir avec le système : `sys` (arguments, sortie) et `os` (environnement, arborescence)
- Lire et écrire des données structurées : `json` et `csv`
- Communiquer avec une base de données SQLite : CRUD, requêtes paramétrées
- Comprendre et éviter l'injection SQL

<!--
Timing : 1 min.
GestParc devient persistant : à la fin de la séance, l'inventaire survit à l'arrêt du programme.
-->

---

<!-- _class: quiz -->

## ⚡ Quiz flash : séance 12

1. Quel mode d'ouverture ajoute à la fin d'un fichier sans l'écraser ?
2. Pourquoi utiliser `with open(...)` ?
3. Comment construire le chemin `data/logs/app.log` de façon portable ?
4. Que renvoie `datetime(2026, 10, 21) - datetime(2026, 10, 1)` ?
5. Quelle fonction de `re` utiliser pour **valider** toute une chaîne ?

<!--
Timing : 10 min.
Réponses : 1. "a" — 2. fermeture garantie du fichier, même en cas d'erreur — 3. Path("data") / "logs" / "app.log" — 4. timedelta(days=20) — 5. re.fullmatch.
-->

---

## Plan de la séance

| Durée | Bloc |
|---|---|
| 10 min | Quiz flash |
| 20 min | Théorie 1 : `sys`, `os`, `json`, `csv` |
| 30 min | 🧪 Lab partie 1 |
| 5 min | Pause |
| 20 min | Théorie 2 : SQLite, CRUD, transactions, injection SQL |
| 30 min | 🧪 Lab partie 2 + GestParc étape 9 |
| 5 min | Récapitulatif |

---

## Le module `sys`

```python
import sys

print(sys.version_info >= (3, 12), sys.platform)
print(sys.argv)                     # arguments de la ligne de commande
print("Erreur de configuration", file=sys.stderr)
sys.exit(2)                         # code de retour (0 = succès)
```

```text
$ python backup.py --dry-run srv-web-01 srv-db-01
True linux
['backup.py', '--dry-run', 'srv-web-01', 'srv-db-01']
```

- `sys.argv[0]` : nom du script ; `sys.argv[1:]` : les arguments
- `sys.exit(code)` : indispensable pour les scripts appelés par cron, Ansible, une CI…
- `sys.path` : les dossiers où Python cherche les modules (S14)

<!--
Timing : 3 min.
Démo dans un terminal : echo $? après le script (ou $LASTEXITCODE sous PowerShell).
Pour des CLI plus riches : module argparse (bonus).
-->

---

## Le module `os` : environnement et système

```python
import os

db_host = os.environ.get("DB_HOST", "localhost")     # avec valeur par défaut
debug = os.environ.get("APP_DEBUG", "0") == "1"
print(db_host, debug, os.getcwd(), os.cpu_count())

os.environ["APP_ENV"] = "test"      # visible par ce processus et ses enfants
```

```text
$ export DB_HOST=srv-db-01          # PowerShell : $env:DB_HOST = "srv-db-01"
$ python app.py
srv-db-01 False /home/amira/gestparc 8
```

Variables d'environnement : configuration **sans modifier le code** (mots de passe, chemins, environnement dev/prod).

<!--
Timing : 3 min.
Bonne pratique (12-factor app) : la configuration vient de l'environnement ; jamais de mot de passe en dur dans le code.
-->

---

## Parcourir une arborescence : `os.walk`

```python
import os

for folder, subfolders, files in os.walk("projet"):
    for name in files:
        path = os.path.join(folder, name)
        size = os.path.getsize(path)
        if size > 1_000_000:
            print(f"{path} : {size / 1_048_576:.1f} Mo")
```

| `os` / `os.path` | `pathlib` équivalent |
|---|---|
| `os.path.join(a, b)` | `Path(a) / b` |
| `os.path.exists(p)` | `Path(p).exists()` |
| `os.listdir(d)` | `Path(d).iterdir()` |
| `os.walk(d)` | `Path(d).rglob("*")` (ou `Path.walk()` en 3.12+) |

<!--
Timing : 2 min.
os.walk parcourt récursivement : chaque tour donne un dossier, ses sous-dossiers et ses fichiers.
Usage admin : trouver les gros fichiers, les fichiers anciens, compter par extension.
-->

---

## Le format JSON : `json`

```python
import json

config = {"site": "Tunis", "servers": ["srv-web-01", "srv-db-01"], "backup": {"enabled": True, "hour": 2}}
text = json.dumps(config, ensure_ascii=False, indent=2)
data = json.loads(text)
print(data["backup"]["hour"], type(data["servers"]))

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)
with open("config.json", encoding="utf-8") as f:
    print(json.load(f) == config)
```

| Python | `dict` | `list`, `tuple` | `str` | `int`, `float` | `True` / `False` | `None` |
|---|---|---|---|---|---|---|
| JSON | objet | tableau | chaîne | nombre | `true` / `false` | `null` |

<!--
Timing : 3 min.
dumps / loads : avec des chaînes ; dump / load : avec des fichiers (moyen mnémotechnique : s = string).
Types non sérialisables (date, set, objets) : TypeError → convertir avant (isoformat(), list()) ou default=str.
JSON : API web, fichiers de configuration, échanges entre applications.
-->

---

## Le format CSV : `csv`

```python
import csv

with open("employes.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f, delimiter=";"):
        print(row["nom"], row["service"])         # chaque ligne est un dict de str

rows = [{"service": "DSI", "effectif": 12}, {"service": "Finance", "effectif": 5}]
with open("effectifs.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["service", "effectif"], delimiter=";")
    writer.writeheader()
    writer.writerows(rows)
```

- Toujours `newline=""` avec le module `csv` (sinon lignes vides sous Windows)
- Excel en français : séparateur `;` et parfois encodage `utf-8-sig` (BOM)
- Toutes les valeurs lues sont des **chaînes** : à convertir

<!--
Timing : 3 min.
Le module csv gère les guillemets et les séparateurs dans les valeurs : ne pas parser un CSV avec split(";").
-->

---

<!-- _class: lab -->

## 🧪 À vous : Lab partie 1 (30 min)

Notebook **`S13_lab_enonce.ipynb`**, partie 1

- Ex. 1 ⭐ : analyser les arguments d'une commande (`sys.argv`)
- Ex. 2 ⭐⭐ : configuration par variables d'environnement
- Ex. 3 ⭐⭐ : audit d'une arborescence (`os.walk`)
- Ex. 4 ⭐⭐ : configuration JSON (dates et ensembles)
- Ex. 5 ⭐⭐ : statistiques depuis un CSV, rapport en CSV

---

## SQLite et le module `sqlite3`

- Base de données **relationnelle** complète dans **un seul fichier** (ou en mémoire)
- Incluse dans Python : rien à installer, idéale pour des applications locales, des tests, des prototypes

```python
import sqlite3

conn = sqlite3.connect("parc.db")          # ":memory:" pour une base temporaire
conn.execute("""CREATE TABLE IF NOT EXISTS ticket (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    priority TEXT CHECK (priority IN ('P1', 'P2', 'P3')),
                    status TEXT DEFAULT 'NEW')""")
conn.execute("INSERT INTO ticket (title, priority) VALUES (?, ?)", ("VPN lent", "P2"))
conn.commit()
for row in conn.execute("SELECT id, title, status FROM ticket"):
    print(row)
conn.close()
```

```text
(1, 'VPN lent', 'NEW')
```

<!--
Timing : 3 min.
Même API (DB-API 2.0) pour PostgreSQL (psycopg), MySQL... : ce que l'on apprend ici se transpose.
Outil graphique conseillé : DB Browser for SQLite.
-->

---

## CRUD avec des requêtes paramétrées

| Opération | SQL | Python |
|---|---|---|
| **C**reate | `INSERT INTO ... VALUES (?, ?)` | `conn.execute(sql, (a, b))` |
| **R**ead | `SELECT ... WHERE id = ?` | `.fetchone()`, `.fetchall()`, boucle `for` |
| **U**pdate | `UPDATE ... SET status = ? WHERE id = ?` | `cursor.rowcount` = lignes modifiées |
| **D**elete | `DELETE FROM ... WHERE id = ?` | |

```python
cur = conn.execute("UPDATE ticket SET status = ? WHERE priority = ?", ("ASSIGNED", "P1"))
print(cur.rowcount, "ticket(s) mis à jour")
conn.executemany("INSERT INTO ticket (title, priority) VALUES (?, ?)",
                 [("Écran noir", "P3"), ("Serveur arrêté", "P1")])
conn.row_factory = sqlite3.Row             # accès par nom : row["title"]
```

<!--
Timing : 3 min.
Les ? sont remplacés par les valeurs du tuple, de façon sûre (échappement géré par le pilote).
Attention au tuple à un élément : (valeur,) avec la virgule.
cursor.lastrowid : identifiant de la ligne insérée.
-->

---

## Les transactions

```python
try:
    with conn:                                   # transaction : commit ou rollback automatique
        conn.execute("UPDATE stock SET qty = qty - 1 WHERE item = ?", ("laptop",))
        conn.execute("INSERT INTO assignment (item, employee) VALUES (?, ?)", ("laptop", None))
except sqlite3.IntegrityError as exc:
    print("Annulé :", exc)                       # le stock n'a PAS été décrémenté
```

```text
Annulé : NOT NULL constraint failed: assignment.employee
```

- `with conn:` → `commit()` si tout réussit, `rollback()` en cas d'exception
- Rappel S11 : le virement atomique, cette fois garanti par la base

<!--
Timing : 3 min.
Sans commit, les modifications sont perdues à la fermeture.
IntegrityError : contrainte violée (NOT NULL, UNIQUE, CHECK, clé étrangère).
-->

---

## ⚠️ L'injection SQL

```python
login = "admin' --"                              # saisie malveillante
sql = f"SELECT * FROM users WHERE login = '{login}' AND password = 'x'"
print(sql)
# SELECT * FROM users WHERE login = 'admin' --' AND password = 'x'
#                                          ^^ tout ce qui suit est un commentaire !
```

```python
# ✅ Toujours des paramètres : la saisie reste une simple valeur
conn.execute("SELECT * FROM users WHERE login = ? AND password_hash = ?", (login, digest))
```

**Jamais** de f-string, de `+` ou de `%` pour insérer une valeur dans une requête SQL.

<!--
Timing : 3 min.
OWASP Top 10 : l'injection reste l'une des failles les plus exploitées.
Le lab (ex. 8) fait réaliser l'attaque sur une base de test, puis la correction.
Les mots de passe ne se stockent jamais en clair (hashlib / bcrypt) : simplifié ici.
-->

---

## Agrégations et jointures

```python
query = """
    SELECT e.department, COUNT(t.id) AS tickets, ROUND(AVG(t.hours), 1) AS avg_hours
    FROM ticket AS t
    JOIN employee AS e ON e.id = t.requester_id
    WHERE t.status = ?
    GROUP BY e.department
    ORDER BY tickets DESC
"""
for row in conn.execute(query, ("CLOSED",)):
    print(dict(row))
```

```text
{'department': 'DSI', 'tickets': 4, 'avg_hours': 3.2}
{'department': 'Finance', 'tickets': 2, 'avg_hours': 1.5}
```

Faire travailler la base (filtrer, trier, agréger) plutôt que tout charger en Python.

<!--
Timing : 2 min.
dict(row) fonctionne grâce à row_factory = sqlite3.Row.
-->

---

## Pièges fréquents

| Piège | Conséquence | Correction |
|---|---|---|
| Requête construite avec une f-string | injection SQL | paramètres `?` |
| Oubli de `commit()` | modifications perdues | `with conn:` |
| `(valeur)` au lieu de `(valeur,)` | erreur de paramètres | tuple à un élément |
| CSV ouvert sans `newline=""` | lignes vides (Windows) | `newline=""` |
| Valeurs CSV non converties | `"10" + "5"` = `"105"` | `int()`, `float()` |
| `json.dump` d'une `date` ou d'un `set` | `TypeError` | `isoformat()`, `list()`, `default=str` |
| Mot de passe dans le code | fuite de secrets | variable d'environnement |

---

<!-- _class: lab -->

## 🧪 À vous : Lab partie 2 (30 min)

Notebook **`S13_lab_enonce.ipynb`**, parties 2 et 3

- Ex. 6 ⭐ : créer une table et l'interroger
- Ex. 7 ⭐⭐ : un petit dépôt CRUD de tickets
- Ex. 8 ⭐⭐ : attaque puis correction d'une injection SQL
- Ex. 9 ⭐⭐⭐ : jointures, agrégations et transaction
- Synthèse : import d'un CSV dans SQLite et export JSON
- **GestParc – étape 9** : CSV, JSON et persistance SQLite

---

## Récapitulatif

- `sys.argv`, `sys.exit(code)`, `sys.stderr` · `os.environ.get(nom, défaut)`, `os.walk`
- `json` : `dump` / `load` (fichiers), `dumps` / `loads` (chaînes), `ensure_ascii=False`, `indent`
- `csv` : `DictReader` / `DictWriter`, `delimiter=";"`, `newline=""`, tout est texte
- `sqlite3` : `connect`, `execute` avec `?`, `fetchone` / `fetchall`, `row_factory`, `with conn:`
- **Jamais** de requête SQL construite par concaténation

**Séance 14** : modules, packages, pip et bonnes pratiques (PEP 8)

<!--
Timing : 5 min.
-->
