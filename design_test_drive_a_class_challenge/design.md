sou# Music Listening Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

> As a user
> So that I can keep track of my music listening
> I want to add tracks I've listened to and see a list of them.

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TrackList:
    def __init__(self):
        # Side effects:
        #   initiates an empty list 
        pass

    def add_track(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object (track list)
    
    def list_of_tracks(self):
        # Returns:
        #   list of tracks

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a track
adds to track list
"""
track_list = TrackList()
track_list.add_track("Enter Sandman")

"""
Given multiple tracks
adds multiple tracks to list
"""

track_list = TrackList()
track_list.add_track("Enter Sandman")
track_list.add_track("In da Club")

"""
Given multiple tracks
return the list of tracks
"""
track_list = TrackList()
track_list.add_track("Enter Sandman")
track_list.add_track("In da Club")
track_list.list_of_tracks()

"""
Given an empty track list
Return an error 'There are no tracks in this track list'
"""

track_list = TrackList()
track_list.list_of_tracks() # Error = 'There are no tracks in this track list'

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
