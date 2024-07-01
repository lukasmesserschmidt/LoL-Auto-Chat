# Creating Presets

## Preset Folder

You can rename the preset folder as you like.

## .txt Files

- ally_death
- ally_kill
- self_death
- self_kill

**Do not alter the names of the .txt files!**

### Contents of .txt Files

- Contains messages used for corresponding in-game events.

### Names of .txt Files

- Indicates which in-game event each .txt file's messages are used for.

## Generate Chat Messages

Use this prompt with ChatGPT to create a list of chat messages for League of Legends tailored to specific emotions, styles, and game contexts.

### Prompt

Create unique chat messages for League of Legends. The messages should be based on a given emotion/tone, style, game context/what happened and who receives the message. Each message should be on a separate line, making it easy to copy them into a .txt file. The messages should always refer directly to a player. The percentage indicates how often the player should be referred to by the champion name using the placeholder "|CN|". The remaining percentage should refer to the player using pronouns like "you" or "your". If the message refers to a enemy player, than start the message with “/all”. Respond only with the messages. The messages should be in English, and ensure that there is only one message per line, without any numbering or additional characters.

Number of messages: 

Message Length: 

Percentage of messages using the champion name: 

Emotion/Tone: 

Style: 

Game context/What happened: 

Who receives the message:

### Prompt Explanation

#### Message Format

- **Number of messages**: Specify how many messages you want to create.
  - Example: 50 Messages

- **Message Length**: Specify the desired length of each message.
  - Example: short, medium, long

- **Percentage of messages using the champion name**: Determine the percentage (%) of messages that should refer to the player using their champion name. The rest should use pronouns like "you" or "your".
  - Example: 50% (This means half of the messages will use the champion name and the other half will use pronouns.)

#### Creative Freedom

- **Emotion/Tone**: Describe the emotional mood or tone for the messages.
  - Example: humorous, serious, encouraging

- **Style**: Specify any particular style for the messages.
  - Example: formal, casual, tactical

#### Limited Scenarios

- **Game context/What happened**: Provide details about the game context or specific events that should influence the content of the messages.
  - Options: self got a kill, self died, ally got a kill, ally died

- **Who receives the message**: Specify who receives each message.
  - Options: ally, enemy

### Copying and Pasting Messages

If you find the generated messages satisfactory, please copy and paste them into the respective .txt file. If you choose not to use messages for a specific event, leave that .txt file empty.

Ensure the correct usage of "/all" for messages to enemy players and the placeholder "|CN|" for champion names. Each message should be placed on a new line within the file to ensure functionality.