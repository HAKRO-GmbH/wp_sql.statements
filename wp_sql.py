import mysql.connector

class wp_sql():
    def count_user():
       conn = mysql.connector.connect(user='nadine', password='hakro1969',
                                    host='10.69.30.123',
                                    database='wp860')

        c = conn.cursor()
        sql = ''' SELECT COUNT(ID) AS AnzahlUser FROM `wpw4_users` '''
        c.execute(sql)
        d = c.fetchall() 
        return(d)

    def count_user1():
        conn = mysql.connector.connect(user='nadine', password='hakro1969',
                                    host='10.69.30.123',
                                    database='wp860')

        c = conn.cursor()
        sql = ''' SELECT COUNT(*) FROM `wpw4_users` '''
        c.execute(sql)
        d = c.fetchone()
        return(d)
