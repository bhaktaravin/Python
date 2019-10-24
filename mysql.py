import pymysql
def connection():
    db = pymysql.connect("localhost","root","password","mysql")
    cursor = db.cursor()

    sql = "SELECT * FROM monsters;"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for r in results:
            cardId = r[0]
            name = r[1]
            attack = r[2]
            defense = r[3]

            """print(cardId,name, attack, defense)"""
            giveBack(results)


    except:
        print("Error")

    db.close()
    

def giveBack(results):
    return results