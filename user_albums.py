def make_album(artist_name , album ,num_tracks = ''):
    '''Builds a dictionary describing a music album'''
    record = { 'artist' : artist_name.title() , 'album' : album.title() }
    if num_tracks :
        record['number of tracks'] = num_tracks
    else:
        pass
    return record
    
   

while True:
    print("\nPlease,enter name of an album's title and its artist: ")
    print("(enter 'q' at any time to quit)\n")
    
    album = input("Album: ")
    
    if album.lower() == 'q':
        break
        
        
    artist = input("Artist: ")
    
    if artist.lower() == 'q' :
        break
    
    info = make_album(artist , album)
    
    print("\n")
    print(info)
    
print("\n") 
    

