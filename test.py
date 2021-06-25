import unittest

from musicalLake import *

class TestSum(unittest.TestCase):
    firstSong = Song(["brr", "fiu"], True)
    secondSong = Song(["pep", "birip", "trri-trri"], False)
    thirdSong = Song(["bri-bri", "plop"], True)

    def test_get_list(self):
        """
        Test that it get a list
        """
        sound = "brr"
        nextSounds = getSounds(sound, self.firstSong, self.secondSong, self.thirdSong)
        self.assertEqual(type(nextSounds), list)

    def test_get_str(self):
        """
        Test that it get a sring
        """
        sound = "croac"
        nextSounds = getSounds(sound, self.firstSong, self.secondSong, self.thirdSong)
        self.assertEqual(type(nextSounds), str)
    
    def test_first_song_sounds(self):
        """
        Check if it gets the correct sounds for the first song
        """
        sound = "brr"
        expectedSounds = ["fiu", "cric-cric", "brrah"]
        
        nextSounds = getSounds(sound, self.firstSong, self.secondSong, self.thirdSong)
        self.assertEqual(nextSounds, expectedSounds)

    def test_second_song_sounds(self):
        """
        Check if it gets the correct sounds for the first song
        """
        sound = "pep"
        expectedSounds = ["birip", "trri-trri", "croac"]
        
        nextSounds = getSounds(sound, self.firstSong, self.secondSong, self.thirdSong)
        self.assertEqual(nextSounds, expectedSounds)

    def test_third_song_sounds(self):
        """
        Check if it gets the correct sounds for the first song
        """
        sound = "bri-bri"
        expectedSounds = ["plop", "cric-cric", "brrah"]
        
        nextSounds = getSounds(sound, self.firstSong, self.secondSong, self.thirdSong)
        self.assertEqual(nextSounds, expectedSounds)
    
    def test_repeated_cricket_sound(self):
        """
        Check if putting the sound that repeats in first and third song can get the expected brrah sound as a result
        """
        sound = "cric-cric"
        expectedSounds = "The next sound will be: brrah"
        
        nextSounds = getSounds(sound, self.firstSong, self.secondSong, self.thirdSong)
        self.assertEqual(nextSounds, expectedSounds)
    
    def test_brrah_sound(self):
        """
        Check if says that is the last sound
        """
        sound = "brrah"
        expectedSounds = "Mmm, it seems like there will be a silence now. But don't worry a new song will start right after!"
        
        nextSounds = getSounds(sound, self.firstSong, self.secondSong, self.thirdSong)
        self.assertEqual(nextSounds, expectedSounds)

    def test_croac_sound(self):
        """
        Check if says that is the last sound
        """
        sound = "croac"
        expectedSounds = "Mmm, it seems like there will be a silence now. But don't worry a new song will start right after!"
        
        nextSounds = getSounds(sound, self.firstSong, self.secondSong, self.thirdSong)
        self.assertEqual(nextSounds, expectedSounds)
    
    def test_not_found_sound(self):
        """
        Check that let the user know that the sound is not found
        """
        sound = "asdd"
        expectedSounds = "Agg! this is a bit embarrasing, but I couldn't find the next sounds. Can you make sure you input the sound correctly and one at the time, please?"
        
        nextSounds = getSounds(sound, self.firstSong, self.secondSong, self.thirdSong)
        self.assertEqual(nextSounds, expectedSounds)

if __name__ == '__main__':
    unittest.main()