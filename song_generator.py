##song generator


#main function
##ask what key the user wants the song to be in, or if the key should be chosen randomly
def main():
    keys=["C","C# or Db","D","D# or Eb", "E", "F", "F# or Gb", "G", "G# or Ab", "A", "A# or Bb", "B"]
    ##I don't want to deal with major or minor keys...
    common_keys=["C","D","E", "G", "A"]
    ##this is subjective at this point
    for i in range (1,12):
        print (i, keys[i])
    key=input("what key would you like the song to be in? Enter one of the above, or choose [r]andomly")
    ##How are we going to deal with

main()
#except:
#    print ("nope, that didn't work.")
