# RHDSRandomizer
A randomizer for Rhythm Heaven DS (or Rhythm Tengoku GOLD as it's called in Japan).

## Requirements
- Python 3
- A *\~legally acquired\~* **US Version** .nds file of `Rhythm Heaven` for the NDS (Can't provide)
- [Tinke](https://www.romhacking.net/utilities/817/) - Tinke is a program to see, convert, and edit the files of NDS games, very similar to other utilities like Tahaxan and Crystal Tile 2. `Used to edit the arm9.bin file`

## Usage
1. Download `randomizer.py`
2. Load up Tinke and open the .nds file
3. Go to `ftc/arm9.bin` and click `'Extract'` <img src="https://i.imgur.com/93p2KDY.png" alt="Image highlighting the ftc folder in Tinke">
4. Place the `arm9.bin` **NOT arm7.bin** file in the same folder as `randomizer.py` <img src="https://i.imgur.com/8zptKrz.png" alt="in the ftc folder, highlighting where arm9.bin is">
5. Run the python file
6. Go back to Tinke and on `ftc/arm9.bin`, click `'Change file'` and upload the newly randomized arm9.bin file you just modified
7. Click `'Save ROM'`
8. Enjoy your randomized copy of Rhythm Heaven DS!

## Current Features
- Randomizes all 50 of the minigames with each other

### In Development
- Allow you to set the seed manually, to allow for consistent scrambles
- Titles and Descriptions update properly with the randomized games
### Planned
- Direct integration of the extracting/dumping of the files into the ROM
- Flag to toggle remixes, sequels (on, off, shuffle in their own category)
- Flag to make sequels come after their original games randomized
- User interface to set different flags
- Testing and compatibility for JP/EU versions
- Game logo updates properly with the randomized games
- Archipelago Integration :eyes:

## **Note**
This mod seems to work with the RH Touchless mod, from what I tested. Just make sure to patch the file with the Touchless mod **before** applying the randomization!
## Credits
- @TheAlternateDoctor and @patataofcourse at the Rhythm Heaven Modding Discord for helping me with the research on the code for the game!
