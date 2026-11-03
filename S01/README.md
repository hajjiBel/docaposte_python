<div align="center">

# 🐍 Séance 1 — Premiers pas avec Python

**Installer son environnement · Exécuter du code · Écrire ses premières variables**

![Durée](https://img.shields.io/badge/⏱_Durée-60_min-0d6efd?style=for-the-badge)
![Niveau](https://img.shields.io/badge/Niveau-Débutant-28a745?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GestParc](https://img.shields.io/badge/🛠_GestParc-Étape_0-fd7e14?style=for-the-badge)

</div>

---

## 🎯 Objectifs

| | Compétence |
|:-:|---|
| 🧰 | Installer **Python**, un **IDE**, un **venv** et **JupyterLab** |
| ▶️ | Exécuter du code dans le **REPL**, un **script** et un **notebook** |
| ✍️ | Écrire des instructions, des **commentaires** et des **variables** |
| 🚨 | Lire un **message d'erreur** |

---

## 🗺️ Déroulé du lab

```mermaid
flowchart LR
    A["🧰 Partie 1<br/>Installation<br/><i>30 min</i>"]:::p1 --> B["✍️ Partie 2<br/>Instructions & variables<br/><i>30 min</i>"]:::p2
    B --> C["🧩 Synthèse<br/>Analyse de logs"]:::syn
    C --> D["🛠️ GestParc<br/>Étape 0 : bannière"]:::proj
    D --> E["🚀 Bonus<br/>import this, help()"]:::bonus

    classDef p1 fill:#0d6efd,color:#fff,stroke:#084298,stroke-width:2px
    classDef p2 fill:#20c997,color:#fff,stroke:#0f6848,stroke-width:2px
    classDef syn fill:#6f42c1,color:#fff,stroke:#3d1a78,stroke-width:2px
    classDef proj fill:#fd7e14,color:#fff,stroke:#984c0c,stroke-width:2px
    classDef bonus fill:#ffc107,color:#000,stroke:#997404,stroke-width:2px
```

---

## 🧰 Partie 1 : la chaîne d'installation

```mermaid
flowchart LR
    P["🐍 Python 3.12+"]:::a --> V["📦 venv<br/><code>.venv</code>"]:::b --> I["💻 VS Code / PyCharm"]:::c --> J["📓 JupyterLab"]:::d

    classDef a fill:#3776AB,color:#fff,stroke:#1d3f61
    classDef b fill:#198754,color:#fff,stroke:#0b4229
    classDef c fill:#0dcaf0,color:#000,stroke:#087990
    classDef d fill:#f37626,color:#fff,stroke:#8a3d0c
```

> [!TIP]
> Sous Windows, cochez **« Add python.exe to PATH »** dans l'installeur. Sous Linux, n'utilisez jamais `sudo pip install` : installez les paquets **dans un venv**.

---

## ✍️ Partie 2 : l'essentiel en un coup d'œil

```python
# Un commentaire commence par #
hostname = "srv-web-01"        # affectation : nom = valeur (snake_case)
disk_free_gb = 512 - 389       # opérateurs : +  -  *  /  //  %  **
print("Libre :", disk_free_gb) # print affiche plusieurs valeurs
```

| Opérateur | Rôle | Exemple | Résultat |
|:-:|---|---|:-:|
| `/` | division décimale | `7 / 2` | `3.5` |
| `//` | division entière | `7 // 2` | `3` |
| `%` | reste (modulo) | `7 % 2` | `1` |
| `**` | puissance | `2 ** 32` | `4294967296` |

---

## 🏋️ Exercices

| # | Exercice | Difficulté | Notion clé |
|:-:|---|:-:|---|
| 1 | Durée d'une séance | ⭐ | calculs simples |
| 2 | Taux d'occupation d'un disque | ⭐ | pourcentage, `/` |
| 3 | Budget d'achat de postes (TVA 19 %) | ⭐⭐ | HT / TVA / TTC |
| 4 | Basculement de serveurs | ⭐⭐ | échange avec `temp` |
| 5 | Corriger les noms de variables | ⭐⭐ | `SyntaxError`, mots réservés |
| 6 | Lire un message d'erreur | ⭐⭐⭐ | `NameError`, casse |
| 🧩 | **Synthèse** : durée d'analyse d'un fichier de logs | ⭐⭐⭐ | `//`, `%`, conversions de durée |

> [!NOTE]
> Chaque exercice est suivi d'une cellule **✅ Vérification**. S'il n'y a pas d'`AssertionError`, la réponse est correcte. Des indices 💡 sont repliés sous chaque énoncé.

---

## 🛠️ Projet fil rouge GestParc : étape 0

```text
gestparc/
├── .venv/
├── README.md
└── main.py   →   ========================================
                  GestParc v0.1.0
                  Gestion de parc informatique
                  Auteur : Votre nom
                  ========================================
```

➡️ **Prochaine étape (S2)** : représenter l'inventaire avec des listes, des tuples et des dictionnaires.

---

<div align="center">

📓 **Notebook :** [`S01_lab_enonce.ipynb`](S01_lab_enonce.ipynb) · ⏭️ [Séance 2](../S02/)

</div>
