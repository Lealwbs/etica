# Manipulação Comportamental em Escala: Dark Patterns, Engenharia de Interfaces e a Erosão da Autonomia Digital

**Departamento de Ciência da Computação • Disciplina: Ética na Computação • Seminário de Pesquisa**  
**Autores:** Ítalo Leal e Equipe de Apresentação  
**Data:** Outubro de 2026  
**Documento Oficial em PDF (6 Páginas):** [`Relatorio_Etica_Dark_Patterns.pdf`](./Relatorio_Etica_Dark_Patterns.pdf)

---

### Resumo Executivo

Este relatório examina o fenômeno dos *dark patterns* sob a perspectiva da ética aplicada à computação e da engenharia de software, tomando como ponto de partida a pesquisa seminal de Mathur et al. (ACM CSCW, 2019). Analisa-se a transição da arquitetura de informação persuasiva para a coerção comportamental algorítmica, demonstrando como vulnerabilidades cognitivas humanas são exploradas sistematicamente para maximizar métricas transacionais em plataformas digitais. O trabalho disseca a arquitetura técnica dessas práticas — incluindo a injeção client-side de escassez fabricada e a terceirização via *Dark Patterns as a Service* (DPaaS) —, confronta seus mecanismos com a teoria do processo dual da psicologia cognitiva e fundamenta a crítica moral na ética deontológica de Immanuel Kant. Por fim, avaliam-se as repercussões regulatórias no Brasil (CDC e LGPD), nos Estados Unidos (ações da FTC) e na União Europeia (Digital Services Act), propondo diretrizes para uma engenharia defensiva e para a responsabilidade profissional do desenvolvedor.

**Palavras-chave:** Dark Patterns; Ética na Computação; Autonomia Moral; Engenharia de Software; Teoria do Processo Dual; Regulação de Plataformas.

---

## 1. Introdução: Da Persuasão Comercial à Coerção Algorítmica

Historicamente, a interface gráfica do usuário (GUI) foi concebida na ciência da computação como uma ponte de tradução semântica: um meio instrumental neutro destinado a diminuir a distância de execução entre a intenção mental do operador humano e os comandos interpretados pela máquina. Contudo, nas últimas duas décadas, o modelo de negócios predominante no ecossistema da internet deslocou a interface de sua função utilitária original para transformá-la em uma alavanca ativa de extração econômica e modulação de comportamento.

Nesse cenário de intensificação das métricas de conversão e retenção, cunhou-se em 2010 o termo *dark patterns* pelo designer de interação Harry Brignull, definindo padrões de arquitetura de interface cuidadosamente elaborados para induzir o usuário a realizar ações que ele presumivelmente não tomaria se as informações estivessem dispostas de forma transparente e equitativa. Longe de representarem falhas de usabilidade ou meros descuidos de ergonomia visual, essas construções são fruto de engenharia deliberada, valendo-se de experimentos controlados (testes A/B massivos) e refinamento contínuo para converter vieses cognitivos em fluxos financeiros.

A distinção entre o *design persuasivo legítimo* e o *dark pattern* reside no respeito à autodeterminação do agente. Enquanto a publicidade honesta busca evidenciar qualidades objetivas de um produto ou facilitar o percurso do consumidor preservando a clareza de suas alternativas, os padrões manipulativos operam mediante assimetria informacional deliberada, indução de pânico cognitivo e ocultação de consequências materiais. Quando um sistema força a aceitação de seguros embutidos por padrão, impõe barreiras assimétricas para cancelamento de serviços ou falsifica a escassez de estoques por meio de contadores temporais forjados em scripts client-side, rompe-se o pacto de transparência da computação interativa.

O problema atinge relevância crítica para a ética na computação porque desloca a culpa do engano para o próprio usuário: o indivíduo clica com o próprio mouse ou toca na própria tela, nutrindo a ilusão de que sua decisão foi soberana. Como demonstraremos a seguir, no entanto, essa soberania é esvaziada quando as condições materiais da deliberação racional são sabotadas pela própria arquitetura do software.

---

## 2. A Tecnologia em Exame: A Arquitetura dos Dark Patterns em Escala

Embora os relatos anedóticos sobre armadilhas em sites de comércio eletrônico fossem abundantes na literatura de interação humano-computador (IHC), a verdadeira dimensão quantitativa e estrutural do problema permaneceu desconhecida até a publicação do estudo *Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites*, conduzido por pesquisadores das universidades de Princeton e Chicago (Mathur et al., 2019). A pesquisa representou um marco metodológico ao construir uma infraestrutura automatizada de auditoria comportamental de software em larga escala.

### 2.1 Metodologia de Rastreamento e Escopo Empírico

Para superar as limitações de amostras manuais restritas, os pesquisadores desenvolveram um rastreador web distribuído baseado na plataforma OpenWPM e no framework Selenium, instrumentando instâncias automatizadas de navegadores capazes de simular o comportamento de navegação humana em 11.227 lojas virtuais selecionadas a partir do ranking global da Alexa. O rastreador navegou por aproximadamente 53.000 páginas de produtos, processando a árvore de elementos do Document Object Model (DOM), capturando respostas assíncronas de rede e registrando renderizações gráficas em múltiplos pontos temporais.

| Categoria | Mecanismo Técnico Observado | Vulnerabilidade Explorada | Prevalência Empírica |
| :--- | :--- | :--- | :--- |
| **Urgência** | Contadores regressivos de oferta que reiniciam a cada carregamento ou ciclo temporal. | Aversão à perda, estresse decisório e sobrecarga do Sistema 1. | 393 sites (21,6%) |
| **Escassez** | Alertas de "apenas 2 itens em estoque" sem sincronização com o banco relacional real. | Heurística de valor por rarefação e urgência competitiva. | 581 sites (31,9%) |
| **Prova Social** | Pop-ups exibindo compras recentes geradas dinamicamente via geradores pseudoaleatórios. | Efeito manada (*bandwagon effect*) e validação de pares. | 261 sites (14,3%) |
| **Ação Oculta (Sneaking)** | Inclusão não solicitada de garantias ou doações no carrinho com caixas pré-marcadas. | Inércia do usuário e falha no escrutínio de itens discriminados. | 116 sites (6,4%) |
| **Custos Ocultos** | Ocultação deliberada de taxas obrigatórias até o último clique do fluxo de checkout. | Falácia do custo irrecuperável (*sunk cost fallacy*). | 27 sites (1,5%) |
| **Desvio (Misdirection)** | *Confirmshaming*: linguagem depreciativa e assimetria cromática violenta em botões de recusa. | Coerção emocional, culpa artificial e indução visual ao erro. | 189 sites (10,4%) |
| **Obstrução** | Assinatura em um clique vs. cancelamento por labirintos de atendimento telefônico (*Roach Motel*). | Custos de fricção intencionais (*sludge*) e esgotamento cognitivo. | 251 sites (13,8%) |

*Tabela 1: Taxonomia empírica de Dark Patterns identificados no rastreamento de 11.227 e-commerces. Fonte: Adaptado de Mathur et al. (CSCW, 2019).*

Ao todo, foram identificadas 1.818 instâncias de *dark patterns* distribuídas em 1.254 plataformas (representando aproximadamente 11,1% de todo o universo auditado). Contudo, o dado de maior impacto ético revelado pelo estudo contradiz a intuição comum de que práticas predatórias seriam exclusividade de comércios eletrônicos obscuros ou periféricos: **sites de alto tráfego registraram probabilidade até três vezes maior de implementar padrões coercitivos** em comparação a portais de menor relevância. A sofisticação da engenharia comportamental é, portanto, diretamente proporcional à escala econômica das corporações envolvidas.

### 2.2 A Engenharia Reversa do Engano: Fraude no Código Client-Side

O rigor metodológico da equipe de Princeton residiu em não tratar as mensagens exibidas na tela como dados verdadeiros a priori. Os autores implementaram rotinas de inspeção cronológica: as páginas que exibiam contadores regressivos de urgência foram requisitadas repetidamente em intervalos de 4 horas ao longo de 5 dias consecutivos. O resultado expôs a falsidade matemática do estímulo: os cronômetros nunca chegavam a zero e nunca encerravam promoções; ao contrário, simplesmente reiniciavam sua contagem estática a cada visita ou ao término do ciclo.

Mais grave ainda foi a análise estática e dinâmica dos scripts JavaScript injetados no navegador do cliente. Os pesquisadores encontraram funções nativas de geração numérica pseudoaleatória — notadamente chamadas a `Math.random()` — associadas diretamente à renderização de indicadores de "visitantes online no momento" e "itens restantes no armazém". Da mesma forma, notificações de prova social que afirmavam, por exemplo, que "Mariana de Curitiba acabou de comprar este produto" eram alimentadas por vetores estáticos em JSON contendo nomes e cidades fictícias, iterados em intervalos pré-programados para simular atividade comercial artificial.

```javascript
// Exemplo de script de prova social e urgência artificial identificado em auditoria
function renderFakeSocialProof() {
  const nomes = ["Carlos M.", "Ana P.", "Juliana R.", "Marcos S."];
  const cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"];
  const tempoAtras = Math.floor(Math.random() * 12) + 2; // Entre 2 e 14 minutos
  
  // Sorteio puramente cosmético desprovido de qualquer transação no backend
  const usuario = nomes[Math.floor(Math.random() * nomes.length)];
  const local = cidades[Math.floor(Math.random() * cidades.length)];
  
  toast.innerHTML = `<strong>${usuario}</strong> (${local}) comprou este item há ${tempoAtras} min.`;
  toast.classList.add("visible");
}
```

### 2.3 A Industrialização da Coerção: Dark Patterns as a Service (DPaaS)

Outro achado estrutural do estudo de Mathur et al. foi a constatação de que a maioria dos comerciantes virtuais não escreve seu próprio código de manipulação. Identificou-se um mercado consolidado de provedores terceirizados vendendo *Dark Patterns as a Service* (DPaaS). Foram catalogadas 22 entidades comerciais fornecendo plugins modulares prontos para integração em plataformas como Shopify, Magento e WooCommerce. Ferramentas como o plugin *Boost* adotavam publicamente o slogan *"Fake it till you make it"* em seu material promocional, incentivando lojistas a forjar estoques e avaliações. Esse modelo pulveriza a responsabilidade moral: o lojista transfere a culpa para a extensão de software, e o desenvolvedor do plugin alega oferecer apenas uma funcionalidade neutra solicitada pelo mercado.

---

## 3. Fundamentos Cognitivos e o Dilema Ético do Desenvolvedor

Para compreender por que os *dark patterns* são eticamente reprováveis, é imprescindível recorrer à economia comportamental e à psicologia cognitiva. Em sua clássica Teoria do Processo Dual, Daniel Kahneman e Amos Tversky demonstram que a mente humana opera por meio de dois modos fundamentais de processamento: o **Sistema 1** (automático, rápido, heurístico, emocional e de baixo consumo de energia mental) e o **Sistema 2** (deliberativo, lógico, analítico, consciente e custoso metabolicamente).

Os padrões manipulativos são intencionalmente calibrados para sobrecarregar ou contornar o Sistema 2, forçando a tomada de decisões no âmbito impulsivo do Sistema 1. O bombardeio sensorial de contadores regressivos em vermelho, sinos pulsantes e mensagens de escassez iminente ativa os circuitos neurológicos de resposta ao perigo e aversão à perda. Diante da ameaça imediata de perder uma oportunidade única, o consumidor é privado do tempo de reflexão necessário para avaliar se o produto é genuinamente necessário, se o preço total é justo ou se as cláusulas contratuais são abusivas.

### 3.1 Paternalismo Libertário (Nudge) vs. Paternalismo Predatório (Sludge)

A arquitetura de escolhas em interfaces digitais nunca é neutra: qualquer tela impõe opções pré-selecionadas, ordenações de itens e hierarquias de cor. Em 2008, Richard Thaler e Cass Sunstein formularam o conceito de *Nudge* (paternalismo libertário), segundo o qual o arquiteto de escolhas deve organizar o ambiente de decisão de modo a incentivar escolhas benéficas para a saúde, bem-estar financeiro e autonomia do próprio indivíduo (como a doação presumida de órgãos ou a adesão automática a fundos de previdência com opção imediata de descadastro), sempre preservando intacta a liberdade de escolha a custo de fricção próximo de zero.

Os *dark patterns* representam a completa perversão dessa premissa, convertendo-se em paternalismo predatório ou *Sludge*. Nesse modelo, a corporação utiliza a arquitetura de escolha para maximizar os interesses da organização às expensas do bem-estar do consumidor. Introduz-se atrito intencional (*asymmetric friction*) para punir qualquer tentativa de exercício de autonomia que contrarie as metas financeiras da empresa, exemplificado na assimetria entre assinar um serviço com um único clique e ser obrigado a percorrer múltiplos formulários labirínticos para solicitar o cancelamento.

### 3.2 A Normalização do Desvio nas Sprints de Engenharia de Software

No cotidiano das equipes de tecnologia, a implementação de padrões obscuros decorre de uma cultura organizacional hipertrofiada de Otimização de Taxa de Conversão (CRO) e métricas de curto prazo (como GMV e CAC). O desenvolvedor frontend ou o engenheiro de dados recebe cartões no Jira exigindo, por exemplo, "diminuir o contraste do botão de cancelamento" ou "adicionar um timer no checkout". Cria-se uma cisão de responsabilidade pessoal: o profissional alega que está apenas cumprindo requisitos gerenciais, enquanto os analistas de produto amparam-se na validação empírica de testes A/B que apontam incremento no faturamento.

Essa postura viola frontalmente o Código de Ética e Conduta Profissional da ACM (Association for Computing Machinery). A Seção 1.2 do código determina expressamente o dever de *"Evitar Danos"*, ressaltando que danos incluem não apenas lesões físicas, mas consequências cognitivas, financeiras e privação injustificada de tempo. Paralelamente, a Seção 1.4 impõe a obrigação de *"Ser Justo e Agir sem Discriminação"*, preconizando a transparência e a recusa em participar de práticas que deliberadamente ludibriem os destinatários finais do software. O argumento de que "o cliente clicou por vontade própria" não isenta o engenheiro que codificou a armadilha visual.

---

## 4. Análise Filosófica: Autonomia, Dignidade e a Crítica Kantiana

Ao transitar da psicologia comportamental para a filosofia moral, o problema dos *dark patterns* atinge seu núcleo ético mais profundo: a destruição da autonomia moral do indivíduo. Na obra *Fundamentação da Metafísica dos Costumes* (1785), Immanuel Kant argumenta que o valor intrínseco de um ser humano — sua dignidade — repousa na sua capacidade de agir como um agente moral autônomo, dotado da faculdade de deliberar conforme razões livremente ponderadas e autodeterminadas, e não sob impulsos coercitivos externos.

O princípio fundamental da ética deontológica kantiana expressa-se na segunda formulação do Imperativo Categórico, conhecida como a **Fórmula da Humanidade**: *"Age de tal maneira que uses a humanidade, tanto na tua pessoa como na pessoa de qualquer outro, sempre e simultaneamente como um fim e nunca simplesmente como um meio"*. Quando uma equipe de engenharia de software desenha um fluxo de navegação manipulativo, ela viola precisamente essa máxima. O usuário é reificado: deixa de ser tratado como um sujeito racional detentor de direitos e fins próprios para ser degradado à condição de mero meio instrumental de enriquecimento acionário, uma variável numérica a ser convertida num funil de vendas.

A própria noção de "consentimento digital" torna-se uma ficção vazia no contexto de arquiteturas predatórias. Do ponto de vista filosófico, não há volição livre quando a alternativa discordante é deliberadamente sabotada através de *confirmshaming* (chantagem moral que agride a autoestima do indivíduo com frases como "Não, eu prefiro pagar caro") ou ofuscamento tipográfico (links de saída renderizados em tons de cinza claro sobre fundo branco). A interface opera como uma coerção física sutil, moldando os caminhos possíveis da vontade humana e expropriando o sujeito de seu livre-arbítrio prático.

---

## 5. Repercussões Contemporâneas, Arcabouço Jurídico e Engenharia Defensiva

As consequências éticas da manipulação digital deixaram o terreno estritamente acadêmico para se tornarem o epicentro de investigações judiciais de escala global. O marco mais expressivo ocorreu em junho de 2023, quando a Federal Trade Commission (FTC), órgão regulador de comércio dos Estados Unidos, ajuizou uma histórica ação civil pública contra a gigante Amazon.

> **Estudo de Caso: O Escândalo do "Iliad Flow" na Amazon Prime (FTC v. Amazon, 2023)**  
> A denúncia da FTC revelou documentos corporativos internos comprovando que a Amazon batizou seu fluxo de cancelamento de assinatura Prime com o codinome "Iliad Flow", em alusão direta à obra épica de Homero — um labirinto deliberado pontuado por obstáculos intransponíveis. Enquanto o cadastro no serviço podia ser realizado com um único clique de forma quase instantânea, o usuário que pretendia cancelar era obrigado a atravessar quatro páginas complexas, confrontado com textos prolixos, botões ambíguos de duplo sentido (nos quais "cancelar" significava manter os benefícios e pausar cobrança futura) e avisos repetitivos de perda catastrófica. Documentos vazados atestaram que os líderes de produto comemoravam internamente a queda substancial nas taxas de cancelamento obtidas através do aumento do estresse cognitivo do usuário.

### 5.1 O Arcabouço Legal Brasileiro e Internacional

No ordenamento jurídico brasileiro, a resposta aos *dark patterns* encontra esteio em diplomas consolidados. O Código de Defesa do Consumidor (CDC, Lei nº 8.078/1990) estabelece no Artigo 6º o direito básico à informação adequada, clara e veraz sobre produtos e serviços, além da proteção contra métodos comerciais coercitivos e desleais. No Artigo 37, o CDC tipifica expressamente a **publicidade enganosa** — aquela capaz de induzir em erro o consumidor a respeito da natureza, características ou preço do produto — e veda a publicidade abusiva. Por sua vez, o Artigo 39, inciso I, proíbe a venda casada, enquadrando diretamente práticas de *Sneak into Basket* em que itens como seguros e fretes prioritários são injetados sem consentimento prévio e expresso.

Complementarmente, a Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018) estipula em seus Artigos 7º e 8º que o consentimento do titular de dados pessoais deve ser uma **manifestação livre, informada e inequívoca**. A utilização de *banners* de cookies desenhados com opções assimétricas (um botão colorido chamativo para "Aceitar Tudo" e um link minúsculo, quase invisível, para "Configurar Opções") configura vício de consentimento por dolo de terceiro. Perante a doutrina civilista contemporânea, tal consentimento é juridicamente nulo, sujeitando as organizações infratoras às sanções administrativas da ANPD e a ações civis públicas.

Na vanguarda legislativa mundial, a União Europeia aprovou o *Digital Services Act* (DSA, Regulamento UE 2022/2065), cujo Artigo 25 proíbe expressamente os fornecedores de plataformas online de desenhar, organizar ou operar suas interfaces de modo a distorcer ou prejudicar a capacidade de tomada de decisão livre dos destinatários do serviço. As penalidades previstas no bloco europeu atingem até 6% do faturamento global das companhias infratoras, alterando de forma drástica o cálculo de custo-benefício que outrora justificava a adoção dessas táticas abusivas.

### 5.2 Soluções Técnicas e Engenharia de Software Defensiva

A resposta ao problema não deve emanar exclusivamente do aparato judicial; ela requer a mobilização ativa da comunidade de ciência da computação no desenvolvimento de contramedidas técnicas. Destacam-se iniciativas contemporâneas voltadas à **auditoria ética automatizada**. Assim como o ecossistema de software incorporou verificadores de acessibilidade (como as diretrizes WCAG) e linters de segurança da informação nos pipelines de Integração Contínua e Entrega Contínua (CI/CD), é plenamente viável criar regras de linting para inspecionar assimetrias cromáticas de contraste, caixas de diálogo pré-marcadas e padrões abusivos de formulários antes que o código atinja o ambiente de produção.

Na ponta do usuário, projetos de código aberto vêm desenvolvendo extensões de navegadores dotadas de modelos de Processamento de Linguagem Natural (NLP) e visão computacional treinados para reconhecer e neutralizar *dark patterns* em tempo real — suprimindo contadores falsos de urgência, desmarcando caixas predatórias e restaurando a simetria visual de botões de cancelamento.

---

## 6. Conclusão e Provocações para o Futuro da Computação

A proliferação de *dark patterns* nas interfaces digitais modernas desmascara o mito da neutralidade axiológica da tecnologia. Cada componente de interface, cada linha de código JavaScript que manipula o DOM e cada teste A/B reflete decisões morais com impacto material profundo sobre o bem-estar psicológico, a higidez financeira e a liberdade política dos cidadãos conectados. Como futuros cientistas da computação e engenheiros de software, é inadmissível abrigarmo-nos sob a complacência de que "estamos apenas executando especificações de produto".

Superar esse cenário exige uma transformação cultural profunda nas organizações de tecnologia: substituir métricas míopes de conversão instantânea por indicadores de sustentabilidade relacional a longo prazo (como o arrependimento pós-compra, retenção orgânica e a confiança mútua), aliando rigor regulatório a uma formação ética intransigente nos cursos de graduação em computação. Se o software é a infraestrutura invisível que organiza a sociedade contemporânea, a defesa da dignidade humana deve ser tratada como o primeiro e mais inegociável requisito não funcional de qualquer sistema.

---

## 7. Declaração sobre o Uso de Ferramentas de Inteligência Artificial

Em estrito cumprimento às diretrizes pedagógicas da disciplina de Ética na Computação e em consonância com as orientações do docente responsável, declara-se que ferramentas de Inteligência Artificial Generativa foram empregadas **exclusivamente como instrumento de apoio formal à revisão gramatical, aprimoramento estilístico de coesão textual e auxílio na tipografia e compilação do relatório em formato PDF**.

A concepção temática, o levantamento dos dados científicos empíricos do artigo base de Mathur et al. (CSCW 2019), a estruturação do debate filosófico kantiano, a análise das teorias cognitivas de Kahneman e Thaler, o exame dos marcos jurídicos (CDC, LGPD, DSA, FTC) e a redação dos argumentos críticos constitutivos deste trabalho foram concebidos e formulados integralmente pelos alunos membros do grupo, que assumem a plena e intransferível responsabilidade intelectual, moral e acadêmica pelo conteúdo apresentado.

---

## 8. Referências Bibliográficas

1. **ACM.** *ACM Code of Ethics and Professional Conduct*. Association for Computing Machinery, 2018. Disponível em: <https://www.acm.org/code-of-ethics>. Acesso em: 10 out. 2026.
2. **BRASIL.** *Lei nº 8.078, de 11 de setembro de 1990*. Código de Defesa do Consumidor. Dispõe sobre a proteção do consumidor e dá outras providências. Brasília, DF: Presidência da República, 1990.
3. **BRASIL.** *Lei nº 13.709, de 14 de agosto de 2018*. Lei Geral de Proteção de Dados Pessoais (LGPD). Brasília, DF: Presidência da República, 2018.
4. **BRIGNULL, Harry.** *Dark Patterns: deceptions designed online*. A List Apart, v. 318, 2010. Disponível em: <https://alistapart.com/article/dark-patterns-deceptions-designed-online/>. Acesso em: 08 out. 2026.
5. **FEDERAL TRADE COMMISSION (FTC).** *FTC Takes Action Against Amazon for Enrolling Consumers in Prime Without Consent and Sabotaging Their Attempts to Cancel*. Washington: FTC Press Release, jun. 2023.
6. **KAHNEMAN, Daniel.** *Rápido e Devagar: duas formas de pensar*. Tradução de Cássio de Arantes Leite. Rio de Janeiro: Objetiva, 2012.
7. **KANT, Immanuel.** *Fundamentação da Metafísica dos Costumes*. Tradução de Paulo Quintela. Lisboa: Edições 70, 2007 [1785].
8. **MATHUR, Arunesh; ACAR, Gunes; FRIEDMAN, Michael J.; LUCHERINI, Elena; MAYER, Jonathan; CHETTY, Marshini; NARAYANAN, Arvind.** *Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites*. In: Proceedings of the ACM on Human-Computer Interaction, Vol. 3, No. CSCW, Article 81, Nov. 2019. DOI: 10.1145/3359183.
9. **THALER, Richard H.; SUNSTEIN, Cass R.** *Nudge: o empurrão para a escolha certa*. Tradução de Marcello Lino. Rio de Janeiro: Record, 2019 [2008].
10. **UNIÃO EUROPEIA.** *Regulamento (UE) 2022/2065 do Parlamento Europeu e do Conselho* (Digital Services Act - DSA), de 19 de outubro de 2022. Jornal Oficial da União Europeia, L 277/1, 2022.
