s = "??:??"

time = list(s)

if time[0] == '?':
    time[0] = '2' if time[1] == '?' or time[1] <= '3' else '1'

if time[1] == '?':
    time[1] = '9' if time[0] < '2' else '3'

if time[3] == '?':
    time[3] = '5'
if time[4] == '?':
    time[4] = '9'

print(''.join(time))
