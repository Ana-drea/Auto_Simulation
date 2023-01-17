import time
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions as ex
from selenium.webdriver.common.keys import Keys


def create_new_job(Project_code, day_count):
    element = wd.find_element(by=By.XPATH, value='//*[@id="specsNavBar"]/div[3]/div[2]/div[2]/button')
    element.click()
    time.sleep(1)
    # 待确认
    try:
        element = wd.find_element(By.ID, "select2-chosen-1")
        element.click()
    except ex:
        time.sleep(1)
        element = wd.find_element(By.ID, "select2-chosen-1")
        element.click()
    time.sleep(1)
    element = wd.find_element(by=By.XPATH, value='//*[@id="s2id_autogen1_search"]')
    element.send_keys("ADSK_Simulation_FY24")
    time.sleep(1)
    element = wd.find_element(by=By.XPATH, value='//*[@id="select2-results-1"]/li')
    element.click()
    time.sleep(1)

    element = wd.find_element(by=By.XPATH, value='//*[@id="createNewJobForm"]/div[2]/button[1]')
    element.click()
    time.sleep(3)

    # switch to the project detail page
    search_window = wd.current_window_handle
    element = wd.find_element(by=By.XPATH, value='//*[@id="Name"]')
    element.clear()
    time.sleep(1)
    now_time = datetime.datetime.now().strftime('_%Y%m%d')
    element.send_keys(project_name[Project_code] + now_time)
    time.sleep(1)
    element = wd.find_element(by=By.XPATH, value='//*[@id="s2id_autogen2"]')
    time.sleep(1)
    element.send_keys("SW.Translation")
    time.sleep(2)
    element = wd.find_element(by=By.XPATH, value='//*[@id="select2-drop"]/ul/li[1]')
    element.click()
    time.sleep(2)
    #Planned end date:
    result_time = add_days(day_count)
    element = wd.find_element(by=By.XPATH, value='//*[@id="DueDate"]')
    for i in range(16):
        element.send_keys(Keys.BACK_SPACE)
    element.send_keys(result_time.strftime("%m/%d/%Y 19:00"))
    time.sleep(1)

    # add target languages
    for lan in project_lan_list[Project_code]:
        # add language
        element = wd.find_element(by=By.XPATH, value='//*[@id="specs-target-languages"]')
        # clear the input
        element.clear()
        element.send_keys(lan)
        time.sleep(2)
        element = wd.find_element(by=By.XPATH,
                                  value='//*[@id="handoffForm"]/div[5]/div[2]/div[1]/div[3]/div[3]/table/tbody/tr')
        element.click()

    # click on "save" to save the settings
    time.sleep(1)
    element = wd.find_element(by=By.XPATH, value='//*[@id="handoffSaveBtn"]')
    element.click()

    # Change the project to "Order" in order to add workflows
    # status:
    element = wd.find_element(by=By.XPATH, value='//*[@id="dropdownMenuStatusId"]')
    element.click()
    time.sleep(3)

    # order:
    # element = wd.find_element(by=By.XPATH, value='//*[@id="job-menu"]/div[2]/ul/li[2]')
    element = wd.find_element(by=By.XPATH, value='//*[@id="job-menu"]/div[2]/ul/li[2]/a')
    element.click()
    time.sleep(1)

    # uncheck notify checkbox:
    element = wd.find_element(by=By.XPATH, value='//*[@id="CanSendJobNotificationModal"]')
    if element.is_selected():
        element.click()
        time.sleep(1)
    time.sleep(1)

    # save the change
    element = wd.find_element(by=By.XPATH, value='//*[@id="handoffActionConfirm"]')
    element.click()
    time.sleep(3)


def create_workflow(Project_code, day_count):
    # jump to the Workflows page:
    search_window = wd.current_window_handle
    element = wd.find_element(by=By.XPATH, value='//*[@id="handoffWorkflowBeta"]')
    element.click()
    # click on "create workflows" dropdown:
    element = wd.find_element(by=By.XPATH, value='//*[@id="workflowTable"]/div[1]/div[4]/div/button[2]')
    element.click()
    time.sleep(1)
    # select the workflow template "SW-SIM_MAT":
    element = wd.find_element(by=By.XPATH, value='//*[@id="workflowTable"]/div[1]/div[4]/div/ul/li[5]')
    element.click()
    time.sleep(1)

    # click "Add all" to add all target languages:
    element = wd.find_element(by=By.XPATH,
                              value='//*[@id="CreateWorfklowFromTemplate"]/form/div[2]/div[4]/div/div[1]/div[3]/div[1]/small/button')
    element.click()
    time.sleep(1)
    # select the "name" input box, clear its content, and type in the name of the workflow:
    element = wd.find_element(By.CSS_SELECTOR, ".form-group > #Name")
    element.clear()
    element.send_keys("SW-" + project_abbre_name[Project_code] + "-2024")
    time.sleep(1)
    # click on "create" to create workflow:
    element = wd.find_element(by=By.XPATH, value='//*[@id="CreateWorfklowFromTemplate"]/form/div[3]/button[1]')
    element.click()
    time.sleep(3)

    # ADSK-SW-Translation workflow:
    result_time = add_days(day_count)
    #planned end date:
    element = wd.find_element(by=By.XPATH, value='//*[@id="CustomWorkflow_Activity_PlannedEnd"]')
    for i in range(16):
        element.send_keys(Keys.BACK_SPACE)
    element.send_keys(result_time.strftime("%m/%d/%Y 18:00"))
    time.sleep(1)
    #requestor:
    js1 = 'document.querySelector("#s2id_CustomWorkflow_AdvancedAssignment_Component_RequestorIds > ul > li.select2-search-choice > a").click()'
    wd.execute_script(js1)
    element = wd.find_element(by=By.XPATH, value='//*[@id="s2id_autogen2"]')
    element.send_keys("andrea zhou")
    time.sleep(1)
    element = wd.find_element(by=By.XPATH, value='//*[@id="select2-drop"]/ul/li')
    element.click()
    time.sleep(3)

    # Asignees, check "by preference":
    element = wd.find_element(by=By.XPATH,
                              value='//*[@id="WorkflowTaskForm"]/form/div[2]/div[4]/div[2]/div/div[1]/div[1]/label[2]/input')
    element.click()
    time.sleep(1)
    # click "save and next":
    element = wd.find_element(by=By.XPATH, value='//*[@id="WorkflowTaskForm"]/form/div[3]/button[1]')
    element.click()
    time.sleep(1)

    #final delivery workflow:
    time.sleep(2)
    #planned start date:
    element = wd.find_element(by=By.XPATH, value='//*[@id="CustomWorkflow_Activity_PlannedStart"]')
    for i in range(16):
        element.send_keys(Keys.BACK_SPACE)
    element.send_keys(result_time.strftime("%m/%d/%Y 18:00"))
    time.sleep(1)
    #planned end date:
    element = wd.find_element(by=By.XPATH, value='//*[@id="CustomWorkflow_Activity_PlannedEnd"]')
    for i in range(16):
        element.send_keys(Keys.BACK_SPACE)
    element.send_keys(result_time.strftime("%m/%d/%Y 19:00"))
    time.sleep(1)

    # requestor:
    js1 = 'document.querySelector("#s2id_CustomWorkflow_AdvancedAssignment_Component_RequestorIds > ul > li.select2-search-choice > a").click()'
    wd.execute_script(js1)
    element = wd.find_element(by=By.XPATH, value='//*[@id="s2id_autogen7"]')
    element.send_keys("andrea zhou")
    time.sleep(1)
    element = wd.find_element(by=By.XPATH, value='//*[@id="select2-drop"]/ul/li')
    element.click()
    time.sleep(1)
    # Asignees, type in and choose myself:
    element = wd.find_element(by=By.XPATH, value='//*[@id="s2id_autogen10"]')
    element.send_keys("andrea zhou")
    time.sleep(1)
    element = wd.find_element(by=By.XPATH, value='//*[@id="select2-drop"]/ul/li')
    element.click()
    # click on "Save":
    element = wd.find_element(by=By.XPATH, value='//*[@id="WorkflowTaskForm"]/form/div[3]/button[1]')
    element.click()
    time.sleep(3)
    # click on "Attachments":
    element = wd.find_element(by=By.XPATH, value='//*[@id="handoffAttachments"]')
    element.click()
    time.sleep(2)
    # jump to the Attachments page:
    search_window = wd.current_window_handle
    # click on "download only folders":
    element = wd.find_element(by=By.XPATH, value='//*[@id="jobAttachmentsTable"]/div[1]/div[3]/button[2]')
    element.click()


CFD_lan_list = ["Chinese (China)",
                "Chinese (Taiwan)",
                "Korean (Korea)",
                "French (France)",
                "Japanese (Japan)",
                "Russian (Russia)",
                "German (Germany)",
                "Italian (Italy)"]

INV_Nastran_lan_list = ["Chinese (China)",
                        "Chinese (Taiwan)",
                        "French (France)",
                        "German (Germany)",
                        "Italian (Italy)",
                        "Japanese (Japan)",
                        "Korean (Korea)"]

Moldflow_lan_list = ["Chinese (China)",
                     "Chinese (Taiwan)",
                     "French (France)",
                     "German (Germany)",
                     "Italian (Italy)",
                     "Japanese (Japan)",
                     "Korean (Korea)",
                     "Portuguese (Portugal)",
                     "Spanish (Spain)"]

SCM_lan_list = ["Chinese (China)",
                "Chinese (Taiwan)",
                "French (France)",
                "German (Germany)",
                "Italian (Italy)",
                "Japanese (Japan)",
                "Korean (Korea)",
                "Portuguese (Portugal)",
                "Russian (Russia)",
                "Spanish (Spain)"]

SIM_MAT_lan_list = ["Chinese (China)",
                    "Chinese (Taiwan)",
                    "French (France)",
                    "German (Germany)",
                    "Italian (Italy)",
                    "Japanese (Japan)",
                    "Korean (Korea)",
                    "Portuguese (Portugal)",
                    "Spanish (Spain)"]

project_lan_list = {"1": CFD_lan_list,
                    "2": INV_Nastran_lan_list,
                    "3": Moldflow_lan_list,
                    "4": SCM_lan_list,
                    "5": SIM_MAT_lan_list}

project_name = {"1": "CFD",
                "2": "INV_Nastran",
                "3": "Moldflow",
                "4": "SCM",
                "5": "SIM_MAT"}

project_abbre_name = {"1": "CFD",
                      "2": "INV_NAS",
                      "3": "MF",
                      "4": "SCM",
                      "5": "SM"}

#input: string, day_count e.g.:"3"
#output: datetime, result_time e.g.: 2022-06-01 14:27:22.909090
def add_days(day_count):
    result_time = datetime.datetime.now()
    i = 0
    while i < int(day_count):
        if (result_time+datetime.timedelta(days=1)).isoweekday()<6:
            i += 1
        result_time += datetime.timedelta(days=1)
    # result_time_s = result_time.strftime("%m/%d/%Y 18:00")
    return result_time






Project_code = input("Please choose the number of project to create job:\n"
                     "1. CFD\n"
                     "2. INV_Nastran\n"
                     "3. Moldflow\n"
                     "4. SCM\n"
                     "5. SIM_MAT\n")

day_count = input("In how many days do you expect your bundles back?")
print(add_days(day_count).strftime("%m/%d/%Y 18:00"))

# in company network, no need to type in username and password
wd = webdriver.Chrome(service=Service(r'C:\Users\AnZhou\Downloads\chromedriver_win32\chromedriver.exe'))
# wd.get("https://projects.moravia.com/jobs/1776411/workflows")
#go to ADSK_Simulation_FY23
# wd.get("https://projects.moravia.com/projects/44930/jobs")
wd.get("https://projects.moravia.com/projects/45315/jobs")

time.sleep(50)

create_new_job(Project_code, day_count)
create_workflow(Project_code, day_count)
