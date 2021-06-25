class Song:

    # This sounds will be the same for all the songs
    stopSounds = ["brrah", "croac"]
    cricketSound = "cric-cric"

    def __init__(self, sounds, cricketRepeatedSound):
        self.__sounds = sounds
        self.__cricketRepeatedSound = cricketRepeatedSound

    def hasSound(self, currentSound):
        self.currentSound = currentSound
        if currentSound in self.__sounds:
            return True
        return False
            
    def isStopSound(self, currentSound):
        self.currentSound = currentSound
        if currentSound in self.stopSounds:
            return("Mmm, it seems like there will be a silence now. But don't worry a new song will start right after!")
        elif (currentSound == self.cricketSound ):
            return("The next sound will be: {}" .format(self.stopSounds[0]))
        
        return False

    def getComingSounds(self):
        soundIndex = self.__sounds.index(self.currentSound)
        # add the next sounds the a resulting list
        resultantSounds = [sound for sound in self.__sounds if soundIndex < self.__sounds.index(sound)]

        # add the cricket sound and brrah for the 1st and 3rd song and just croac for the 2nd
        if self.__cricketRepeatedSound is True:
            resultantSounds.append (self.cricketSound)
            resultantSounds.append (self.stopSounds[0])
        else:
            resultantSounds.append (self.stopSounds[1])
        return resultantSounds

    # print the different sounds
    def printSounds(self, soundToPrint):
        if(type(soundToPrint) == str):
            print(soundToPrint)
        elif (type(soundToPrint) == list):
            print("The next sounds will be:") 
            print(*soundToPrint, sep = ", ")
        else:
            print("Ups there was an error, try again.")

# get an array with the sounds or a string with the error
def getSounds(sound, firstSong, secondSong, thirdSong):
    stopSound = firstSong.isStopSound(sound)
    if (stopSound):
        return stopSound
    elif (firstSong.hasSound(sound)):
        return firstSong.getComingSounds()
    elif (secondSong.hasSound(sound)):
        return secondSong.getComingSounds()
    elif (thirdSong.hasSound(sound)):
        return thirdSong.getComingSounds()
    else:
        return("Agg! this is a bit embarrasing, but I couldn't find the next sounds. Can you make sure you input the sound correctly and one at the time, please?")

def main():
    # declare the songs
    firstSong = Song(["brr", "fiu"], True)
    secondSong = Song(["pep", "birip", "trri-trri"], False)
    thirdSong = Song(["bri-bri", "plop"], True)

    # input from console the heard sound
    sound = input("Enter the last sound you heard:")
    
    nextSounds = getSounds(sound, firstSong, secondSong, thirdSong)
    firstSong.printSounds(nextSounds)

if __name__ == "__main__":
    main()     
