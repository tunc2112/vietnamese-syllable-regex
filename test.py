import re
from vietnamese_syllable_regex import *

if __name__ == '__main__':
	for w in ["nghiêng", "khảo", "gì", "giếng", "quay", "quốc", "kao", "cào", "ngoéo", "nghành", "k", "gi", "qu"]:
		print(split_vietnamese_syllable(w))
