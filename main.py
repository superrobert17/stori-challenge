
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import smtplib
import csv
import pymysql
import os


#Variables entorno
username = os.environ.get('USER_MAIL', 'your user mail')
password_mail = os.environ.get('PASS_MAIL', 'your password mail')
sender_mail = os.environ.get('SENDER_MAIL', 'your sender mail')
receiver_mail = os.environ.get('RECEIVER_MAIL', 'your receiver mail')
host=os.environ.get('MYSQL_HOST', 'your database host')
user=os.environ.get('MYSQL_USER', 'root')
password=os.environ.get('MYSQL_PASSWORD', 'your password database')
db=os.environ.get('MYSQL_DB', 'your database')



#Función que lee el archivo csv
def read_file():

    with open('transactions.csv')as file:
        reader = csv.reader(file, delimiter=",")

        header = next(file)
        rows = []
        for row in reader :
            rows.append(row)

    save_data(rows)

#FIN read_file


#Declara conección a BD mysql
connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db
    )
#Función que guarda los datos extraidos del archivo csv
def save_data(data):

    cursor = connection.cursor()
    data_insert = []
    for row in data:
        date = datetime.strptime(row[1], '%Y/%m/%d')
        num = float(row[2])
        data_insert.append([date,num])
    
    sql = "INSERT INTO transactions(date,transaction) VALUES (%s, %s)"

    cursor.executemany(sql, data_insert)
    connection.commit()

#FIN save_data



#Configuración para envio mail

email = username
password = password_mail

sender = sender_mail
receiver = receiver_mail
subject = "Balance"

#Función que envía el mail 
def send_mail():
    multipart = MIMEMultipart()
    multipart['Subject'] = 'Balance'
    multipart['From'] = 'stori@stori.com'
    multipart['To'] = receiver_mail
   
    multipart.attach(MIMEText(temp, 'html'))
 
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email, password)
    server.sendmail(sender, receiver, multipart.as_string())

    server.quit()
#FIn send_mail

#Variables para mostrar en template
total=float
months = []
avg_credit = float
avg_debit = float

#consultas para obtener datos guardados
cursor = connection.cursor()
#obtiene el total 
sql = "SELECT SUM(transaction) FROM transactions" 
cursor.execute(sql)

res = cursor.fetchone()
total = res[0]
total = round(total,2)
#obtiene el total de transacciones por mes
sql = "SELECT MONTH(date),COUNT(transaction) FROM transactions GROUP BY MONTH(date) ORDER BY MONTH(date)"
cursor.execute(sql)

res = cursor.fetchall()

for row in res:
    date = datetime.strptime(str(row[0]), "%m")
    full_month_name = date.strftime("%B")
    num = row[1]
    months.append([full_month_name,num])

#obtiene el promedio de credito
sql = "SELECT avg(transaction) FROM transactions where transaction > 0"
cursor.execute(sql)
res = cursor.fetchone()
avg_credit = res[0]
avg_credit = round(avg_credit,2)

#obtiene el promedio de debito   
sql = "SELECT avg(transaction) FROM transactions where transaction < 0"
cursor.execute(sql)
res = cursor.fetchone()
avg_debit = res[0]
avg_debit = round(avg_debit,2)

aux_months = ""
for i in months:
    aux_months+= f'''<tr style="font-size:12px; font-weight:bold;">
                        <td width="50%" style="border:1px solid black; text-align: center;">{i[0]} - {i[1]}</td>
                    </tr>
                '''
#Carga de template donde se le envían las variables a mostrar
bodytemp = r'template/template.html'
with open(bodytemp, "r", encoding='utf-8') as f:
    temp= f.read().format(total = total, avg_credit = avg_credit, avg_debit = avg_debit, months = aux_months)   



#Llamado a funciones

read_file()

send_mail()

#FIN script