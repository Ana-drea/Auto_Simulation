import os.path
import shutil
import sys
import argparse

Moldflow_lan_list = ["chs",
                     "cht",
                     "fra",
                     "deu",
                     "ita",
                     "jpn",
                     "kor",
                     "ptg",
                     "esn"]

LSR_tool_folder = r"C:\tools\LSReview"

if __name__ == '__main__':
    # target_folder = input("Type in the folder path you want to put the single language lpu:\n"
    #                       r"e.g.:C:\Users\AnZhou\Downloads\temp\LSReview"
    #                       "\n"
    #                       "This folder should also contain the old lpu (named like'old_All_Moldflow.lpu' and new lpu (named like'new_All_Moldflow.lpu'"
    #                       "\n")


    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default=None)
    args = parser.parse_args()
    target_folder = args.path

    for lan in Moldflow_lan_list:
        #create subfolder for each language
        lan_subfolder = os.path.join(target_folder, lan)
        if not os.path.exists(lan_subfolder):
            os.mkdir(lan_subfolder)
        #copy the necessary batch file under language subfolder
        bat_path_1 = os.path.join(LSR_tool_folder, "DiffLpuLS.bat")
        bat_path_2 = os.path.join(LSR_tool_folder, "DiffLpuWrapper.bat")
        shutil.copy(bat_path_1, lan_subfolder)
        shutil.copy(bat_path_2, lan_subfolder)
        #create old and new folder under language subfolder to put old and new lpus
        old_folder = os.path.join(lan_subfolder, "old")
        new_folder = os.path.join(lan_subfolder, "new")
        if not os.path.exists(old_folder):
            os.mkdir(old_folder)
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        #copy DiffLpuLS.bat to new folder
        shutil.copy(bat_path_1, new_folder)
        for filename in os.listdir(target_folder):
            if filename.startswith("old"):
                #copy old lpu to old folder, and rename it with 3 letter language code e.g. chs_All_Moldflow.lpu
                lpu_full_path = os.path.join(target_folder, filename)
                lpu_name_with_lan_code = lan + "_" + filename.split("old_")[1]
                lpu_destination = os.path.join(old_folder, lpu_name_with_lan_code)
                shutil.copyfile(lpu_full_path, lpu_destination)
            if filename.startswith("NEW") or filename.startswith("new"):
                # copy new lpu to new folder, and rename it with 3 letter language code e.g. chs_All_Moldflow.lpu
                lpu_full_path = os.path.join(target_folder, filename)
                lpu_name_with_lan_code = lan + "_" + filename.split("new_")[1]
                lpu_destination = os.path.join(new_folder, lpu_name_with_lan_code)
                shutil.copyfile(lpu_full_path, lpu_destination)


