import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Nim', 'D', 'Go', 'Rust')
y_pos = np.arange(len(objects))
performance = [77944,1345624,2019395,2463888]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Size')
plt.title('Binary executable file size')

# plt.show()
plt.savefig('compare-bin-size.png')
