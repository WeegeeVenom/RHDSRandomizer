import random
import randomConstants as randoC
from datetime import datetime
from traceback import print_exc
from sys import exc_info
from os import path, getcwd
GAME_OVERLAYS_ADDR = 0x10D50 #for arm9.bin
DESCRIPTIONS_ADDR = 0x61C4 #for overlay9_18.bin

filepath = __file__.rsplit('\\', 1)[0]
#Generates dict of all of the overlays to be swapped
def gameOverlayExtractor(binaryList, filename, address, bytesCount): 
	outDict = {}
	try:
		with open(path.join(filepath, filename), 'rb') as inF:
			inF.seek(address)
			for i in binaryList:
				bytesData = inF.read(bytesCount)
				if i:
					outDict[int.from_bytes(bytesData[0:2], byteorder = 'little')] = {'overlay': bytesData}
		return outDict
	except FileNotFoundError:
		print_exc()
		print('ERROR:', exc_info()[1])
		print('Current working directory: ', getcwd())
		input('Press Enter to close this program. ')
		exit()
	except Exception:
		print_exc()
		print('ERROR:', exc_info()[1])
		input('Press Enter to close this program. ')
		exit()


#uses the shuffled dictionary to write back into the arm9.bin file
def fileEditor(inDict, filename, startAddr, keys, bytesCount, offSet):
	try:
		with open(path.join(filepath, filename), 'r+b') as editF: #Overlays swapping section
			i = 0
			for _, ele in inDict.items():
				editF.seek(startAddr + ((keys[i] - offSet) * bytesCount))
				editF.write(ele[overlay])
				i += 1
	except FileNotFoundError:
		print_exc()
		print('ERROR:', exc_info()[1])
		print('Current working directory: ', getcwd())
		input('Press Enter to close this program. ')
		exit()
	except Exception:
		print_exc()
		print('ERROR:', exc_info()[1])
		input('Press Enter to close this program. ')
		exit()

if __name__ == '__main__':
	try:
		seed = datetime.now().timestamp() 
		outDict = gameOverlayExtractor(randoC.GAMES_BINARYLIST, 'arm9.bin', GAME_OVERLAYS_ADDR, 8) #dictionary for game overlays, titles, and descriptions
		keys = list(outDict.keys())
		random.seed(seed)
		random.Random().shuffle(keys)
		fileEditor(outDict, 'arm9test.bin', GAME_OVERLAYS_ADDR, keys, 8, 60) #TODO: CHANGE THIS
		print("Process complete.")
	except Exception:
		print_exc()
		print('ERROR:', exc_info()[1])
		input('Press Enter to close this program. ')
		exit()


#TODO: Make outDict contain 3 things: overlay, title, desc
	#Do this by manually making a dictionary for each title and desc, with the key matching the outDict key. Add them into it.