import json
from urllib.request import Request, urlopen
import mysql.connector
import requests
import shutil

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="codeweekly",
)
mycursor = mydb.cursor()

#insert some investments to table
sql = "INSERT INTO checkusers_investment (investment_type, manager, investment_desc) VALUES (%s, %s, %s)"
type1 = ("type one", "Jonh Smith", "this is investment one" )
type2 = ("type two", "Sarah Jane", "this is investment two")

mycursor.execute(sql, type1)
mycursor.execute(sql, type2)
mydb.commit()
#get api data
req = Request("https://reqres.in/api/users", headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(req).read()
data = json.loads(webpage.decode())
user_data = data["data"]

# sql to insert data recieved
sql = "INSERT INTO checkusers_workers (internal_id, first_name, last_name, email, investment_id) VALUES (%s, %s, %s, %s, 1)"

for user in user_data:
    val = (user["id"], user["first_name"], user["last_name"], user["email"])
    mycursor.execute(sql, val)
    url = user["avatar"]
    image = requests.get(url, stream=True)
    image.raw.decode_content = True
    #save image
    with open("./images/" + user["first_name"] + user["last_name"] + ".jpg", "wb") as f:
        shutil.copyfileobj(image.raw, f)

mydb.commit()
