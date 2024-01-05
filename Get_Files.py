# 模块注释
# TargetPath 指定目标路径
# Mix_GB 指定目标文件的最大大小

import os

# Get_TarFiles 函数会返回一个包含目标目录的文件的列表
def Get_TarFiles(TargetPath,Mix_GB):

    Files_List = os.listdir(TargetPath) # 根据目标路径列出文件
    All_Files = []

    for file in Files_List:

        file = TargetPath + "\\" + file
        filesize = os.path.getsize(file)

        if (os.path.isfile(file)) == True and filesize <= Mix_GB:

            All_Files.append(file)
    
    return(All_Files)

# Get_AllFiles 函数会返回一个包含目标目录以及子目录的文件的列表
def Get_AllFiles(TargetPath,Mix_GB):

    All_Files = []

    for a in os.walk(TargetPath):

        ListLength = len(a)
        FatherPath = a[0]
        SonFile = a[ListLength - 1]

        for b in SonFile:

            file = FatherPath + "\\" + b

            if os.path.getsize(file) <= Mix_GB:

                All_Files.append(file)
    
    return(All_Files)

if __name__ == '__main__':
    print("此模块不可直接运行")