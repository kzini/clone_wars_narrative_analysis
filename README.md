# Star Wars: The Clone Wars  
## Análise narrativa com NLP e redes complexas

## Visão geral

Este projeto analisa a estrutura narrativa da série *Star Wars: The Clone Wars* a partir de legendas em texto, combinando técnicas de processamento de linguagem natural (NLP), análise de redes complexas e classificação temática.

O objetivo não é prever eventos ou personagens, mas compreender como a narrativa evolui estrutural e semanticamente ao longo das temporadas, identificando padrões de centralidade, fragmentação e mudança temática.

---

## Questão analítica

A série apresenta múltiplos núcleos narrativos e dezenas de personagens recorrentes.  
A questão central do projeto é:

> Como a complexidade estrutural das relações entre personagens e os temas narrativos evoluem ao longo das temporadas?

A análise investiga como mudanças na densidade relacional e na centralidade dos personagens se associam a momentos de transição narrativa ao longo da série.

---

## Metodologia

### 1. Processamento de linguagem natural

- Extração de entidades nomeadas (`PERSON`) com spaCy (`en_core_web_trf`)
- Normalização extensiva de nomes (aliases, títulos e variações)
- Filtragem semântica de entidades irrelevantes

**Decisão metodológica**  
Foi priorizado controle semântico e coerência narrativa em vez de pipelines totalmente automáticos.

---

### 2. Modelagem das relações narrativas

- Relações inferidas por coocorrência textual
- Arestas ponderadas pela frequência de coocorrência
- Agregação das relações por temporada

> As relações representam proximidade narrativa, não necessariamente interação social direta.

---

### 3. Análise de redes de personagens

- Construção de grafos sazonais com NetworkX
- Métricas analisadas:
  - número de personagens
  - número de relações
  - grau médio
  - personagem mais central por temporada
- Detecção de comunidades
- Visualização interativa com PyVis

Notebook principal:  
`notebooks/character_network.ipynb`

---

### 4. Análise temporal

- Comparação longitudinal entre temporadas
- Séries temporais de métricas estruturais
- Avaliação da estabilidade e ruptura de relações centrais

**Insight-chave**  
A redução progressiva de interações entre personagens centrais antecipa rupturas narrativas explícitas, sugerindo o uso consciente da densidade relacional como ferramenta narrativa.

---

### 5. Classificação temática

- Classificação temática via zero-shot learning
- Modelo: `facebook/bart-large-mnli`
- Definição manual de conjuntos semânticos de temas
- Agregação temporal por temporada

**Nota**  
Os scores representam tendências relativas, não medidas absolutas.

Notebook:  
`notebooks/theme_classification.ipynb`

---

## Principais resultados

- Temporadas iniciais apresentam redes mais densas e centralizadas
- Temporadas intermediárias mostram fragmentação narrativa e aumento do número de comunidades
- Temporadas finais apresentam redução estrutural e reconcentração narrativa
- Mudanças na centralidade dos personagens acompanham arcos narrativos
- A evolução temática antecipa eventos-chave da narrativa
- O Lado Sombrio apresenta intensificação progressiva até a temporada final

---

## Estrutura do projeto

```
clone_wars_narrative_analysis
├── data/
│   └── subs/
├── src/
│   ├── data_processing.py
│   ├── network_analysis.py
│   └── visualization.py
├── notebooks/
│   ├── character_network.ipynb
│   └── theme_classification.ipynb
└── README.md

```

---

## Limitações

- Relações baseadas em coocorrência não garantem interação direta
- Dependência da qualidade textual das legendas
- Classificação temática baseada em inferência semântica

---

## Tecnologias utilizadas

Python · spaCy · NetworkX · PyVis · Transformers · pandas · NumPy · matplotlib

---

## Como Reproduzir

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
