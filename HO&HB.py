import os
import zipfile
import shutil
import subprocess
from zip_folders import zip_main


def unzip_file(path):
    fullname = os.path.basename(path)
    name = fullname.split(".zip")[0]
    targetpath = os.path.dirname(path) + "\\" + name + "\\"
    if not os.path.exists(targetpath):
        os.mkdir(targetpath)
        f = zipfile.ZipFile(path)
        f.extractall(targetpath)
        f.close()
    return targetpath


def copy_files_to_S2folders(gitpath, targetpath, project_name):
    language_list = os.listdir(gitpath)
    for language in language_list:
        srcfolder = os.path.join(gitpath, language)
        bundlesrcpath = os.path.join(srcfolder, project_name + ".tbulic18")
        reportsrcpath = os.path.join(srcfolder, project_name + "__" + language.lower() + "_Statistics.txt")
        bundletgtpath = os.path.join(targetpath, "Internal", "Source", "ADSK-SW-Translation", lan_codes.get(language))
        reporttgtpath = os.path.join(targetpath, "Internal", "Analysis", "ADSK-SW-Translation", lan_codes.get(language))
        if os.path.exists(bundlesrcpath) and os.path.exists(reportsrcpath) and os.path.exists(
                bundletgtpath) and os.path.exists(reporttgtpath):
            shutil.copy(bundlesrcpath, bundletgtpath)
            shutil.copy(reportsrcpath, reporttgtpath)
        else:
            print("invalid path" + bundlesrcpath + ", please check")


def copy_files_to_gitfolders(fromtranspath, gitpath, project_name):
    language_list = os.listdir(os.path.join(fromtranspath, "Internal", "Deliveries", "Final-Delivery"))
    if project_name == "Moldflow":
        for language in language_list:
            if language != "_Global":
                srcfolder = os.path.join(fromtranspath, "Internal", "Deliveries", "Final-Delivery", language)
                bundlesrcpath = os.path.join(srcfolder, project_name + ".tbulic18")
                bundletgtpath = os.path.join(gitpath, lan_codes_esn.get(language))
                if os.path.exists(bundlesrcpath) and os.path.exists(
                        bundletgtpath):
                    shutil.copy(bundlesrcpath, bundletgtpath)
                else:
                    print("invalid path" + bundlesrcpath + ", please check")
    else:
        for language in language_list:
            if language != "_Global":
                srcfolder = os.path.join(fromtranspath, "Internal", "Deliveries", "Final-Delivery", language)
                bundlesrcpath = os.path.join(srcfolder, project_name + ".tbulic18")
                bundletgtpath = os.path.join(gitpath, lan_codes.get(language))
                if os.path.exists(bundlesrcpath) and os.path.exists(
                        bundletgtpath):
                    shutil.copy(bundlesrcpath, bundletgtpath)
                else:
                    print("invalid path" + bundlesrcpath + ", please check")


def copy_folder(totranspath, fromtranspath):
    subfoldernames = os.listdir(totranspath)
    for name in subfoldernames:
        totranspath_new = os.path.join(totranspath, name)
        # 定义新的写入路径（就是在原来目录下拼接上文件名）
        fromtranspath_new = os.path.join(fromtranspath, name)
        # 判断该读入路径是否是文件夹，如果是文件夹则复制并执行递归
        if os.path.isdir(totranspath_new):
            # 判断写入路径中是否存在该文件夹，如果不存在就创建该文件夹
            if not os.path.exists(fromtranspath_new):
                # 创建要写入的文件夹
                os.mkdir(fromtranspath_new)
            # 执行递归函数，将文件夹中的文件复制到新创建的文件夹中（保留原始目录结构）
            copy_folder(totranspath_new, fromtranspath_new)


def copy_folder_to_fromtrans(gitfolderpath):
    totranspath = os.path.join(gitfolderpath, "totrans")
    fromtranspath = os.path.join(gitfolderpath, "fromtrans")
    if not os.path.exists(fromtranspath):
        # 创建要写入的文件夹
        os.mkdir(fromtranspath)
    copy_folder(totranspath, fromtranspath)
    return os.path.join(fromtranspath, os.listdir(fromtranspath)[0])


lan_codes = {"CHS": "zh-CN",
             "CHT": "zh-TW",
             "DEU": "de-DE",
             "ESP": "es-ES",
             "ESN": "es-ES",
             "FRA": "fr-FR",
             "ITA": "it-IT",
             "JPN": "ja-JP",
             "KOR": "ko-KR",
             "PTG": "pt-PT",
             "PTB": "pt-BR",
             "RUS": "ru-RU",
             "PLK": "pl-PL",
             "TRK": "tr-TR",
             "zh-CN": "CHS",
             "zh-TW": "CHT",
             "de-DE": "DEU",
             "es-ES": "ESP",
             "fr-FR": "FRA",
             "it-IT": "ITA",
             "ja-JP": "JPN",
             "ko-KR": "KOR",
             "pt-PT": "PTG",
             "pt-BR": "PTB",
             "ru-RU": "RUS",
             "pl-PL": "PLK",
             "tr-TR": "TRK"
             }

lan_codes_esn = {"CHS": "zh-CN",
                 "CHT": "zh-TW",
                 "DEU": "de-DE",
                 "ESP": "es-ES",
                 "ESN": "es-ES",
                 "FRA": "fr-FR",
                 "ITA": "it-IT",
                 "JPN": "ja-JP",
                 "KOR": "ko-KR",
                 "PTG": "pt-PT",
                 "PTB": "pt-BR",
                 "RUS": "ru-RU",
                 "PLK": "pl-PL",
                 "TRK": "tr-TR",
                 "zh-CN": "CHS",
                 "zh-TW": "CHT",
                 "de-DE": "DEU",
                 "es-ES": "ESN",
                 "fr-FR": "FRA",
                 "it-IT": "ITA",
                 "ja-JP": "JPN",
                 "ko-KR": "KOR",
                 "pt-PT": "PTG",
                 "pt-BR": "PTB",
                 "ru-RU": "RUS",
                 "pl-PL": "PLK",
                 "tr-TR": "TRK"
                 }

project_code = {"1": "CFD360",
                "2": "scm",
                "3": "Moldflow",
                "4": "SIM_MAT"}

host_project_path = {
    "1": r"C:\Users\AnZhou\Downloads\temp\cfd",
    "2": r"C:\Users\AnZhou\Downloads\temp\scm",
    "3": r"C:\Users\AnZhou\Downloads\temp\moldflow",
    "4": r"C:\Users\AnZhou\Downloads\temp\sim_mat"
}
guest_project_path = {
    "1": r"C:\CFD360\lpu\All\.BundleTransfer\FromTrans",
    "2": r"C:\scm\lpu\All\.BundleTransfer\FromTrans",
    "3": r"C:\new folder\Moldflow\lpu\All\.BundleTransfer\FromTrans",
    "4": r"C:\new folder\SIM_MAT\lpu\All\.BundleTransfer\FromTrans"
}


def unzip():
    # ask for the complete path of zip file and unzip it to a folder with the same name
    unzippath = input("Type in the folder path you want to unzip:")
    # return the unzipped folder path
    S2path = unzip_file(unzippath)
    print(S2path)


def handout():
    S2path = input("Type in the Symfonie folder path you want to send the bundles:\n"
                   "e.g.:C:\\Users\\\AnZhou\\\Downloads\\\Moldflow_20220520")
    gitpath = input("Type in the gitcontractor folder path you want to extract the bundles:\n"
                    "e.g.:C:\\Users\\AnZhou\\Downloads\\temp\\moldflow\\totrans\\2022-05-19")
    p_code = input("Type in the number for the project you want to copy:"
                   "1: CFD,"
                   "2: SCM,"
                   "3: Moldflow,"
                   "4: SIM_MAT")
    project_name = project_code[p_code]
    copy_files_to_S2folders(gitpath, S2path, project_name)
    zip_main(S2path)


def handback():
    p_code = input("Type in the number of the project:"
                   "1: CFD,"
                   "2: SCM,"
                   "3: Moldflow,"
                   "4: SIM_MAT")
    project_name = project_code[p_code]
    gitfolderpath = input("What's the git folder path you want to send the bundles?\n"
                          "default: %s" %(host_project_path[p_code]) ) or host_project_path[p_code]
    fromtranspath = copy_folder_to_fromtrans(gitfolderpath)
    os.startfile(os.path.join(gitfolderpath, "fromtrans"))
    sym_path = input("Type in the symfonie folder path you want to extract the bundles:\n"
                     r"e.g.:C:\Users\AnZhou\Downloads\Moldflow_20220609")
    copy_files_to_gitfolders(sym_path, fromtranspath, project_name)
    #if there're multiple date folders under fromtranspath,this will filter the latest date e.g. choose "2022-06-09" over "2022-05-11"
    path_with_date = max(os.listdir(fromtranspath))
    host_path = os.path.join(fromtranspath, path_with_date)
    guest_path = os.path.join(guest_project_path[p_code], path_with_date)
    # os.system(r"CopyFromHostToGuest.bat %s %s" %(host_path, guest_path))

choice = input("Type in the number of action you want to do:"
               "1. unzip folder"
               "2. handout process"
               "3. handback process")
if choice == "1":
    unzip()
elif choice == "2":
    handout()
elif choice == "3":
    handback()
