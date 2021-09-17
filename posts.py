import os, requests, time, sys
from config import Config as c
import numpy as np
import mysql.connector

from datetime import datetime
from wp_sql import wp_sql

#p = sys.argv[1]

def gen_content():
    time.sleep(0.1)
    url = f'http://hipsum.co/api/?type=hipster-centric&sentences={np.random.randint(10,20)}&paras={np.random.randint(5,20)}'
    x = requests.post(url)
    return x.text


def gen_data():
    sql = wp_sql(c.user, c.password, c.server, c.db, c.tprefix)
    post_id = int(sql.get_max_post_id() + 1)
    sql.assign_category(post_id)
    post_title = f'This is HAKRO Intranet-Post #{post_id}'
    now  = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
       'ID' : post_id,
       'post_author' : 8,
       'post_date' : now,
       'post_date_gmt' : now,
       'post_content' : str(gen_content()),
       'post_title' : post_title,
       'post_excerpt' : '',
       'post_status' : 'publish',
       'comment_status' : 'open',
       'ping_status' : 'open',
       'post_password' : '',
       'post_name' : post_title.replace(' ', '_'),
       'to_ping' : '',
       'pinged' : '',
       'post_modified' : now,
       'post_modified_gmt' : now,
       'post_content_filtered' : '',
       'post_parent' : 0,
       'guid' : f'http://10.69.30.123/wp/?p={post_id}',
       'menu_order' : 0,
       'post_type' : 'post',
       'post_mime_type' : '',
       'comment_count' : 0
    }

    return data


def main():
    for i in range(1000):
        sql = wp_sql(c.user, c.password, c.server, c.db, c.tprefix)
        res = sql.set_post(gen_data())
        #x = sql.assign_category(res['ID'])
        print(gen_data())

if __name__ == "__main__":
    main()