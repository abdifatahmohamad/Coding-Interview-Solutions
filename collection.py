//Two sum number


// Valid Anagram

def valid_anagram(first, second):
	if len(first) != len(second):
		return False
		
	


	lookup = {}
	
	for char in first:
		letter  = first[char]
		if lookup[letter]:
			lookup[letter] += 1
		else:
			lookup[letter] = 1
			
		
	for char in second:
		letter = second[char]
		if not lookup[letter]:
			return False
		else:
			lookup[letter] -= 1
	
	 	
	
    return True
	 
	

print(valid_anagram("anagram", "nagaram"))
