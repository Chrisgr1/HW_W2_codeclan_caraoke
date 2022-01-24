import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("We Will Rock You", "Queen", "Buddy, you're a boy, make a big noise... \n rest of lyrics")

    def test_song_has_song_title(self):
        self.assertEqual("We Will Rock You", self.song.song_title)
    
    def test_song_has_song_artist(self):
        self.assertEqual("Queen", self.song.song_artist)
    
    def test_song_has_song_lyrics(self):
        self.assertEqual("Buddy, you're a boy, make a big noise... \n rest of lyrics", self.song.song_lyrics)