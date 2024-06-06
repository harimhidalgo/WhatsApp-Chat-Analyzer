# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:50:59 2023

@author: Harim_Hidalgo
"""

import re
import pandas as pd
import matplotlib.pyplot as plt
from nltk import word_tokenize, FreqDist
from wordcloud import WordCloud
import emoji
import nltk


def extract_date(line):
    date_pattern = r'(\d{2}/\d{2}/\d{2})'

    date_match = re.search(date_pattern, line)
    
    if date_match:
        date = date_match.group(1)
        return date
    else:
        return None

def extract_author(line):
    author_pattern = r'-\s+(.*?):'

    author_match = re.search(author_pattern, line)
    
    if author_match:
        author = author_match.group(1)
        return author
    else:
        return None

def extract_message(line):
    message_pattern = r'-(.*?:)\s+(.*)'
    message_match = re.search(message_pattern, line)
    
    if message_match:
        message = message_match.group(2)
        return message
    else:
        return None

    
data = {'Date': [], 'Author': [], 'Message': []}


with open(r"ADD\YOUR\FILE\PATH\HERE", 'r', encoding='utf-8') as file:
    for line in file:
        date = extract_date(line)
        if date:
            data['Date'].append(date)
        author = extract_author(line)
        if author:
            data['Author'].append(author)
        message = extract_message(line)
        if message:
            data['Message'].append(message)


df = pd.DataFrame(data)



# Calculate and plot messages sent per day
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')
messages_per_day = df.groupby('Date')['Message'].count()
plt.figure(figsize=(12, 6))
messages_per_day.plot(kind='line', marker='o', color='g')
plt.title('Messages Sent per Day')
plt.xlabel('Date')
plt.ylabel('Number of Messages')
plt.tight_layout()
plt.show()

# Calculate and plot messages sent per person
messages_per_person = df['Author'].value_counts()
plt.figure(figsize=(10, 6))
messages_per_person.plot(kind='bar', color='r')
plt.title('Messages Sent per Person')
plt.xlabel('Author')
plt.ylabel('Number of Messages')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Get most common words
borrar = ['algún', 'alguna', 'algunas', 'alguno', 'algunos', 'ambos', 'ampleamos', 'ante', 'antes', 'aquel', 'aquellas', 'aquellos', 'aqui', 'arriba', 'atras', 'bajo', 'bastante', 'bien', 'cada', 'cierta', 'ciertas', 'cierto', 'ciertos', 'como', 'con', 'conseguimos', 'conseguir', 'consigo', 'consigue', 'consiguen', 'consigues', 'cual', 'cuando', 'dentro', 'desde', 'donde', 'dos', 'el', 'ellas', 'ellos', 'empleais', 'emplean', 'emplear', 'empleas', 'empleo', 'en', 'encima', 'entonces', 'entre', 'era', 'eramos', 'eran', 'eras', 'eres', 'es', 'esta', 'estaba', 'estado', 'estais', 'estamos', 'estan', 'estoy', 'fin', 'fue', 'fueron', 'fui', 'fuimos', 'gueno', 'ha', 'hace', 'haceis', 'hacemos', 'hacen', 'hacer', 'haces', 'hago', 'incluso', 'intenta', 'intentais', 'intentamos', 'intentan', 'intentar', 'intentas', 'intento', 'ir', 'la', 'largo', 'las', 'lo', 'los', 'mientras', 'mio', 'modo', 'muchos', 'muy', 'nos', 'nosotros', 'otro', 'para', 'pero', 'podeis', 'podemos', 'poder', 'podria', 'podriais', 'podriamos', 'podrian', 'podrias', 'por', 'por qué', 'porque', 'primero', 'puede', 'pueden', 'puedo', 'quien', 'sabe', 'sabeis', 'sabemos', 'saben', 'saber', 'sabes', 'ser', 'si', 'siendo', 'sin', 'sobre', 'sois', 'solamente', 'solo', 'somos', 'soy', 'su', 'sus', 'también', 'teneis', 'tenemos', 'tener', 'tengo', 'tiempo', 'tiene', 'tienen', 'todo', 'trabaja', 'trabajais', 'trabajamos', 'trabajan', 'trabajar', 'trabajas', 'trabajo', 'tras', 'tuyo', 'ultimo', 'un', 'una', 'unas', 'uno', 'unos', 'usa', 'usais', 'usamos', 'usan', 'usar', 'usas', 'uso', 'va', 'vais', 'valor', 'vamos', 'van', 'vaya', 'verdad', 'verdadera', 'verdadero', 'vosotras', 'vosotros', 'voy', 'yo', 'él', 'ésta', 'éstas', 'éste', 'éstos', 'última', 'últimas', 'último', 'últimos', 'a', 'añadió', 'aún', 'actualmente', 'adelante', 'además', 'afirmó', 'agregó', 'ahí', 'ahora', 'al', 'algo', 'alrededor', 'anterior', 'apenas', 'aproximadamente', 'aquí', 'así', 'aseguró', 'aunque', 'ayer', 'buen', 'buena', 'buenas', 'bueno', 'buenos', 'cómo', 'casi', 'cerca', 'cinco', 'comentó', 'conocer', 'consideró', 'considera', 'contra', 'cosas', 'creo', 'cuales', 'cualquier', 'cuanto', 'cuatro', 'cuenta', 'da', 'dado', 'dan', 'dar', 'de', 'debe', 'deben', 'debido', 'decir', 'dejó', 'del', 'demás', 'después', 'dice', 'dicen', 'dicho', 'dieron', 'diferente', 'diferentes', 'dijeron', 'dijo', 'dio', 'durante', 'e', 'ejemplo', 'ella', 'ello', 'embargo', 'encuentra', 'esa', 'esas', 'ese', 'eso', 'esos', 'está', 'están', 'estaban', 'estar', 'estará', 'estas', 'este', 'esto', 'estos', 'estuvo', 'ex', 'existe', 'existen', 'explicó', 'expresó', 'fuera', 'gran', 'grandes', 'había', 'habían', 'haber', 'habrá', 'hacerlo', 'hacia', 'haciendo', 'han', 'hasta', 'hay', 'haya', 'he', 'hecho', 'hemos', 'hicieron', 'hizo', 'hoy', 'hubo', 'igual', 'indicó', 'informó', 'junto', 'lado', 'le', 'les', 'llegó', 'lleva', 'llevar', 'luego', 'lugar', 'más', 'manera', 'manifestó', 'mayor', 'me', 'mediante', 'mejor', 'mencionó', 'menos', 'mi', 'misma', 'mismas', 'mismo', 'mismos', 'momento', 'mucha', 'muchas', 'mucho', 'nada', 'nadie', 'ni', 'ningún', 'ninguna', 'ningunas', 'ninguno', 'ningunos', 'no', 'nosotras', 'nuestra', 'nuestras', 'nuestro', 'nuestros', 'nueva', 'nuevas', 'nuevo', 'nuevos', 'nunca', 'o', 'ocho', 'otra', 'otras', 'otros', 'parece', 'parte', 'partir', 'pasada', 'pasado', 'pesar', 'poca', 'pocas', 'poco', 'pocos', 'podrá', 'podrán', 'podría', 'podrían', 'poner', 'posible', 'próximo', 'próximos', 'primer', 'primera', 'primeros', 'principalmente', 'propia', 'propias', 'propio', 'propios', 'pudo', 'pueda', 'pues', 'qué', 'que', 'quedó', 'queremos', 'quién', 'quienes', 'quiere', 'realizó', 'realizado', 'realizar', 'respecto', 'sí', 'sólo', 'se', 'señaló', 'sea', 'sean', 'según', 'segunda', 'segundo', 'seis', 'será', 'serán', 'sería', 'sido', 'siempre', 'siete', 'sigue', 'siguiente', 'sino', 'sola', 'solas', 'solos', 'son', 'tal', 'tampoco', 'tan', 'tanto', 'tenía', 'tendrá', 'tendrán', 'tenga', 'tenido', 'tercera', 'toda', 'todas', 'todavía', 'todos', 'total', 'trata', 'través', 'tres', 'tuvo', 'usted', 'varias', 'varios', 'veces', 'ver', 'vez', 'y', 'ya', 'multimedia', 'omitido', '<', '>', 'jsjs', 'jaja', 'jajaja', 'jajajaja', 'jiji', 'jajajajajaj', 'jajs', 'jaja', 'jsja', '?', ':', ',', '(', ')', '+', '|', '/', '!', 'te','❤️','jajajajaja','3','ti', 'ay', 'tú', 'ti', '♥️', 'tu', 'jajsja', '*', ':3', '"', "'", "😍", "🥰", "😂", "😂♥️", "😂❤️", '🥺', "”", 'https', 'awww', 'awwwwww', ':333' ,'://3' ,'jajajajajaja' ,'jsjsjsjs', '🥰❤️' ,'🥲' ,'😘' ,'jsjsjs', 'yap', '//3', ':0', ':333', '\U0001f979❤️' , '😍❤️', '😂❤️', ':3333', 'awwww', 'chiquisss', 'chiquiiiis', 'c', 'mis' ,'sé', 'sipi']                                            

all_messages = ' '.join(df['Message'])
tokens = word_tokenize(all_messages.lower())
tokens = [word for word in tokens if word not in borrar]
words_freq = FreqDist(tokens)
common_words = words_freq.most_common(27)

# Generate bar chart for most common words
plt.figure(figsize=(10, 6))
plt.bar([word[0] for word in common_words], [word[1] for word in common_words])
plt.title('Top 10 Most Common Words')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Generate word cloud for all messages
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(tokens))
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Word Cloud of All Messages')
plt.axis('off')
plt.tight_layout()
plt.show()

