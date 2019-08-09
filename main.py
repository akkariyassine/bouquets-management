from Streams.Film import Film
from Streams.Channel import Channel
from bouquets.bouquets import Bouquet





class Main():

    def prod(self):
       bouquet = Bouquet("test")
       channel = Channel()
       film = Film()
       print("Welcome to Bouquets managment APP , those are your choices")
       print("1- show all Bouquets")
       print("2- add bouquet")
       print("3- update bouquet")
       print("4- delete bouquet ")
       print("5- show a specifique bouquet")
       print("6- show all Channel")
       print("7- add Channel")
       print("8- update Channel")
       print("9- delete Channel")
       print("10- show a specifique Channel")
       print("11- show all Movie")
       print("12- add Movie")
       print("13- update Movie")
       print("14- delete Movie ")
       print("15- show a specifique Movie")
       x = input("your choise please : " )
       if(x=="1"):
        bouquet.DescribeAll()
        self.prod()
       elif(x=="2"):
         bouquet.SetBouquet()
         self.prod()
       elif(x=="3"):
         bouquet.Updatebouquet()
         self.prod()
       elif (x == "4"):
         bouquet.Delbouquet()
         self.prod()
       elif (x == "5"):
           bouquet.Describe()
           self.prod()
       elif (x == "6"):
           channel.DescribeAll()
           self.prod()
       elif (x == "7"):
           channel.Setchannel()
           self.prod()
       elif (x == "8"):
           channel.Updatechannel()
           self.prod()
       elif (x == "9"):
           channel.Delchannel()
           self.prod()
       elif (x == "10"):
           channel.Describe()
           self.prod()
       elif (x == "11"):
           film.DescribeAll()
           self.prod()
       elif (x == "12"):
           film.SetFilm()
           self.prod()
       elif (x == "13"):
           film.UpdateFilm()
           self.prod()
       elif (x == "14"):
           film.DelFilm()
           self.prod()
       elif (x == "15"):
           film.Describe()
           self.prod()
       else :
           print("wrong choice take a look again ")
           self.prod()



class run :
    main = Main()
    main.prod()




