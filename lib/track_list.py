class TrackList:
    def __init__(self):
        self._track_list = []
        

    def add_track(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object (track list)
        self._track_list.append(track)
        
    
    def list_of_tracks(self):
        if self._track_list == []:
            raise Exception('There are no tracks in this track list')
        return self._track_list