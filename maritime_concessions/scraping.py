from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def scrap_page() -> list:
    # Setup webdriver
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver = webdriver.Remote("http://selenium:4444/wd/hub", options=firefox_options)

    driver.get("https://www.concesionesmaritimas.cl/")

    driver.implicitly_wait(20)

    # Switch to frame and its iframe
    driver.switch_to.frame("centro_sigmar")
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    # Region
    region_element = driver.find_element(
        By.XPATH, "/html/body/font/form/center/table[1]/tbody/tr[2]/td[1]/select"
    )
    region_select = Select(region_element)
    region_select.select_by_visible_text("II")

    # Gobernación
    gob_element = driver.find_element(
        By.XPATH, "/html/body/font/form/center/table[1]/tbody/tr[4]/td[1]/select"
    )
    gob_select = Select(gob_element)
    gob_select.select_by_visible_text("GOBERNACIÓN MARÍTIMA ANTOFAGASTA")

    # Captania
    captaincy_element = driver.find_element(
        By.XPATH, "/html/body/font/form/center/table[1]/tbody/tr[6]/td/select"
    )
    captaincy_select = Select(captaincy_element)
    captaincy_select.select_by_visible_text("ANTOFAGASTA")

    # Ver listado
    captaincy_element = driver.find_element(
        By.XPATH, "/html/body/font/form/table[2]/tbody/tr[1]/td/img[2]"
    )
    captaincy_element.click()
    driver.implicitly_wait(10)

    # Pagination
    xpaths = [
        f"/html/body/font/form/p[4]/font/table/tbody/tr/td[{i}]/font/a"
        for i in range(2, 7)
    ]

    table_data = []
    for xpath in xpaths:
        # Table element
        table_element = driver.find_element(
            By.XPATH, "/html/body/font/form/div/center/table"
        )

        rows = table_element.find_elements(By.TAG_NAME, "tr")

        for row in rows[1:]:
            colunas = row.find_elements(By.TAG_NAME, "td")

            row_data = {
                "numero": colunas[0].text,
                "numero_concecion": colunas[1].text,
                "tipo_concesion": colunas[2].text,
                "comuna": colunas[3].text,
                "lugar": colunas[4].text,
                "rs_ds": colunas[5].text,
                "tipo_tramite": colunas[6].text,
                "concesionario": colunas[7].text,
                "tipo_vigencia": colunas[8].text,
            }

            # Adicionar o dicionário à lista de dados da tabela
            table_data.append(row_data)

        try:
            link = driver.find_element(
                By.XPATH,
                xpath,
            )

            link.click()
            driver.implicitly_wait(15)
        except Exception as e:
            print(e)

    driver.quit()

    return table_data
