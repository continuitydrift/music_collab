##song generator

import random
#main function
##ask what key the user wants the song to be in, or if the key should be chosen randomly
def main():
    global key, keys
    keys=["C","C# or Db","D","D# or Eb", "E", "F", "F# or Gb", "G", "G# or Ab", "A", "A# or Bb", "B"]
    ##I don't want to deal with major or minor keys...
    common_keys=["C","D","E", "G", "A"]
    ##this is subjective at this point
    for i in range (0,12):
        print (i, keys[i])
    key_ans=input("what key would you like the song to be in? Enter one of the above, or choose [r]andomly")
    if key_ans=="r":
        roll=random.randint(0,12)
        key=keys[roll]
        print ("your song is in the key of", key)
    ##I like how this program naturally puns on "key"
    else:
        key_num=int(key_ans)
        #converting input to integer
        try:
            key=keys[key_num]
            print ("your song is in the key of", key)
        except:
            print ("I couldn't make sense of that answer for some reason.")

def common_chords():
    global key, keys
    key_index={}
    for i in range(0,12):
        key_index[i]=keys[i]
    for i in key_index:
        print (i, key_index[i])
        if key in key_index[i]:
            I=i-1
            #This should get the number corresponding with the first position.
    print ("the key of", key, "has the first position number of", I)
    IV=I+5
    if IV>11:
        fourth=key_index[IV-12]
        #this will loop past the end of the scale
    else:
        fourth=key_index[IV]

    print ("the fourth position chord is", fourth)
    V=I+7
    if V>11:
        fifth=key_index[V-12]
    else:
        fifth=key_index[V]
    print ("the fifth position chord is", fifth)

    #fourth=
main()
common_chords()
#except:
#    print ("nope, that didn't work.")
