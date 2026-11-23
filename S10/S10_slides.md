---
marp: true
theme: default
paginate: true
size: 16:9
header: 'Python – Programmation, approche objet et bonnes pratiques'
footer: 'S10 · La gestion des exceptions'
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

# Séance 10
## La gestion des exceptions

**Objectifs de la séance**
- Lire une trace d'erreur et comprendre le mécanisme des exceptions
- Capturer des exceptions précises avec `try` / `except`, utiliser `else` et `finally`
- Connaître la hiérarchie des exceptions
- Utiliser les assertions, lever des exceptions avec `raise`
- Créer ses propres exceptions métier

<!--
Timing : 1 min.
On transforme enfin les « Prix refusé » et les False silencieux de GestParc en vraies erreurs.
-->

---

<!-- _class: quiz -->

## ⚡ Quiz flash : séance 9

1. Que fait `super().__init__(...)` dans le constructeur d'une sous-classe ?
2. Comment connaître l'ordre de recherche des méthodes de la classe `D` ?
3. Qu'est-ce qu'un mixin ?
4. Que se passe-t-il si on instancie une classe abstraite ?
5. Donner un exemple de polymorphisme dans GestParc.

<!--
Timing : 10 min.
Réponses : 1. initialise la partie « classe mère » de l'objet — 2. D.__mro__ — 3. une petite classe qui ajoute une capacité (NetworkMixin) — 4. TypeError — 5. maintenance_interval_months() différente selon Laptop, Server, Printer...
-->

---

## Plan de la séance

| Durée | Bloc |
|---|---|
| 10 min | Quiz flash |
| 20 min | Théorie 1 : traces, `try` / `except`, hiérarchie, `else` / `finally` |
| 30 min | 🧪 Lab partie 1 |
| 5 min | Pause |
| 20 min | Théorie 2 : assertions, `raise`, exceptions personnalisées, bonnes pratiques |
| 30 min | 🧪 Lab partie 2 + GestParc étape 7 |
| 5 min | Récapitulatif |

---

## Lire une trace d'erreur (traceback)

```text
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    report = build_report(inventory)
  File "main.py", line 7, in build_report
    ratio = used / total
            ~~~~~^~~~~~~
ZeroDivisionError: division by zero
```

- Se lit **de bas en haut** : type d'exception, message, puis la ligne fautive
- Remonte la **pile d'appels** jusqu'au point de départ
- Une exception non capturée **arrête** le programme

<!--
Timing : 2 min.
Une exception est un objet (une instance de classe) qui « remonte » les appels de fonctions jusqu'à être capturée.
-->

---

## Capturer une exception : `try` / `except`

```python
raw_values = ["42", "3.5", "N/A", "17"]
total = 0
for raw in raw_values:
    try:
        total += int(raw)
    except ValueError:
        print(f"Valeur ignorée : {raw!r}")
print("Total :", total)
```

```text
Valeur ignorée : '3.5'
Valeur ignorée : 'N/A'
Total : 59
```

Le programme **continue** : l'erreur a été traitée.

<!--
Timing : 3 min.
Dans le try : le moins de code possible, seulement ce qui peut échouer.
-->

---

## Capturer une exception précise

```python
config = {"port": "8080", "timeout": "abc"}

for key in ["port", "timeout", "retries"]:
    try:
        value = int(config[key])
        print(key, "=", value)
    except KeyError:
        print(f"{key} : paramètre absent")
    except ValueError as exc:
        print(f"{key} : valeur invalide ({exc})")
```

```text
port = 8080
timeout : valeur invalide (invalid literal for int() with base 10: 'abc')
retries : paramètre absent
```

`except (KeyError, ValueError):` capture plusieurs types · `as exc` donne accès à l'objet exception

<!--
Timing : 3 min.
Les except sont testés dans l'ordre : le premier qui correspond est exécuté.
-->

---

## La hiérarchie des exceptions

![h:420 center](img/s10_exceptions.svg)

<!--
Timing : 3 min.
except LookupError capture IndexError ET KeyError.
except Exception capture presque tout (mais pas KeyboardInterrupt ni SystemExit).
En bleu : les exceptions de GestParc que l'on va créer ce soir. Pointillés : héritage multiple (InvalidEquipmentDataError est aussi une ValueError).
-->

---

## `else` et `finally`

```python
def read_backup_size(path: str) -> int | None:
    print("Ouverture de", path)
    try:
        size = {"/backup/db.dump": 2048}[path]
    except KeyError:
        print("Sauvegarde introuvable")
        return None
    else:
        print("Lecture réussie")          # seulement si aucune exception
        return size
    finally:
        print("Fermeture de", path)       # TOUJOURS exécuté

print(read_backup_size("/backup/web.tar"))
```

```text
Ouverture de /backup/web.tar
Sauvegarde introuvable
Fermeture de /backup/web.tar
None
```

<!--
Timing : 3 min.
finally s'exécute même en cas de return ou d'exception non capturée : idéal pour libérer une ressource (fichier, connexion).
En S12, l'instruction with fera ce travail automatiquement pour les fichiers.
-->

---

<!-- _class: lab -->

## 🧪 À vous : Lab partie 1 (30 min)

Notebook **`S10_lab_enonce.ipynb`**, partie 1

- Ex. 1 ⭐ : conversion sûre d'une saisie
- Ex. 2 ⭐⭐ : charger une configuration en collectant les erreurs
- Ex. 3 ⭐⭐ : `else` et `finally` autour d'une connexion simulée
- Ex. 4 ⭐⭐ : capturer par famille d'exceptions

---

## Les assertions

```python
def usage_percent(used: float, total: float) -> float:
    assert total > 0, "total doit être strictement positif"
    assert 0 <= used <= total, f"used hors limites : {used}"
    return used / total * 100

print(usage_percent(389, 512))
usage_percent(600, 512)
```

```text
75.9765625
AssertionError: used hors limites : 600
```

- Vérifient des **hypothèses du développeur** (invariants, préconditions internes)
- Peuvent être **désactivées** (`python -O`) : jamais pour valider une saisie utilisateur
- Ce sont elles qui vérifient vos exercices depuis S1 !

<!--
Timing : 2 min.
Règle : assert pour détecter les bugs ; raise pour signaler une situation anormale mais prévisible (donnée invalide, ressource absente).
-->

---

## Lever une exception : `raise`

```python
class Equipment:
    def __init__(self, asset_tag: str, price: float) -> None:
        self.asset_tag = asset_tag
        self.price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"Prix négatif pour {self.asset_tag} : {value}")
        self._price = value

try:
    Equipment("LT-001", -50)
except ValueError as exc:
    print("Erreur :", exc)
```

```text
Erreur : Prix négatif pour LT-001 : -50
```

<!--
Timing : 3 min.
Comparer avec S7 : le setter affichait un message et l'objet était créé avec un prix incohérent. Maintenant, l'objet n'est pas créé du tout.
raise sans argument dans un except : relance l'exception courante.
-->

---

## Créer ses propres exceptions

```python
class GestParcError(Exception):
    """Base de toutes les erreurs métier."""

class EquipmentNotFoundError(GestParcError, LookupError):
    def __init__(self, asset_tag: str) -> None:
        super().__init__(f"Équipement introuvable : {asset_tag}")
        self.asset_tag = asset_tag

try:
    raise EquipmentNotFoundError("XX-999")
except GestParcError as exc:
    print(type(exc).__name__, "|", exc, "|", exc.asset_tag)
```

```text
EquipmentNotFoundError | Équipement introuvable : XX-999 | XX-999
```

Une **classe de base** propre à l'application permet de tout capturer d'un coup : `except GestParcError`.

<!--
Timing : 3 min.
Une exception personnalisée est une classe comme une autre : héritage, attributs supplémentaires...
Nommage : suffixe Error.
-->

---

## Chaîner les exceptions : `raise ... from`

```python
def load_price(raw: str) -> float:
    try:
        return float(raw)
    except ValueError as exc:
        raise InvalidEquipmentDataError(f"Prix illisible : {raw!r}") from exc
```

```text
ValueError: could not convert string to float: 'mille'

The above exception was the direct cause of the following exception:

InvalidEquipmentDataError: Prix illisible : 'mille'
```

On **traduit** une erreur technique en erreur métier, sans perdre la cause.

<!--
Timing : 2 min.
L'attribut __cause__ de la nouvelle exception contient l'exception d'origine.
-->

---

## Bonnes pratiques et pièges

| ❌ À éviter | ✅ À préférer |
|---|---|
| `except:` ou `except Exception: pass` | capturer l'exception **précise** attendue |
| un `try` qui englobe 50 lignes | un `try` minimal autour de l'opération risquée |
| renvoyer `None` / `False` en cas d'erreur grave | lever une exception explicite |
| `assert` pour valider une saisie | `raise ValueError(...)` |
| messages vagues (`"Erreur"`) | message précis avec la valeur fautive |
| tester avant d'agir (LBYL) dans tous les cas | **EAFP** : essayer, puis gérer l'échec |

*EAFP : Easier to Ask Forgiveness than Permission* — style idiomatique en Python

<!--
Timing : 2 min.
Un except trop large masque les bugs (une faute de frappe devient « silencieuse »).
LBYL : if key in d: d[key] / EAFP : try: d[key] except KeyError.
-->

---

<!-- _class: lab -->

## 🧪 À vous : Lab partie 2 (30 min)

Notebook **`S10_lab_enonce.ipynb`**, parties 2 et 3

- Ex. 5 ⭐ : assertions de préconditions
- Ex. 6 ⭐⭐ : `raise` dans les propriétés (reprise de l'onduleur de S7)
- Ex. 7 ⭐⭐ : exceptions personnalisées d'un pipeline de déploiement
- Ex. 8 ⭐⭐⭐ : nouvelles tentatives et `raise ... from`
- Synthèse : import robuste d'une liste d'employés
- **GestParc – étape 7** : exceptions métier

---

## Récapitulatif

- `try` / `except Type as exc` / `else` / `finally`
- Capturer **précisément** ; la hiérarchie permet de capturer une famille (`LookupError`)
- `assert` pour les invariants ; `raise` pour signaler une erreur
- Exceptions personnalisées : une classe de base métier + des sous-classes explicites
- `raise ... from exc` pour traduire une erreur en conservant sa cause

**Séance 11 (TP)** : héritage + exceptions sur un système de comptes bancaires

<!--
Timing : 5 min.
-->
