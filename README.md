# WhatsApp-Chat-Analyzer
This repository contains a Python script for analyzing WhatsApp chat logs, creating visual of the data. 

This Python script is designed to analyze WhatsApp chat logs. It extracts dates, authors, and messages from the chat, and provides various visualizations such as messages per day, messages per person, most common words, and a word cloud. The script requires a text file of the chat history exported from WhatsApp.

Prerequisites
Make sure you have the following Python libraries installed:

re
pandas
matplotlib
nltk
wordcloud
emoji
You can install these libraries using pip:

bash
Copiar código
pip install pandas matplotlib nltk wordcloud emoji
How to Use
Download Your WhatsApp Chat History:
Export your WhatsApp chat history to a text file and save it on your computer.

Update File Path:
Open the script and update the file path in the open function to point to your downloaded WhatsApp chat history file:

python
Copiar código
with open(r"ADD\YOUR\FILE\PATH\HERE", 'r', encoding='utf-8') as file:
Run the Script:
Execute the script. It will process the chat data and generate visualizations.

Functions
