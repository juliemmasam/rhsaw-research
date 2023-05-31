import gps

print("Entering the program")
session = gps.gps()
print("Done getting the session")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


while True: 
    print("Entering iteration:")
    try:
        print("Trying connection:")
        report = session.next()
        print(report['class'])
    except KeyError: 
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration: 
        session = None
        print("GPSD has terminated.")