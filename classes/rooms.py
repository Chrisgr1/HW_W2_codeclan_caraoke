from classes.guest import Guest
class Room:
    def __init__(self, room_number, guest_list, song_list, room_capacity):
        self.room_number = room_number
        self.guest_list = guest_list
        self.song_list = song_list
        self.room_capacity = room_capacity


    def add_song(self, room_number, song):
        for each_song in self.song_list:
            if song == each_song:
                continue
            else:
                break
        song_list = self.song_list.append(song)

   
    def check_in_guest(self, guest):
        if len(self.guest_list)==self.room_capacity:
            return ("Sorry. Room is full.")
        for each_guest in self.guest_list:
            if guest == each_guest:
                return "Can't add. Already here."
        self.guest_list.append(guest)
        guest.wallet.pay_to_check_in(10)
    
        

    def check_out_guest(self, guest):
        for each_guest in self.guest_list:
            if guest == each_guest:
                continue
            else:
                break
            print ("Error. No such guest.")
        guest_list = self.guest_list.remove(guest)