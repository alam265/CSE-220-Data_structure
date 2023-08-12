class Movie:
    def __init__(self,name,genre,duration):
        self.name = name 
        self.genre = genre
        self.duration = duration
    def movieInfo(self):
        return f"Movie Name: {self.name}\nGenre: {self.genre}\nDuration: {self.duration}"
    @classmethod
    def createMovie_fromString(cls,string):
        name, genre, duration = string.split('-')
        return Movie(name,genre,duration)
    
class StarCinema:
    dic = {}
    
    def __init__(self,branch_name):
        self.branch_name = branch_name
        self.movie_list = []
        

        print(f"Welcome to {self.branch_name} of StarCineplex")

    def addMovies(self,*obj_movie):
        for movie in obj_movie:
            if movie in self.movie_list:
                print("Movie is already added")
            elif movie not in self.movie_list:
                self.movie_list.append(movie)
                print(f"{movie.name} added to {self.branch_name} branch")

        
        StarCinema.dic[self.branch_name] = self.movie_list
    
    @classmethod
    def showAllBranchInfo(cls):
        
        for k,v in cls.dic.items():
            print(f"Branch name: {k}")
            c=1
            for i in v:
                print(f"Movie No: {c}")
                print(i.movieInfo())
                print('*'*25)
                c+=1
            print("#"*25)


    def removeMovie(self,obj):
        self.movie_list.remove(obj)

    @classmethod
    def check(cls,string):
        found = False
        for k,v in cls.dic.items():
            for movie in v:
                if movie.name == string:
                    print(f"{movie.name} movie is streaming in {k} branch ")
                    found = True
                    movie_genre = movie.genre
                    movie_dur = movie.duration
        if found == True :
            print(f"The Movie is a {movie_genre} and Duration is {movie_dur}")
        else:
            print(f"{string} is not being streamed anywhere")
            




movie1 = Movie('Oppenheimer', 'Biographical Drama', 180)
movie2 = Movie('Barbie', 'Fantasy Comedy', 114)
movie3 = Movie('Mission: Impossible – Dead Reckoning Part One', 'Action', 163)
print('1==========================================')
print(movie3.movieInfo())
print('2==========================================')
movie4 = Movie.createMovie_fromString('Prohelika-Drama-153')
print('3==========================================')
print(movie4.movieInfo())
print('4==========================================')
branch1 = StarCinema('Mohakhali')
print('5==========================================')
branch1.addMovies(movie1, movie2, movie4)
print('6==========================================')
branch1.addMovies(movie1, movie3)
print('7==========================================')
StarCinema.showAllBranchInfo()
print('8==========================================')
branch2 = StarCinema('Mirpur')
print('9==========================================')
branch2.addMovies(movie1, movie2, movie3)
print('10==========================================')
StarCinema.showAllBranchInfo()
print('11==========================================')
StarCinema.check('Oppenheimer')
print('12=========================================')
StarCinema.check('Sound of Freedom')
print('13=========================================')
branch1.removeMovie(movie2)
StarCinema.showAllBranchInfo()
print('14=========================================')
branch2.removeMovie(movie1)
StarCinema.showAllBranchInfo()
