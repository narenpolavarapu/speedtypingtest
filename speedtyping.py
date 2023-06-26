import time

def speedtypingtest():
    text = "speed typing test in python"
    print("Type the following text:")
    print(text)
    print("Press Enter when you're ready.")
    input()

    print("Starting test...")
    start = time.time()

    readtext = input()

    end = time.time()
    totaltime = end - start

    if(readtext==text):
        print("\nResults:")
        print("Time elapsed: {:.2f} seconds".format(totaltime))
    else:
        print("you enetered the text wrong!! Try again")

   
speedtypingtest()

