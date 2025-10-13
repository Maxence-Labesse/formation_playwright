"""
EXERCICES PRATIQUES PLAYWRIGHT
===============================

À faire APRÈS avoir vu la démo principale.
Chaque exercice est progressif et commenté.
"""

from playwright.async_api import async_playwright
import asyncio
import json


# ============================================================================
# EXERCICE 1 : NAVIGATION ET EXTRACTION SIMPLE
# ============================================================================
# Objectif : Se familiariser avec Page et Locator
# Difficulté : ⭐ Facile

async def exercice_1():
    """
    Tâche : Aller sur Wikipedia et extraire :
    - Le titre de la page
    - Le premier paragraphe
    - Le nombre de sections (h2)
    
    Site : https://fr.wikipedia.org/wiki/Web_scraping
    """
    
    print("\n" + "="*60)
    print("EXERCICE 1 : Navigation et extraction simple")
    print("="*60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # TODO : Compléter le code
        await page.goto('https://fr.wikipedia.org/wiki/Web_scraping')
        
        # TODO : Extraire le titre (h1#firstHeading)
        titre = "À COMPLÉTER"
        
        # TODO : Extraire le premier paragraphe (premier p après #mw-content-text)
        premier_paragraphe = "À COMPLÉTER"
        
        # TODO : Compter les sections h2
        nombre_sections = 0
        
        print(f"Titre : {titre}")
        print(f"Premier paragraphe (50 premiers caractères) : {premier_paragraphe[:50]}...")
        print(f"Nombre de sections : {nombre_sections}")
        
        await browser.close()


# ============================================================================
# EXERCICE 2 : ITERATION SUR DES ELEMENTS
# ============================================================================
# Objectif : Parcourir une liste d'éléments
# Difficulté : ⭐⭐ Moyen

async def exercice_2():
    """
    Tâche : Scraper les 10 premières citations de quotes.toscrape.com
    Extraire pour chaque citation :
    - Le texte
    - L'auteur
    - Les tags
    
    Site : https://quotes.toscrape.com/
    """
    
    print("\n" + "="*60)
    print("EXERCICE 2 : Itération sur des éléments")
    print("="*60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        await page.goto('https://quotes.toscrape.com/')
        await page.wait_for_load_state('networkidle')
        
        # TODO : Trouver tous les blocs de citation (.quote)
        citations = []  # Liste vide à remplir
        
        # TODO : Pour chaque citation, extraire :
        # - .text (le texte de la citation)
        # - .author (le nom de l'auteur)
        # - .tags .tag (tous les tags)
        
        # Exemple de structure attendue :
        # citations = [
        #     {
        #         'texte': '...',
        #         'auteur': '...',
        #         'tags': ['tag1', 'tag2']
        #     },
        #     ...
        # ]
        
        # Afficher les résultats
        for i, citation in enumerate(citations, 1):
            print(f"\n{i}. {citation.get('texte', 'N/A')}")
            print(f"   Auteur : {citation.get('auteur', 'N/A')}")
            print(f"   Tags : {', '.join(citation.get('tags', []))}")
        
        await browser.close()


# ============================================================================
# EXERCICE 3 : INTERACTION AVEC FORMULAIRE
# ============================================================================
# Objectif : Remplir et soumettre un formulaire
# Difficulté : ⭐⭐ Moyen

async def exercice_3():
    """
    Tâche : Utiliser le formulaire de recherche de quotes.toscrape.com
    1. Cliquer sur "Login"
    2. Remplir username et password
    3. Se connecter
    4. Vérifier qu'on est bien connecté
    
    Credentials : username=admin, password=admin
    Site : https://quotes.toscrape.com/login
    """
    
    print("\n" + "="*60)
    print("EXERCICE 3 : Interaction avec formulaire")
    print("="*60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()
        
        await page.goto('https://quotes.toscrape.com/login')
        
        # TODO : Remplir le champ username
        # TODO : Remplir le champ password
        # TODO : Cliquer sur le bouton de connexion
        
        # Vérifier qu'on est connecté
        await page.wait_for_load_state('networkidle')
        
        # TODO : Vérifier la présence d'un élément qui prouve la connexion
        # (par exemple, le lien "Logout")
        
        est_connecte = False  # À MODIFIER
        
        if est_connecte:
            print("✅ Connexion réussie !")
        else:
            print("❌ Échec de connexion")
        
        await browser.close()


# ============================================================================
# EXERCICE 4 : PAGINATION
# ============================================================================
# Objectif : Naviguer sur plusieurs pages
# Difficulté : ⭐⭐⭐ Difficile

async def exercice_4():
    """
    Tâche : Scraper les citations des 3 premières pages
    Et compter le nombre total de citations
    
    Site : https://quotes.toscrape.com/
    """
    
    print("\n" + "="*60)
    print("EXERCICE 4 : Pagination")
    print("="*60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        page = await browser.new_page()
        
        toutes_citations = []
        
        # TODO : Boucle sur les 3 premières pages
        # Indices :
        # - Extraire les citations de la page actuelle
        # - Chercher le bouton "Next"
        # - Cliquer dessus
        # - Répéter
        
        await page.goto('https://quotes.toscrape.com/')
        
        for num_page in range(3):
            await page.wait_for_load_state('networkidle')
            
            # TODO : Extraire les citations de cette page
            citations_page = []  # À compléter
            
            toutes_citations.extend(citations_page)
            print(f"Page {num_page + 1} : {len(citations_page)} citations")
            
            # TODO : Cliquer sur "Next" (sauf si dernière page)
            
        print(f"\n📊 Total : {len(toutes_citations)} citations scrapées")
        
        await browser.close()


# ============================================================================
# SOLUTIONS (À DÉCOMMENTER APRÈS AVOIR ESSAYÉ)
# ============================================================================

async def solution_exercice_1():
    """Solution de l'exercice 1"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        await page.goto('https://fr.wikipedia.org/wiki/Web_scraping')
        await page.wait_for_load_state('networkidle')
        
        # Titre
        titre = await page.locator('h1#firstHeading').text_content()
        
        # Premier paragraphe
        premier_paragraphe = await page.locator('#mw-content-text p').first.text_content()
        
        # Nombre de sections
        sections = page.locator('h2')
        nombre_sections = await sections.count()
        
        print(f"Titre : {titre}")
        print(f"Premier paragraphe : {premier_paragraphe[:100]}...")
        print(f"Nombre de sections : {nombre_sections}")
        
        await browser.close()


async def solution_exercice_2():
    """Solution de l'exercice 2"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        await page.goto('https://quotes.toscrape.com/')
        await page.wait_for_load_state('networkidle')
        
        quote_elements = page.locator('.quote')
        citations = []
        
        count = await quote_elements.count()
        for i in range(min(10, count)):
            quote = quote_elements.nth(i)
            
            texte = await quote.locator('.text').text_content()
            auteur = await quote.locator('.author').text_content()
            
            # Tags
            tag_elements = quote.locator('.tags .tag')
            tag_count = await tag_elements.count()
            tags = [await tag_elements.nth(j).text_content() for j in range(tag_count)]
            
            citations.append({
                'texte': texte,
                'auteur': auteur,
                'tags': tags
            })
        
        for i, citation in enumerate(citations, 1):
            print(f"\n{i}. {citation['texte']}")
            print(f"   Auteur : {citation['auteur']}")
            print(f"   Tags : {', '.join(citation['tags'])}")
        
        await browser.close()


async def solution_exercice_4():
    """Solution de l'exercice 4"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        page = await browser.new_page()
        
        await page.goto('https://quotes.toscrape.com/')
        toutes_citations = []
        
        for num_page in range(3):
            await page.wait_for_load_state('networkidle')
            
            # Extraire citations de la page
            quotes = page.locator('.quote .text')
            quote_count = await quotes.count()
            citations_page = [await quotes.nth(i).text_content() for i in range(quote_count)]
            
            toutes_citations.extend(citations_page)
            print(f"Page {num_page + 1} : {len(citations_page)} citations")
            
            # Cliquer sur Next si pas dernière page
            if num_page < 2:
                next_button = page.locator('li.next a')
                if await next_button.is_visible():
                    await"""
EXERCICES PRATIQUES PLAYWRIGHT
===============================

À faire APRÈS avoir vu la démo principale.
Chaque exercice est progressif et commenté.
"""

from playwright.sync_api import sync_playwright
import json


# ============================================================================
# EXERCICE 1 : NAVIGATION ET EXTRACTION SIMPLE
# ============================================================================
# Objectif : Se familiariser avec Page et Locator
# Difficulté : ⭐ Facile

def exercice_1():
    """
    Tâche : Aller sur Wikipedia et extraire :
    - Le titre de la page
    - Le premier paragraphe
    - Le nombre de sections (h2)
    
    Site : https://fr.wikipedia.org/wiki/Web_scraping
    """
    
    print("\n" + "="*60)
    print("EXERCICE 1 : Navigation et extraction simple")
    print("="*60)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # TODO : Compléter le code
        page.goto('https://fr.wikipedia.org/wiki/Web_scraping')
        
        # TODO : Extraire le titre (h1#firstHeading)
        titre = "À COMPLÉTER"
        
        # TODO : Extraire le premier paragraphe (premier p après #mw-content-text)
        premier_paragraphe = "À COMPLÉTER"
        
        # TODO : Compter les sections h2
        nombre_sections = 0
        
        print(f"Titre : {titre}")
        print(f"Premier paragraphe (50 premiers caractères) : {premier_paragraphe[:50]}...")
        print(f"Nombre de sections : {nombre_sections}")
        
        browser.close()


# ============================================================================
# EXERCICE 2 : ITERATION SUR DES ELEMENTS
# ============================================================================
# Objectif : Parcourir une liste d'éléments
# Difficulté : ⭐⭐ Moyen

def exercice_2():
    """
    Tâche : Scraper les 10 premières citations de quotes.toscrape.com
    Extraire pour chaque citation :
    - Le texte
    - L'auteur
    - Les tags
    
    Site : https://quotes.toscrape.com/
    """
    
    print("\n" + "="*60)
    print("EXERCICE 2 : Itération sur des éléments")
    print("="*60)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto('https://quotes.toscrape.com/')
        page.wait_for_load_state('networkidle')
        
        # TODO : Trouver tous les blocs de citation (.quote)
        citations = []  # Liste vide à remplir
        
        # TODO : Pour chaque citation, extraire :
        # - .text (le texte de la citation)
        # - .author (le nom de l'auteur)
        # - .tags .tag (tous les tags)
        
        # Exemple de structure attendue :
        # citations = [
        #     {
        #         'texte': '...',
        #         'auteur': '...',
        #         'tags': ['tag1', 'tag2']
        #     },
        #     ...
        # ]
        
        # Afficher les résultats
        for i, citation in enumerate(citations, 1):
            print(f"\n{i}. {citation.get('texte', 'N/A')}")
            print(f"   Auteur : {citation.get('auteur', 'N/A')}")
            print(f"   Tags : {', '.join(citation.get('tags', []))}")
        
        browser.close()


# ============================================================================
# EXERCICE 3 : INTERACTION AVEC FORMULAIRE
# ============================================================================
# Objectif : Remplir et soumettre un formulaire
# Difficulté : ⭐⭐ Moyen

def exercice_3():
    """
    Tâche : Utiliser le formulaire de recherche de quotes.toscrape.com
    1. Cliquer sur "Login"
    2. Remplir username et password
    3. Se connecter
    4. Vérifier qu'on est bien connecté
    
    Credentials : username=admin, password=admin
    Site : https://quotes.toscrape.com/login
    """
    
    print("\n" + "="*60)
    print("EXERCICE 3 : Interaction avec formulaire")
    print("="*60)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        page.goto('https://quotes.toscrape.com/login')
        
        # TODO : Remplir le champ username
        # TODO : Remplir le champ password
        # TODO : Cliquer sur le bouton de connexion
        
        # Vérifier qu'on est connecté
        page.wait_for_load_state('networkidle')
        
        # TODO : Vérifier la présence d'un élément qui prouve la connexion
        # (par exemple, le lien "Logout")
        
        est_connecte = False  # À MODIFIER
        
        if est_connecte:
            print("✅ Connexion réussie !")
        else:
            print("❌ Échec de connexion")
        
        browser.close()


# ============================================================================
# EXERCICE 4 : PAGINATION
# ============================================================================
# Objectif : Naviguer sur plusieurs pages
# Difficulté : ⭐⭐⭐ Difficile

def exercice_4():
    """
    Tâche : Scraper les citations des 3 premières pages
    Et compter le nombre total de citations
    
    Site : https://quotes.toscrape.com/
    """
    
    print("\n" + "="*60)
    print("EXERCICE 4 : Pagination")
    print("="*60)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        
        toutes_citations = []
        
        # TODO : Boucle sur les 3 premières pages
        # Indices :
        # - Extraire les citations de la page actuelle
        # - Chercher le bouton "Next"
        # - Cliquer dessus
        # - Répéter
        
        page.goto('https://quotes.toscrape.com/')
        
        for num_page in range(3):
            page.wait_for_load_state('networkidle')
            
            # TODO : Extraire les citations de cette page
            citations_page = []  # À compléter
            
            toutes_citations.extend(citations_page)
            print(f"Page {num_page + 1} : {len(citations_page)} citations")
            
            # TODO : Cliquer sur "Next" (sauf si dernière page)
            
        print(f"\n📊 Total : {len(toutes_citations)} citations scrapées")
        
        browser.close()


# ============================================================================
# EXERCICE 5 : CAS RÉEL - VOTRE SITE
# ============================================================================
# Objectif : Adapter à vos propres besoins
# Difficulté : Variable

def exercice_5_template():
    """
    Template pour tester VOS propres sites
    
    Adaptez ce code à votre cas d'usage :
    - Tests de régression
    - Scraping de données
    - Monitoring
    """
    
    print("\n" + "="*60)
    print("EXERCICE 5 : Votre site")
    print("="*60)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        page = context.new_page()
        
        # TODO : Remplacer par l'URL de votre site
        url = "https://votre-site.com"
        
        print(f"🌐 Navigation vers : {url}")
        page.goto(url)
        page.wait_for_load_state('networkidle')
        
        # Exemple 1 : Tester un parcours utilisateur
        # -------------------------------------------
        # TODO : Adapter à votre parcours
        # page.get_by_role('link', name='Produits').click()
        # page.get_by_placeholder('Rechercher').fill('test')
        # etc.
        
        # Exemple 2 : Scraper des données
        # --------------------------------
        # TODO : Adapter à votre structure HTML
        # produits = page.locator('.votre-classe-produit')
        # for i in range(produits.count()):
        #     nom = produits.nth(i).locator('.nom').text_content()
        #     prix = produits.nth(i).locator('.prix').text_content()
        
        # Exemple 3 : Vérifier des éléments critiques
        # --------------------------------------------
        # TODO : Vérifier que les éléments importants sont présents
        # assert page.locator('.header').is_visible()
        # assert page.locator('.footer').is_visible()
        
        print("✅ Test terminé")
        
        # DEBUG : Pause interactive si besoin
        # page.pause()
        
        browser.close()


# ============================================================================
# EXERCICE 6 : GESTION D'ERREURS
# ============================================================================
# Objectif : Rendre le scraper robuste
# Difficulté : ⭐⭐⭐ Difficile

def exercice_6():
    """
    Tâche : Créer un scraper robuste qui gère :
    - Les timeouts
    - Les éléments manquants
    - Les erreurs de connexion
    
    Site : https://books.toscrape.com/
    """
    
    print("\n" + "="*60)
    print("EXERCICE 6 : Gestion d'erreurs robuste")
    print("="*60)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            # Navigation avec timeout
            page.goto('https://books.toscrape.com/', timeout=10000)
            page.wait_for_load_state('networkidle')
            
            produits = page.locator('.product_pod')
            
            resultats = []
            for i in range(produits.count()):
                try:
                    produit = produits.nth(i)
                    
                    # TODO : Extraire les infos avec gestion d'erreur
                    # Si un élément n'existe pas, mettre "N/A"
                    
                    titre = "N/A"
                    try:
                        titre = produit.locator('h3 a').get_attribute('title', timeout=2000)
                    except:
                        pass
                    
                    prix = "N/A"
                    try:
                        # TODO : Compléter
                        pass
                    except:
                        pass
                    
                    # TODO : Ajouter d'autres champs avec gestion d'erreur
                    
                    resultats.append({
                        'titre': titre,
                        'prix': prix
                    })
                    
                except Exception as e:
                    print(f"⚠️  Erreur produit {i} : {e}")
                    continue
            
            print(f"\n✅ {len(resultats)} produits extraits avec succès")
            
            # Sauvegarder en JSON
            with open('resultats_exercice6.json', 'w', encoding='utf-8') as f:
                json.dump(resultats, f, indent=2, ensure_ascii=False)
            print("💾 Résultats sauvegardés dans resultats_exercice6.json")
            
        except Exception as e:
            print(f"❌ Erreur critique : {e}")
        
        finally:
            browser.close()


# ============================================================================
# EXERCICE BONUS : ATTENTES ET SYNCHRONISATION
# ============================================================================
# Objectif : Maîtriser les différents types d'attentes
# Difficulté : ⭐⭐ Moyen

def exercice_bonus():
    """
    Démonstration des différentes attentes disponibles
    """
    
    print("\n" + "="*60)
    print("EXERCICE BONUS : Types d'attentes")
    print("="*60)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto('https://quotes.toscrape.com/')
        
        print("\n1️⃣ wait_for_load_state()")
        print("   Attendre que la page soit chargée")
        page.wait_for_load_state('networkidle')
        print("   ✅ Page chargée")
        
        print("\n2️⃣ wait_for_selector()")
        print("   Attendre qu'un élément apparaisse")
        page.wait_for_selector('.quote', timeout=5000)
        print("   ✅ Citations visibles")
        
        print("\n3️⃣ locator.wait_for()")
        print("   Attendre un état spécifique d'un élément")
        quote = page.locator('.quote').first
        quote.wait_for(state='visible')
        print("   ✅ Première citation visible")
        
        print("\n4️⃣ is_visible()")
        print("   Vérifier si un élément est visible (sans attendre)")
        if page.locator('.quote').is_visible():
            print("   ✅ Citations présentes")
        
        print("\n5️⃣ wait_for_timeout()")
        print("   Pause fixe (à éviter en prod, utile pour debug)")
        page.wait_for_timeout(1000)  # 1 seconde
        print("   ✅ Pause terminée")
        
        print("\n6️⃣ expect_* (pour les tests)")
        print("   Assertions avec attente automatique")
        # from playwright.sync_api import expect
        # expect(page.locator('.quote')).to_be_visible()
        print("   ℹ️  Nécessite pytest-playwright")
        
        browser.close()


# ============================================================================
# SOLUTIONS (À DÉCOMMENTER APRÈS AVOIR ESSAYÉ)
# ============================================================================

def solution_exercice_1():
    """Solution de l'exercice 1"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto('https://fr.wikipedia.org/wiki/Web_scraping')
        page.wait_for_load_state('networkidle')
        
        # Titre
        titre = page.locator('h1#firstHeading').text_content()
        
        # Premier paragraphe
        premier_paragraphe = page.locator('#mw-content-text p').first.text_content()
        
        # Nombre de sections
        sections = page.locator('h2')
        nombre_sections = sections.count()
        
        print(f"Titre : {titre}")
        print(f"Premier paragraphe : {premier_paragraphe[:100]}...")
        print(f"Nombre de sections : {nombre_sections}")
        
        browser.close()


def solution_exercice_2():
    """Solution de l'exercice 2"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto('https://quotes.toscrape.com/')
        page.wait_for_load_state('networkidle')
        
        quote_elements = page.locator('.quote')
        citations = []
        
        for i in range(min(10, quote_elements.count())):
            quote = quote_elements.nth(i)
            
            texte = quote.locator('.text').text_content()
            auteur = quote.locator('.author').text_content()
            
            # Tags
            tag_elements = quote.locator('.tags .tag')
            tags = [tag_elements.nth(j).text_content() for j in range(tag_elements.count())]
            
            citations.append({
                'texte': texte,
                'auteur': auteur,
                'tags': tags
            })
        
        for i, citation in enumerate(citations, 1):
            print(f"\n{i}. {citation['texte']}")
            print(f"   Auteur : {citation['auteur']}")
            print(f"   Tags : {', '.join(citation['tags'])}")
        
        browser.close()


def solution_exercice_4():
    """Solution de l'exercice 4"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        
        page.goto('https://quotes.toscrape.com/')
        toutes_citations = []
        
        for num_page in range(3):
            page.wait_for_load_state('networkidle')
            
            # Extraire citations de la page
            quotes = page.locator('.quote .text')
            citations_page = [quotes.nth(i).text_content() for i in range(quotes.count())]
            
            toutes_citations.extend(citations_page)
            print(f"Page {num_page + 1} : {len(citations_page)} citations")
            
            # Cliquer sur Next si pas dernière page
            if num_page < 2:
                next_button = page.locator('li.next a')
                if next_button.is_visible():
                    next_button.click()
        
        print(f"\n📊 Total : {len(toutes_citations)} citations")
        browser.close()


# ============================================================================
# MENU PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║            EXERCICES PRATIQUES PLAYWRIGHT                ║
    ╚══════════════════════════════════════════════════════════╝
    
    Choisissez un exercice :
    
    1. Navigation et extraction simple ⭐
    2. Itération sur des éléments ⭐⭐
    3. Interaction avec formulaire ⭐⭐
    4. Pagination ⭐⭐⭐
    5. Template pour votre site
    6. Gestion d'erreurs robuste ⭐⭐⭐
    7. BONUS : Types d'attentes
    
    Solutions (après avoir essayé) :
    11. Solution exercice 1
    12. Solution exercice 2
    14. Solution exercice 4
    """)
    
    choix = input("\nVotre choix : ").strip()
    
    if choix == "1":
        exercice_1()
    elif choix == "2":
        exercice_2()
    elif choix == "3":
        exercice_3()
    elif choix == "4":
        exercice_4()
    elif choix == "5":
        exercice_5_template()
    elif choix == "6":
        exercice_6()
    elif choix == "7":
        exercice_bonus()
    elif choix == "11":
        solution_exercice_1()
    elif choix == "12":
        solution_exercice_2()
    elif choix == "14":
        solution_exercice_4()
    else:
        print("❌ Choix invalide")