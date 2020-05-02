def Arithmacalc(chunk):
	while "^" in chunk:
		i = chunk.index("^")
		thing = float(chunk[i-1] ** chunk[i+1])
		chunk [i-1] = thing
		del chunk[i:i+2]
		#print(f"chunk[] = {chunk}")
	while "/" in chunk:
		i = chunk.index("/")
		thing = float(chunk[i-1] / chunk[i+1])
		chunk [i-1] = thing
		del chunk[i:i+2]
		#print(f"chunk[] = {chunk}")
	while "*" in chunk:
		i = chunk.index("*")
		thing = float(chunk[i-1] * chunk[i+1])
		chunk [i-1] = thing
		del chunk[i:i+2]
		#print(f"chunk[] = {chunk}")
	while "-" in chunk:
		i = chunk.index("-")
		thing = float(chunk[i-1] - chunk[i+1])
		chunk [i-1] = thing
		del chunk[i:i+2]
		#print(f"chunk[] = {chunk}")	
	while "+" in chunk:
		i = chunk.index("+")
		thing = float(chunk[i-1] + chunk[i+1])
		chunk [i-1] = thing
		del chunk[i:i+2]
		#print(f"chunk[] = {chunk}")
	return thing