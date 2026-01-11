import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
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

def plot_season_themes(season_themes, themes):
  comparison_data = []
  for season, themes_df in season_themes.items():
      for _, row in themes_df.iterrows():
          comparison_data.append({
              'season': season,
              'theme': row['theme'],
              'score': row['score']
          })

  comparison_df = pd.DataFrame(comparison_data)

  plt.figure(figsize=(14, 8))
  sns.barplot(data=comparison_df, x='theme', y='score', hue='season', palette='Paired')
  plt.title('Evolução de Temas por Temporada - The Clone Wars', fontweight='bold')
  plt.xticks(rotation=45)
  plt.legend(title='Temporada')
  plt.tight_layout()
  plt.show()

def plot_themes_evolution(season_themes, themes):
    comparison_data = []
    for season, themes_df in season_themes.items():
        for _, row in themes_df.iterrows():
            comparison_data.append({
                'season': season,
                'theme': row['theme'],
                'score': row['score']
            })
    comparison_df = pd.DataFrame(comparison_data)

    plt.figure(figsize=(12, 6))
    for theme in themes:
        theme_data = comparison_df[comparison_df['theme'] == theme]
        plt.plot(theme_data['season'], theme_data['score'], marker='o', label=theme, linewidth=3)

    plt.title('Evolução de temas em The Clone Wars', fontweight='bold')
    plt.xlabel('Temporadas')
    plt.ylabel('Intensidade do Tema')

    season_values = sorted(comparison_df['season'].unique())
    plt.xticks(season_values)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def plot_specific_theme_evolution(df, theme_title, color):
  plt.figure(figsize=(12, 6))

  seasons = sorted(df['season'].unique())
  theme_scores = [df[df['season'] == s]['theme_score'].mean() for s in seasons]

  plt.plot(
      seasons,
      theme_scores,
      marker='o',
      linewidth=3,
      markersize=8,
      color=color,
      alpha=0.8,
      label=theme_title
  )

  plt.fill_between(seasons, theme_scores, alpha=0.2, color=color)
  plt.title(f'Evolução do {theme_title} por temporada',
            fontsize=14, fontweight='bold')
  plt.xlabel('Temporada')
  plt.ylabel('Intensidade')
  plt.xticks(seasons)
  plt.legend()
  plt.tight_layout()
  plt.show()