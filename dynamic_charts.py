import matplotlib.pyplot as plt
import mysql.connector
import mysql.connector
from flask import Flask
from matplotlib import animation

app = Flask(__name__)

# Connecting to mysql database

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="StockData")
mycursor = mydb.cursor()

# Fecthing Data From mysql to my python progame

mycursor.execute("select id, rate from stockgold")
result = mycursor.fetchall

id = []
rate = []

def graf(i):
    def new():
        for i in mycursor:
            rate.append(i[0])
            id.append(i[1])
            break

    new()

    print("id = ", id)
    print("rate = ", rate)

    # Visulizing Data using Matplotlib
    plt.plot(id, rate)
    plt.ylim(0, 3000)
    plt.xlabel("rate")
    plt.ylabel("id")
    plt.title("Stock Information")

anime = animation.FuncAnimation(plt.gcf(),graf ,interval = 1500)

plt.show()

if __name__ == '__main__':
        app.run(port=4000, debug=True)
