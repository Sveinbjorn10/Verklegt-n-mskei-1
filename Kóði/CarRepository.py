import Car

class CarRepository:
    
    def __init__(self):
        self.__cars = []

    def add_car(self, Car):
        # first add to file then to private list
        with open("./data/videos.txt", "a+") as videos_file:
            title = car.get_title()
            genre = car.get_genre()
            length = car.get_length()
            videos_file.write("{},{},{}\n".format(title, genre, length))

    def get_videos(self):
        if self.__videos == []:
            with open("./data/videos.txt", "r") as video_file:
                for line in video_file.readlines():
                    title, genre, length = line.split(",")
                    new_video = Video(title, genre, length)
                    self.__videos.append(new_video)    
        
        return self.__videos

