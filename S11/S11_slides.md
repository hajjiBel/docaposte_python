---
marp: true
theme: default
paginate: true
size: 16:9
header: 'Python – Programmation, approche objet et bonnes pratiques'
footer: 'S12 · Fichiers et modules de base'
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

# Séance 12
## Fichiers et modules de base

**Objectifs de la séance**
- Lire et écrire des fichiers texte : `open`, `with`, modes, encodage
- Manipuler chemins et dossiers avec `pathlib`
- Utiliser les modules `math`, `random`, `datetime` et `time`
- Valider et extraire des informations avec les expressions régulières (`re`)

<!--
Timing : 1 min.
Module 6 : utilisation des librairies du langage. GestParc va enfin écrire des fichiers et lire des journaux.
-->

---

<!-- _class: quiz -->

## ⚡ Quiz flash : séance 11

1. Pourquoi `InvalidAmountError` hérite-t-elle à la fois de `BankError` et de `ValueError` ?
2. Que garantit un virement « atomique » ?
3. Que fait `raise` sans argument dans un bloc `except` ?
4. Dans le traitement par lot, pourquoi un `try` par opération plutôt qu'un seul `try` autour de la boucle ?
5. Comment le compte épargne interdit-il le 4e retrait sans modifier `withdraw` ?

<!--
Timing : 10 min.
Réponses : 1. pour être capturée par except BankError OU except ValueError — 2. tout ou rien : pas d'argent perdu — 3. relance l'exception courante — 4. une erreur ne doit pas interrompre le traitement des lignes suivantes — 5. en redéfinissant _check_withdrawal (polymorphisme).
-->

---

## Plan de la séance

| Durée | Bloc |
|---|---|
| 10 min | Quiz flash |
| 20 min | Théorie 1 : fichiers, `with`, encodage, `pathlib` |
| 30 min | 🧪 Lab partie 1 |
| 5 min | Pause |
| 20 min | Théorie 2 : `import`, `math`, `random`, `datetime`, `time`, `re` |
| 30 min | 🧪 Lab partie 2 + GestParc étape 8 |
| 5 min | Récapitulatif |

---

## Ouvrir un fichier : `open()` et ses modes

```python
f = open("servers.txt", "w", encoding="utf-8")
f.write("srv-web-01\n")
f.write("srv-db-01\n")
f.close()                      # indispensable : sinon données perdues
```

| Mode | Signification | Si le fichier n'existe pas | Si le fichier existe |
|---|---|---|---|
| `"r"` | lecture (défaut) | `FileNotFoundError` | lu depuis le début |
| `"w"` | écriture | créé | **écrasé** |
| `"a"` | ajout | créé | écrit à la fin |
| `"x"` | création exclusive | créé | `FileExistsError` |
| `+ "b"` | binaire (`"rb"`, `"wb"`) | | octets (`bytes`) |

<!--
Timing : 3 min.
Le mode "w" écrase sans prévenir : piège classique.
Toujours préciser encoding="utf-8" en mode texte (sur Windows, l'encodage par défaut peut être cp1252).
-->

---

## L'instruction `with` : fermeture garantie

```python
with open("servers.txt", "w", encoding="utf-8") as f:
    for hostname in ["srv-web-01", "srv-db-01", "srv-app-01"]:
        f.write(hostname + "\n")
# ici, le fichier est fermé, même en cas d'exception

with open("servers.txt", encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        print(number, line.strip())
```

```text
1 srv-web-01
2 srv-db-01
3 srv-app-01
```

`with` = un `try` / `finally` automatique (rappel S10) : **toujours** l'utiliser.

<!--
Timing : 3 min.
Un fichier ouvert est un itérable de lignes : la boucle for lit ligne par ligne sans tout charger en mémoire (idéal pour les gros journaux).
Chaque ligne contient son \n final : strip() ou rstrip("\n").
-->

---

## Lire un fichier

| Méthode | Résultat |
|---|---|
| `f.read()` | tout le contenu dans **un** `str` |
| `f.readline()` | la ligne suivante (`""` à la fin du fichier) |
| `f.readlines()` | liste de toutes les lignes (avec `\n`) |
| `for line in f:` | ligne par ligne, **économe en mémoire** |

```python
with open("app.conf", encoding="utf-8") as f:
    settings = {}
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            settings[key.strip()] = value.strip()
```

<!--
Timing : 2 min.
Exemple concret : lecture d'un fichier de configuration clé=valeur (ex. 2 du lab).
-->

---

## L'encodage du texte

```python
text = "Équipement réservé – coût : 1 200 DT"
with open("note.txt", "w", encoding="cp1252") as f:     # ancien encodage Windows
    f.write(text)

try:
    with open("note.txt", encoding="utf-8") as f:
        print(f.read())
except UnicodeDecodeError as exc:
    print("Mauvais encodage :", exc.reason)

with open("note.txt", encoding="cp1252") as f:
    print(f.read())
```

```text
Mauvais encodage : invalid continuation byte
Équipement réservé – coût : 1 200 DT
```

Règle : **UTF-8 partout**, et toujours `encoding=` explicite (détails str / bytes en S14).

<!--
Timing : 2 min.
Fichiers venant d'Excel ou de vieux systèmes Windows : souvent cp1252. Option errors="replace" pour lire malgré tout.
-->

---

## `pathlib` : les chemins comme des objets

```python
from pathlib import Path

logs = Path("data") / "logs"            # l'opérateur / assemble les chemins
logs.mkdir(parents=True, exist_ok=True)
(logs / "web.log").write_text("GET /\n", encoding="utf-8")

for path in sorted(logs.glob("*.log")):
    print(path.name, path.stem, path.suffix, path.stat().st_size, "octets")
print(logs.exists(), logs.is_dir(), logs.resolve().is_absolute())
```

```text
web.log web .log 6 octets
True True True
```

`Path.home()`, `Path.cwd()`, `.parent`, `.read_text()`, `.rename()`, `.unlink()`, `.rglob("*.py")`

<!--
Timing : 3 min.
pathlib fonctionne de la même façon sous Windows et Linux (séparateurs \ et / gérés automatiquement).
open() accepte aussi un objet Path.
-->

---

<!-- _class: lab -->

## 🧪 À vous : Lab partie 1 (30 min)

Notebook **`S12_lab_enonce.ipynb`**, partie 1

- Ex. 1 ⭐ : écrire puis relire une liste de serveurs
- Ex. 2 ⭐⭐ : lire un fichier de configuration
- Ex. 3 ⭐⭐ : journal en mode ajout et lecture des dernières lignes
- Ex. 4 ⭐⭐ : rotation de journaux avec `pathlib`
- Ex. 5 ⭐⭐ : problèmes d'encodage

Les fichiers sont créés dans le dossier `lab_s12/`, à côté du notebook.

---

## Importer un module

```python
import math                          # on préfixe : math.sqrt(...)
from datetime import date, timedelta # on importe des noms précis
import random as rnd                 # alias
```

- Un module = un fichier `.py` qui regroupe fonctions, classes, constantes
- La **bibliothèque standard** est livrée avec Python : rien à installer
- Documentation : *docs.python.org/fr/3/library/*
- Détails (packages, `__name__`, pip) en **S14**

<!--
Timing : 1 min.
Les stagiaires ont déjà croisé import copy, from abc import ... : on officialise.
-->

---

## `math` et `random`

```python
import math
import random

print(math.ceil(42 / 12), math.floor(7.9), math.sqrt(2), math.log2(1024), math.pi)

random.seed(2026)                       # résultats reproductibles
print(random.randint(1, 6), random.choice(["web", "db", "app"]))
servers = [f"srv-{i:02d}" for i in range(1, 21)]
print(random.sample(servers, 3))        # 3 serveurs distincts tirés au sort
```

- `math` : `ceil`, `floor`, `sqrt`, `log`, `log2`, `pi`, `isclose`, `inf`
- `random` : `random()`, `uniform`, `randint`, `choice`, `choices`, `sample`, `shuffle`, `seed`
- Mots de passe / jetons de sécurité : module **`secrets`**, jamais `random`

<!--
Timing : 3 min.
math.ceil(42 / 12) : nombre de baies de 12 U pour 42 serveurs.
random.seed : indispensable pour des tests reproductibles (simulations, jeux de données de test).
-->

---

## `datetime` : dates, heures et durées

```python
from datetime import date, datetime, timedelta

opened = datetime(2026, 10, 21, 9, 30)
deadline = opened + timedelta(hours=8)
now = datetime.fromisoformat("2026-10-21T18:15:00")

print(deadline.strftime("%d/%m/%Y %H:%M"), now > deadline)
print(now - opened, (now - opened).total_seconds() / 3600)
print(date(2026, 12, 31) - date(2026, 10, 21))
print(datetime.strptime("21/10/2026 08:15", "%d/%m/%Y %H:%M").isoformat())
```

```text
21/10/2026 17:30 True
8:45:00 8.75
71 days, 0:00:00
2026-10-21T08:15:00
```

<!--
Timing : 4 min.
date (jour), datetime (jour + heure), timedelta (durée). Soustraire deux dates donne un timedelta.
strftime : date -> texte ; strptime : texte -> date. Formats : %d %m %Y %H %M %S %A.
date.today(), datetime.now() : attention, résultats non reproductibles dans les tests (on passe la date du jour en paramètre).
-->

---

## `time` : mesurer et attendre

```python
import time

start = time.perf_counter()
total = sum(range(10_000_000))
elapsed = time.perf_counter() - start
print(f"Calcul en {elapsed:.3f} s")

time.sleep(0.5)                   # pause d'une demi-seconde
print(time.time())                # secondes depuis le 01/01/1970 (timestamp Unix)
```

- `perf_counter()` : chronomètre précis pour mesurer une durée
- `sleep()` : attendre (scripts de surveillance, nouvelles tentatives)
- `time()` : horodatage Unix (journaux, fichiers)

<!--
Timing : 2 min.
Pour comparer des algorithmes sérieusement : module timeit (bonus).
-->

---

## Expressions régulières : le module `re`

| Motif | Signification | Motif | Signification |
|---|---|---|---|
| `\d` | un chiffre | `+` | 1 fois ou plus |
| `\w` | lettre, chiffre ou `_` | `*` | 0 fois ou plus |
| `\s` | espace, tabulation | `?` | 0 ou 1 fois |
| `.` | n'importe quel caractère | `{3}` / `{2,4}` | exactement 3 / de 2 à 4 |
| `[A-Z]` | un caractère de l'intervalle | `^` / `$` | début / fin |
| `(...)` | groupe capturant | `a\|b` | a ou b |

```python
import re
print(bool(re.fullmatch(r"INC-\d{4}", "INC-2048")))
print(re.findall(r"\d+\.\d+\.\d+\.\d+", "from 10.0.0.5 to 192.168.1.20"))
```

```text
True
['10.0.0.5', '192.168.1.20']
```

<!--
Timing : 3 min.
Toujours des chaînes brutes r"..." pour éviter de doubler les \.
Rappel S4 : l'automate de reconnaissance des tickets tient maintenant en une ligne.
search : n'importe où ; match : au début ; fullmatch : toute la chaîne ; findall : toutes les occurrences ; sub : remplacer.
-->

---

## Groupes nommés : analyser une ligne de journal

```python
import re

LOG = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>[\d:]{8}) "
    r"\[(?P<level>INFO|WARN|ERROR)\] (?P<asset>[A-Z]{2}-\d{3}) (?P<message>.+)$"
)
line = "2026-10-21 08:15:02 [WARN] SV-001 disk /var usage=91%"
m = LOG.match(line)
if m:
    print(m.group("level"), m["asset"], m.groupdict()["message"])
print(re.sub(r"usage=(\d+)%", r"usage=\1 pourcents", line))
```

```text
WARN SV-001 disk /var usage=91%
2026-10-21 08:15:02 [WARN] SV-001 disk /var usage=91 pourcents
```

<!--
Timing : 3 min.
re.compile : on compile une fois, on utilise sur des milliers de lignes.
Groupes nommés (?P<nom>...) : code beaucoup plus lisible que group(3).
m vaut None si la ligne ne correspond pas : toujours tester.
Outil conseillé : regex101.com pour mettre au point un motif.
-->

---

## Pièges fréquents

| Piège | Conséquence | Correction |
|---|---|---|
| Mode `"w"` au lieu de `"a"` | fichier écrasé | vérifier le mode |
| Pas de `with` | fichier non fermé, données perdues | `with open(...) as f:` |
| Pas d'`encoding=` | accents illisibles selon l'OS | `encoding="utf-8"` |
| Chemins en dur `"C:\\data\\x.txt"` | non portable | `Path("data") / "x.txt"` |
| `random` pour un mot de passe | prévisible | module `secrets` |
| `datetime.now()` dans une fonction testée | tests non reproductibles | passer la date en paramètre |
| Motif sans `r"..."` | `\d` mal interprété | chaîne brute |
| `re.match` au lieu de `fullmatch` | validation partielle | `fullmatch` pour valider |

---

<!-- _class: lab -->

## 🧪 À vous : Lab partie 2 (30 min)

Notebook **`S12_lab_enonce.ipynb`**, parties 2 et 3

- Ex. 6 ⭐ : dimensionner une salle serveur (`math`)
- Ex. 7 ⭐⭐ : tirage au sort reproductible pour un audit (`random`)
- Ex. 8 ⭐⭐ : délais de résolution des tickets (`datetime`)
- Ex. 9 ⭐ : chronométrer (`time`)
- Ex. 10 ⭐⭐⭐ : validations et extractions (`re`)
- Synthèse : analyse d'un journal d'accès web
- **GestParc – étape 8** : garanties, rapport texte, analyse du journal de maintenance

---

## Récapitulatif

- `with open(chemin, mode, encoding="utf-8") as f:` ; modes `r`, `w`, `a`, `x`, `b`
- `pathlib.Path` : `/`, `glob`, `mkdir`, `read_text`, `write_text`, `stat`
- `math` (calculs), `random` + `seed` (aléatoire reproductible), `secrets` (sécurité)
- `datetime` : `date`, `datetime`, `timedelta`, `strftime` / `strptime`, `fromisoformat`
- `time.perf_counter()` pour mesurer
- `re` : `fullmatch`, `search`, `findall`, `sub`, `compile`, groupes nommés

**Séance 13** : système, CSV, JSON et base de données SQLite

<!--
Timing : 5 min.
-->
