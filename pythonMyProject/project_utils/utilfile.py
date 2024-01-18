import csv
import traceback


# import pandas as pd
# from project_utils import UtilsRandom
#

def returnAppEnvFromInitFile():
    """
    返回配置文件'../App_Env/AppEnvFile'中app的环境
    :return: test or release
    """
    list = []
    result = ''
    file = Utilfile("./App_env/app_envfile.csv")
    file2 = Utilfile("../App_env/app_envfile.csv")

    try:
        list = file.get_csv_data()
    except Exception:
        list = file2.get_csv_data()

    if list[0][1] in ('T', 't', 'True', 'true', 'Yes', 'YES', 'yes', 'Y', 'y', 'Test', 'test'):
        result = "test"
    elif list[0][2] in ('T', 't', 'True', 'true', 'Yes', 'YES', 'yes', 'Y', 'y', 'Release', 'release', 'R', 'r') and \
            list[0][1] == '':
        result = "release"
    return result
    # print(list)



class Utilfile():
    def __init__(self, filePath):
        self.filePath = filePath

    # 写文件
    def write(self, fileData):
        global csvFile
        try:
            csvFile = open(self.filePath, 'a', encoding='utf8', newline='')
            writer = csv.writer(csvFile)
            writer.writerows(fileData)
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)
        finally:
            csvFile.close()

    # 读取文件
    def read(self):
        csvFile = open(self.filePath, encoding='utf8')
        try:
            return csvFile.readlines()
        finally:
            csvFile.close()

    # 数据驱动读取CSV的数据
    def get_csv_data(self):
        value_rows = []
        with open(self.filePath, encoding='utf8') as f:
            # 忽略表头
            f_csv = csv.reader(f)
            next(f_csv)
            for r in f_csv:
                value_rows.append(r)
        return value_rows

    # 改文件
    def modify_csv_column(self, index1, index2, value1, value2):
        """
        更新CSV文件中指定行的某个字段的值
        :param index1: 索引，用来定位被修改字段的所在行
        :param index2: 索引，被修改字段的索引
        :param value1: 字段值，用来定位被修改字段的所在行
        :param value2: 字段值，被修改字段的值
        :return:
        """
        index1 = int(index1)
        index2 = int(index2)

        with open(self.filePath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                if row[index1] == value1:
                    row[index2] = value2
                rows.append(row)

        # newline="" 去除空行
        with open(self.filePath, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)


if __name__ == '__main__':
    # utilsFile = UtilsFile("../TestData/Data_testEnv/test_LoginCase.csv")
    # fileData = []
    # for i in range(100):
    #     fileData.append([UtilsRandom.getRandomChineseName(), UtilsRandom.getRandomEmail(), UtilsRandom.getRandomMobilePhone()])
    #     # fileData.append(["姓名","邮箱","手机号码"])
    #     utilsFile.write(fileData)
    # for line in utilsFile.read():
    #     print(line)
    # #
    # # print(utilsFile.read())
    # # print(utilsFile.get_csv_data())
    # #-------------------------------------------
    #
    # newData = "aaa,777"
    path = "../drafts/testWrite.csv"

    # with open(path, 'r') as f:
    #     reader = csv.reader(f)
    #     rows = []
    #     for row in reader:
    #         if row[0] == 'aaa':
    #             row[1] = '999'
    #         rows.append(row)
    #
    # with open(path, 'w', newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(rows)
    Utilfile(path).modify_csv_column(index1=0, value1='aaa', index2=1, value2="hhhh")





