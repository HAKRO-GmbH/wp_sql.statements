import mysql.connector

class wp_sql():

    def __init__(self, user, password, server, db, tprefix) -> None: #Jede Klasse benötigt in der Regel eine init-Funktion um Variablen global in der Klasse verfügbar zu machen
        self.user = user #In der main.py habe ich die erste Instanz mit sql initialisiert und an der Stelle den User 'nadine' übergeben. Self steht für die Instanz
        self.password = password
        self.server = server
        self.db = db
        self.tprefix=tprefix
        self.conn = mysql.connector.connect(user=self.user, password=self.password,
                                            host=self.server,
                                            database=self.db)

    ''' 
        def makecon(self): #Hier holen wir uns die global verfügbaren Variablen und die Funktion returned nur das Verbindungs-Objekt // dont repeat yourself - faul sein :)
        try: #Schritt 1 - Try
            conn = mysql.connector.connect(user=self.user, password=self.password,
                                            host=self.server,
                                            database=self.db)
            if conn:
                return conn #Wenn Verbindung OK dann Verbindung returnen
            else:
                print(f'Fehler: keine Ahnung warum') #Wenn nicht, keine Ahnung - richtige Fehler fängt except ab

        except Exception as e: #Wenn nicht 1 dann Fehler
            print(f'Datenbankfehler: {e}') #In e steht die Fehlermessage des SQL-Servers // kann dem User helfen
        
        finally: #Schlussendlich mache das - in diesem Fall: nichts 
            pass
    '''
    def get_max_post_id(self): #self ist hier wieder die Instanz aus main.py
        conn = self.conn
        c = conn.cursor()
        sql = f'SELECT MAX(ID) FROM {self.tprefix}posts'
        c.execute(sql)
        d = c.fetchall() 
        return d[0][0]

    def count_user(self): #self ist hier wieder die Instanz aus main.py
        conn = self.conn
        c = conn.cursor()
        sql = ''' SELECT COUNT(ID) AS AnzahlUser FROM `wpw4_users` '''
        c.execute(sql)
        d = c.fetchall() 
        return d

    def count_user1(self):
        conn = self.conn
        c = conn.cursor()
        sql = ''' SELECT COUNT(*) FROM `wpw4_users` '''
        c.execute(sql)
        d = c.fetchone()
        return d
    
    def filter_categories(self):
        conn = self.conn
        c = conn.cursor()
        sql = ''' SELECT DISTINCT 
                    post_title 
                    , post_content
                    , ID  
                    ,(SELECT group_concat(wpw4_terms.name separator ', ') 
                        FROM wpw4_terms 
                        INNER JOIN wpw4_term_taxonomy on wpw4_terms.term_id = wpw4_term_taxonomy.term_id 
                        INNER JOIN wpw4_term_relationships wpr on wpr.term_taxonomy_id = wpw4_term_taxonomy.term_taxonomy_id 
                        WHERE taxonomy= 'category' and wpw4_posts.ID = wpr.object_id 
                    ) AS "Categories" 
                    ,(SELECT group_concat(wpw4_terms.name separator ', ') 
                        FROM wpw4_terms 
                        INNER JOIN wpw4_term_taxonomy on wpw4_terms.term_id = wpw4_term_taxonomy.term_id 
                        INNER JOIN wpw4_term_relationships wpr on wpr.term_taxonomy_id = wpw4_term_taxonomy.term_taxonomy_id 
                        WHERE taxonomy= 'post_tag' and wpw4_posts.ID = wpr.object_id 
                    ) AS "Tags" 
                    FROM wpw4_posts 
                    WHERE post_type = 'post' AND post_status = 'publish' '''
        c.execute(sql)
        d = c.fetchall()
        return(d)

    def set_post(self, data):
        try:
            conn = self.conn
            c = conn.cursor()
            placeholder = ", ".join(["%s"] * len(data))
            sql = "insert into `{table}` ({columns}) values ({values});".format(table='wpw4_posts', columns=",".join(data.keys()), values=placeholder)
            c.execute(sql, list(data.values()))
            conn.commit()
            conn.close()
            return 'Post OK'
        except Exception as e:
            print(f'Fehler: {e}')
            return 1
        finally:
            pass


    def assign_category(self, post_id):
        conn = self.conn
        post_id = (post_id, )
        c = conn.cursor()
        sql = '''INSERT INTO wp860.wpw4_term_relationships(object_id, term_taxonomy_id, term_order) VALUES (%s, 94, 0);'''
        c.execute(sql, post_id)
        conn.commit()
        conn.close()
        return 0