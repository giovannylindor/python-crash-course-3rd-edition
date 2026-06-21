def make_album(artistName, albumTitle, songAmount=None):
    if songAmount:
            dictionary = {'Artist Name': artistName, 'Album Title': albumTitle, 'Songs': songAmount}
    else:
        dictionary = {'Artist Name': artistName, 'Album Title': albumTitle}
    return dictionary

album_one = make_album('JAY-Z', 'Reasonable Doubt', 15)
album_two = make_album(artistName='Kendrick Lamar', albumTitle='To Pimp A Butterfly')
album_three = make_album('J-Cole', 'The Fall Off')

def loop():
     while True: 
          print("User Albums --> Press 'Q' to Quit")
          artist = input("Enter Artist: ")
          
          if artist.upper() == 'Q':
               break
          album_title = input("Enter Album Title: ")
          
          if album_title.upper() == 'Q':
               break
          
          make_album(artist, album_title)
          print(f"\nAdded {album_title.title()}, by {artist.title()}!")


loop()