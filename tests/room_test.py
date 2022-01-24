import unittest
from classes.rooms import Room
from classes.guest import *
from classes.song import *


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest1 = ("Van", "Wilder", 100)
        self.guest2 = ("Yee", "Zee", 50)
        self.guest3 = ("B", "Real", 0)
        self.guestlist1 = []
        self.guestlist2 = [self.guest1]
        self.guestlist3 = [self.guest1, self.guest2]
     
        self.song1 = ("We Will Rock You", "Queen", "Buddy, you're a boy, make a big noise... \n rest of lyrics")
        self.song2 = ("Song 2", "Blur", "woo-hoo, do de do")
        self.songlist1 = []
        self.songlist2 = [self.song1]
        self.songlist3 = [self.song1, self.song2]


        self.room1 = Room(101, self.guestlist1, self.songlist1, 10)
        self.room2 = Room(102, self.guestlist2, self.songlist2, 15)
        self.room3 = Room(103, self.guestlist3, self.songlist3, 2)


    def test_room_has_number(self):
        self.assertEqual(101, self.room1.room_number)

    def test_room_has_capcity(self):
        self.assertEqual(10, self.room1.room_capacity)

    def test_room_has_no_guests(self):
        self.assertEqual([],self.room1.guest_list)

    def test_room_has_1_guest(self):
        self.assertEqual([("Van", "Wilder", 100)],self.room2.guest_list)

    def test_room_has_more_guest(self):
        self.assertEqual([("Van", "Wilder", 100), ("Yee", "Zee", 50)],self.room3.guest_list)

    def test_room_has_no_songs(self):
        self.assertEqual([], self.room1.song_list)

    def test_room_has_1_songs(self):
        self.assertEqual([("We Will Rock You", "Queen", "Buddy, you're a boy, make a big noise... \n rest of lyrics")],  self.room2.song_list)

    def test_room_has_more_songs(self):
        self.assertEqual([("We Will Rock You", "Queen", "Buddy, you're a boy, make a big noise... \n rest of lyrics"), ("Song 2", "Blur", "woo-hoo, do de do")],  self.room3.song_list)

    def test_can_add_song(self):
        songlist = self.room1.add_song(self.room1.room_number, self.song1)
        self.assertEqual([("We Will Rock You", "Queen", "Buddy, you're a boy, make a big noise... \n rest of lyrics")], self.room1.song_list)
 
    def test_can_check_in_guest__success(self):
        guestlist = self.room1.check_in_guest(self.guest1)
        self.assertEqual([("Van", "Wilder", 100)], self.room1.guest_list)

    def test_can_check_in_guest__room_full(self):
        guestlist = self.room3.check_in_guest(self.guest3)
        self.assertEqual([('Van', 'Wilder', 100), ('Yee', 'Zee', 50)],self.room3.guest_list)

    def test_can_check_in_guest__already_here(self):
        guestlist = self.room3.check_in_guest(self.guest2)
        self.assertEqual([('Van', 'Wilder', 100), ('Yee', 'Zee', 50)],self.room3.guest_list)

    def test_can_check_out_guest(self):
        guestlist = self.room2.check_out_guest(self.guest1)
        self.assertEqual([], self.room2.guest_list)
