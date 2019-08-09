from connectionDB import Database

class Stream:

    def __init__(self, name, id, bouquet):
        self.name = name
        self.id = id
        self.bouquet = bouquet
        self.base = Database
        self.mydb = self.base.connect_dbs()
        self.mycursor = self.mydb.cursor()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_bouquet(self):
        return self.bouquet

    def set_bouquet(self, bouquet):
        self.bouquet = bouquet

    def showStreams(self , type):
        if(type=='film'):
            self.mycursor.execute("SELECT * FROM FILMS")
            myresult = self.mycursor.fetchall()
            for x in myresult:
                print(x)
        else:
            self.mycursor.execute("SELECT * FROM CHANNELS")
            myresult = self.mycursor.fetchall()
            for x in myresult:
                print(x)

    def VerifStream(self , type,id):
        if(type=='film'):
            self.mycursor.execute("SELECT * FROM FILMS where id="+id)
            myresult = self.mycursor.fetchall()
            return(myresult.__len__())


        else:
            self.mycursor.execute("SELECT * FROM CHANNELS where id="+id)
            myresult = self.mycursor.fetchall()
            return(myresult.__len__())

    def lenghtStream(self, type):
        if (type == 'film'):
            self.mycursor.execute("SELECT * FROM FILMS")
            myresult = self.mycursor.fetchall()
            return len(myresult)

        else:
            self.mycursor.execute("SELECT * FROM CHANNELS")
            myresult = self.mycursor.fetchall()
            return len(myresult)




