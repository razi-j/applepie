import mariadb

try:
    mariadb.connect(
            user='root',
            password='root',
            host="localhost",
            port=3306,
            database="afk")
except mariadb.Error as e:
    print(f"Error! {e}")
