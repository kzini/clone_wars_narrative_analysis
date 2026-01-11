import re
import chardet
import pandas as pd
from nltk import sent_tokenize

def load_and_process_subtitles(subtitles_path):    
    scripts = []
    episode_num = []
    season_num = []
    
    for path in subtitles_path:
        with open(path, 'rb') as file:
            raw_data = file.read()
            encoding = chardet.detect(raw_data)['encoding']
        
        with open(path, 'r', encoding=encoding) as file:
            content = file.read()
        
        content = content.replace('<i>', '').replace('</i>', '') # Remove tags de itálico das legendas
        subtitle_blocks = content.strip().split('\n\n')
        
        text_lines = []
        for block in subtitle_blocks:
            lines = block.split('\n')
            if len(lines) > 2:
                block_text = ' '.join(lines[2:])
                text_lines.append(block_text)
        
        script = ' '.join(text_lines).replace('\n', ' ').replace('  ', ' ')
        
        filename = path.split('\\')[-1]
        match = re.search(r'Season\s+(\d+)\s*-\s*(\d+)', filename)
        
        if match:
            season = int(match.group(1))
            episode = int(match.group(2))
        
        scripts.append(script)
        episode_num.append(episode)
        season_num.append(season)
    
    return pd.DataFrame({
    'season': season_num,
    'episode': episode_num, 
    'script': scripts
    })

def get_ners(script, nlp_model):
    script_sentences = sent_tokenize(script)
    ner_output = []
    
    for sentence in script_sentences:
        doc = nlp_model(sentence)
        ners = set()
        for ent in doc.ents: 
            if ent.label_=='PERSON':
                full_name = ent.text
                first_name=full_name.split(' ')[0]
                ners.add(first_name)
        ner_output.append(list(ners))
    return ner_output

def normalize_names(ner_list):
    normalized_ner_list = []
    
    for sentence_entities in ner_list:
        normalized_sentence = []
        for entity in sentence_entities:
            normalized_entity = name_mapping.get(entity, entity)
            if normalized_entity is not None:
                normalized_sentence.append(normalized_entity)
        
        # Remove duplicatas na mesma sentença
        normalized_sentence = list(set(normalized_sentence))
        normalized_ner_list.append(normalized_sentence)
    
    return normalized_ner_list

name_mapping = {
    # Anakin
    'Ani': 'Anakin', 
    'Skywalker': 'Anakin',
    'Skyguy': 'Anakin',  
    # Obi-Wan
    'Obi': 'Obi-Wan',
    'Kenobi': 'Obi-Wan',
    'Wan': 'Obi-Wan',
    '-Wan': 'Obi-Wan',
    'Ben': 'Obi-Wan',
    # Ahsoka
    'Ahsoka': 'Ahsoka',
    'Snips': 'Ahsoka',
    'Tano': 'Ahsoka',
    'R2': 'R2-D2',

    # outros
    'Artoo': 'R2-D2',
    'Artooie': 'R2-D2',
    'Threepio': 'C3P0',
    'Padme': 'Padmé',
    'Padm': 'Padmé',
    'Amidala': 'Padmé',
    'Amadala': 'Padmé',
    'Jar': 'Jar Jar Binks',
    'Binks': 'Jar Jar Binks',
    'Rexster': 'Rex',
    'Mon': 'Mon Mothma',
    'Maul': 'Darth Maul',
    'Tyrannus': 'Dooku',
    'Tyranus': 'Dooku',
    'Count': 'Dooku',
    'Mace': 'Mace Windu',
    'Windu': 'Mace Windu',
    'Quinlan': 'Quinlan Vos',
    'Vos': 'Quinlan Vos',
    'Ventress': 'Asajj Ventress',
    'Asajj': 'Asajj Ventress',
    'Plo': 'Plo Koon',
    'Kit': 'Kit Fisto',
    'Fisto': 'Kit Fisto',
    'Aayla': 'Aayla Secura',
    'Secura': 'Aayla Secura',
    'Bail': 'Bail Organa',
    'Organa': 'Bail Organa',
    'Cad': 'Cad Bane',
    'Bane': 'Cad Bane',
    'Mundi': 'Ki-Adi-Mundi',
    'Ki-Adi': 'Ki-Adi-Mundi',
    'Boba': 'Boba Fett',
    'Gallia': 'Adi Gallia',
    'Adi': 'Adi Gallia',
    'Eeth': 'Eeth Koth',
    'Koth': 'Eeth Koth',
    'Shaak': 'Shaak Ti',
    'Nute': 'Nute Gunray',
    'Gunray': 'Nute Gunray',
    'Pong': 'Pong Krell',
    'Savage': 'Savage Opress',
    'Saw': 'Saw Gerrera',
    'Gerrera': 'Saw Gerrera',
    'VIZSLA': 'Vizsla',
    'Pre': 'Vizsla',
    'Qui': 'Qui-Gon',
    'Sidious': 'Darth Sidious',
    'Tambor': 'Wat Tambor',
    'Wat': 'Wat Tambor',
    "Sifo-Dyas's": 'Sifo-Dyas',
    "Sifo-Dyas?": 'Sifo-Dyas',
    'Sifo': 'Sifo-Dyas',
    'Barriss': 'Barriss Offee',
    'Luminara': 'Luminara Unduli', 
    'Unduli': 'Luminara Unduli',
    'Hondo': 'Hondo',
    'Ohnaka': 'Hondo',
    'Latss': 'Latts',
    'Ta': 'Orn Free Taa',
    'Orn': 'Orn Free Taa',
    'Mina': 'Mina Bonteri',
    'Bogie': 'Boil',
    'Tal': 'Tal Merrik',  
    'Merrik': 'Tal Merrik',
    'Ono': 'Onaconda Farr',
    'Farr': 'Onaconda Farr',
    'Prince': 'Lee-Char',
    'Moralo': 'Moralo Eval',
    'Jackar': 'Jackar Bowmani',
    'Bowmani': 'Jackar Bowmani',

    'Master': None,
    'Jedi': None,
    'Padawan': None,
    'youngling': None,
    'Sith': None,
    'Darth': None,
    'dey': None,
    'the': None,
    'Hutt': None,
    'Roger': None,
    'roger': None,
    '-': None,
    'Shadow': None,
    'Viceroy': None,
    'ho': None,
    'Hidey-': None,
    'bogey': None,
    'God': None,
    'Gungan': None,
    'Wookiee': None,
    'Da': None,
    'Nightbrothers': None,
    'The': None,
    'Clones': None,
    'Clone': None,
    'Trooper': None,
    'Mmm': None,
    '.': None,
    'Meesa': None,
    'meesa': None,
    'mesa': None,
    'Yousa': None,
    'yousa':  None,
    'Me-sa': None,
    'Weesa': None,
    'mooie': None,
    'Pаdаwаn': None,
    'Milady': None,
    'milady': None,
    'Hutts': None,
    'Jedi': None,
    'Tiplee': None,
    'Jocasta': None,
    'Rodia': None,
    'jogan': None,
    'Wesa': None,
    'Mesa': None,
    'Hesa': None,
    'hesa': None,
    'Pykes': None,
    'Pyke': None,
    'Apprentice': None,
    'Abafar': None,
    'Sarrish': None,
    'Black': None,
    'Scipio': None,
    'Pykes': None,
    'Muuns': None,
    'Skako': None,
    'Kessel': None,
    'Yesa': None,
    'Martez': None,
    'Kamino': None,
    'Naboo': None,
    'Mandalore': None,
    'Mustafar': None,
    'Geonosia': None,
    'Kaminonan': None,
    'Kamanoain': None,
    'Saleucami': None,
    'Coruscant': None,
    'Geonosis': None,
    'Mandalorian': None,
    'Felucia': None,
    'Umbara': None,
    'Onderon': None, 
    'Dathomir': None,
    'Rodia': None,
    'Droll': None,
    'Shesa': None,
    'Datsa': None,
    'Disa': None,
    'Queenie': None,
    'Masterin': None,
    'Bardottan': None,
    'Frangawl': None,
    'Dagoyan': None,
    'Pantora': None,
    'Balith': None,
    'Millius': None,
    'Dechee': None,
    'Bardotta': None,
    'Quarren': None,
    'Nal': None,
    'HUTTESE': None,
    'this': None,
    'Your': None,
    'Oba': None,
    # Personagens que são apenas citados
    'Jango': None,
    'Qui-Gon': None    
}

