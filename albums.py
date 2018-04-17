def make_album(artist_name , album ,num_tracks = ''):
    '''Builds a dictionary describing a music album'''
    record = { 'artist' : artist_name.title() , 'album' : album.title() }
    if num_tracks :
        record['number of tracks'] = num_tracks
    else:
        pass
    return record
    
print("\n")    

print( make_album('the chainsmokers' , 'collage(2016)'))
print("\n")

print( make_album(album = 'red(2012)',artist_name ='taylor swift'))
print("\n")

print( make_album('skillet' , album = 'comatose(2006)'))
print("\n")

print(make_album('linkin park','Minutes to midnight(2007)',12))

