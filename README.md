# Análise narrativa de *Star Wars: The Clone Wars*

Este projeto investiga padrões narrativos, evolução temática e centralidade de personagens na série animada Star Wars: The Clone Wars (2008–2020). Utilizando técnicas de NLP e análise de redes complexas, o objetivo é entender como histórias e personagens se desenvolvem ao longo das sete temporadas.

## Motivação

Séries animadas longas como *The Clone Wars* apresentam múltiplas linhas narrativas e dezenas de personagens recorrentes. Com tantas interações, torna-se difícil identificar padrões de narrativa, temas recorrentes e a evolução de personagens ao longo do tempo. Este projeto visa responder perguntas como:

- Quais temas narrativos predominam em cada temporada?

- Como a presença e centralidade de personagens evoluem ao longo da série?

- Como o “Lado Sombrio” se manifesta e cresce na narrativa através das sete temporadas?

A análise permite visualizar o ritmo da narrativa, conflitos centrais e evolução dos personagens, demonstrando competências de ciência de dados aplicadas a storytelling.

## Abordagem

O projeto foi dividido em dois eixos complementares:

### 1. Análise de personagens e redes de interação (character_network/)

- Coleta e pré-processamento: limpeza de legendas (.srt) e normalização de nomes de personagens.

- Reconhecimento de entidades: spaCy (en_core_web_trf) para identificar personagens.

- Extração de coocorrências: construção de redes de interação com NetworkX.

- Visualização e análise: grafos interativos (PyVis) e métricas de centralidade para identificar personagens-chave e suas mudanças de relevância ao longo das temporadas.

### 2. Análise Temática de Roteiros (theme_classifier/)

- Classificação zero-shot: uso de modelos transformers para identificar temas narrativos em episódios.

- Dicionários de temas customizados: incluindo tópicos como guerra, lealdade, traição, esperança, poder e Lado Sombrio.

- Análise temporal: evolução da intensidade de temas por temporada, com destaque para a progressão do Lado Sombrio.

- Visualização: gráficos de barras e linhas para comparar temas ao longo do tempo e identificar padrões recorrentes.

## Principais descobertas

**Padrões temáticos dominantes**
Guerra, lealdade e traição emergem como pilares narrativos consistentes.

Esperança e amizade aparecem estrategicamente em arcos específicos como contrapontos emocionais.

**Estrutura narrativa dinâmica**
Alternância entre elencos amplos (Temporada 2: 64 personagens) e focos restritos (Temporada 6: 29 personagens).

Integração progressiva: Redução de 8 para 3 comunidades entre temporadas, indicando narrativas mais entrelaçadas.

**Evolução do Lado Sombrio**
Aumento consistente da presença temática do Lado Sombrio através das temporadas.

Alinhamento com o arco de transformação de Anakin Skywalker na trilogia cinematográfica.

**Rotatividade de protagonismo**
Personagens centrais variam estrategicamente: Anakin (temps 1-2-4), Ahsoka (temps 3-5), Dooku (temp 6), Rex (temp 7).

Reflete mudanças intencionais no foco dos arcos dramáticos

## Melhorias Futuras

- **Sistema automatizado de classificação de personagens**: Atualmente, a identificação de facções e normalização de nomes é feita manualmente. Uma melhoria seria implementar um sistema baseado em aprendizado de máquina para classificação automática.

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

### 3. Execute os notebooks na pasta `notebooks/` para reproduzir os experimentos

> Desenvolvido por Bruno Casini  
> Contato: kzini1701@gmail.com   
> LinkedIn: www.linkedin.com/in/kzini
