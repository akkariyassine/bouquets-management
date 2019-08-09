from connectionDB import Database

class Bouquet():

    def __init__(self, name=''):
        self.name = name
        self.base = Database
        self.mydb = self.base.connect_dbs()
        self.mycursor = self.mydb.cursor()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


    def VerifBouquet(self ,id):
            self.mycursor.execute("SELECT * FROM BOUQUETS where id="+id)
            myresult = self.mycursor.fetchall()
            return(myresult.__len__())



    def lenghtBouquet(self):
            self.mycursor.execute("SELECT * FROM BOUQUETS")
            myresult = self.mycursor.fetchall()
            return len(myresult)


    def SetBouquet(self):
        name = input("enter the bouquet's  name ")
      
        sql = "INSERT INTO BOUQUETS (name) VALUES  ('" + name + "');"
        self.mycursor.execute(sql)
        self.mydb.commit()
        print(self.mycursor.rowcount, "bouquet added successfully .")

    def Delbouquet(self):
        if ( self.lenghtBouquet()== 0):
            print("there is no bouquet to delete")
        else:
            print("this is your bouquet list")
            self.DescribeAll()
            id = input("choose one to delete and enter the id ")
            if (self.VerifBouquet(id) == 0):
                print("wrong choice let's try again")
                self.Delbouquet()
            else:
                sql = "DELETE FROM BOUQUETS WHERE id =" + id
                self.mycursor.execute(sql)
                self.mydb.commit()
                print("bouquet deleted successfully ")

    def Updatebouquet(self):

        if ( self.lenghtBouquet()== 0):
            print("there is no bouquet to update")
        else:
            sql = ''
            print("this is your bouquet list")
            self.DescribeAll()
            id = input("choose one to update and enter the id ")
            if (self.VerifBouquet(id) == 0):
                print("wrong choice let's try again")
                self.Updatebouquet()
            else:
                name = input("enter the bouquet's new name")
                if(name==''):
                    print('no Update happned')
                else :
                    sql = "UPDATE BOUQUETS SET name='" + name + "' WHERE id =" + id + ";"
            self.mycursor.execute(sql)
            self.mydb.commit()
            print("update bouquet finish successfully ")

    def Describe(self):
        if (self.lenghtBouquet() == 0):
            print("there is no bouquet to describe")
        else:
            print("this is your bouquet list")
            self.DescribeAll()
            id = input("choose one to describe and enter the id ")
            if (self.VerifBouquet(id) == 0):
                print("wrong choice let's try again")
                self.Describe()
            self.mycursor.execute("SELECT * FROM BOUQUETS WHERE id=" + id + ";")
            myresult = self.mycursor.fetchall()
            for x in myresult:
                print("id= " + str(x[0]))
                print("name= " + x[1])


    def DescribeAll(self):
        if (self.lenghtBouquet() == 0):
            print("there is no bouquet to describe")
        else:
            self.mycursor.execute("SELECT * FROM BOUQUETS ;")
            myresult = self.mycursor.fetchall()
            for x in myresult:
                print("id= " + str(x[0]) + " // " + "name= " + x[1])

    def existBouquet(self):
        if (self.lenghtBouquet() == 0):
            return False
        else:
            return True



    def VerifExist(self , id):
         if (self.lenghtBouquet() == 0):
             print("there is no bouquet to describe")
             return False
         else:
             self.mycursor.execute("SELECT * FROM BOUQUETS where id="+id+";")
             myresult = self.mycursor.fetchall()
             if(len(myresult)==0):
                 return False
             else :
                 return True







