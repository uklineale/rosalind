from lib import substring

assert substring('GATATATGCATATACTT', 'ATAT') == [2,4,10]

locations = substring('TTGCACTCAGGTGACTCAGGTCTCTATTCTCAGGTCTCAGGTACTAAGCTCAGGTCTCAGGTACGTAGCTACACTCAGGTGGCACCCGTTGCACTCAGGTACACCTCAGGTCCAGGTCTCAGGTGCACGGCTCAGGTCTCAGGTTGAACCCTCAGGTCTCAGGTCTCAGGTGTGACTCAGGTCTCAGGTCTCAGGTTCTTCTCAGGTTCTTTCTCAGGTCCCTCAGGTCCGCTCAGGTCTCACTCAGGTACTCTCAGGTACTCAGGTAAAAAACAGCTCAGGTCTCAGGTAACCACTCAGGTCTCAGGTTTCTCAGGTCCCTCAGGTATCTCAGGTTGCTCAGGTAACTCAGGTTTACGTCTCAGGTTGTACACCGCCTCAGGTCTCAGGTCTACTCTGCTCAGGTCTCAGGTATTTGTTGCGCTCAGGTTCTCAGGTCGCTCAGGTTGCGCTCAGGTTCCGCACCGACTCAGGTACTCAGGTGCTCAGGTTCTCAGGTTGCCTCAGGTCTCAGGTGTTCTCAGGTTCTCCTCAGGTCTATACTCAGGTGATGTACTCAGGTTCGCTCAGGTCTCAGGTCACTCAGGTTCTCAGGTTAAATGGTACGACTCAGGTTTCTCAGGTAAGCAAGCCTCAGGTTTCTCAGGTTAAACTCAGGTTACTCAGGTTGTGGCTCAGGTGTCTCAGGTCTCAGGTGTGGGCTCTCAGGTCTCTCAGGTATGACACCTCAGGTTCTCAGGTTCTCAGGTTGTCTCAGGTCTCAGGTGCTCAGGTATCACTCAGGTTCTCAGGTGCCTCAGGTTTGTCTCAGGTCATCTCAGGTGCTCAGGTGGATGGCCCTCAGGTGCTCAGGTCTCAGGTCAACGCCTCAGGTAACTCAGGTCCTCAGGT', 'CTCAGGTCT')
print(locations)
print(' '.join([str(i) for i in locations]))

