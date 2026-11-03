<div align="center">

# 🧠 Séance 4 — TP : réalisation d'algorithmes

**Algorithmes classiques · Automates à états**

![Durée](https://img.shields.io/badge/⏱_Durée-85_min-0d6efd?style=for-the-badge)
![Niveau](https://img.shields.io/badge/Niveau-Intermédiaire+-dc3545?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GestParc](https://img.shields.io/badge/🛠_GestParc-Bonus-fd7e14?style=for-the-badge)

</div>

---

## 🎯 Objectifs

| | Compétence |
|:-:|---|
| 🔄 | Traduire un **algorithme** en Python |
| 🔢 | Implémenter **Fibonacci**, **PGCD/PPCM**, les **années bissextiles** et les **nombres premiers** |
| ⚙️ | Simuler des **automates à états** avec une table de transitions |
| 🧪 | Tester un algorithme sur des **cas connus** et des **cas limites** |

---

## 🔢 Partie 1 : algorithmes numériques (40 min)

| Algorithme | Idée clé en Python |
|---|---|
| 🌀 **Fibonacci** | `a, b = b, a + b` |
| ➗ **PGCD (Euclide)** | `while b != 0: a, b = b, a % b` |
| 🔗 **PPCM** | `a * b // pgcd` |
| 📅 **Bissextile** | `(y % 4 == 0 and y % 100 != 0) or y % 400 == 0` |
| 🔍 **Premier** | aucun diviseur `d` tel que `d * d <= n` |
| 🧹 **Crible d'Ératosthène** | barrer les multiples de `p` à partir de `p * p` |

> [!TIP]
> **Cas d'usage concret :** une sauvegarde tous les 12 jours et un audit tous les 18 jours retombent le même jour tous les **PPCM(12, 18) = 36 jours**.

---

## ⚙️ Partie 2 : automates à états (45 min)

Un automate comporte des **états**, un **état initial** et des **transitions** déclenchées par des **événements**.
En Python, on l'écrit avec une variable `state` et un dictionnaire `transitions[state][event]`.

### 🚦 Exemple : le feu tricolore avec mode clignotant

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

### 🎫 Exemple : reconnaître un numéro de ticket `INC-1234`

```mermaid
flowchart LR
    S0(("début")):::st --> |I| S1((1)):::st --> |N| S2((2)):::st --> |C| S3((3)):::st --> |"-"| D0((4)):::dg
    D0 --> |chiffre| D1((5)):::dg --> |chiffre| D2((6)):::dg --> |chiffre| D3((7)):::dg --> |chiffre| OK((("✅ OK"))):::ok
    S0 & S1 & S2 & S3 & D0 & D1 & D2 & D3 -.-> |autre| ER["❌ ERROR"]:::err

    classDef st fill:#0d6efd,color:#fff,stroke:#084298
    classDef dg fill:#6f42c1,color:#fff,stroke:#3d1a78
    classDef ok fill:#198754,color:#fff,stroke:#0b4229,stroke-width:3px
    classDef err fill:#dc3545,color:#fff,stroke:#842029
```

---

## 🏋️ Exercices

| # | Exercice | Difficulté | Notion clé |
|:-:|---|:-:|---|
| 1 | Les premiers termes de Fibonacci | ⭐ | cas limites `n = 0, 1, 2` |
| 2 | Premier terme qui dépasse un seuil | ⭐⭐ | `while` |
| 3 | PGCD et PPCM : planification de tâches | ⭐⭐ | Euclide |
| 4 | Années bissextiles 1900 à 2030 | ⭐ | conditions combinées |
| 5 | Un nombre est-il premier ? | ⭐⭐ | `d * d <= n`, `break` |
| 6 | Crible d'Ératosthène | ⭐⭐⭐ | liste de booléens |
| 7 | Feu tricolore avec mode clignotant | ⭐⭐ | table de transitions |
| 8 | Distributeur de boissons | ⭐⭐⭐ | états `IDLE` / `PAYING`, montants en millimes |
| 9 | Nombres binaires divisibles par 3 | ⭐⭐ | état = reste modulo 3 |
| 10 | Reconnaissance des numéros de ticket | ⭐⭐⭐ | automate et état `ERROR` |
| 🧩 | **Synthèse** : workflow d'un ticket d'incident | ⭐⭐⭐ | `NEW → … → CLOSED`, actions refusées |

---

## 🛠️ Projet fil rouge GestParc : bonus facultatif

Pas de nouvelle étape : les TP restent indépendants. Pour ceux qui ont terminé, **valider les numéros d'inventaire** au format `LT-001` (2 lettres connues, un tiret, puis 3 chiffres) et en déduire la catégorie.

🚀 **Pour aller plus loin :** suite de Syracuse, automate de connexion SSH (verrouillage après 3 échecs), nombres parfaits.

---

<div align="center">

📓 **Notebook :** [`S04_lab_enonce.ipynb`](S04_lab_enonce.ipynb) · ⏮️ [Séance 3](../S03/)

</div>
