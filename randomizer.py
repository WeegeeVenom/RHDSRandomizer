import random
from datetime import datetime
from traceback import print_exc
from sys import exc_info
GAME_OVERLAYS_ADDR = 0x10D50 #for arm9.bin
DESCRIPTIONS_ADDR = 0x61C4 #for overlay9_18.bin
#GAMES_BINARYLIST is offset by 60 (first is 60 or 3c)
GAMES_BINARYLIST = [0,0,0,1,1,1,1,1,1,0,
					0,0,1,1,0,0,0,0,0,1,
					0,0,0,1,1,1,0,0,1,1,
					1,1,1,1,0,1,1,1,0,0,
					0,1,1,1,1,1,1,1,1,1,
					1,1,1,1,1,0,0,0,0,0,
					0,0,0,0,0,0,1,0,0,0,
					0,0,1,1,1,1,1,1,1,1,
					1,1,1,1,0,0,0,1,0,0,
					0,0,0,0,0,0,0,0,1,0]



def gameOverlayExtractor(binaryList, inFile, address, bytesCount): 
	outDict = {}
	with open(inFile, 'rb') as inF:
		inF.seek(address)
		for i in binaryList:
			bytesData = inF.read(bytesCount)
			if i:
				outDict[int.from_bytes(bytesData[0:2], byteorder = 'little')] = bytesData
	return outDict

def fileEditor(inDict, filename, startAddr, keys, bytesCount, offSet):
	with open(filename, 'r+b') as editF:
		i = 0
		for _, ele in inDict.items():
			editF.seek(startAddr + ((keys[i] - offSet) * bytesCount))
			editF.write(ele)
			i += 1

if __name__ == '__main__':
	try:
		seed = datetime.now().timestamp() 
		outDict = gameOverlayExtractor(GAMES_BINARYLIST, 'arm9.bin', GAME_OVERLAYS_ADDR, 8) #dictionary for game overlays
		with open('test.bin', 'wb') as f:
			for _, ele in outDict.items():
				f.write(ele)
		keys = list(outDict.keys())
		random.seed(seed)
		random.Random().shuffle(keys)
		fileEditor(outDict, 'test2.bin', GAME_OVERLAYS_ADDR, keys, 8, 60)
	except Exception:
		print_exc()
		print('ERROR:', exc_info()[1])
		input('Press Enter to close this program. ')
