import matplotlib.pyplot as plt
import numpy as np
from .network_analysis import get_relationship_data

def plot_relationships_comparison(relationships_by_season, character, characters_to_compare):
    relationship_data = {}
    seasons = sorted(relationships_by_season.keys())
    
    for char_name in characters_to_compare:
        rel_data, _ = get_relationship_data(relationships_by_season, character, char_name)
        relationship_data[char_name] = rel_data
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = plt.cm.tab20(np.linspace(0, 1, len(characters_to_compare)))
    
    for i, (char_name, data) in enumerate(relationship_data.items()):
        ax.plot(seasons, data, marker='o', linewidth=3, markersize=6,
                label=char_name, color=colors[i], alpha=0.8)
    
    ax.set_title(f"Relações de {character} ao longo das temporadas", 
                fontsize=16, fontweight='bold')
    ax.set_xlabel('Temporada', fontsize=12)
    ax.set_ylabel('Número de Interações', fontsize=12)
    ax.set_xticks(seasons)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.,
             fontsize=11, frameon=True, shadow=True) 
    plt.tight_layout()
    plt.show()
