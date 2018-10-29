import os
import sys

print(sys.path[0])

def IsSubString(SubStrList, Str):
    flag = True
    for substr in SubStrList:
        if not (substr in Str):
            flag = False

    return flag


# 扫面文件
def GetFileList(FindPath, FlagStr=[]):
    FileList = []
    FileNames = os.listdir(FindPath)
    if len(FileNames) > 0:
        for fn in FileNames:
            if len(FlagStr) > 0:
                if IsSubString(FlagStr, fn):
                    fullfilename = os.path.join(FindPath, fn)
                    FileList.append(fullfilename)
            else:
                fullfilename = os.path.join(FindPath, fn)
                FileList.append(fullfilename)

    if len(FileList) > 0:
        FileList.sort()

    return FileList

os.chdir("/home/lhd/桌面/master_thesis_code-master/mydata")

print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(os.path.abspath(__file__)))

test_txt = open('test.txt', 'w')
# 制作标签数据，如果是狗的，标签设置为0，如果是猫的标签为1
imgfile = GetFileList('./')  # 将数据集放在与.py文件相同目录下
for img in imgfile:
    str1 = os.getcwd() + img[1:] +'\n'  # 用空格代替转义字符 \t
    test_txt.writelines(str1)

# imgfile = GetFileList('train/n02091467')
# for img in imgfile:
#     str2 = img + ' ' + '0' + '\n'
#     train_txt.writelines(str2)
# train_txt.close()

# # 测试集文件列表
# test_txt = open('val.txt', 'w')
# # 制作标签数据，如果是男的，标签设置为0，如果是女的标签为1
# imgfile = GetFileList('val/n01440764')  # 将数据集放在与.py文件相同目录下
# for img in imgfile:
#     str3 = img + ' ' + '1' + '\n'
#     test_txt.writelines(str3)
#
# imgfile = GetFileList('val/n02091467')
# for img in imgfile:
#     str4 = img + ' ' + '0' + '\n'
#     test_txt.writelines(str4)
test_txt.close()

print("成功生成文件列表")