import random
def writer():
    letters = [chr(i) for i in range (65, 91)]
    keys = ['u', 'd', 'l', 'r']
    speeds = [i for i in range (6, 11)]
    song_name = random.sample(letters, 10)
    song_name = ''.join(song_name)
    txtless_name = song_name
    song_name += '.txt'
    song = open(song_name, 'w')
    song.write(f'{txtless_name} = pyrythms.Song([')
    for i in range(100):
        song.write(f"'o{random.choice(keys)}{random.choice(speeds)}'")
        if i < 99:
            song.write(',')
    song.write('])')

writer()

