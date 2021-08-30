import mysql.connector

class wp_sql():

    def __init__(self, user, password, server, db) -> None: #Jede Klasse benötigt in der Regel eine init-Funktion um Variablen global in der Klasse verfügbar zu machen
        self.user = user #In der main.py habe ich die erste Instanz mit sql initialisiert und an der Stelle den User 'nadine' übergeben. Self steht für die Instanz
        self.password = password
        self.server = server
        self.db = db
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

    def count_user(self): #self ist hier wieder die Instanz aus main.py
        conn = self.conn
        c = conn.cursor()
        sql = ''' SELECT COUNT(ID) AS AnzahlUser FROM `wpw4_users` '''
        c.execute(sql)
        d = c.fetchall() 
        return(d)

    def count_user1(self):
        conn = self.conn
        c = conn.cursor()
        sql = ''' SELECT COUNT(*) FROM `wpw4_users` '''
        c.execute(sql)
        d = c.fetchone()
        return(d)
