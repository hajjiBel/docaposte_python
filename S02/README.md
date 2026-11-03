<div align="center">

# 🧱 Séance 2 — Syntaxe de base

**Types · f-strings · Séquences · Dictionnaires · Ensembles · Références**

![Durée](https://img.shields.io/badge/⏱_Durée-60_min-0d6efd?style=for-the-badge)
![Niveau](https://img.shields.io/badge/Niveau-Débutant+-28a745?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GestParc](https://img.shields.io/badge/🛠_GestParc-Étape_1-fd7e14?style=for-the-badge)

</div>

---

## 🎯 Objectifs

| | Compétence |
|:-:|---|
| 🔢 | Utiliser les **types de base** et les **conversions** |
| 🖨️ | Formater un affichage avec les **f-strings** |
| 📚 | Manipuler `str`, `list`, `tuple`, `range`, `dict` et `set` |
| 🔗 | Maîtriser l'**affectation par référence** et les **copies** |
| 📤 | Décomposer une séquence (**unpacking**) |

---

## 🗺️ Les structures de données de Python

```mermaid
flowchart TB
    T["🐍 Types Python"]:::root
    T --> S["🔢 Scalaires"]:::scal
    T --> Q["📚 Séquences<br/><i>ordonnées, indexables</i>"]:::seq
    T --> M["🗂️ Dictionnaire"]:::map
    T --> E["🎯 Ensemble"]:::set

    S --> S1["int · float · bool · None"]:::scal2
    Q --> Q1["str 🔒"]:::seq2
    Q --> Q2["tuple 🔒"]:::seq2
    Q --> Q3["list ✏️"]:::seq2
    Q --> Q4["range 🔒"]:::seq2
    M --> M1["dict ✏️<br/>clé → valeur"]:::map2
    E --> E1["set ✏️<br/>sans doublons"]:::set2

    classDef root fill:#212529,color:#fff,stroke:#000,stroke-width:2px
    classDef scal fill:#0d6efd,color:#fff,stroke:#084298
    classDef scal2 fill:#cfe2ff,color:#052c65,stroke:#0d6efd
    classDef seq fill:#198754,color:#fff,stroke:#0b4229
    classDef seq2 fill:#d1e7dd,color:#0a3622,stroke:#198754
    classDef map fill:#fd7e14,color:#fff,stroke:#984c0c
    classDef map2 fill:#ffe5d0,color:#653208,stroke:#fd7e14
    classDef set fill:#6f42c1,color:#fff,stroke:#3d1a78
    classDef set2 fill:#e2d9f3,color:#2c1559,stroke:#6f42c1
```

<p align="center">🔒 immuable &nbsp;·&nbsp; ✏️ modifiable</p>

---

## ⚡ Aide-mémoire

<table>
<tr><th>🖨️ f-strings</th><th>✂️ Slicing</th><th>🎯 Ensembles</th></tr>
<tr><td>

```python
f"{name:<12}"   # gauche, 12 car.
f"{x:>5.1f}"    # droite, 1 déc.
f"{load:.1%}"   # pourcentage
f"{n:,}"        # 17,400
```

</td><td>

```python
s[0]      # premier
s[-1]     # dernier
s[:10]    # 10 premiers
s[::2]    # 1 sur 2
```

</td><td>

```python
a & b   # intersection
a | b   # union
a - b   # différence
```

</td></tr>
</table>

### 🔗 Alias, copie superficielle ou copie profonde ?

```mermaid
flowchart LR
    A["b = a"]:::alias -->|"même objet"| R1["⚠️ modifier b<br/>modifie a"]:::bad
    B["b = a.copy()"]:::shallow -->|"listes internes<br/>partagées"| R2["⚠️ attention aux<br/>objets imbriqués"]:::warn
    C["b = copy.deepcopy(a)"]:::deep -->|"tout est copié"| R3["✅ indépendants"]:::ok

    classDef alias fill:#dc3545,color:#fff,stroke:#842029
    classDef shallow fill:#ffc107,color:#000,stroke:#997404
    classDef deep fill:#198754,color:#fff,stroke:#0b4229
    classDef bad fill:#f8d7da,color:#58151c,stroke:#dc3545
    classDef warn fill:#fff3cd,color:#664d03,stroke:#ffc107
    classDef ok fill:#d1e7dd,color:#0a3622,stroke:#198754
```

---

## 🏋️ Exercices

| # | Exercice | Difficulté | Notion clé |
|:-:|---|:-:|---|
| 1 | Variables typées | ⭐ | annotations, `None` |
| 2 | Lire un fichier de configuration | ⭐ | `int()`, `float()` |
| 3 | Ligne de rapport de supervision | ⭐⭐ | alignement f-string |
| 4 | Traiter une saisie | ⭐⭐ | `input`, format français |
| 5 | Découper une ligne de log | ⭐ | slicing |
| 6 | Gérer une liste de serveurs | ⭐⭐ | `append`, `insert`, `pop`, `join` |
| 7 | Dictionnaire d'équipement et ensembles | ⭐⭐ | `get`, `&`, `\|`, `-` |
| 8 | Références et copies | ⭐⭐⭐ | `deepcopy` |
| 9 | Décomposition | ⭐⭐ | `a, *rest = seq` |
| 🧩 | **Synthèse** : export de tâches projet | ⭐⭐⭐ | `split`, `set`, f-string |

---

## 🛠️ Projet fil rouge GestParc : étape 1

L'inventaire prend forme : **une liste de dictionnaires**.

```python
inventory = [
    {"asset_tag": "LT-001", "category": "laptop",  "brand": "Dell", "price": 3200.0,  "assigned_to": "Bob"},
    {"asset_tag": "SV-001", "category": "server",  "brand": "HPE",  "price": 18500.0, "assigned_to": None},
    {"asset_tag": "PR-001", "category": "printer", "brand": "HP",   "price": 950.0,   "assigned_to": "Joe"},
]
```

➡️ **Prochaine étape (S3)** : un menu console en boucle pour lister, rechercher et ajouter des équipements.

---

<div align="center">

📓 **Notebook :** [`S02_lab_enonce.ipynb`](S02_lab_enonce.ipynb) · ⏮️ [Séance 1](../S01/) · ⏭️ [Séance 3](../S03/)

</div>
