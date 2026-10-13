# 🎓 Seminário: Ética na Computação — Dark Patterns em Escala

Repositório oficial com todo o material de apresentação, pesquisa e roteiro para o seminário da disciplina de **Ética na Computação**.

---

## 🗂️ Estrutura de Pastas e Arquivos

Aqui está o mapa completo de onde encontrar cada arquivo no projeto:

```
etica/
├── 📁 apresentacao/             # 🎯 O QUE VOCÊ USA NO DIA DA APRESENTAÇÃO
│   ├── Seminario_Etica_Dark_Patterns.pdf    # Apresentação final em PDF (32 slides prontos para projetar)
│   └── Apresentacao_Etica_Dark_Patterns.pptx # Apresentação completa em PowerPoint (.pptx editável)
│
├── 📁 roteiro/                  # 🗣️ GUIA DE FALA E DINÂMICAS DA EQUIPE
│   └── ROTEIRO_SEMINARIO_DARK_PATTERNS.md  # Roteiro minuto a minuto (4 integrantes, falas e debate)
│
├── 📁 referencias/              # 📚 ARTIGOS E EMBASAMENTO TEÓRICO
│   └── Dark_Patterns_at_Scale.pdf           # Artigo científico base (Mathur et al., ACM CSCW 2019)
│
├── 📁 gerador_de_slides/        # ⚙️ SCRIPTS E FONTES DE GERAÇÃO (Uso técnico / opcional)
│   ├── build_master_pdf.py                  # Script Python que renderiza e une os slides
│   ├── build_presentation.py                # Script Python que gera a apresentação em PPTX
│   ├── google_slides_original.pdf           # Cópia original exportada do Google Slides
│   ├── novos_slides.html                    # Código HTML estilizado com os slides adicionais
│   └── novos_slides.pdf                     # PDF intermediário dos novos slides
│
├── .gitignore                   # Arquivos ignorados pelo Git
└── README.md                    # Guia explicativo do repositório
```

---

## 📖 Qual arquivo é qual?

### 1. 🎯 [`apresentacao/`](./apresentacao/) — Para Apresentar
* **[`Seminario_Etica_Dark_Patterns.pdf`](./apresentacao/Seminario_Etica_Dark_Patterns.pdf)**: **A versão final master recomendada para projetar na aula.** Contém 32 slides em alta resolução (formato 16:9 widescreen), unindo o design original do Google Slides com os novos slides de dinâmica com a turma, engenharia reversa de código JS, filosofia moral e regulação jurídica.
* **[`Apresentacao_Etica_Dark_Patterns.pptx`](./apresentacao/Apresentacao_Etica_Dark_Patterns.pptx)**: Slides em formato editável do Microsoft PowerPoint, com cartões modernos e as anotações de orador (*speaker notes*) embutidas em cada slide.

### 2. 🗣️ [`roteiro/`](./roteiro/) — Para Estudar e Ensaiar
* **[`ROTEIRO_SEMINARIO_DARK_PATTERNS.md`](./roteiro/ROTEIRO_SEMINARIO_DARK_PATTERNS.md)**: **Documento indispensável para a equipe.** Divide os 40 minutos de apresentação entre os 4 integrantes (~10 min cada), trazendo:
  * Exatamente o que cada integrante fala slide a slide.
  * Como conduzir as 3 dinâmicas interativas com a turma.
  * Respostas prontas e fundamentadas para as perguntas da banca/professor no debate final.

### 3. 📚 [`referencias/`](./referencias/) — Para Consulta Teórica
* **[`Dark_Patterns_at_Scale.pdf`](./referencias/Dark_Patterns_at_Scale.pdf)**: Artigo científico original publicado na conferência *ACM CSCW 2019* (*"Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites"*), que serviu de base empírica e científica para todo o seminário.

### 4. ⚙️ [`gerador_de_slides/`](./gerador_de_slides/) — Ferramental Técnico (Opcional)
Contém os códigos e assets intermediários usados para compilar e gerar a apresentação programaticamente:
* `build_master_pdf.py`: Script que utiliza headless browser (Edge) e PyMuPDF para compilar o PDF final com paginação perfeita.
* `build_presentation.py`: Script Python com biblioteca `python-pptx` para recriar toda a estrutura em PowerPoint.
* `novos_slides.html` e `novos_slides.pdf`: Template web e PDF intermediário com os novos blocos de conteúdo.
* `google_slides_original.pdf`: Base original exportada do Google Slides antes das integrações.

---

## 📌 Tema do Seminário

* **Tema:** Manipulação Comportamental e Arquitetura de Interfaces (Dark Patterns em Escala).
* **Artigo Base:** *Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites* (Mathur et al., ACM CSCW, 2019).
* **Eixos Centrais:**
  * **Técnico:** Como plataformas e scripts de terceiros (DPaaS) injetam escassez falsa, contagens regressivas fictícias e taxas ocultas.
  * **Psicológico & IHC:** Heurísticas cognitivas, viés de ancoragem e fadiga decisória.
  * **Ético & Filosófico:** Violação da autonomia e imperativo categórico (Kant) vs. paternalismo libertário (*Nudge*) e predatório (*Sludge*).
  * **Profissional & Legal:** Código de Conduta da ACM, Marco Civil / LGPD, AI Act da União Europeia e sanções da FTC.
