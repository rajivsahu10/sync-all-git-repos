import subprocess
import yaml
import pprintpp
from icecream import ic
from pathlib import Path
from prettytable import PrettyTable

with open('config.yaml', 'r') as configFile:
    config = yaml.safe_load(configFile)

location = config['location']
print("-"*100)
pprintpp.pprint(location)
print("-"*100)

reposPath = Path(location)
x = PrettyTable()
x.field_names = ["Directory", "Is a Git Repo"]
if not reposPath.is_dir():
    print("Please configure the repository parent location correctly in config file")

for currentDir in reposPath.iterdir():
    gitPath = currentDir.joinpath(".git")
    isGitDir = "No"
    if gitPath.exists():
        isGitDir = "Yes"
    # print(f"Directory : {currentDir} :  {isGitDir}")
    x.add_row([currentDir, isGitDir])

x.align = "l"
ic(x)


# exit(0)
# obj = os.scandir("D:/workspacePython")
# currentDir = os.getcwd()
#
# print(f"current : {currentDir}")
#
# # List all files and directories in the specified path
# # print("Files and Directories in '% s':" % )
# for entry in obj:
#     if entry.is_dir() or entry.is_file():
#         folder = os.path.join(currentDir, entry.name)
#         gitFolder = os.path.join(folder, ".git")
#         isGitDir = "No"
#         if os.path.isdir(gitFolder):
#             isGitDir = "Yes"
#         print(f"Directory : {folder} :  isGitDir")


