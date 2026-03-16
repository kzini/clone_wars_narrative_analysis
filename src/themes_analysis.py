import nltk
from nltk.tokenize import sent_tokenize
import numpy as np
import re

def get_themes_clone_wars(script, theme_classifier, themes):
    script_sentences = sent_tokenize(script)

    script_batches = []
    sentence_batch_size = 25
    for index in range(0, len(script_sentences), sentence_batch_size):
        sent = " ".join(script_sentences[index:index+sentence_batch_size])
        script_batches.append(sent)

    emotion_output = theme_classifier(script_batches, themes, multi_label=True)

    emotions = {}
    for output in emotion_output:
        for label, score in zip(output['labels'], output['scores']):
            if score < 0.3:
                continue
            if label not in emotions:
                emotions[label] = []
            emotions[label].append(score)

    emotions = {key: np.mean(np.array(value)) for key, value in emotions.items()}
    return emotions

def detect_themes_presence(script, themes):
    if not script or not script.strip():
        return 0.0

    sentences = sent_tokenize(script)
    total_score = 0.0
    counted_sentences = 0

    for sentence in sentences:
        sentence_lower = sentence.lower()
        if len(sentence_lower.split()) < 4:
            continue

        sentence_score = 0.0
        for theme, data in themes.items():
            for keyword in data['keywords']:
                if re.search(r'\b{}\b'.format(re.escape(keyword)), sentence_lower):
                    sentence_score += data['weight']
                    break

        if sentence_score > 0:
            total_score += sentence_score
            counted_sentences += 1

    if counted_sentences == 0:
        return 0.0

    normalized_score = total_score / counted_sentences
    return normalized_score

