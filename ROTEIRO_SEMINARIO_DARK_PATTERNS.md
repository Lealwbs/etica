# GUIA MESTRE & ROTEIRO: SEMINÁRIO DE ÉTICA NA COMPUTAÇÃO (40 MINUTOS)
## Tema: Manipulação Comportamental, Dark Patterns em Escala e a Ilusão do Livre-Arbítrio
**Artigo Base:** *Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites* (Mathur et al., ACM CSCW, 2019)  
**Equipe:** 4 Integrantes (~10 minutos por bloco)  
**Arquivo de Apresentação Gerado:** [Apresentacao_Etica_Dark_Patterns.pptx](file:///d:/Code/etica/Apresentacao_Etica_Dark_Patterns.pptx) (26 Slides formatados, tema escuro moderno, notas de orador e momentos de interação)

---

## COMO USAR NO GOOGLE SLIDES
Para colocar todos esses slides novos e formatados diretamente no seu Google Slides existente:
1. Abra a sua apresentação no Google Slides.
2. Clique no menu superior: **Arquivo (File)** -> **Importar slides (Import slides)**.
3. Clique na aba **Fazer upload (Upload)** e selecione o arquivo gerado: `D:\Code\etica\Apresentacao_Etica_Dark_Patterns.pptx`.
4. Você pode selecionar **Todos os slides** ou escolher exatamente quais deseja manter/substituir. Todas as caixas, cores, títulos e **notas de orador** virão juntas automaticamente!

---

## 1. O NÚCLEO FILOSÓFICO: PATERNALISMO, LIVRE-ARBÍTRIO E DARK PATTERNS

O seminário ganha nota 10 quando transcende a lista de prints e entra na ética profunda. Seus argumentos filosóficos prontos para a fala:

### A) A Ilusão do Livre-Arbítrio Digital (Kant vs. Arquitetura Comportamental)
* **O Argumento:** Quando um usuário clica em "Comprar" sob a pressão de um cronômetro falso de 3 minutos e um alerta piscando "restam apenas 2 unidades", ele agiu por livre-arbítrio?
* **A Resposta Filosófica:** Não. O filósofo **Immanuel Kant** defendia que a dignidade humana reside na autonomia moral — a capacidade de agir conforme a razão deliberada. O Dark Pattern opera como uma **violência cognitiva sutil**: ele induz um estado de estresse artificial que sequestra a razão do usuário.
* **Kant e a Instrumentalização:** O Imperativo Categórico de Kant diz: *"Trate a humanidade sempre como um fim em si mesma, e nunca meramente como um meio"*. Os dark patterns fazem o oposto: reduzem o ser humano a uma mera variável em um teste A/B para extrair lucro.

### B) Paternalismo Libertário (Nudge) vs. Paternalismo Predatório (Sludge)
* **Richard Thaler & Cass Sunstein (Prêmio Nobel - Livro *Nudge*):**
  * Toda interface precisa de uma arquitetura de escolha (algo precisa vir marcado ou pré-selecionado por padrão).
  * **Paternalismo Libertário:** O designer usa o "empurrãozinho" (*nudge*) para favorecer o bem-estar do próprio usuário (exemplo: doar órgãos por padrão, poupança automática para aposentadoria, sugerir senhas fortes). A liberdade de escolha é preservada: o usuário pode recusar com zero esforço.
  * **A Corrupção (Paternalismo Predatório / Sludge / Dark Patterns):** A corporação sequestra essa arquitetura de escolha. Ela decide o que é melhor para o faturamento DELA e desenha a interface para punir o usuário que tenta escolher diferente (exemplo: *Roach Motel* na Amazon, cobranças surpresa no checkout).
* **A Pergunta para a Turma:** *"Se as empresas já usam arquitetura de escolha para nos prejudicar, o Estado deve ser paternalista e proibir certos designs em lei (como a UE fez com o Digital Services Act), ou isso viola a livre concorrência?"*

---

## 2. CRONOGRAMA MINUTO A MINUTO (40 MINUTOS TOTAL)

| Bloco | Tempo | Responsável | Conteúdo & Dinâmica |
| :--- | :--- | :--- | :--- |
| **Bloco 1** | 00:00 - 10:00 | **Integrante 1** | **Abertura, Aquecimento Interativo e o Choque Científico:** Slides 1 ao 7. Dinâmica do *"Quem já caiu?"* e a metodologia técnica do rastreador de 11k sites. |
| **Bloco 2** | 10:00 - 20:00 | **Integrante 2** | **Taxonomia na Prática & Mini-Quiz:** Slides 8 ao 14. Dimensões de manipulação, Urgência, Escassez, Custos Ocultos e a votação *"Persuasão ou Golpe?"* com a turma. |
| **Bloco 3** | 20:00 - 30:00 | **Integrante 3** | **Manipulação Social, Obstrução e a Fraude Terceirizada:** Slides 15 ao 19. Confirmshaming, o labirinto do Prime da Amazon, as 22 empresas de plugins (DPaaS) e a psicologia do Sistema 1/2 de Kahneman. |
| **Bloco 4** | 30:00 - 40:00 | **Integrante 4** | **Filosofia, Dilema do Dev & Debate Aberto:** Slides 20 ao 26. Livre-arbítrio (Kant), Paternalismo (*Nudge* vs *Sludge*), Simulação de Sprint com a sala, leis (LGPD/FTC) e debate final. |

---

## 3. ROTEIRO DETALHADO DOS 4 BLOCOS COM NOTAS DE FALA

### BLOCO 1: INTEGRANTE 1 (Minutos 00:00 a 10:00)
* **Slides:** 1 ao 7
* **Abertura (Slide 1):**
  > *"Bom dia a todos e professor! Hoje nosso seminário não é apenas sobre designs feios ou inconvenientes na internet. Vamos discutir como a arquitetura de software e a inteligência de produto estão sendo sistematicamente programadas para sequestrar a nossa autonomia e nos fazer gastar dinheiro e dados contra a nossa vontade."*
* **MOMENTO INTERATIVO 01 (Slide 2 - 3 minutos):**
  * *Pergunte diretamente para a sala:*
    1. *"Levanta a mão quem aqui já comprou algo porque um contador dizia que a promoção acabava em 5 minutos?"* (Espere as mãos subirem).
    2. *"Quem aqui já tentou cancelar um streaming ou plano e quase jogou o computador na parede de tanta raiva com os obstáculos?"*
    3. *"Quem já viu aquele pop-up dizendo: 'Não, eu odeio economizar dinheiro' para te forçar a assinar?"*
  * *Conclusão do orador:* *"Todos nós já caímos. E isso não acontece porque somos ingênuos; acontece porque há equipes inteiras de engenharia e ciência de dados otimizando essas armadilhas."*
* **Conceito & Fronteira (Slides 3 e 4):**
  * Diferencie: UI com defeito é descuido; Dark Pattern é intencional.
  * Diferencie: Marketing persuasivo honesto (exibir fotos boas, política de troca) vs. Manipulação (forjar dados e explorar vulnerabilidades).
* **O Estudo Base & A Engenharia Reversa (Slides 5, 6 e 7):**
  * Explique a grandeza do artigo: Mathur et al. (Princeton / UChicago, 2019).
  * Rastrearam **11.227 lojas mundiais** com um robô em Selenium e OpenWPM em **53.000 páginas**.
  * Chame atenção para o fato chocante: **sites grandes enganam até 3x mais que sites pequenos**.
  * **O pulo do gato técnico (Slide 7):** Conte como os pesquisadores pegaram a mentira no código:
    > *"Eles não ficaram no 'achismo'. Gravaram as páginas a cada 4 horas por 5 dias: os cronômetros simplesmente reiniciavam! E ao inspecionarem o JavaScript, encontraram funções `Math.random()` e listas estáticas sorteando compradores imaginários em pop-ups de venda."*

---

### BLOCO 2: INTEGRANTE 2 (Minutos 10:00 a 20:00)
* **Slides:** 8 ao 14
* **As Dimensões da Coerção (Slides 8 e 9):**
  * Explique as 5 regras da taxonomia: Assimétrico (botão verde gigante vs link invisível cinza), Oculto (chamariz/decoy), Enganoso (mentira declarada), Omissão de Informação e Restritivo.
* **Categorias Empíricas (Slides 10, 11, 12 e 13):**
  * *Urgência:* O estresse do relógio que anula o pensamento analítico.
  * *Escassez:* A fraude do "Restam apenas 2 unidades" (presente em mais de 600 lojas analisadas).
  * *Sneak into Basket:* Adicionar seguro de viagem ou garantia estendida direto no carrinho por padrão (explorando a inércia humana de não desmarcar).
  * *Custos Ocultos:* As famigeradas "taxas de conveniência" em compras de ingressos, reveladas apenas na última tela depois que você já preencheu tudo (explorando a falácia do custo irrecuperável).
* **MOMENTO INTERATIVO 02: Mini-Quiz (Slide 14 - 3 minutos):**
  * Coloque os dois casos na tela e faça a sala votar levantando a mão:
    * **Caso A (Hotel na praia):** O site diz "Apenas 1 quarto!", mas o hotel tem 8 vazios (só tinha 1 no contrato do site).
      * *Resposta:* **É Dark Pattern** (Engano por omissão de contexto para forçar compra imediata).
    * **Caso B (Frete grátis progressivo):** Barra que diz "Faltam R$ 30 para frete grátis".
      * *Resposta:* **É Design Persuasivo Legítimo** (As regras são transparentes, não há mentira nem assimetria forçada).

---

### BLOCO 3: INTEGRANTE 3 (Minutos 20:00 a 30:00)
* **Slides:** 15 ao 19
* **Manipulação Social & Desvio (Slides 15 e 16):**
  * *Confirmshaming:* A humilhação emocional para impedir que você feche a propaganda.
  * *Prova Social Fake:* A exploração do efeito manada através de notificações clonadas ou geradas por script.
* **Obstrução Absoluta & O Caso Amazon (Slide 17):**
  * O padrão *Roach Motel* (fácil de assinar, impossível de sair).
  * Conte o escândalo da Amazon em 2023:
    > *"A Amazon batizou o fluxo de cancelamento do Prime internamente de 'Iliad Flow' (em alusão à Ilíada de Homero, uma jornada épica cheia de monstros e armadilhas). Eram 6 páginas e vários cliques em botões com duplo sentido para tentar fazer você desistir de cancelar. A FTC multou a empresa e abriu processo histórico."*
* **Dark Patterns as a Service (Slide 18):**
  * Apresente as **22 empresas de software terceirizadas** que vendem isso pronto para Shopify e WooCommerce.
  * O plugin *Boost* com o slogan oficial: *"Fake it till you make it"*.
  * O banimento do plugin *Beeketing* (usado em centenas de lojas) após o escândalo.
* **A Psicologia Cognitiva (Slide 19):**
  * Daniel Kahneman (*Rápido e Devagar*): Sistema 1 (emocional, rápido, impulsivo) vs. Sistema 2 (lógico, lento).
  * Os Dark Patterns bombardeiam estímulos de escassez e medo exatamente para sobrecarregar a mente e forçar o Sistema 1 a comprar sem reflexão.

---

### BLOCO 4: INTEGRANTE 4 (Minutos 30:00 a 40:00)
* **Slides:** 20 ao 26
* **O Debate Filosófico: Livre-Arbítrio (Slide 20):**
  * Questione a autonomia da vontade:
    > *"Se toda a arquitetura de informação foi viciada para induzir um único resultado, podemos afirmar que o consumidor comprou por livre e espontânea vontade? Conforme Kant, a dignidade humana é violada quando tratamos as pessoas como meros instrumentos para bater metas financeiras."*
* **Paternalismo Libertário vs. Predatório (Slide 21):**
  * Apresente o conceito de **Nudge** (Richard Thaler & Cass Sunstein).
  * O "empurrãozinho" do bem (doação de órgãos, poupança) versus a armadilha do mal (*Sludge*).
  * A grande questão: O Estado deve intervir para proteger o usuário, ou o usuário deve arcar com a responsabilidade de suas escolhas?
* **O Dilema do Desenvolvedor (Slide 22):**
  * A pressão das metas de CRO (Conversion Rate Optimization).
  * O Código de Ética da ACM (Artigo 1.2: *Avoid Harm*; Artigo 1.4: *Be Fair*).
  * *"Apenas cumpri ordens do Product Manager"* não é defesa ética para um engenheiro de software.
* **MOMENTO INTERATIVO 03: Simulação de Sprint (Slide 23 - 3 minutos):**
  * Leia o cenário da Black Friday (o PM exigindo contador falso para bater a meta da equipe).
  * Pergunte para 2 pessoas na sala: *"O que você faria na reunião? Aceitaria calado, recusaria de frente ou proporia uma alternativa ética?"*
  * Discuta como articular a alternativa ética: alertar a gestão sobre riscos de processos no Procon, perda de reputação e nulidade jurídica.
* **Leis & Futuro Técnico (Slides 24 e 25):**
  * Brasil: CDC (Art. 37/39) e LGPD (consentimento viciado é nulo).
  * União Europeia: Digital Services Act (DSA) proibindo expressamente interfaces manipulativas sob multa de até 6% do faturamento global.
  * Contra-medidas: AdBlockers de Dark Patterns, detecção por IA e padrões de navegadores.
* **Conclusão & Perguntas Abertas (Slide 26 - 4 minutos):**
  * Abra para o professor e a turma com as 3 perguntas provocativas do slide.

---

## 4. PERGUNTAS BLINDADAS (CASO O PROFESSOR OU A TURMA APERTEM)

1. **Professor: "Mas se o usuário clicar por vontade própria, onde está a ilegalidade?"**
   * *Resposta:* O Código Civil brasileiro e o CDC deixam claro que existe o "Vício de Consentimento" (dolo ou coação psicológica). Se a informação que motivou a compra era falsa (um cronômetro que nunca expirava ou um estoque que nunca existiu), o consentimento foi obtido mediante fraude, tornando o ato juridicamente nulo.

2. **Colega: "Se a empresa não usar técnicas agressivas de conversão, ela quebra diante dos concorrentes?"**
   * *Resposta:* Esse é o dilema da "Tragédia dos Comuns" e do equilíbrio de Nash. Se um trapaceia, todos sentem pressão para trapacear. É exatamente por isso que a regulação (como o Digital Services Act na Europa e a atuação da FTC nos EUA) e a ética profissional são essenciais: para nivelar o campo de jogo e punir quem trapaceia, premiando o comércio ético.

3. **Professor: "O que nós, como profissionais de computação, podemos fazer de prático?"**
   * *Resposta:* Além da recusa ética individual baseada no código da ACM, podemos implementar métricas que mensurem a saúde do relacionamento com o usuário (arrependimento pós-compra, taxa de cancelamento, NPS real) e construir ferramentas automatizadas de auditoria ética em CI/CD.
