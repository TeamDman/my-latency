"""

06/05/2025 19:53:25 Reply from 8.8.8.8: bytes=32 time=18ms TTL=113
06/05/2025 19:53:26 Reply from 8.8.8.8: bytes=32 time=15ms TTL=113
06/05/2025 19:53:27 Reply from 8.8.8.8: bytes=32 time=18ms TTL=113
06/05/2025 19:53:28 Reply from 8.8.8.8: bytes=32 time=17ms TTL=113
06/05/2025 19:53:29 Reply from 8.8.8.8: bytes=32 time=16ms TTL=113

Open data.txt in utf-8 and read the lines and find lines like this and extract the data in a structured way.
Plot the ping time over time using seaborn.

"""

import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Pattern for lines like: 06/05/2025 19:53:25 Reply from 8.8.8.8: bytes=32 time=18ms TTL=113
line_re = re.compile(r'^(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}) Reply from [^:]+: bytes=\d+ time=(\d+)ms TTL=\d+')

timestamps = []
ping_times = []

with open('data.txt', encoding='utf-8') as f:
    for line in f:
        m = line_re.match(line)
        if m:
            dt = datetime.strptime(m.group(1), '%m/%d/%Y %H:%M:%S')
            time_ms = int(m.group(2))
            timestamps.append(dt)
            ping_times.append(time_ms)

if not timestamps:
    print('No ping data found.')
    exit(1)

df = pd.DataFrame({'timestamp': timestamps, 'ping_ms': ping_times})

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='timestamp', y='ping_ms')
plt.title('Ping Time to 8.8.8.8 Over Time')
plt.xlabel('Time')
plt.ylabel('Ping (ms)')
plt.tight_layout()
plt.savefig('ping_plot.png')
print('Plot saved to ping_plot.png')