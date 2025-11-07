import pandas as pd
import networkx as nx
from pyvis.network import Network

def generate_relationships_by_season(df, window=10):
    relationships_by_season = {}
    
    for season in sorted(df['season'].unique()):
        season_df = df[df['season'] == season]
        entity_relationship = []
        
        # Processa cada episódio da temporada
        for _, row in season_df.iterrows():
            previous_entities_in_window = []
            
            for sentence in row['ners_normalized']:
                previous_entities_in_window.append(sentence)
                previous_entities_in_window = previous_entities_in_window[-window:]
                
                previous_entities_flattened = sum(previous_entities_in_window, [])
                
                for entity in sentence:            
                    for entity_in_window in previous_entities_flattened:
                        if entity != entity_in_window:
                            entity_rel = sorted([entity, entity_in_window])
                            entity_relationship.append(entity_rel)
        
        if entity_relationship:
            relationship_df = pd.DataFrame({'value': entity_relationship})
            relationship_df['source'] = relationship_df['value'].apply(lambda x: x[0])
            relationship_df['target'] = relationship_df['value'].apply(lambda x: x[1])
            
            relationship_df = (relationship_df
                              .groupby(['source', 'target'])
                              .count()
                              .reset_index()
                              .sort_values('value', ascending=False))
            
            relationships_by_season[season] = relationship_df
        else:
            relationships_by_season[season] = pd.DataFrame()
    
    return relationships_by_season

def assign_group(character_name):
    jedi = ['Anakin', 'Obi-Wan', 'Ahsoka', 'Yoda', 'Mace Windu', 'Plo Koon', 'Aayla Secura', 
    'Barriss Offee', 'Shaak Ti', 'Sifo-Dyas', 'Qui-Gon', 'Pong Krell', 'Quinlan Vos', 'Luminara Unduli', 
    'Tiin', 'Kit Fisto', 'Bolla', 'Ki-Adi-Mundi', 'Nahda', 'Nema', 'Eeth Koth', 'Nahdar', 'Piell', 
    'Ropal', 'Adi Gallia']
    
    sith = ['Dooku', 'Asajj Ventress', 'Darth Maul', 'Darth Sidious', 'Savage Opress']

    clones = [
        'Rex', 'Cody', 'Waxer', 'Bly', 'Echo', 'Jesse', 'Krell', 'Gregor',
        'Kix', 'Fives', 'Wolffe', 'Ponds', 'Fox', 'El-Les', 'Hevy', 'Lucky',
        'Redeye', 'Dogma', 'Hardcase', 'Coburn', 'Chopper', 'Odd', 'Denal',
        'Hawkeye', 'Trapper', 'Slick', 'Broadside', 'Buzz', 'Gearshift',
        'Lunker', 'Hawk', 'Red', 'Sarge', 'Meebur', 'Jax', 'Jiro', 'Jinx',
        'Thorn', 'Wooley', 'Vaughn', 'Havoc', 'Rys', 'Shiney', 'Tiplar',
        'Rush', 'Hunter', 'Wrecker', 'Tech', 'Boil', 'Gree', 'Spark', 'Crys', 
        'Cut', 'Tup', 'Boss', 'Ringo', 'Crasher'
    ]
   
    bounty_hunters = [
    'Cad Bane', 'Bossk', 'Aurra', 'Embo', 'Boba Fett', 'Castas',
    'Dengar', 'Highsinger', 'Latts', 'Aurra', 'Dengar', 'Cato'
]

    politicians = [
    'Padmé', 'Palpatine', 'Onaconda Farr', 'Nute Gunray', 'Chuchi ', 'Kharrus', 'Cho', 'Chuchi', 
    'Kharrus', 'Peteen', 'Kin', 'Clovis', 'Valorum', 'Lott', 'Bail Organa', 'Jar Jar Binks', 'Chi', 
    'Aang', 'Mina Bonteri', 'Lolo', 'Mon Mothma', 'Tills'
]

    mandalorians = ['Satine', 'Vizsla', 'Bo-Katan', 'Ursa', 'Almec', 'Korkie']

    if character_name in jedi:
        return 'jedi'
    elif character_name in sith:
        return 'sith'
    elif character_name in clones:
        return 'clone'
    elif character_name in bounty_hunters:    
        return 'bounty_hunter'   
    elif character_name in politicians:    
        return 'politician' 
    elif character_name in mandalorians:    
        return 'mandalorian' 
    else:
         return 'other'

def create_season_network(relationship_df, season_number, min_occurrences):
    rel_filtered = relationship_df[relationship_df['value'] >= min_occurrences]
    
    if rel_filtered.empty:
        print(f"Temporada {season_number}: Não há relações significativas!")
        return None
    
    G_season = nx.Graph()
    for _, row in rel_filtered.iterrows():
        G_season.add_edge(row['source'], row['target'], weight=row['value'])
    
    net = Network(notebook=True, cdn_resources='remote', width="800px", height="600px", 
                  bgcolor='#222222', font_color='white')
    
    # Configurações
    net.set_options("""
    var options = {
      "physics": {
        "enabled": true,
        "stabilization": {"iterations": 100},
        "solver": "forceAtlas2Based",
        "forceAtlas2Based": {
          "gravitationalConstant": -50,
          "centralGravity": 0.01,
          "springLength": 100,
          "springConstant": 0.08,
          "damping": 0.4
        }
      },
      "interaction": {
        "hover": true,
        "hoverConnectedEdges": true,
        "tooltipDelay": 200,
        "navigationButtons": true,
        "keyboard": true
      },
      "nodes": {
        "font": {
          "size": 20, 
          "face": "Tahoma",
          "color": "white",
          "strokeWidth": 2,
          "strokeColor": "#222222"
        },
        "shadow": {
          "enabled": true,
          "color": "rgba(0,0,0,0.5)",
          "size": 10,
          "x": 5,
          "y": 5
        },
        "shapeProperties": {
          "useBorderWithImage": true
        },
        "borderWidth": 2,
        "borderWidthSelected": 4,
        "color": {
          "border": "#2B7CE9",
          "background": "#97C2FC",
          "highlight": {
            "border": "#2B7CE9",
            "background": "#D2E5FF"
          },
          "hover": {
            "border": "#2B7CE9",
            "background": "#FFFF00"
          }
        }
      },
      "edges": {
        "color": {
          "color": "rgba(255,255,255,0.5)",
          "highlight": "#FFA500",
          "hover": "#FFD700"
        },
        "width": 2,
        "hoverWidth": 3,
        "selectionWidth": 4,
        "smooth": {
          "enabled": true,
          "type": "continuous"
        },
        "arrows": {
          "to": {
            "enabled": false,
            "scaleFactor": 1.5
          }
        },
        "shadow": {
          "enabled": true,
          "color": "rgba(0,0,0,0.3)",
          "size": 5,
          "x": 3,
          "y": 3
        }
      },
      "layout": {
        "improvedLayout": true,
        "hierarchical": {
          "enabled": false,
          "direction": "UD",
          "sortMethod": "directed"
        }
      },
      "groups": {
        "jedi": {
          "color": {
            "border": "#00FF00",
            "background": "#00CC00",
            "highlight": {"border": "#00FF00", "background": "#00FF99"}
          },
          "font": {"color": "white"}
        },
        "sith": {
          "color": {
            "border": "#FF0000", 
            "background": "#CC0000",
            "highlight": {"border": "#FF0000", "background": "#FF6666"}
          }
        },
        "bounty_hunter": {
          "color": {
            "border": "#888888",
            "background": "#FF9900",
            "highlight": {"border": "#888888", "background": "#EEEEEE"}
          }
        },
        "clone": {
          "color": {
            "border": "#4169E1",
            "background": "#87CEEB",
            "highlight": {"border": "#4169E1", "background": "#ADD8E6"}
          }
        },
        "politician": {
            "color": {
                "border": "#800080",
                "background": "#D8BFD8",
                "highlight": {"border": "#800080", "background": "#E6E6FA"}
            }
        },
        "mandalorian": {
            "color": {
                "border": "#6600ff",
                "background": "#660000",
                "highlight": {"border": "#660033", "background": "#E6E6FA"}
            }
        },
        "other": {
          "color": {
            "border": "#A9A9A9",
            "background": "#D3D3D3",
            "highlight": {"border": "#A9A9A9", "background": "#E8E8E8"}
          }
        }
      }
    }
    """)
    
    for node in G_season.nodes():
        group = assign_group(node)
        size = 20 + (G_season.degree(node) * 2)
        net.add_node(node, group=group, size=size, 
                    title=f"{node}\nGrupo: {group}\nTemporada: {season_number}")
    
    for edge in G_season.edges(data=True):
        source, target, data = edge
        weight = data.get('weight', 1)
        net.add_edge(source, target, value=weight, 
                    title=f"Interações: {weight}\nTemporada: {season_number}")
    
    filename = f"network_season_{season_number}.html"
    net.show(filename)
    
    # Estatísticas
    top_relation = rel_filtered.iloc[0]
    print(f"Temporada {season_number}:")
    print(f"{len(G_season.nodes())} personagens, {len(G_season.edges())} relações")
    print(f"Relação principal: {top_relation['source']} - {top_relation['target']} ({top_relation['value']} interações)")
    print(f"Salvo como: \033[1;31m{filename}\033[0m")
    print()
    
    return G_season

def analyze_seasons_comparison(season_networks):
    comparison_data = []
    
    for season, G in season_networks.items():
        if G:
            # Calcular métricas
            degrees = dict(G.degree())
            centrality = nx.degree_centrality(G)
            
            comparison_data.append({
                'season': season,
                'nodes': len(G.nodes()),
                'edges': len(G.edges()),
                'avg_degree': sum(degrees.values()) / len(degrees),
                'density': nx.density(G),
                'top_character': max(degrees.items(), key=lambda x: x[1])[0],
                'top_centrality': max(centrality.items(), key=lambda x: x[1])[0]
            })
    
    comparison_df = pd.DataFrame(comparison_data)
    
    print("Análise comparativa entre temporadas:")
    print("=" * 35)
    
    for _, row in comparison_df.iterrows():
        print(f"- Temporada {row['season']}:")
        print(f"     Personagens: {row['nodes']}")
        print(f"     Relações: {row['edges']}")
        print(f"     Grau médio: {row['avg_degree']:.2f}")
        print(f"     Personagem central: {row['top_character']}")
        print()
    
    return comparison_df

def get_relationship_data(relationships_by_season, char1, char2):
    relationship_data = []
    seasons = sorted(relationships_by_season.keys())
    
    for season in seasons:
        rel_df = relationships_by_season[season]
        
        relation = rel_df[((rel_df['source'] == char1) & (rel_df['target'] == char2)) |
                         ((rel_df['source'] == char2) & (rel_df['target'] == char1))]
        
        relationship_data.append(relation['value'].values[0] if not relation.empty else 0)
    
    return relationship_data, seasons

