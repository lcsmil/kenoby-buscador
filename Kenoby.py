from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buscaKenoby(cidade):
    data = {}
    for link in links:
        try:
            driver.get(link)
            element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "result-position")))
            html = driver.page_source
            soup = BeautifulSoup(html)
            for i in cidade:
                links2 = soup.find_all("a", attrs={'data-city':str(i)})
                data2 = {}
                for link2 in links2:
                    title2 = link2.string
                    data2[title2] = link2.get_text()
                    print(link + " - " + str(i))
        except:
            pass
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found")

driver = webdriver.Chrome(executable_path=r'C:\lucas\Documents\Python\chromedriver.exe')
  
try:
    # to search 
    query = "site:jobs.kenoby.com"

    links = []

    for j in search(query, tld="com", num=10, stop=150, pause=10, lang="pt-BR"): 
        links.append(j)
        print(j)

except:
    #to read txt
    print("blocked by Google")
    try:
        f = open("listakenoby.txt")
        for line in f:
            line = line.strip('\n')
            links.append(line)
    finally:
        f.close()

cidade= []
cidade.append("Curitiba")
cidade.append("São José dos Campos")
cidade.append("Jacareí")
cidade.append("Colombo")
cidade.append("São José dos Pinhais")
cidade.append("Pinhais")
cidade.append("Caçapava")
buscaKenoby(cidade)

