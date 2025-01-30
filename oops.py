class laptop():     #class definition
    storage ="32GB" # attributes 
    Brand = "dell"
    color = "red"
    screen_size = "15.6"
    def course(self):   #methods
        print("i am write a program in",self.Brand)
    def game(self):
        print("playing the games")
        self.course()
    def files(self):
        print("opeaning sum important files")
        self.game()
#objectname = classname()       
Brand = laptop() 
Brand.course()
Brand.game() 
Brand.files()      
