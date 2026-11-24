class Cricket:
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def info(self):
        print(f"Criket-Player name: {self.__name}, score: {self.__score}")
    def play(self):
        print(f"{self.__name} hit a six on the previous ball!!!")
    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score>=0:
            self.__score=new_score
        else:
            print("Score can not be less than 0. Please retry")

class Football:
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def info(self):
        print(f"Football-Player name: {self.__name}, goals: {self.__score}")
    def play(self):
        print(f"{self.__name}scored a hattrick in the previous match!!")
    def get_score(self):
        return self.__score
    def set_score(self,new_score):
        if new_score>=0:
            self.__score=new_score
        else:
            print("Goals scored an not be less than 0.")

cricketplay=("Virat",108)
footballplay=("Haaland",4)
print("SPORTS GALLERY!")
for sport in (cricketplay,footballplay):
    sport.info()
    sport.play()
    print()

print("Direct change try")
cricketplay.__score=999
print(f"get_score still shows{cricketplay.get_score()}")

print("Updating score")
cricketplay.set_score(200)
cricketplay.set_score(5)