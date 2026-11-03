<div align="center">

# 🧠 Séance 4 — TP : réalisation d'algorithmes

**Méthode · Algorithmes classiques · Automates à états**

![Durée](https://img.shields.io/badge/⏱_Lab-85_min-0d6efd?style=for-the-badge)
![Niveau](https://img.shields.io/badge/Niveau-Intermédiaire+-dc3545?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GestParc](https://img.shields.io/badge/🛠_GestParc-Bonus-fd7e14?style=for-the-badge)

</div>

---

## 🎯 Objectifs de la séance

| | Compétence |
|:-:|---|
| 🔄 | Traduire un **algorithme** en Python avec des variables, des conditions et des boucles |
| 🔢 | Implémenter **Fibonacci**, le **PGCD**, les **années bissextiles** et les **nombres premiers** |
| ⚙️ | Modéliser et simuler des **automates à états** : feu tricolore, distributeur, reconnaissance de chaînes |
| 🧪 | **Tester** systématiquement son code sur des cas connus |

---

## 🗺️ Déroulé du TP

```mermaid
flowchart LR
    Q["🧠 Quiz flash"]:::quiz --> M["📖 Méthode +<br/>rappels numériques"]:::th
    M --> P1["🧪 Partie 1 · 40 min<br/>Fibonacci, PGCD,<br/>bissextiles, premiers"]:::lab
    P1 --> A["📖 Les automates<br/>à états"]:::th
    A --> P2["🧪 Partie 2 · 45 min<br/>feu, distributeur,<br/>chaînes, synthèse"]:::lab
    P2 --> B["✅ Bilan"]:::rec

    classDef quiz fill:#ffc107,color:#000,stroke:#997404,stroke-width:2px
    classDef th fill:#0d6efd,color:#fff,stroke:#084298,stroke-width:2px
    classDef lab fill:#20c997,color:#fff,stroke:#0f6848,stroke-width:2px
    classDef rec fill:#6f42c1,color:#fff,stroke:#3d1a78,stroke-width:2px
```

<details>
<summary><b>🧠 Quiz flash : révision de la séance 3</b> (cliquer pour voir les réponses)</summary>

| Question | Réponse |
|---|---|
| Que vaut `"ERROR" in "2026-10-21 ERROR disk full"` ? | `True` (recherche de sous-chaîne) |
| Corriger `if level == "ERROR" or "FATAL":` | `if level in ("ERROR", "FATAL"):` |
| Quand le `else` d'une boucle `for` s'exécute-t-il ? | quand la boucle se termine **sans `break`** |
| Qu'affiche `for i, s in enumerate(["a", "b"], start=1): print(i, s)` ? | `1 a` puis `2 b` |
| `msg` vaut `"pair"` si `n` est pair, sinon `"impair"` | `msg = "pair" if n % 2 == 0 else "impair"` |

</details>

---

## 🧭 La méthode de travail

```mermaid
flowchart LR
    C["🤔 Comprendre<br/>reformuler, choisir<br/>des exemples connus"]:::s1 --> E["📝 Écrire<br/>l'algorithme en<br/>pseudo-code"]:::s2 --> T["🐍 Traduire<br/>en Python, par<br/>petites étapes"]:::s3 --> V["🧪 Tester<br/>cas normal +<br/>cas limites"]:::s4 --> R["🔍 Relire<br/>noms explicites,<br/>pas de doublons"]:::s5

    classDef s1 fill:#0d6efd,color:#fff,stroke:#084298
    classDef s2 fill:#6610f2,color:#fff,stroke:#3d0a91
    classDef s3 fill:#3776AB,color:#fff,stroke:#1d3f61
    classDef s4 fill:#d63384,color:#fff,stroke:#801f4f
    classDef s5 fill:#198754,color:#fff,stroke:#0b4229
```

> [!TIP]
> Les **cas limites** à tester : `0`, `1`, les valeurs négatives et la liste vide. Les cellules ✅ du notebook jouent le rôle de tests ; en S15, nous écrirons de vrais **tests unitaires**.

---

## 🔢 Partie 1 : algorithmes numériques (40 min)

| Algorithme | 💡 Idée clé | 🐍 En Python |
|---|---|---|
| 🌀 **Fibonacci** | F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) | `a, b = b, a + b` |
| ➗ **PGCD (Euclide)** | pgcd(a, b) = pgcd(b, a % b) jusqu'à ce que b = 0 | `while b != 0: a, b = b, a % b` |
| 🔗 **PPCM** | se déduit du PGCD | `a * b // pgcd` |
| 📅 **Bissextile** | divisible par 4 et pas par 100, **ou** divisible par 400 | `(y % 4 == 0 and y % 100 != 0) or y % 400 == 0` |
| 🔍 **Premier** | aucun diviseur entre 2 et √n | tester `d * d <= n` |
| 🧹 **Crible d'Ératosthène** | barrer les multiples de chaque premier | à partir de `p * p` |

<table>
<tr><th>➗ Euclide pas à pas : PGCD(1071, 462)</th><th>🌀 Fibonacci</th></tr>
<tr><td>

| a | b | a % b |
|:-:|:-:|:-:|
| 1071 | 462 | 147 |
| 462 | 147 | 21 |
| 147 | 21 | 0 |
| **21** | 0 | ✅ |

</td><td>

```python
a, b = 0, 1
fib = []
for _ in range(10):
    fib.append(a)
    a, b = b, a + b
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

</td></tr>
</table>

> [!NOTE]
> **Cas d'usage concret :** une sauvegarde tous les 12 jours et un audit tous les 18 jours retombent le même jour tous les **PPCM(12, 18) = 36 jours**.

---

## ⚙️ Partie 2 : automates à états (45 min)

Un automate, c'est un **ensemble d'états**, un **état initial** et des **transitions** déclenchées par des **événements**.
En Python, l'**état courant** est rangé dans une variable et les **transitions** dans un dictionnaire.

### 🚦 Le feu tricolore avec mode clignotant

```mermaid
stateDiagram-v2
    direction LR
    [*] --> RED
    RED --> GREEN : tick (30 s)
    GREEN --> ORANGE : tick (25 s)
    ORANGE --> RED : tick (5 s)
    RED --> BLINKING : fault
    GREEN --> BLINKING : fault
    ORANGE --> BLINKING : fault
    BLINKING --> RED : repair

    classDef red fill:#dc3545,color:#fff,stroke:#842029,stroke-width:2px
    classDef green fill:#198754,color:#fff,stroke:#0b4229,stroke-width:2px
    classDef orange fill:#fd7e14,color:#fff,stroke:#984c0c,stroke-width:2px
    classDef blink fill:#ffc107,color:#000,stroke:#997404,stroke-width:2px
    class RED red
    class GREEN green
    class ORANGE orange
    class BLINKING blink
```

```python
transitions = {
    "RED":    ("GREEN", 30),   # état suivant, durée de l'état courant
    "GREEN":  ("ORANGE", 25),
    "ORANGE": ("RED", 5),
}
state, elapsed = "RED", 0
for step in range(4):
    next_state, duration = transitions[state]
    print(f"t={elapsed:>3}s : {state} pendant {duration}s")
    elapsed += duration
    state = next_state
```

```text
t=  0s : RED pendant 30s
t= 30s : GREEN pendant 25s
t= 55s : ORANGE pendant 5s
t= 60s : RED pendant 30s
```

### 🎫 Reconnaître un numéro de ticket `INC-` suivi de 4 chiffres

```mermaid
flowchart LR
    S0(("START")):::st --> |I| S1(("I")):::st --> |N| S2(("N")):::st --> |C| S3(("C")):::st --> |"-"| DA(("DASH")):::st
    DA --> |chiffre| D1(("D1")):::dg --> |chiffre| D2(("D2")):::dg --> |chiffre| D3(("D3")):::dg --> |chiffre| D4((("✅ D4"))):::ok
    S0 & S1 & S2 & S3 & DA & D1 & D2 & D3 & D4 -.-> |autre| ER["❌ ERROR"]:::err

    classDef st fill:#0d6efd,color:#fff,stroke:#084298
    classDef dg fill:#6f42c1,color:#fff,stroke:#3d1a78
    classDef ok fill:#198754,color:#fff,stroke:#0b4229,stroke-width:3px
    classDef err fill:#dc3545,color:#fff,stroke:#842029
```

| État | Caractère lu | Nouvel état |
|---|---|---|
| `START` | `I` | `I` |
| `I` | `N` | `N` |
| `N` | `C` | `C` |
| `C` | `-` | `DASH` |
| `DASH`, `D1`, `D2`, `D3` | un chiffre | `D1`, `D2`, `D3`, `D4` |
| tout autre cas | … | `ERROR` (état absorbant) |

> [!IMPORTANT]
> La chaîne est **acceptée** si l'automate termine dans l'état **`D4`**. Exemple : `INC-2048` ✅, `INC-20A8` ❌, `INC-20481` ❌.

---

## 🏋️ Exercices du lab

| # | Exercice | Difficulté | Notion clé |
|:-:|---|:-:|---|
| 1 | Les n premiers termes de Fibonacci | ⭐ | cas limites `n = 0, 1, 2` |
| 2 | Premier terme qui dépasse un seuil | ⭐⭐ | `while` |
| 3 | PGCD et PPCM : planification de tâches | ⭐ / ⭐⭐ | Euclide |
| 4 | Années bissextiles de 1900 à 2030 | ⭐ | conditions combinées |
| 5 | Un nombre est-il premier ? | ⭐⭐ | `d * d <= n`, `break` |
| 6 | Crible d'Ératosthène | ⭐⭐⭐ | liste de booléens |
| 7 | Feu tricolore avec mode clignotant | ⭐⭐ | table de transitions |
| 8 | Distributeur de boissons (monnaie, rendu) | ⭐⭐⭐ | états `IDLE` / `PAYING`, montants en millimes |
| 9 | Nombres binaires divisibles par 3 | ⭐⭐ | état = reste modulo 3 |
| 10 | Reconnaissance des numéros de ticket | ⭐⭐⭐ | automate et état `ERROR` |
| 🧩 | **Synthèse** : workflow d'un ticket d'incident | ⭐⭐⭐ | `NEW → … → CLOSED`, actions refusées |

---

## 🛠️ Projet fil rouge GestParc : bonus facultatif

Pas de nouvelle étape : les TP restent indépendants. Pour ceux qui ont terminé, **validez les numéros d'inventaire** au format `LT-001` (2 lettres connues, un tiret, 3 chiffres) et déduisez-en la catégorie.

🚀 **Pour aller plus loin :** suite de Syracuse, automate de connexion SSH (verrouillage après 3 échecs), nombres parfaits.

---

## ✅ Bilan du TP

| | À retenir |
|:-:|---|
| 🧪 | un algorithme se teste sur des **cas connus** et des **cas limites** |
| 🔄 | le motif `a, b = b, a + b` évite les variables temporaires |
| 🔁 | `while` convient quand on **ne connaît pas** le nombre de tours (Euclide, seuil) |
| ⚙️ | un automate = **état courant** + **table de transitions** (dictionnaire) |
| 🔁 | le code de cette séance contient beaucoup de **répétitions**… |

➡️ **Séance 5 :** les **fonctions**, pour rendre ces algorithmes réutilisables.

---

<div align="center">

📓 **Notebook :** [`S04_lab_enonce.ipynb`](S04_lab_enonce.ipynb) · ⏮️ [Séance 3](../S03/)

</div>
