from lib.track_list import TrackList
import pytest

"""
Given a track
adds to track list
"""

def test_add_multiple_tracks():
    track_list = TrackList()
    track_list.add_track("Enter Sandman")
    track_list.add_track("In da club")
    assert track_list._track_list == ["Enter Sandman", "In da club"]

"""
Given multiple tracks
return the list of tracks
"""

def test_list_of_tracks_to_be_returns():
    track_list = TrackList()
    track_list.add_track("Enter Sandman")
    track_list.add_track("In da club")
    assert track_list.list_of_tracks() == ["Enter Sandman", "In da club"]

"""
Given an empty track list
Return an error 'There are no tracks in this track list'
"""

def test_empty_track_list_returns_error():
    track_list = TrackList()
    with pytest.raises(Exception) as err:
        track_list.list_of_tracks()
    error_message = str(err.value)
    assert error_message == 'There are no tracks in this track list'