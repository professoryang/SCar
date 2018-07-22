# import pymysql
#
#
# with open('brands.txt', encoding='utf-8')as f:
#     while True:
#
#         url, name = tuple(f.readline().split(','))
#         if not url:
#             break
#         print(url, name)
#         db = pymysql.connect(
#             host='192.168.61.132',
#             port=3306,
#             user='root',
#             password='root',
#             db='secondcar',
#             charset='utf8')
#         cursor = db.cursor()
#         print('数据库连接成功')
#
#         cursor.execute('insert s_brand (name,url) values (%s,%s)', (name, url))
#         print('添加成功！')

# with open('outers.txt', encoding='utf-8')as f:
#     while True:
#         name, kind = tuple(f.readline().split(','))
#         if not name:
#             break
#         print(name, kind)
#         db = pymysql.connect(
#             host='192.168.61.132',
#             port=3306,
#             user='root',
#             password='root',
#             db='secondcar',
#             charset='utf8')
#         cursor = db.cursor()
#         print('数据库连接成功')
#
#         cursor.execute('insert s_outer(name,kind) values(%s,%s)', (name, kind))
#         db.commit()


