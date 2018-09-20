#!/usr/bin/env python3
import mpv

player = mpv.MPV(ytdl=True, input_default_bindings=True, input_vo_keyboard=True)

#player.playlist_append('https://0edit.bandcamp.com/album/neotokyo-nsf')
#player.playlist_append('https://www.youtube.com/watch?list=PL892CB43BF340CFC2')
#player.playlist_append('https://www.youtube.com/watch?list=UUJ792iJjUFoJ6sbkeJMvylQ')
#player.playlist_pos = 0
#player.playlist_next()
#help(player)
#player.play('https://www.youtube.com/watch?list=PL892CB43BF340CFC2')
player.play('ytdl://CCM7gtcj6Kk')
#player.play('https://0edit.bandcamp.com/album/neotokyo-nsf')
g = True
while True:
    # To modify the playlist, use player.playlist_{append,clear,move,remove}. player.playlist is read-only

    print(player.playlist)
    player.wait_for_playback()
    if g:
        g = False
        #player.playlist_next()
