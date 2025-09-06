# Projeto de Data Science *Star Wars: The Clone Wars*

Este projeto analisa a série animada *Star Wars: The Clone Wars* (2008–2020) utilizando técnicas de **Processamento de Linguagem Natural (PLN)** e **análise de redes complexas**.  
O objetivo é investigar padrões narrativos, centralidade de personagens e evolução temática ao longo das sete temporadas.

## Estrutura do Projeto

- **character_network/**  
  Notebook para construção de redes de interação entre personagens.  
  Técnicas utilizadas:  
  - Processamento e limpeza de legendas (`.srt`)  
  - Reconhecimento de Entidades Nomeadas (spaCy `en_core_web_trf`)  
  - Normalização de nomes de personagens  
  - Extração de coocorrências de personagens  
  - Construção de grafos com NetworkX e PyVis  
  - Análise longitudinal (comparação entre temporadas)  

- **theme_classifier/**  
  Notebook e código para análise temática dos roteiros.  
  Técnicas utilizadas:  
  - Classificação zero-shot com modelos transformers  
  - Dicionários customizados de motivos narrativos)  
  - Análise temporal da frequência dos temas ao longo dos episódios

## Como Reproduzir

1. Clone o repositório:
```bash
git clone https://github.com/kzini/the_clone_wars_narrative_analysis
cd ***
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute os notebooks na pasta `notebooks/` para reproduzir os experimentos.

> Desenvolvido por Bruno Casini  
> Contato: kzini1701@gmail.com


