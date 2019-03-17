from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup

link = "http://www.webcrawler.com/serp?q=molestation+in+india&sc=S2UY1ybTpJXz63tuxhYYqwdh-xZ9N3bgvAJ0y-4xjNaL8OQrjPNxsn8n18XD5QlzLUvyoUf4CPkKSvhiLirBkI6xZ_PgU24UDaLGuW9DwjUvWW_X1Rp0U3WjAAip0zPTi8gvD9kFuqhmaOj3TwCYzlbk2PfMhFVCdEjCyJYUcNmA-33GByAWluJ2RawgQfxMK1lCTi-ckrYlW35IQ3ckzXssYLWdMbBZIbj4gFW_ZlpeAd6w8RXr1DfBRUwMxzjt2UpMIyYsxvq8GJSO9x6BqmEMVdmAi-aZqIfh6NeEcOW8UxTME3vtNwQdnwRZIzSHSdiTKTg8TTRfYIuOb23me9xGek0scAL66mcclXw55gbdW3krbWG22EUQBnErFptLOORGd4HtKINRjWM63oKYbYp5poc-n9GTUwJWoCrWGo6TOuyi8MlkxxGc4Gj_kP9LELfIiovDgZmkazOhR9_lXXdlFBTd4x0ZuDau3Fln87OGieOgZnvix8RvLG7mUdmiic-RLOrX1Oqw9PP_Lv7kquQcqF-w1pvfS0T3AxUAcRZSvmTF9DbVOrv9CUTC0zDL4wJLADY0UJ3yTqK2QoLRaVFPjbUMYlBRwNGQs28IGyXwr_wV0KSwNWdHYhn2I4-cBgBUvkNlDvcbbRGSWTmdSOS3LNq70VtLga91DZOT0hLfdl0EpWmFnicq8fDiWBIKYUQGv3UoJVsMtFGukADnwAoa4yDG3RfMEemGD9AT21sOZcJEg4XWYW5sTuZtbI_w8fc3PgIPYTMun6vWPFnLZ7F2uJ7ev7FDtK-fjJPnNvI92RSweafn4Nx2fmswSL8opulohl27vIKnD5phNa_VU8Nnd5HdXtvrkxjjpXxP6ZsPzich2Sx0Xpz2FGZyppORDt-LjfAyCG7EQS5myVDKvry1W5iTil7DDgZR8qOX-OXZVduJb3tW39WqgQ8XZ2dXucL4UuJIynHP2xwmuFv1PdY-3lZ05VFyUiLaVe6VL46lxDO0C4wArvsWemCE7H1gvq1ka_NpgCFil2w8cS6pvNRP6H2Qnx-gJWFGCeEMMfOXV1l2ApYbqNAAdcwrdYowxw1bQ53azc-bTT4HK_DLYU2s6xLc7JNWoPgs9c4mHZs_0fDrJB62ZCmyA9RArOev5GwxWMHtkkNDoi7T6In9vcxw2piU-Oic2v5GVbuS6i5cLudaWPGwAJic_VE7NFtI4AGSfTHQzhlk9OB0Lr1gtk-6exGphdXEmAj_tp2azlZOPmmDROJn43gv2OqPCERfTUbgZdjJfA6fKUiHIaoIU1ZUxCKOZ08Fkga8W3xcldhpgt5tXsUdoioN6QEy2fFT3VCBrqxGPwBzNTRObyNlSsbgLOvBrpvN2zhw2n05IWRKUmE6_juQVHm-6NphZ_M_2bcjIQFW3o0dwUv-CdbBPvh_fis_twAqewLwRgSwcwUi7D8Gla0ruuVFNbXgeHEvOKukqtLQtSSNihQ3YP9Bkdux086IH_TdjxBV30R4l5xlSLI&capv=xZdUHnAYHTsWlSBU11jFNhlTIEJ9C_jYsLbN31qFdUSbUT8p9AViHtzW8nHkVBM"

try:
    page = urlopen(link)
except Exception:
    print("URL not opened.")
    exit(0)

heading = []
source = []
description = []

try:
    soup = BeautifulSoup(page, 'html.parser')
    articles = soup.find_all('p', attrs={'class': 'article'})
    for i in range(len(articles)):
        p = articles[i]
        link = p.find('a')
        heading.append(link.find('span').get_text())
        span1 = p.find('span', attrs={'class': 'source'})
        source.append(span1.get_text())
        span2 = p.find('span', attrs={'class': 'description'})
        description.append(span2.get_text())
    source = [s.split(',') for s in source]
    source_link = [s[0] for s in source]
    date = [s[1] for s in source]
    print('Scrapping Done.')
except Exception:
    print("Scrapping Error.")


data = list(zip(source_link, date, heading, description))
df = pd.DataFrame(data, columns=['Source', 'Date', 'Heading', 'Description'])
df.to_csv('heading.csv', index=False, header=True)
