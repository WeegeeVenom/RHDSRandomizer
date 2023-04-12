import random
from datetime import datetime
GAME_OVERLAYS_ADDR = 0x10D50
GAMES_BINARYLIST = [0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0]


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


seed = datetime.now().timestamp()
outDict = fileExtractor(GAMES_BINARYLIST, 'arm9.bin', GAME_OVERLAYS_ADDR, 8)
keys = list(outDict.keys())
random.seed(seed)
random.Random().shuffle(keys)
fileEditor(outDict, 'arm9.bin', GAME_OVERLAYS_ADDR, keys, 8, 60)
