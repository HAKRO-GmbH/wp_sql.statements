'''
Einstiegspunkt für eine generelle Test-App/Script
'''
from wp_sql import wp_sql

def main():
    sql = wp_sql('nadine', 'hakro1969', '10.69.30.123', 'wp860') #Instanz für __init__ // hier heißt self dann sql
    statement_1 = sql.count_user() #deine Funktion von mir eingebunden
    statement_2 = sql.count_user1() #deine Funktion von mir eingebunden
    print(statement_1, statement_2) #Beispiel von tue was damit

    '''
    Wir könnten z.B. einen 2ten SQL Server instanzieren und unsere Daten verwenden --> mit der gleichen Klasse

    sql2 = wp.sql('testuser', 'supersicher', '10.69.30.124, 'wp861') #Instanz für __init__ // hier heißt self dann sql2
    statement_3 = sql.count_user() #deine Funktion von mir eingebunden
    statement_4 = sql.count_user1() #deine Funktion von mir eingebunden
    print(statement_3, statement_4) #Beispiel von tue was damit

    Somit haben wir Zeit gespart und haben Funktionen die wir nur einmal anfassen müssen - dementsprechend hoch kann die Qualität werden

    Grüßle
    Carlos
    '''



if __name__ == '__main__':
    main()