from unicodedata import numeric
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import bs4
import pandas as pd
import matplotlib as mpl
# reset defaults because we change them further down this notebook
mpl.rcParams.update(mpl.rcParamsDefault)
import matplotlib.pyplot as plt

url = 'https://www.boligportal.dk'

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")

# headless is needed here because we do not have a GUI version of firefox
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options, executable_path=r'/tmp/geckodriver')


browser.get(url)
browser.implicitly_wait(2)
button = browser.find_element_by_id('declineButton')
button.click()


search_field = browser.find_element_by_class_name("HomePageSearchBar")
search_field.send_keys('københavn')
autocompleteList = browser.find_elements_by_css_selector("#app > div.css-1w8perf > div > div > div.css-jlp53q > div.css-ahwvt > div > div > ul > li:nth-child(1)")
autocompleteList[0].click()



d= []
i = 1
go = True
while go:
    i += 1
    browser.implicitly_wait(4)
    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')
    annoncer = soup.select("#app > div:nth-child(3) > div:nth-child(1) > div > div > div.temporaryFlexColumnClassName.css-ssqjpe > div.css-lakxun > div.css-1noaovx > div")
    nextButton = browser.find_element_by_css_selector("#app > div:nth-child(3) > div:nth-child(1) > div > div > div.temporaryFlexColumnClassName.css-ssqjpe > div.css-pto9tz > div > div > button:nth-child(4)")
    nextButton.click()
    for e in annoncer:
        t = e.find("div", class_="css-do1lz2").text
        t = t.split(" · ")
        kvadratMeter = t[2].split(" ")[0]

        uploaded = e.find("span", class_="css-1bremdn").text
        pris = e.find("span", class_="css-dpmn2u").text
        pris = pris.replace("kr.", "")
        pris = pris.replace(".", "")
        
        
        print(pris)
        if "time" in uploaded or "min" in uploaded:
            data={'pris':int(pris), 'uploaded':uploaded, 'type': t[1], 'størrelse': int(kvadratMeter)}
            d.append(data)
        else:
            print("stop: ", uploaded)
            go = False
            break
            
        
    
    

df = pd.DataFrame(data=d)
typer = df.type.value_counts()

mpl.use("pdf")
plt.bar(typer.index, typer.values, width=0.5, align='center')
plt.xlabel("Type", fontsize=10)
plt.ylabel("Antal", fontsize=10)
plt.savefig('barchart.png',bbox_inches='tight')
plt.close()

df['avg_kv2_pris'] = df.pris.div(df.størrelse)

means = df.groupby('type')['avg_kv2_pris'].mean()
plt.bar(means.index, means.values, width=0.5, align='center')
plt.xlabel("Type", fontsize=10)
plt.ylabel("Gennemsnit kvm pris", fontsize=10)
plt.savefig('barchart1.png',bbox_inches='tight')
plt.close()
print(means)
print(df)
