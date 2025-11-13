# Equipe: Matheus Forte de Melo, Matheus Kuchenbecker, Luan ELizeu Santos, Willian Carlos Busch e Jefferson Machado

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def get_visible_result_page(driver):
	for page_id in ("page-a", "page-b"):
		page = driver.find_element(By.ID, page_id)
		if page.is_displayed():
			return page
	return None

def test_return_to_index(driver):
	wait = WebDriverWait(driver, 10)
	try:
		visible_page = wait.until(lambda drv: get_visible_result_page(drv))
		back_button = visible_page.find_element(By.CSS_SELECTOR, "button[onclick='goToIndex()']")
		back_button.click()
		wait.until(EC.visibility_of_element_located((By.ID, "page-index")))
		print("\033[32mTeste de retorno funcionou! Página inicial exibida novamente após clicar em Novo Teste.\033[0m")
	except:
		raise Exception("Teste de retorno não funcionou. Não foi possível identificar mudança e/ou botão.")

def test_flow(driver, test_value, expected_page):
	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of_element_located((By.ID, "page-index")))
	input_field = wait.until(EC.visibility_of_element_located((By.ID, "userInput")))

	input_field.clear()
	input_field.send_keys(str(test_value))

	execute_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='runTest()']")
	execute_button.click()

	if test_value > 0:
		result_section = wait.until(EC.visibility_of_element_located((By.ID, "page-a")))
		wait.until(EC.text_to_be_present_in_element((By.ID, "resultValueA"), str(test_value)))
	else:
		result_section = wait.until(EC.visibility_of_element_located((By.ID, "page-b")))
		wait.until(EC.text_to_be_present_in_element((By.ID, "resultValueB"), str(test_value)))

	actual_page_id = result_section.get_attribute("id")
	assert expected_page == actual_page_id, f"Esperado {expected_page}, porém a página exibida foi {actual_page_id}."
	assert result_section.is_displayed(), f"A seção {expected_page} não apareceu como esperado."
	print(f"\033[32mTeste com valor {test_value} confirmou a exibição da seção {expected_page}.\033[0m")


try:
	driver.get("https://matheus-forte-melo.github.io/atividade_testes_webdriver/index_ex.html")
	test_flow(driver, 10, 'page-a') # Sinta-se livre para alterar o valor para outro para forçar um teste falho.
	test_return_to_index(driver)
	test_flow(driver, -5, 'page-b')
	test_return_to_index(driver)
finally:
	driver.quit()

