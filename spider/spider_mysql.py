import pymysql

# 定义一个类，将连接MySQL的操作写入其中
class down_mysql:
    def __init__(self, city_name, jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang):
        self.city_name = city_name
        self.jd_name = jd_name
        self.jd_jb = jd_jb
        self.jd_jieshao = jd_jieshao
        self.jd_price = jd_price
        self.jd_xiaoliang = jd_xiaoliang
        self.connect = pymysql.connect(
            host='localhost',
            db='spider_sql',
            port=3306,
            user='root',
            passwd='123456',
            charset='utf8',
            use_unicode=False
        )
        self.cursor = self.connect.cursor()

    # 保存数据到MySQL中
    def save_mysql(self):
        sql = "insert into qu_na_table(city_name,jd_name,jd_jb,jd_jieshao,jd_price,jd_xiaoliang) VALUES (%s,%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql, (
            self.city_name, self.jd_name, self.jd_jb, self.jd_jieshao, self.jd_price, self.jd_xiaoliang))
            self.connect.commit()
            print('数据插入成功')
        except :
            print()
            print('数据插入错误')

