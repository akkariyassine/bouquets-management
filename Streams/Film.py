from Streams.Stream import Stream
from connectionDB import Database
from bouquets.bouquets import Bouquet


class Film(Stream):

    def __init__(self, name="", id=0, bouquet=0,duree=""):
        Stream.__init__(self, name, id, bouquet)
        self.duree = duree
        self.base = Database
        self.mydb = self.base.connect_dbs()
        self.mycursor = self.mydb.cursor()
        self.bouquetX = Bouquet()


    def get_duree(self):
        return self.duree

    def set_duree(self, duree):
        self.duree = duree

    def SetFilm(self):
        if (self.bouquetX.DescribeAll() == False):
            pass
        else:
            print("this is the bouquet list , choise one of them to your new channel please ")
            self.bouquetX.DescribeAll()
            bouquet = input("enter the film's bouquet id  ")
            if (self.bouquetX.VerifExist(str(bouquet)) == False):
                print("bouquet not exist")
                self.SetFilm()
            else:
                name = input("enter the film's  name ")
                duree = input("enter the film's  duree ")
                sql = "INSERT INTO FILMS (name, bouquet,duree) VALUES  ('" + name + "', '" + bouquet + "','" + duree + "')"
                self.BASE(sql)



    def DelFilm(self):
            if(self.lenghtStream('film')==0):
                print("there is no film to delete")
            else:
                print("this is your film list")
                self.showStreams('film')
                id = input("choose one to delete and enter the id ")
                if (self.VerifStream('film', id) == 0):
                    print("wrong choice let's try again")
                    self.DelFilm()
                else:
                    sql = "DELETE FROM FILMS WHERE id =" + id
                    self.BASE(sql)

    def UpdateFilm(self):
        sql = ""
        if (self.lenghtStream('film') == 0):
            print("there is no film to update")
        else:
            print("this is your film list")
            self.showStreams('film')
            id = input("choose one to update and enter the id ")
            if (self.VerifStream('film', id) == 0):
                print("wrong choice let's try again")
                self.UpdateFilm()
            else:
               if (self.bouquetX.existBouquet() == False):
                   print("there is no bouquet Please create one ");

               else:
                   print("this is the bouquet list , choise one of them to your  movie please ")
                   self.bouquetX.DescribeAll()
                   bouquet = input("enter the channel's bouquet id  ")
                   if(bouquet==""):
                       print("you must choice a bouquet !")
                   else :
                       if (self.bouquetX.VerifExist(str(bouquet)) == False):
                           print("bouquet not exist")
                           self.UpdateFilm()
                       else:
                           name = input("enter the film's new name")
                           duree = input("enter the film's new duree")

                           if (name == '' and duree == "" and bouquet == ""):
                               print("no update happned")

                           elif (name == ''):
                               if (duree == '' and bouquet != ''):
                                   sql = "UPDATE FILMS SET bouquet='" + bouquet + "' WHERE id =" + id + ";"
                               elif (bouquet == "" and duree != ""):
                                   sql = "UPDATE FILMS SET duree='" + duree + "' WHERE id =" + id + ";"
                               else:
                                   sql = "UPDATE FILMS SET duree='" + duree + "', bouquet='" + bouquet + "' WHERE id =" + id + ";"
                           elif (duree == ''):
                               if (name == '' and bouquet != ''):
                                   sql = "UPDATE FILMS SET bouquet='" + bouquet + "' WHERE id =" + id + ";"
                               elif (bouquet == "" and name != ""):
                                   sql = "UPDATE FILMS SET name='" + name + "' WHERE id =" + id + ";"
                               else:
                                   sql = "UPDATE FILMS SET name='" + name + "', bouquet='" + bouquet + "' WHERE id =" + id + ";"
                           else:
                               self.sql = "UPDATE FILMS SET name='" + name + "', bouquet='" + bouquet + " ', duree='" + duree + "' WHERE id =" + id + ";"
                       self.BASE(sql)

    def Describe(self):
        if (self.lenghtStream('film') == 0):
            print("there is no film to describe")
        else:
            print("this is your film list")
            self.showStreams('film')
            id = input("choose one to describe and enter the id ")
            if (id == ""):
                print("enter your id please")
                self.Describe()
            else:
                if (self.VerifStream('film', id) == 0):
                    print("wrong choice let's try again")
                    self.Describe()
                self.mycursor.execute("SELECT * FROM FILMS WHERE id=" + id + ";")
                myresult = self.mycursor.fetchall()
                for x in myresult:
                    print("id= " + str(x[0]))
                    print("name= " + x[1])
                    print("id bouquet =" + str(x[2]))
                    print("duree= " + x[3])


    def DescribeAll(self):
        if (self.lenghtStream('film') == 0):
            print("there is no film to describe")
        else:

            self.mycursor.execute("SELECT * FROM FILMS ;")
            myresult = self.mycursor.fetchall()
            for x in myresult:

                print("id= " + str(x[0]))
                print("name= " + x[1])
                print("id bouquet =" + str(x[2]))
                print("duree= " + x[3])
                print("/////////////////////////////////////////////")


    def BASE(self , sql):
         self.mycursor.execute(sql)
         self.mydb.commit()
         print("operation finish successfully ")