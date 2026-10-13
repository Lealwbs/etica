# Seminário: Manipulação Comportamental e Dark Patterns em Escala

Repositório com o material de apresentação e pesquisa para o seminário da disciplina de **Ética na Computação**.

## 📌 Tema
**Manipulação comportamental e arquitetura de interfaces (Dark Patterns em Escala)**
* **Artigo Base:** *Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites* (Mathur et al., ACM CSCW, 2019).
* **A Controvérsia:** Estudo empírico em larga escala sobre como interfaces web são sistematicamente desenhadas para induzir decisões contrárias ao interesse do usuário (como confirmações forçadas, escassez fictícia e custos ocultos).
* **Debate Ético & Filosófico:** 
  * A responsabilidade ética do desenvolvedor frontend e do designer de interação (IHC).
  * A fronteira entre design persuasivo, otimização de conversão (CRO) e coerção comportamental.
  * Livre-arbítrio e autonomia (Immanuel Kant) versus determinismo algorítmico.
  * Paternalismo libertário (*Nudge*) vs. paternalismo predatório (*Sludge*).

---

## 📂 Conteúdo do Repositório

* **[`Apresentacao_Etica_Dark_Patterns.pptx`](./Apresentacao_Etica_Dark_Patterns.pptx):** Apresentação completa em 26 slides (widescreen 16:9, tema escuro moderno, cartões estruturados, notas de orador e momentos interativos com a sala). Pode ser aberta no PowerPoint ou importada diretamente no Google Slides.
* **[`ROTEIRO_SEMINARIO_DARK_PATTERNS.md`](./ROTEIRO_SEMINARIO_DARK_PATTERNS.md):** Guia detalhado minuto a minuto para uma apresentação de 40 minutos em 4 integrantes (~10 min cada), incluindo notas de fala, condução das dinâmicas interativas e respostas blindadas para o debate.
* **[`build_presentation.py`](./build_presentation.py):** Script Python automatizado utilizando `python-pptx` para gerar/atualizar o arquivo de apresentação.
* **[`Dark_Patterns_at_Scale.pdf`](./Dark_Patterns_at_Scale.pdf):** Artigo científico original publicado na ACM CSCW 2019.

---

## 🚀 Como Executar o Gerador de Slides (Opcional)

Para reconstruir ou editar programaticamente os slides via Python:

```bash
pip install python-pptx
python build_presentation.py
```
