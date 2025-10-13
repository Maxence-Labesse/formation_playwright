"""
FORMATION PLAYWRIGHT - Script de Démonstration
===============================================

Ce script illustre les concepts essentiels de Playwright :
- Navigation et interaction avec une page web
- Utilisation des Locators pour cibler des éléments
- Extraction de données (scraping)
- Bonnes pratiques

Pour l'adapter à vos sites :
1. Changez l'URL
2. Modifiez les sélecteurs CSS/XPath selon vos besoins
3. Ajoutez vos propres interactions
"""

from playwright.async_api import async_playwright
import asyncio


async def demo_page_et_locators():
    """
    Démo des 2 objets principaux : Page et Locator
    """
    
    async with async_playwright() as p:
        # 1. LANCEMENT DU NAVIGATEUR
        # ---------------------------
        # headless=False → on voit le navigateur (utile pour debugger)
        # slow_mo=500 → ralentit les actions de 500ms (pour suivre visuellement)
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        
        # Créer un contexte (comme une session de navigation privée)
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 720},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        
        # 2. OBJET PAGE : représente un onglet du navigateur
        # ---------------------------------------------------
        page = await context.new_page()
        
        print("📍 Navigation vers Wikipedia...")
        await page.goto('https://fr.wikipedia.org/wiki/Python_(langage)')
        
        # Attendre que la page soit complètement chargée
        await page.wait_for_load_state('networkidle')
        
        
        # 3. OBJET LOCATOR : pour cibler des éléments
        # --------------------------------------------
        
        # Exemple 1 : Trouver le titre principal
        print("\n🔍 Exemple 1 : Extraire le titre")
        titre_locator = page.locator('h1#firstHeading')
        titre_text = await titre_locator.text_content()
        print(f"   Titre de la page : {titre_text}")
        
        
        # Exemple 2 : Trouver et cliquer sur un lien
        print("\n🔍 Exemple 2 : Cliquer sur un lien")
        # On cherche le lien "modifier le code" dans le sommaire
        lien_modifier = page.get_by_role('a', name='modifier le code').first
        await lien_modifier.click()
        await asyncio.sleep(2)  # Pause pour observer
        print("   → Lien cliqué !")
        
        # Revenir à la page principale
        await page.goto('https://fr.wikipedia.org/wiki/Python_(langage)')
        await asyncio.sleep(1)
        
        
        # Exemple 3 : Extraire plusieurs éléments
        print("\n🔍 Exemple 3 : Liste d'éléments")
        await page.goto('https://quotes.toscrape.com/')
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(1)  # Pause pour observer
        
        # Trouver toutes les citations
        citations_locators = page.locator('.quote .text')
        nombre_citations = await citations_locators.count()
        print(f"   Nombre de citations trouvées : {nombre_citations}")
        
        # Parcourir et afficher les 3 premières
        for i in range(min(3, nombre_citations)):
            citation = await citations_locators.nth(i).text_content()
            print(f"   Citation {i+1} : {citation}")
            await asyncio.sleep(0.5)  # Pause entre chaque citation
        
        
        # Exemple 4 : Remplir un formulaire
        print("\n🔍 Exemple 4 : Interaction avec formulaire")
        await page.goto('https://quotes.toscrape.com/login')
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(1)
        
        # Remplir le formulaire de login (credentials de test : admin/admin)
        print("   Remplissage du formulaire...")
        username_field = page.locator('#username')
        await username_field.fill('admin')
        await asyncio.sleep(0.5)
        
        password_field = page.locator('#password')
        await password_field.fill('admin')
        await asyncio.sleep(0.5)
        
        # Cliquer sur le bouton
        login_button = page.locator('input[type="submit"]')
        await login_button.click()
        
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(1)
        print("   ✅ Formulaire soumis !")
        
        
        # Exemple 5 : Attendre qu'un élément apparaisse
        print("\n🔍 Exemple 5 : Attentes explicites")
        # Vérifier qu'on est bien connecté
        logout_link = page.get_by_role('link', name='Logout')
        await logout_link.wait_for(state='visible', timeout=5000)
        print("   ✅ Connexion vérifiée (lien Logout visible)")
        await asyncio.sleep(1)
        
        
        # Pause pour observer
        print("\n⏸️  Pause de 3 secondes pour observer le résultat final...")
        await asyncio.sleep(3)
        
        # Fermeture
        await browser.close()
        print("\n✅ Démo terminée !")


async def demo_cas_usage_reel():
    """
    Exemple plus réaliste : scraper les prix d'un site e-commerce
    """
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)  # Plus lent pour suivre
        context = await browser.new_context()
        page = await context.new_page()
        
        print("🛒 Exemple e-commerce : scraping de produits")
        print("=" * 50)
        
        # Site d'exemple pour e-commerce scraping
        await page.goto('https://books.toscrape.com/')
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(1)
        
        # Extraire les produits de la première page
        produits = page.locator('.product_pod')
        nombre_produits = await produits.count()
        
        print(f"\n📦 {nombre_produits} produits trouvés\n")
        await asyncio.sleep(1)
        
        # Extraire infos des 5 premiers produits
        for i in range(min(5, nombre_produits)):
            produit = produits.nth(i)
            
            # Titre
            titre = await produit.locator('h3 a').get_attribute('title')
            
            # Prix
            prix = await produit.locator('.price_color').text_content()
            
            # Disponibilité
            dispo_raw = await produit.locator('.availability').text_content()
            dispo = dispo_raw.strip()
            
            print(f"{i+1}. {titre}")
            print(f"   Prix : {prix}")
            print(f"   Stock : {dispo}\n")
            await asyncio.sleep(0.5)  # Pause entre chaque produit
        
        await asyncio.sleep(2)
        await browser.close()
        print("✅ Scraping terminé !")


async def demo_debugging():
    """
    Techniques de debugging utiles
    """
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=800)
        page = await browser.new_page()
        
        print("🐛 Techniques de debugging")
        print("=" * 50)
        
        await page.goto('https://quotes.toscrape.com/')
        
        # 1. Screenshot
        print("\n📸 Prendre un screenshot...")
        await page.screenshot(path='debug_screenshot.png')
        print("   → Sauvegardé : debug_screenshot.png")
        
        # 2. Inspecter un élément
        print("\n🔍 Inspecter un élément...")
        quote = page.locator('.quote').first
        html = await quote.inner_html()
        print(f"   HTML : {html[:100]}...")
        
        # 3. Afficher le contenu de la page
        print("\n📄 Titre de la page :")
        title = await page.title()
        print(f"   {title}")
        
        # 4. URL actuelle
        print(f"\n🌐 URL actuelle : {page.url}")
        
        # 5. Pause interactive (utile pour debugger)
        print("\n⏸️  Pour debugger, décommentez la ligne suivante :")
        print("   await page.pause()  # Ouvre l'inspecteur Playwright")
        # await page.pause()  # ← Décommenter pour debugger interactivement
        
        await asyncio.sleep(2)
        await browser.close()


# SÉLECTEURS UTILES - CHEAT SHEET
# ================================
def exemples_selecteurs():
    """
    Exemples de sélecteurs couramment utilisés
    """
    print("""
    
📋 CHEAT SHEET DES SÉLECTEURS
=============================

1. Par ID :
   page.locator('#mon-id')

2. Par classe CSS :
   page.locator('.ma-classe')

3. Par attribut :
   page.locator('[data-testid="mon-element"]')

4. Par texte :
   page.get_by_text('Mon texte exact')
   page.get_by_text('texte partiel', exact=False)

5. Par rôle (recommandé pour accessibilité) :
   page.get_by_role('button', name='Valider')
   page.get_by_role('link', name='Accueil')

6. Par placeholder :
   page.get_by_placeholder('Entrez votre email')

7. Combinaisons :
   page.locator('div.product').locator('.price')

8. XPath (quand CSS ne suffit pas) :
   page.locator('//div[@class="product"]//span[@class="price"]')

9. Filtrer par texte :
   page.locator('.item').filter(has_text='En stock')

10. N-ième élément :
    page.locator('.item').nth(2)  # 3ème élément (index 0)
    page.locator('.item').first   # Premier
    page.locator('.item').last    # Dernier

    """)


if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║         FORMATION PLAYWRIGHT - MENU DÉMO                 ║
    ╚══════════════════════════════════════════════════════════╝
    
    Choisissez une démo :
    
    1. Démo complète : Page et Locators (recommandé pour débuter)
    2. Cas d'usage réel : Scraping e-commerce
    3. Techniques de debugging
    4. Afficher la cheat sheet des sélecteurs
    """)
    
    choix = input("\nVotre choix (1-4) : ").strip()
    
    if choix == "1":
        asyncio.run(demo_page_et_locators())
    elif choix == "2":
        asyncio.run(demo_cas_usage_reel())
    elif choix == "3":
        asyncio.run(demo_debugging())
    elif choix == "4":
        exemples_selecteurs()
    else:
        print("❌ Choix invalide")