<div align="center">

# 🔀 Séance 3 — Les structures de contrôle

**Indentation · Conditions · Opérateurs · Boucles · Menu interactif**

![Durée](https://img.shields.io/badge/⏱_Lab-60_min_+_bonus-0d6efd?style=for-the-badge)
![Niveau](https://img.shields.io/badge/Niveau-Intermédiaire-ffc107?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GestParc](https://img.shields.io/badge/🛠_GestParc-Étape_2-fd7e14?style=for-the-badge)

</div>

---

## 🎯 Objectifs de la séance

| | Compétence |
|:-:|---|
| 📐 | Structurer le code en **blocs** grâce à l'**indentation** |
| 🔀 | Écrire des conditions avec `if` / `elif` / `else` et l'opérateur **ternaire** |
| 🧮 | Utiliser tous les opérateurs : **comparaison**, **logiques**, **appartenance**, **identité** |
| 🔁 | Répéter avec `while` et `for` (`range`, `enumerate`, `zip`) |
| ⏹️ | Contrôler les boucles : `break`, `continue`, `pass` et `else` |

---

## 🗺️ Plan de la séance

```mermaid
flowchart LR
    Q["🧠 Quiz flash"]:::quiz --> T1["📖 Théorie 1<br/>indentation, conditions,<br/>opérateurs"]:::th
    T1 --> L1["🧪 Lab partie 1"]:::lab
    L1 --> T2["📖 Théorie 2<br/>while, for,<br/>branchements"]:::th
    T2 --> L2["🧪 Lab partie 2<br/>+ GestParc étape 2"]:::lab
    L2 --> R["✅ Récap"]:::rec

    classDef quiz fill:#ffc107,color:#000,stroke:#997404,stroke-width:2px
    classDef th fill:#0d6efd,color:#fff,stroke:#084298,stroke-width:2px
    classDef lab fill:#20c997,color:#fff,stroke:#0f6848,stroke-width:2px
    classDef rec fill:#6f42c1,color:#fff,stroke:#3d1a78,stroke-width:2px
```

<details>
<summary><b>🧠 Quiz flash : révision de la séance 2</b> (cliquer pour voir les réponses)</summary>

| Question | Réponse |
|---|---|
| Que vaut `"srv-web-01"[4:7]` ? | `'web'` |
| Que renvoie `type(input("Âge : "))` ? | `<class 'str'>` : toujours du texte |
| Comment créer un ensemble vide ? | `set()` (et non `{}`, qui est un `dict`) |
| `a = [1, 2]`, `b = a`, `b.append(3)` : que vaut `a` ? | `[1, 2, 3]` : `b` est un alias |
| Échanger `x` et `y` en une ligne ? | `x, y = y, x` |

</details>

---

## 📖 Théorie 1 : indentation, conditions, opérateurs

### 📐 L'indentation fait partie de la syntaxe

```python
disk_usage = 0.93
if disk_usage > 0.9:
    print("Disque presque plein")        # bloc du if
    print("Nettoyage des logs requis")   # même bloc
print("Contrôle terminé")                # hors du bloc
```

- Un bloc commence après `:` et il est indenté de **4 espaces** (PEP 8).
- Toutes les lignes d'un bloc ont la **même indentation**.
- Les blocs s'imbriquent : 4 espaces de plus par niveau.
- Ne **jamais** mélanger tabulations et espaces.

### 🔀 `if` / `elif` / `else`

```mermaid
flowchart LR
    U(["💽 usage disque"]):::start --> C1{"≥ 90 % ?"}:::cond
    C1 -- oui --> R1["🔴 CRITICAL"]:::crit
    C1 -- non --> C2{"≥ 70 % ?"}:::cond
    C2 -- oui --> R2["🟠 WARNING"]:::warn
    C2 -- non --> R3["🟢 OK"]:::ok

    classDef start fill:#0d6efd,color:#fff,stroke:#084298
    classDef cond fill:#e2d9f3,color:#2c1559,stroke:#6f42c1,stroke-width:2px
    classDef crit fill:#dc3545,color:#fff,stroke:#842029
    classDef warn fill:#fd7e14,color:#fff,stroke:#984c0c
    classDef ok fill:#198754,color:#fff,stroke:#0b4229
```

```python
if disk_usage >= 0.9:
    level = "CRITICAL"
elif disk_usage >= 0.7:
    level = "WARNING"
else:
    level = "OK"
print(f"Disque à {disk_usage:.0%} : {level}")   # Disque à 78% : WARNING
```

> [!NOTE]
> Les conditions sont testées **dans l'ordre** et seul le **premier bloc vrai** est exécuté. Python n'a pas de `switch` classique : on enchaîne les `elif`. Depuis Python 3.10, `match … case` permet de comparer une valeur à des motifs.

### ❓ L'opérateur ternaire

```python
status = "en ligne" if is_online else "hors ligne"
#        valeur_si_vrai  if condition  else valeur_si_faux
```

> [!TIP]
> Réservez le ternaire aux cas simples : au-delà, un `if` classique est plus lisible.

### 🧮 Les opérateurs

| Famille | Opérateurs | Exemple | Résultat |
|---|---|---|:-:|
| ⚖️ Comparaison | `==` `!=` `<` `<=` `>` `>=` | `"web" == "Web"` | `False` |
| 🔗 Chaînage | encadrement | `0 <= port < 1024` | port système ? |
| 🧠 Logiques | `and` `or` `not` | `not tickets` | `True` si la liste est vide |
| 📥 Appartenance | `in` `not in` | `port in {22, 80, 443}` | `True` / `False` |
| 🆔 Identité | `is` `is not` | `assigned_to is None` | même objet ? |

> [!WARNING]
> Les chaînes se comparent **caractère par caractère** : `"10" < "9"` vaut `True`.

> [!IMPORTANT]
> Valent **faux** : `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}` et `set()`.<br/>
> **Évaluation paresseuse** : `user and user["name"]` ne lit pas la clé si `user` est vide.<br/>
> Sur un `dict`, `in` cherche dans les **clés**. On utilise `is` surtout avec `None`.

---

## 📖 Théorie 2 : les boucles

### 🔁 `while` ou `for` ?

```mermaid
flowchart TB
    Q{"Connaît-on le nombre<br/>de tours à l'avance ?"}:::q
    Q -- "non" --> W["🔄 while condition:<br/>répéter TANT QUE…"]:::w
    Q -- "oui" --> F["📋 for x in séquence:<br/>POUR CHAQUE élément…"]:::f
    W --> W1["saisie à contrôler<br/>nouvelles tentatives<br/>capital à doubler"]:::w2
    F --> F1["liste de serveurs<br/>range(1, n + 1)<br/>dict.items()"]:::f2

    classDef q fill:#e2d9f3,color:#2c1559,stroke:#6f42c1,stroke-width:2px
    classDef w fill:#0d6efd,color:#fff,stroke:#084298,stroke-width:2px
    classDef f fill:#198754,color:#fff,stroke:#0b4229,stroke-width:2px
    classDef w2 fill:#cfe2ff,color:#052c65,stroke:#0d6efd
    classDef f2 fill:#d1e7dd,color:#0a3622,stroke:#198754
```

<table>
<tr><th>🔄 while : contrôler une saisie</th><th>📋 for : somme de 1 à n</th></tr>
<tr><td>

```python
note = float(input("Note (0-20) : "))
while note < 0 or note > 20:
    print("Note invalide, recommencez")
    note = float(input("Note (0-20) : "))
print("Note enregistrée :", note)
```

</td><td>

```python
somme = 0                  # accumulateur
for i in range(1, n + 1):
    somme += i
print("Somme :", somme)    # n=10 → 55
```

</td></tr>
</table>

> [!WARNING]
> La condition d'un `while` doit **finir par devenir fausse**. Sinon, c'est une boucle infinie : interrompez-la avec `Ctrl+C`.

### 🔢 `range()`, `enumerate()`, `zip()`

| Écriture | Résultat |
|---|---|
| `list(range(4))` | `[0, 1, 2, 3]` |
| `list(range(1, 4))` | `[1, 2, 3]` : **la fin est exclue** |
| `list(range(0, 10, 2))` | `[0, 2, 4, 6, 8]` |
| `list(range(5, 0, -1))` | `[5, 4, 3, 2, 1]` : compte à rebours |
| `for i, s in enumerate(servers, start=1)` | `1 srv-web-01`, `2 srv-db-01` |
| `for s, load in zip(servers, loads)` | parcours de deux listes **en parallèle** |

### 🗂️ Parcourir un dictionnaire

| Boucle | Variable(s) |
|---|---|
| `for k in d:` | les clés |
| `for v in d.values():` | les valeurs |
| `for k, v in d.items():` | les clés et les valeurs |

```python
# Compter avec un dictionnaire
freq = {}
for c in "abracadabra":
    freq[c] = freq.get(c, 0) + 1
print(freq)                          # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
print(max(achats, key=achats.get))   # clé de la valeur maximale
```

### ⏹️ `break`, `continue`, `pass` et `else` de boucle

| Mot-clé | Effet |
|---|---|
| `continue` | ⏭️ passe **au tour suivant** |
| `break` | 🛑 **quitte** la boucle |
| `pass` | 💤 ne fait rien (bloc vide pour l'instant) |
| `else` (après `for` / `while`) | ✅ s'exécute si la boucle s'est terminée **sans `break`** |

```python
used_ips = {"10.0.0.10", "10.0.0.11", "10.0.0.13"}
for last_byte in range(10, 15):
    candidate = f"10.0.0.{last_byte}"
    if candidate not in used_ips:
        print("Première IP libre :", candidate)   # 10.0.0.12
        break
else:
    print("Aucune IP libre dans la plage")
```

---

## ⚠️ Pièges fréquents

| Piège | ❌ Exemple | ✅ Correction |
|---|---|---|
| `=` au lieu de `==` | `if level = "OK":` | `if level == "OK":` |
| Oubli des `:` | `else` | `else:` |
| Boucle infinie | compteur jamais incrémenté | vérifier que la condition progresse |
| Modifier la liste parcourue | `for x in l: l.remove(x)` | parcourir une copie `l[:]` |
| `range(len(l))` | `for i in range(len(l)): l[i]` | `for x in l` ou `enumerate` |
| `or` mal utilisé | `if level == "ERROR" or "FATAL":` | `if level in ("ERROR", "FATAL"):` |

---

## 🏋️ Exercices du lab

| # | Exercice | Difficulté | Notion clé |
|:-:|---|:-:|---|
| 1 | Niveau d'alerte d'un disque | ⭐ | `if / elif / else` |
| 2 | Statut avec le ternaire | ⭐ | `a if c else b` |
| 3 | Politique de mots de passe | ⭐⭐ | `and`, `not`, `in` |
| 4 | Règles de pare-feu | ⭐⭐ | appartenance, identité |
| 5 | Priorité d'un ticket (P1 à P4) | ⭐⭐⭐ | conditions imbriquées |
| 6 | Capacité totale d'un cluster | ⭐ | `for`, accumulateur |
| 7 | Liste numérotée | ⭐⭐ | `enumerate` |
| 8 | Serveurs surchargés | ⭐⭐ | `zip` |
| 9 | Nouvelles tentatives avec attente croissante | ⭐⭐ | `while`, plafond |
| 10 | Première adresse IP libre | ⭐⭐⭐ | `break`, `for … else` |
| 🧩 | **Synthèse** : statistiques d'un journal d'événements | ⭐⭐⭐ | `continue`, `break`, dictionnaire de compteurs |

---

## 🛠️ Projet fil rouge GestParc : étape 2

GestParc devient **interactif** avec un menu console en boucle :

```mermaid
flowchart TD
    M["📋 ===== GestParc =====<br/>Afficher le menu"]:::menu --> Ch{"Choix ?"}:::cond
    Ch -- "1" --> L["📃 Lister les équipements"]:::a
    Ch -- "2" --> R["🔍 Rechercher par n° d'inventaire"]:::b
    Ch -- "3" --> S["📊 Statistiques par catégorie"]:::c
    Ch -- "4" --> A["➕ Ajouter un équipement"]:::d
    Ch -- "0" --> Q(["👋 Quitter"]):::quit
    L & R & S & A --> M

    classDef menu fill:#212529,color:#fff,stroke:#000,stroke-width:2px
    classDef cond fill:#e2d9f3,color:#2c1559,stroke:#6f42c1,stroke-width:2px
    classDef a fill:#0d6efd,color:#fff,stroke:#084298
    classDef b fill:#20c997,color:#fff,stroke:#0f6848
    classDef c fill:#fd7e14,color:#fff,stroke:#984c0c
    classDef d fill:#6f42c1,color:#fff,stroke:#3d1a78
    classDef quit fill:#dc3545,color:#fff,stroke:#842029
```

🚀 **Bonus :** réécrire le menu avec `match` / `case`, une table des sous-réseaux et un FizzBuzz version supervision.

---

## ✅ Récapitulatif

| | À retenir |
|:-:|---|
| 📐 | des blocs délimités par `:` et l'indentation (4 espaces) |
| 🔀 | `if` / `elif` / `else` et le ternaire `a if cond else b` |
| 🧮 | comparaison (chaînable), `and` / `or` / `not`, `in`, `is None` |
| 🔁 | `while` : **tant que** ; `for` : **pour chaque élément** |
| 🔢 | `range`, `enumerate`, `zip`, `dict.items()` |
| ⏹️ | `break`, `continue`, `pass` et `else` de boucle |

➡️ **Séance 4 (TP) :** algorithmes classiques et automates à états.

---

<div align="center">

📓 **Notebook :** [`S03_lab_enonce.ipynb`](S03_lab_enonce.ipynb) · ⏮️ [Séance 2](../S02/) · ⏭️ [Séance 4](../S04/)

</div>
