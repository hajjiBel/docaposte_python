<div align="center">

# 🔀 Séance 3 — Les structures de contrôle

**Conditions · Boucles · Menu interactif**

![Durée](https://img.shields.io/badge/⏱_Durée-60_min_+_bonus-0d6efd?style=for-the-badge)
![Niveau](https://img.shields.io/badge/Niveau-Intermédiaire-ffc107?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GestParc](https://img.shields.io/badge/🛠_GestParc-Étape_2-fd7e14?style=for-the-badge)

</div>

---

## 🎯 Objectifs

| | Compétence |
|:-:|---|
| 🔀 | Écrire des conditions avec `if` / `elif` / `else` et l'opérateur **ternaire** |
| 🧮 | Combiner les opérateurs de **comparaison**, **logiques**, `in` et `is` |
| 🔁 | Utiliser `while`, `for`, `range`, `enumerate` et `zip` |
| ⏹️ | Contrôler une boucle avec `break`, `continue`, `pass` et `else` |

---

## 🔀 Partie 1 : conditions

```mermaid
flowchart LR
    U(["💽 usage disque"]):::start --> C1{"≥ 90 % ?"}:::cond
    C1 -- oui --> R1["🔴 CRITICAL"]:::crit
    C1 -- non --> C2{"≥ 75 % ?"}:::cond
    C2 -- oui --> R2["🟠 WARNING"]:::warn
    C2 -- non --> R3["🟢 OK"]:::ok

    classDef start fill:#0d6efd,color:#fff,stroke:#084298
    classDef cond fill:#e2d9f3,color:#2c1559,stroke:#6f42c1,stroke-width:2px
    classDef crit fill:#dc3545,color:#fff,stroke:#842029
    classDef warn fill:#fd7e14,color:#fff,stroke:#984c0c
    classDef ok fill:#198754,color:#fff,stroke:#0b4229
```

```python
status = "disponible" if assigned_to is None else "affecté"   # ternaire
if 0 <= x < 10 and user is not None: ...                       # comparaisons chaînées
```

> [!IMPORTANT]
> Valent **faux** : `False`, `None`, `0`, `""`, `[]` et `{}`. Pour tester `None`, on écrit `is None` et non `== None`.

---

## 🔁 Partie 2 : boucles

| Outil | Usage | Exemple |
|---|---|---|
| `while` | répéter **tant que** une condition est vraie | nouvelles tentatives d'une API |
| `for … in` | parcourir une séquence | liste de serveurs |
| `range(a, b, pas)` | suite d'entiers | adresses `.50` à `.59` |
| `enumerate(seq, 1)` | index et valeur | liste numérotée |
| `zip(a, b)` | parcourir deux listes **en parallèle** | serveurs et charges |
| `break` / `continue` | sortir / passer au tour suivant | 1ʳᵉ IP libre |
| `for … else` | `else` exécuté si la boucle n'a **pas** fait de `break` | « aucune IP libre » |

---

## 🏋️ Exercices

| # | Exercice | Difficulté | Notion clé |
|:-:|---|:-:|---|
| 1 | Niveau d'alerte d'un disque | ⭐ | `if / elif / else` |
| 2 | Statut avec le ternaire | ⭐ | `a if c else b` |
| 3 | Politique de mots de passe | ⭐⭐ | `and`, `not`, `in` |
| 4 | Règles de pare-feu | ⭐⭐ | conditions combinées |
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

🚀 **Bonus :** réécrire le menu avec `match` / `case` (Python 3.10+), une table des sous-réseaux et un FizzBuzz version supervision.

➡️ **Prochaine étape (S4)** : TP d'algorithmes et d'automates à états.

---

<div align="center">

📓 **Notebook :** [`S03_lab_enonce.ipynb`](S03_lab_enonce.ipynb) · ⏮️ [Séance 2](../S02/) · ⏭️ [Séance 4](../S04/)

</div>
