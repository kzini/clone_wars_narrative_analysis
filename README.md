# Análise narrativa de The Clone Wars com redes de personagens e classificação temática via NLP

## Visão geral

Este projeto analisa a estrutura narrativa da série Star Wars: The Clone Wars a partir de legendas em texto, combinando técnicas de NLP, análise de redes complexas e classificação temática. O objetivo é investigar como a estrutura relacional entre personagens e os temas narrativos evoluem ao longo das temporadas, buscando identificar padrões de centralidade, fragmentação da rede e mudanças semânticas associadas à progressiva intensificação do conflito na série.

### O projeto integra três níveis de análise:

1. Extração automática de personagens a partir das legendas.
2. Modelagem de redes narrativas baseadas em coocorrência textual.
3. Classificação temática das falas para identificar mudanças semânticas ao longo da série.

---

## Questão analítica

A série The Clone Wars apresenta uma narrativa composta por múltiplos núcleos de personagens e uma evolução gradual do tom ao longo das temporadas.  
O projeto investiga duas dimensões complementares: a **estrutura narrativa** (como a rede de relações entre personagens evolui ao longo das temporadas) e **conteúdo temático** (como os temas narrativos predominantes mudam ao longo da série).

---

## Metodologia

### 1. Processamento de linguagem natural

- Extração de entidades nomeadas (`PERSON`) com spaCy (`en_core_web_trf`);
- Normalização extensiva de nomes;
- Filtragem semântica de entidades irrelevantes.

---

### 2. Modelagem das relações narrativas

- Relações inferidas por coocorrência textual;
- Arestas ponderadas pela frequência de coocorrência;
- Agregação das relações por temporada.

---

### 3. Análise de redes de personagens

- Construção de grafos sazonais com NetworkX;
- Métricas analisadas:
  - número de personagens
  - número de relações
  - grau médio
  - personagem mais central por temporada
- Detecção de comunidades;
- Visualização interativa com PyVis*.

Notebook:  
`notebooks/character_network.ipynb`

*Os grafos interativos são gerados para todas as temporadas e salvos automaticamente na mesma pasta. No notebook são exibidos apenas alguns exemplos para fins de demonstração.

---

### 4. Análise temporal

- Comparação longitudinal entre temporadas;
- Séries temporais de métricas estruturais;
- Avaliação da estabilidade e ruptura de relações centrais.

---

### 5. Classificação temática

- Classificação temática via zero-shot learning;
- Modelo: `facebook/bart-large-mnli`;
- Definição manual de conjuntos semânticos de temas;
- Agregação temporal por temporada.

Notebook:  
`notebooks/theme_classification.ipynb`

---

## Principais resultados

**Pico de conectividade e densidade:** As temporadas iniciais apresentam as redes mais densas.

**Fragmentação vs. concentração:** O número de comunidades (clusters) atinge o pico nas temporadas intermediárias (até 8 comunidades), indicando uma narrativa de antologia. Na 7ª temporada, a rede se reorganiza em três grandes comunidades relativamente equilibradas (13, 11 e 8 personagens), indicando uma consolidação da narrativa em poucos núcleos principais.

**Isolamento narrativo:** As temporadas 6 e 7 apresentam uma grande redução estrutural, sugerindo um foco em conspirações isoladas e arcos pessoais em detrimento da escala épica anterior.

**Correlação entre rede e emoção:** Foi identificada uma correlação inversa entre o tamanho da rede e o tom da história. Enquanto a conectividade cai, a intensidade do Lado Sombrio cresce progressivamente, atingindo seu pico histórico no desfecho da série.

**Padrões temáticos:** Embora o tema "power" (poder) seja uma constante, os picos de "betrayal" (traição) e "corruption" (corrupção) na 6ª temporada (onde Dooku torna-se central na rede) servem como indicadores estruturais do colapso da República.

### Dinâmica relacional dos protagonistas
**Anakin Skywalker:** suas interações com Obi-Wan dominam as temporadas iniciais, refletindo o eixo mentor-aprendiz da narrativa. A partir das temporadas intermediárias ocorre uma redistribuição das interações para Ahsoka e Rex.

**Ahsoka Tano:** inicialmente fortemente ancorada em Anakin, sua rede torna-se progressivamente mais diversificada, incluindo interações relevantes com Barriss Offee e outros Jedi. 

**Obi-Wan Kenobi:** sua rede é inicialmente dominada pela forte interação com Anakin Skywalker, refletindo o papel central da dupla Jedi nas primeiras temporadas. Ao longo da série essa dependência diminui e surgem interações mais distribuídas com personagens da República, além de confrontos episódicos com antagonistas como Dooku e Darth Maul.

---

## Estrutura do projeto

```
clone_wars_narrative_analysis
├── data/
│   └── subs/
├── src/
│   ├── data_processing.py
│   ├── network_analysis.py
│   ├── themes_analysis.py
│   └── visualization.py
├── notebooks/
│   ├── character_network.ipynb
│   └── theme_classification.ipynb
└── README.md

```

---

## Limitações

- Viés do dataset. Legendagem pode omitir personagens em cena sem fala e interações não verbais;

- As relações representam proximidade textual nas legendas, e não necessariamente interação direta entre os personagens. Com isso, a rede não diferencia interação real de copresença narrativa ou referência indireta;

- A classificação temática é baseada em inferência semântica.

---

## Tecnologias utilizadas

Python · spaCy · NetworkX · PyVis · Transformers · pandas · NumPy · matplotlib

---

## Como reproduzir

### 1. Clone o repositório:
```bash
git clone https://github.com/kzini/the_clone_wars_narrative_analysis
cd clone_wars_narrative_analysis
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Baixe o modelo de NLP do spaCy:
python -m spacy download en_core_web_trf

### 4. Execute os notebooks:
notebooks/character_network.ipynb  
notebooks/theme_classification.ipynb

---

## Autor

**Bruno Casini**  
LinkedIn: https://www.linkedin.com/in/kzini
