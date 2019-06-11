from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# driver = webdriver.Chrome('drivers/chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'drivers/geckodriver.exe')
# driver = webdriver.Chrome()

driver.get("http://qa-test.avenuecode.com/")
signin = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/ul[2]/li[1]/a")
signin.click()

email = driver.find_element_by_id("user_email")
email.click
email.send_keys("gabriel.alves.moura@gmail.com")

senha = driver.find_element_by_id("user_password")
senha.click
senha.send_keys("Gabriel123")

button = driver.find_element_by_name("commit")
button.click()

""" msg = driver.find_element_by_xpath("/html/body/div[1]/div[2]")
assert msg.text == 'Signed in successfully.'
print(msg.text)
assert "ToDo Rails and Angular" in driver.title """

#criando tasks
myTask = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/ul[1]/li[2]/a")
myTask.click()

newTask = driver.find_element_by_id("new_task")
newTask.click()
newTask.send_keys("Teste 1")
newTaskAdd = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/form/div[2]/span")
newTaskAdd.click()

newTaskMin = driver.find_element_by_id("new_task")
newTaskMin.click()
newTaskMin.send_keys("12")
newTaskAdd = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/form/div[2]/span")
newTaskAdd.click()

newTaskMax = driver.find_element_by_id("new_task")
newTaskMax.click()
newTaskMax.send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis")
newTaskAdd = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/form/div[2]/span")
newTaskAdd.click()
sleep(3)

#apagando tasks criadas
dellTask = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/button")
dellTask.click()
dellTask2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td[5]/button")
dellTask2.click()
sleep(3)

#abrindo sub task
subTask1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/table/tbody/tr/td[4]/button")
subTask1.click()

descricaoSubTask = driver.find_element_by_name("new_sub_task")
descricaoSubTask.click()
descricaoSubTask.send_keys("teste descricao de sub task")

dataEntrega = driver.find_element_by_id("dueDate")
dataEntrega.click()
dataEntrega.send_keys(Keys.CONTROL, "a")
dataEntrega.send_keys("10-6-2019")
dataEntrega.send_keys(Keys.ENTER)
sleep(3)

closeSeubTask = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button")
closeSeubTask.click()
sleep(3)

#removendo subtasks
#abrir
subTask1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/table/tbody/tr/td[4]/button")
subTask1.click()
sleep(3)
#removendo
removeSubTask = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/table/tbody/tr/td[3]/button")
removeSubTask.click()
sleep(3)
#fechar as sub tarefas
closeSeubTask = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button")
closeSeubTask.click()
sleep(3)

#removendo todas tarefas
dellTask3 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/table/tbody/tr/td[5]/button")
dellTask3.click()
sleep(3)

#finish
sleep(5)
driver.close()