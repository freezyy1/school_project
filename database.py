import psycopg2
from tokens import host, user, password, db_name

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # the cursor for perfoming database operations
    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")

    # create a jun new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE junior_table(
    #             id serial PRIMARY KEY,
    #             a1 varchar(50) NOT NULL,
    #             a2 varchar(50) NOT NULL,
    #             a3 varchar(50) NOT NULL,
    #             a4 varchar(50) NOT NULL,
    #             b1 varchar(50) NOT NULL,
    #             b2 varchar(50) NOT NULL,
    #             b3 varchar(50) NOT NULL,
    #             b4 varchar(50) NOT NULL,
    #             c1 varchar(50) NOT NULL,
    #             c2 varchar(50) NOT NULL,
    #             c3 varchar(50) NOT NULL,
    #             c4 varchar(50) NOT NULL,
    #             g1 varchar(50) NOT NULL,
    #             g2 varchar(50) NOT NULL,
    #             g3 varchar(50) NOT NULL,
    #             g4 varchar(50) NOT NULL);"""
    #     )

    # create a middle new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE middle_table(
    #             id serial PRIMARY KEY,
    #             a5 varchar(50) NOT NULL,
    #             a6 varchar(50) NOT NULL,
    #             a7 varchar(50) NOT NULL,
    #             a8 varchar(50) NOT NULL,
    #             a9 varchar(50) NOT NULL,
    #             b5 varchar(50) NOT NULL,
    #             b6 varchar(50) NOT NULL,
    #             b7 varchar(50) NOT NULL,
    #             b8 varchar(50) NOT NULL,
    #             b9 varchar(50) NOT NULL,
    #             c5 varchar(50) NOT NULL,
    #             c6 varchar(50) NOT NULL,
    #             c7 varchar(50) NOT NULL,
    #             c8 varchar(50) NOT NULL,
    #             c9 varchar(50) NOT NULL,
    #             g5 varchar(50) NOT NULL,
    #             g6 varchar(50) NOT NULL,
    #             g7 varchar(50) NOT NULL,
    #             g8 varchar(50) NOT NULL,
    #             g9 varchar(50) NOT NULL);"""
    #     )

    #create a high new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE high_table(
    #             id serial PRIMARY KEY,
    #             a10 varchar(50) NOT NULL,
    #             a11 varchar(50) NOT NULL,
    #             b10 varchar(50) NOT NULL,
    #             b11 varchar(50) NOT NULL,
    #             c10 varchar(50) NOT NULL,
    #             c11 varchar(50) NOT NULL,
    #             g10 varchar(50) NOT NULL,
    #             g11 varchar(50) NOT NULL);"""
    #     )

    # connection.commit()
    # print("[INFO] Table created successfully")

    # пример вставки уроков
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO high_table (a10, a11, b10, b11, c10, c11, g10, g11) VALUES
    #         ('русский_язык литература математика физкультура', 'физика химия математика физкультура', 'физкультура физкультура химия', 'русский_язык физика английский_язык', 'русский_язык литература математика физкультура', 'физика химия математика физкультура', 'физкультура физкультура химия', 'русский_язык физика английский_язык');"""
    #     )
    #
    #     print("[INFO] Data was succefully inserted")

    # get data from a table
    with connection.cursor() as cursor:
        postgreSQL_select_Query = "select a11 from high_table"
        cursor.execute(postgreSQL_select_Query)
        print("Выбор строк из таблицы mobile с помощью cursor.fetchall")
        a10 = cursor.fetchall()
        a10 = (" ".join(map(str, a10)))

    #delete a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE high_table;"""
    #     )
    #
    #     print("[INFO] Table was deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")