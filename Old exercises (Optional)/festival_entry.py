# Queue of festivalgoers at entry
# no. of alcohol units
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival (only the names)

# If guns are found, remove them and put them on the watchlist (only the names), they can not enter the festival
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Mark', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

def security_check(queue):

    watchlist = []
    security_alcohol_loot = 0
    allowed_attendees = []
    
    for attendee in queue:
        if attendee['guns'] > 0:
            watchlist.append(attendee['name'])

        else:
            if attendee['alcohol'] > 0:
                security_alcohol_loot += attendee['alcohol']
                attendee['alcohol'] = 0
            allowed_attendees.append(attendee['name'])
    
    print("peaple who can enter: ",allowed_attendees)
    print("peaple in watchlist ",watchlist)

allowed_attendees = security_check(queue)