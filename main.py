'''
Einstiegspunkt für eine generelle Test-App/Script
'''
from wp_sql import wp_sql
import daily

def main():
    sql = wp_sql('nadine', 'hakro1969', '10.69.30.123', 'wp860') #Instanz für __init__ // hier heißt self dann sql
    statement_1 = sql.count_user() #deine Funktion von mir eingebunden
    statement_2 = sql.count_user1() #deine Funktion von mir eingebunden
    print(statement_1, statement_2) #Beispiel von tue was damit

    df = daily.get_df("Del_today_28.08.2021-4_35_20.xlsx")
    print(df.shape)

    x = daily.get_sum(df)
    print(x)



if __name__ == '__main__':
    main()