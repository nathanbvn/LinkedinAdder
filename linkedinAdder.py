from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass
import subprocess

print("\n\n---------------------- LINKEDIN ADDER -------------------------")
print("----------------------------- V2 ------------------------------\n")
recherche = input("Entrez le domaine des personnes du réseau recherché : ")

id = input("Entrez votre identifiant LinkedIn (e-mail) : ")
mdp = str(getpass.getpass('Mot de passe : '))

ajoutsMax = input("Combien de personnes souhaitez-vous ajouter environ ? (1-100) ")
print("\n\n Liste des ajouts : \n")

options = Options()
options.add_argument("--log-level=3") 
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(log_output=subprocess.DEVNULL)  


driver = webdriver.Chrome(service=service, options=options)


nb_ajouts = 0
pagenb = 2

try:
   
    url = "https://www.linkedin.com/login/fr"
    driver.get(url)

   
    element = driver.find_element(By.ID, "username")
    element.send_keys(id)  
    time.sleep(0.5)

    element = driver.find_element(By.ID, "password")
    element.send_keys(mdp) 
    time.sleep(0.5)

    button = driver.find_element(By.CLASS_NAME, "btn__primary--large.from__button--floating")  
    button.click()


    driver.get("https://www.linkedin.com/search/results/people/?keywords="+recherche+"&page="+str(pagenb)+"&sid=MTY")
    
    while int(nb_ajouts) < int(ajoutsMax): 
        time.sleep(5)
        pagenb +=1
        buttonlist = driver.find_elements(By.CLASS_NAME, "ember-view")

        for i in buttonlist : 
            try :
                aria_label = i.get_attribute("aria-label")
                if "Invitez" in str(aria_label):
                    i.click()
                    time.sleep(0.5)
                    btnconfirm = driver.find_element(By.CLASS_NAME,"ml1")
                    btnconfirm.click()
                    name = aria_label.split(" ")
                    print(name[1],name[2],"à été ajouté")
                    nb_ajouts += 1
                    time.sleep(0.5)
            except :
                pass
        
        driver.get("https://www.linkedin.com/search/results/people/?keywords="+recherche+"&page="+str(pagenb)+"&sid=MTY")


finally:

    driver.quit()
    print(nb_ajouts,"ajouts")
    input("Fin du programme (appuyez sur une touche pour quitter)")
