import os
import pymysql
from urllib.request import urlopen
from credentials import configs
import re

#Imported secrets thats ignored from elsewhere to be passed.
db_config = {
    'host': configs['host'],
    'user': configs['user'],
    'password': configs['password']
}

#Validation check for name.
NAME_CHECK = re.compile(r"^[A-Za-z \-']{1,100}$") 

def get_user_input():
    name = input('Enter your name: ').strip()
    if not NAME_CHECK.fullmatch(name):
        raise ValueError("Invalid name")
    return name

#Don't know how to really fix just now dont put anything through the command line!
def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

#Changed HTTP to HTTPS.
def get_data():
    url = 'https://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

#Removed f string that can allow injection used %s as place holders for formatting for data input.
def save_to_db(data):
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, (data, "Another Value"))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
