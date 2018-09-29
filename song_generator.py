##song generator


#......####....####...##..##...####..
#.....##......##..##..###.##..##.....
#......####...##..##..##.###..##.###.
#.........##..##..##..##..##..##..##.
#......####....####...##..##...####..
#................................
#......####...######..##..##..######..#####....####...######...####...#####..
#.....##......##......###.##..##......##..##..##..##....##....##..##..##..##.
#.....##.###..####....##.###..####....#####...######....##....##..##..#####..
#.....##..##..##......##..##..##......##..##..##..##....##....##..##..##..##.
#......####...######..##..##..######..##..##..##..##....##.....####...##..##.
#........................................................................


import random
#main function
##ask what key the user wants the song to be in, or if the key should be chosen randomly
def main():
    global key, keys
    keys=["C","C#/Db","D","D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
    ##I don't want to deal with major or minor keys...
    common_keys=["C","D","E", "G", "A"]
    ##this is subjective at this point
    for i in range (0,12):
        print (i, keys[i])
    key_ans=input("what key would you like the song to be in? Enter one of the above, or choose [r]andomly")
    if key_ans=="r":
        roll=random.randint(0,11)
        #key=keys[roll]
        key=random.choice(common_keys)
        print ("your song is in the key of", key)
    ##I like how this program naturally puns on "key"
    else:
        key_num=int(key_ans)
        #converting input to integer
        try:
            key=keys[key_num]
            print("")
            print ("your song is in the key of", key)
        except:
            print ("I couldn't make sense of that answer for some reason.")

def common_chords():
    global key, keys, key_index, fourth, fifth, I
    key_index={}
    for i in range(0,11):
        key_index[i]=keys[i]
    for i in key_index:
        #print (i, key_index[i])
        if key in key_index[i]:
            I=i
            #This should get the number corresponding with the first position.
    print ("")
    print ("the first position chord is", key)
    IV=I+4
    if IV>11:
        fourth=key_index[IV-12]
        #this will loop past the end of the scale
    else:
        fourth=key_index[IV]

    print ("the fourth position chord is", fourth)
    V=I+6
    if V>11:
        fifth=key_index[V-12]
    else:
        fifth=key_index[V]
    print ("the fifth position chord is", fifth)



def minor_chords():
    global key, keys, key_index, second, third, sixth, I


    II=I+2
    if II>11:
        second=key_index[II-12]
    else:
        second=key_index[II]
    print ("second position chord is", second, "minor")

    III=I+4
    if III>11:
        third=key_index[III-12]
    else:
        third=key_index[III]
    print ("third position chord is", third, "minor")

    VI=I+9
    if VI>11:
        sixth=key_index[VI-12]
    else:
        sixth=key_index[VI]
    print ("sixth position chord is", sixth, "minor")



def generate():
    global key, keys, key_index, second, third, fourth, fifth, sixth

    minor_chords=[second, third, sixth]
    common_chords= [key, fourth, fifth]

    print ("")
    print ("VERSE")
    print ("")
#generating chords
    roll=random.randint(1,4)
    if roll<4:
        verse_one=random.choice(common_chords)
        print (verse_one)
    else:
        verse_one=random.choice(minor_chords)
        print (verse_one, "minor")

    roll=random.randint(1,4)
    if roll<4:
        verse_two=random.choice(common_chords)
        print (verse_two)
    else:
        verse_two=random.choice(minor_chords)
        print (verse_two, "minor")

    roll=random.randint(1,4)
    if roll<3:
        verse_three=random.choice(common_chords)
        print (verse_three)
    elif roll ==3:
        verse_three=verse_one
    else:
        verse_three=random.choice(minor_chords)
        print (verse_three, "minor")

    roll=random.randint(1,4)
    if roll<3:
        verse_four=random.choice(common_chords)
        print (verse_four)
    elif roll ==3:
        verse_four=verse_two
    else:
        verse_four=random.choice(minor_chords)
        print (verse_four, "minor")





    print ("")
    print ("CHORUS")
    print ("")
#generating chords
    roll=random.randint(1,4)
    if roll<4:
        chorus_one=random.choice(common_chords)
        print (chorus_one)
    else:
        chorus_one=random.choice(minor_chords)
        print (chorus_one, "minor")

    roll=random.randint(1,4)
    if roll<4:
        chorus_two=random.choice(common_chords)
        print (chorus_two)
    else:
        chorus_two=random.choice(minor_chords)
        print (chorus_two, "minor")

    roll=random.randint(1,4)
    if roll<3:
        chorus_three=random.choice(common_chords)
        print (chorus_three)
    elif roll ==3:
        chorus_three=chorus_one
    else:
        chorus_three=random.choice(minor_chords)
        print (chorus_three, "minor")

    roll=random.randint(1,4)
    if roll<3:
        chorus_four=random.choice(common_chords)
        print (chorus_four)
    elif roll ==3:
        chorus_four=chorus_two
    else:
        chorus_four=random.choice(minor_chords)
        print (chorus_four, "minor")



main()
common_chords()
minor_chords()
generate()
