from Streams.Stream import Stream
from bouquets.bouquets import Bouquet
from connectionDB import Database

class Channel(Stream):

    def __init__(self, name="", id=0, bouquet=0,satellite=""):
        Stream.__init__(self, name, id, bouquet)
        self.satellite = satellite
        self.base = Database
        self.mydb = self.base.connect_dbs()
        self.mycursor = self.mydb.cursor()
        self.bouquetX = Bouquet()



    def get_satellite(self):
        return self.satellite

    def set_satellite(self, satellite):
        self.satellite = satellite




    def getTables(self):
        base = Database
        mydb = base.connect_dbs()
        mycursor = mydb.cursor()
        mycursor.execute("SHOW COLUMNS FROM CHANNELS")

        for i in mycursor:
            print(i)

    def Setchannel(self):
        if(self.bouquetX.lenghtBouquet()==0):
            print("there is no bouquet to assign to your new channel so please create one ")
        else:
            print("this is the bouquet list , choise one of them to your new channel please ")
            self.bouquetX.DescribeAll()
            bouquet = input("enter the channel's bouquet id  ")
            if (self.bouquetX.VerifExist(str(bouquet)) == False):
                print("bouquet not exist")
                self.Setchannel()
            else:
                name = input("enter the channel's  name ")
                satellite = input("enter the channel's  satellite ")
                sql = "INSERT INTO CHANNELS (name, bouquet,satellite) VALUES  ('" + name + "', '" + bouquet + "','" + satellite + "')"
                self.BASE(sql)






    def Delchannel(self):
        if (self.lenghtStream('channel') == 0):
            print("there is no channel to delete")
        else:
            print("this is your channel list")
            self.showStreams('channel')
            id = input("choose one to delete and enter the id ")
            if (self.VerifStream('channel', id) == 0):
                print("wrong choice let's try again")
                self.Delchannel()
            else:
                sql = "DELETE FROM CHANNELS WHERE id =" + id
                self.BASE(sql)

    def Updatechannel(self):
        if (self.lenghtStream('channel') == 0):
            print("there is no channel to update")
        else:
            sql = ''
            print("this is your channel list")
            self.showStreams('channel')
            id = input("choose one to update and enter the id ")
            if (self.VerifStream('channel', id) == 0):
                print("wrong choice let's try again")
                self.Updatechannel()
            else:
                if (self.bouquetX.existBouquet() == False):
                    print("there is no bouquet Please create one ");
                else:
                    print("this is the bouquet list , choise one of them to your  channel please ")
                    self.bouquetX.DescribeAll()
                    bouquet = input("enter the channel's bouquet id  ")
                    if(bouquet==""):
                        print("you must choice a bouquet !")
                    else :
                        if (self.bouquetX.VerifExist(str(bouquet)) == False):
                            print("bouquet not exist")
                            self.Updatechannel()
                        else:
                            name = input("enter the channel's new name")
                            satellite = input("enter the channel's new satellite")

                            if (name == '' and satellite == "" and bouquet == ""):
                                print("no update happned")

                            elif (name == ''):
                                if (satellite == '' and bouquet != ''):
                                    sql = "UPDATE CHANNELS SET bouquet='" + bouquet + "' WHERE id =" + id + ";"
                                elif (bouquet == "" and satellite != ""):
                                    sql = "UPDATE CHANNELS SET satellite='" + satellite + "' WHERE id =" + id + ";"
                                else:
                                    sql = "UPDATE CHANNELS SET satellite='" + satellite + "', bouquet='" + bouquet + "' WHERE id =" + id + ";"
                            elif (satellite == ''):
                                if (name == '' and bouquet != ''):
                                    sql = "UPDATE CHANNELS SET bouquet='" + bouquet + "' WHERE id =" + id + ";"
                                elif (bouquet == "" and name != ""):
                                    sql = "UPDATE CHANNELS SET name='" + name + "' WHERE id =" + id + ";"
                                else:
                                    sql = "UPDATE CHANNELS SET name='" + name + "', bouquet='" + bouquet + "' WHERE id =" + id + ";"
                            else:
                                sql = "UPDATE CHANNELS SET name='" + name + "', bouquet='" + bouquet + " ', satellite='" + satellite + "' WHERE id =" + id + ";"
                        self.BASE(sql)

    def Describe(self):
        if (self.lenghtStream('channel') == 0):
            print("there is no channel to describe")
        else:
            print("this is your channel list")
            self.showStreams('channel')
            id = input("choose one to describe and enter the id ")
            if(id==""):
                print("enter your id please")
                self.Describe()
            else :
                if (self.VerifStream('channel', id) == 0):
                    print("wrong choice let's try again")
                    self.Describe()
                self.mycursor.execute("SELECT * FROM CHANNELS WHERE id=" + id + ";")
                myresult = self.mycursor.fetchall()
                for x in myresult:
                    print("id= " + str(x[0]))
                    print("name= " + x[1])
                    print("id bouquet =" + str(x[2]))
                    print("satellite= " + x[3])



    def DescribeAll(self):
        if (self.lenghtStream('channel') == 0):
            print("there is no channel to describe")
        else:

            self.mycursor.execute("SELECT * FROM CHANNELS ;")
            myresult = self.mycursor.fetchall()
            for x in myresult:
                print("id= " + str(x[0]))
                print("name= " + x[1])
                print("id bouquet =" + str(x[2]))
                print("satellite= " + x[3])
                print("/////////////////////////////////////////////")

    def BASE(self , sql):
         self.mycursor.execute(sql)
         self.mydb.commit()
         print("operation finish successfully ")


