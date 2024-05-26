n, q = map(int, input().split())
event_list = list()
event =  dict()

for i in range(q):
    event_list.append(list(map(int, input().split())))

for i in range(q):
    if event_list[i][0] == 3:
        if event_list[i][1] not in event:
            print("No")
        else:
            if event[event_list[i][1]] == 1:
                print("No")   
            else:
                print("Yes")
    elif event_list[i][1] in event:
        if event[event_list[i][1]] == 1:
            event[event_list[i][1]] = 2
    else:
        event[event_list[i][1]] = event_list[i][0]