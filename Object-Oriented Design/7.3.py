# JukeBox


class JukeBox:

    def __init__(self, songs):
        self.songs = {}
        for song in songs:
            self.songs[song.title] = song
        self.playing = False

    def play_song(self, song):
        if song in self.songs:
            self.playing = True
            print("Playing '{}'!".format(song))
            return self.songs[song].data
        else:
            raise Exception("This song could not be found on file!")

    def stop_song(self):
        self.playing = False


class Song:

    def __init__(self, title, artist, data):
        self.title = title
        self.artist = artist
        self.data = data


if __name__ == '__main__':
    jukebox = JukeBox([Song('Over the Rainbow', 'No Idea', '--data--')])
    jukebox.play_song('Over the Rainbow')
    jukebox.play_song('QUE PRETENDES')
