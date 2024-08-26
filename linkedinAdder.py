from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

print("---------------------- LINKEDIN ADDER -------------------------")
recherche = input("Entrez le domaine des personnes du réseau recherché : ")
id = input("Entrez votre identifiant LinkedIn (e-mail) : ")
mdp = str(getpass.getpass('Mot de passe : '))
ajoutsMax = input("Combien de personnes souhaitez-vous ajouter environ ? (1-100)")
# Set up Chrome options
options = Options()
# You can add more options if needed, for example:
# options.add_argument('--headless')  # Run Chrome in headless mode

# Initialize the WebDriver
service = Service()  # Specify the path to your chromedriver
driver = webdriver.Chrome(service=service, options=options)
nb_ajouts = 0
pagenb = 2

try:
    # Navigate to the LinkedIn login page
    url = "https://www.linkedin.com/search/results/people/?keywords="+recherche+"&page="+str(pagenb)+"&sid=MTY"
    driver.get(url)

    # Locate the username input field using By.ID
    element = driver.find_element(By.ID, "username")
    element.send_keys(id)  # Send keys to the username field
    time.sleep(1)

    element = driver.find_element(By.ID, "password")
    element.send_keys(mdp)  # Send keys to the username field
    time.sleep(1)

    button = driver.find_element(By.CLASS_NAME, "btn__primary--large.from__button--floating")  # Replace with the actual button ID
    button.click()

# artdeco-button artdeco-button--2 artdeco-button--secondary ember-view

    while nb_ajouts < ajoutsMax: 
        time.sleep(2)
        pagenb +=1
        buttonlist = driver.find_elements(By.CLASS_NAME, "artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view")

        for i in buttonlist : 
            aria_label = i.get_attribute("aria-label")
            if "Invitez" in str(aria_label):
                i.click()
                time.sleep(0.5)
                btnconfirm = driver.find_element(By.CLASS_NAME,"artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml1")
                btnconfirm.click()
                name = aria_label.split(" ")
                print(name[1],name[2],"à été ajouté")
                nb_ajouts += 1
                time.sleep(0.5)
        
        driver.get("https://www.linkedin.com/search/results/people/?keywords="+recherche+"&page="+str(pagenb)+"&sid=MTY")


finally:
    # Optional: Clos
    # e the browser
    driver.quit()
    print(nb_ajouts,"ajouts")
    input("Fin du programme (appuyez sur une touche pour quitter)")
