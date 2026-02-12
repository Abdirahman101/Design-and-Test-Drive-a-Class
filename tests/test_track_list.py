from lib.track_list import TrackList


"""
Given a track
adds to track list
"""

def test_add_multiple_tracks():
    track_list = TrackList()
    track_list.add_track("Enter Sandman")
    track_list.add_track("In da club")
    assert track_list._track_list == ["Enter Sandman", "In da club"]


