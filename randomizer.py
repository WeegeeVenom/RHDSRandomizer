import random
GAME_OVERLAYS_ADDR = 0x10D50
GAMES_BINARYLIST = [0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0]
#TODO: GET THE HEX TABLE IN A LIST
#RANDOMIZE LIST
#DONE - UPDATE THE FILES PROPERLY
#TODO: FIGURE OUT HOW TO SKIP AND UPDATE THE arm09.bin FILE
	# Use a dict with matching values of the first bytes
	# And use random.Random(seed).shuffle(keys)
	# Offset the OVERLAYS_ADDR by the key - base key

def fileExtractor(binaryList, inFile, address, bytesCount): 
	outDict = {}
	with open(inFile, 'rb') as inF:
		inF.seek(address)
		for i in binaryList:
			bytesData = inF.read(bytesCount)
			if i:
				#print(int.from_bytes(bytesData[0:2], byteorder = 'little'))
				outDict[int.from_bytes(bytesData[0:2], byteorder = 'little')] = bytesData
				#outList.append(bytesData)
	return outDict

def fileEditor(inDict, filename, startAddr, keys, bytesCount, offSet):
	with open(filename, 'r+b') as editF:
		i = 0
		for _, ele in inDict.items():
			editF.seek(startAddr + ((keys[i] - offSet) * bytesCount))
			editF.write(ele)
			i += 1

seed = 387179039
#seed = random.Random(555555555)
outDict = fileExtractor(GAMES_BINARYLIST, 'arm9OG.bin', GAME_OVERLAYS_ADDR, 8)
keys = list(outDict.keys())
print(keys)
random.Random(seed).shuffle(keys)
print(outDict)
fileEditor(outDict, 'arm9OGpywritetest.bin', GAME_OVERLAYS_ADDR, keys, 8, 60)
#Starts at 60, so do num - 60 * 3