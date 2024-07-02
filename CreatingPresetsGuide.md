# Creating Presets Guide

1. Start the program.
2. Navigate to the "Preset Menu" by typing "3" and pressing Enter in the "Main Menu".
3. Type "n" and press Enter. This action creates a new preset folder with empty .txt files and opens the folder.
4. Rename the "New Preset" folder to whatever you like.
5. Open the .txt files and write your messages. Ensure that each message is on a new line. To generate a variety of messages, you can use this [Prompt](https://github.com/xJolux/LoL-Auto-Chat/blob/main/Prompt.txt) with ChatGPT (explained below).
6. If you want to dynamically include a player's champion name in a message, use the placeholder "|CN|" instead of the actual name (explained below).
7. Save the .txt files.
8. Select your preset in the "Preset Menu" by typing its corresponding number and pressing Enter. If your preset name does not appear, press Enter to reload the menu.

## Explanations

### Preset Folder

You can rename the preset folder as you like.

### .txt Files

- ally_death.txt
- ally_kill.txt
- self_death.txt
- self_kill.txt

Do not change the names of these .txt files!

 **Contents of .txt Files**

These files contain messages used for specific in-game events.

 **Names of .txt Files**

Each file's name indicates the in-game event its messages are used for.

### Messages

 **Placeholders**

To dynamically include a player's champion name in a message, use the "|CN|" placeholder.

 **Usage of Champion Names in Events**

- "ally_death": Uses the champion name of the ally who died.
- "ally_kill": Uses the champion name of the ally who made the kill.
- "self_death": Uses the champion name of the enemy that killed you.
- "self_kill": Uses the champion name of the enemy that you killed.

## Generate Chat Messages

1. Copy this [Prompt](https://github.com/xJolux/LoL-Auto-Chat/blob/main/Prompt.txt) and paste it into ChatGPT.
2. Customize the criteria in the prompt to your preferences, then submit it.
3. ChatGPT will generate the specified number of messages for each event, following the chosen emotion/tone and style.
4. If you are satisfied with the generated messages and ChatGPT's formatting, copy and paste them into the respective .txt files.
5. Save the .txt files.

### Prompt Explanation

**Message Format**

- **Number of messages per event**: Specify how many messages you want to create for each event.
  - Example: 50

- **Message Length**: Specify the desired length of each message.
  - Example: short, medium, long

- **Percentage of messages using the champion name**: Determine the percentage (%) of messages that should refer to the player using their champion name. The rest should use pronouns like "you" or "your".
  - Example: 50% (This means half of the messages will use the champion name and the other half will use pronouns.)

**Creative Freedom**

- **Emotion/Tone**: Describe the emotional mood or tone for the messages.
  - Example: humorous, serious, encouraging

- **Style**: Specify any particular style for the messages.
  - Example: formal, casual, tactical, pirate

### Copying and Pasting Messages

If you find the generated messages satisfactory, please copy and paste them into the respective .txt file. If you choose not to use messages for a specific event, leave that .txt file empty.

Ensure the correct usage of "/all" for messages to enemy players and the placeholder "|CN|" for champion names. Each message should be placed on a new line within the file for functionality.

### Disclaimer

Please note that ChatGPT's output may not entirely meet your expectations.
