from id_from_username import IdFromUsername
from get_friends import GetFriends

user = IdFromUsername('4taaa')
uid = user.execute()

friends = GetFriends(uid)
statistic = friends.execute()
statistic = sorted(statistic.items(), key = lambda x:x[0])
for i in statistic:
    print( '{} => {}'. format(i[0], i[1]))
#arr = []
#for i in statistic:
#    arr.append(len(i[1]))
#plt.hist(arr, 100)
#plt.show()
