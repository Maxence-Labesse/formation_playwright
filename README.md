# Formation Playwright

Formation interne sur Playwright pour le scraping et les tests automatisés.

## 🚀 Installation

```bash
# Cloner le repo
git clone <url-du-repo>
cd formation-playwright

# Créer et activer le venv
python -m venv venv

# Windows :
venv\Scripts\activate
# Mac/Linux :
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Installer les navigateurs Playwright
playwright install
```

## 📚 Utilisation

### 1. Démos interactives

```bash
python demo_playwright.py
```

Choisir une option :
- **1** : Démo complète (recommandé pour débuter)
- **2** : Cas e-commerce
- **3** : Debugging
- **4** : Cheat sheet sélecteurs

### 2. Exercices pratiques

```bash
python exercices_pratiques.py
```

4 exercices progressifs + solutions.

## 🎯 Objectifs

1. **Maintenance** : Comprendre et maintenir les scrapers du projet
2. **Tests** : Automatiser des parcours clients sur vos interfaces
3. **Debug collaboratif** : Debugger ensemble à distance
4. **Culture tech** : Maîtriser le scraping moderne

## 📖 Documentation complète

Voir `README_FORMATION_PLAYWRIGHT.md` pour :
- Concepts détaillés (Page, Locator)
- Exemples adaptés à vos sites
- Techniques de debugging
- Bonnes pratiques
- FAQ

## 🔧 Structure

```
formation-playwright/
├── demo_playwright.py              # Démos interactives
├── exercices_pratiques.py          # 4 exercices + solutions
├── README_FORMATION_PLAYWRIGHT.md  # Doc complète
├── requirements.txt                # Dépendances
└── .gitignore
```

## 💡 Premiers pas

1. Lancer `python demo_playwright.py` → option 1
2. Observer le navigateur et les logs
3. Lire le code commenté dans `demo_playwright.py`
4. Faire les exercices dans l'ordre

## 📖 Ressources

- **API Locator** : https://playwright.dev/python/docs/api/class-locator
- **Documentation Playwright** : https://playwright.dev/python/

---

**Questions ?** Consultez la doc complète ou demandez en équipe.