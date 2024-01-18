import pymysql


class UtilDB():
    def __init__(self, url, port, dbName, userName, passWord):
        self.url = url
        self.port = port
        self.dbName = dbName
        self.userName = userName
        self.passWord = passWord


    def get_connection(self):
        """
        connect to database
        :return:
        """
        db = pymysql.connect(host=self.url, port=self.port, db=self.dbName, user=self.userName, password=self.passWord)
        return db

    def get_data(self, sql):
        """
        :param sql:
        :return: a Result list[]
        """
        sql = sql
        resultList = []
        DB = UtilDB(url=self.url, port=self.port, dbName=self.dbName, userName=self.userName,
                    passWord=self.passWord)
        # 连接数据库
        connect = DB.get_connection()
        try:
            # 得到cursor游标
            cus = connect.cursor()
            # 执行sql语句
            cus.execute(sql)
            # 得到全部查询结果
            result = cus.fetchall()
            # 通过下标取出每一组数据，添加保存到list中
            for temp in result:
                print(temp)
                u = []
                for i in range(len(temp)):
                    print('len(temp)= %d',len(temp))
                    u.append(temp[i])
                resultList.append(u)
            return resultList
        except Exception:
            raise Exception
        finally:
            connect.close()


    def write_data(self, sql):
        sql = sql
        DB = UtilDB(url=self.url, port=self.port, dbName=self.dbName, userName=self.userName,
                    passWord=self.passWord)
        # 连接数据库
        connect = DB.get_connection()
        try:
            # 得到cursor游标
            cus = connect.cursor()
            # 执行slq语句
            cus.execute(sql)
            # 提交结果
            connect.commit()
        except Exception:
            raise Exception
        finally:
            connect.close()
