# Manipulação Comportamental e Padrões Enganosos em Escala (Dark Patterns at Scale)

**Universidade Federal • Departamento de Ciência da Computação**  
**Disciplina:** Ética na Computação • Seminário Temático  
**Artigo Base:** *Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites* (Mathur et al., ACM CSCW 2019)  
**Grupo / Integrantes:**  
* Henrique Gomes dos Santos Medeiros — Matrícula: 2021084986  
* Isadora Cunha Pimentel — Matrícula: 2021039506  
* Italo Leal Lana Santos — Matrícula: 2024013893  
* Vitor Hugo Dias Santos — Matrícula: 2024014202  
**PDF Gerado:** [`Relatorio_Etica_Dark_Patterns.pdf`](./Relatorio_Etica_Dark_Patterns.pdf)

---

## Resumo

Este relatório analisa o fenômeno dos padrões enganosos de interface (*dark patterns*) no comércio eletrônico sob as perspectivas técnica, empírica e da ética profissional na computação. Com base no estudo científico de Mathur et al. (ACM CSCW 2019), conduzido sobre 11.227 lojas virtuais, examinam-se a taxonomia dessas práticas coercitivas, a terceirização por meio de *Dark Patterns as a Service* (DPaaS) e a manipulação cognitiva exercida sobre os usuários. Discutem-se ainda as implicações éticas à luz da autonomia moral, os enquadramentos legais no ordenamento jurídico brasileiro (CDC e LGPD) e as sanções da FTC, ressaltando o dever e a responsabilidade do desenvolvedor de software na concepção de interfaces transparentes.

**Palavras-chave:** Dark patterns. Ética na computação. Autonomia do usuário. Interfaces coercitivas. Engenharia de software.

---

## 1. Introdução e Definição de Dark Patterns

Este relatório apresenta a síntese temática e a discussão ética do seminário sobre padrões enganosos de interface (comumente denominados *dark patterns*). O trabalho tem como fundamentação científica central o artigo *"Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites"*, de autoria de Arunesh Mathur e colaboradores (publicado na conferência ACM CSCW em 2019), bem como as discussões práticas e éticas conduzidas ao longo dos slides da apresentação.

Conforme apresentado no seminário, os *dark patterns* são definidos como interfaces de usuário desenhadas deliberadamente para induzir decisões que favorecem os interesses da plataforma em detrimento do próprio usuário. Essa prática não decorre de desatenção ou falha de usabilidade técnica, mas sim de uma arquitetura intencional de coerção digital que resulta em compras não planejadas, adesão a serviços recorrentes indesejados, captura abusiva de dados pessoais e, fundamentalmente, na violação da tomada de decisão racional e autônoma do indivíduo.

Um aspecto essencial debatido na introdução diz respeito à fronteira entre o *design persuasivo* legítimo e o *padrão enganoso*. O comércio tradicional sempre utilizou técnicas de persuasão, tais como destacar produtos em promoção, oferecer benefícios claros de frete grátis ou disponibilizar políticas facilitadas de troca e devolução. Essas estratégias buscam convencer o consumidor respeitando a clareza das opções e a sua liberdade de escolha. Em contrapartida, o padrão enganoso subverte o próprio processo decisório por meio de assimetria visual, ocultação de custos e dados essenciais, falsificação de escassez e obstáculos desenhados para impedir a desistência do usuário.

---

## 2. O Estudo Base: Metodologia e Escala (Mathur et al., 2019)

O artigo de Mathur et al. teve como objetivo principal quantificar empiricamente e em larga escala a presença dessas práticas no comércio eletrônico mundial, superando os relatos meramente pontuais ou anedóticos que existiam até então na literatura de Interação Humano-Computador (IHC).

Para conduzir a pesquisa, os autores desenvolveram um rastreador automatizado baseado em navegadores com OpenWPM e Selenium. Esse robô de software realizou uma varredura sobre **11.227 lojas virtuais** de abrangência global, selecionadas a partir do ranking de acessos da Alexa. No total, foram extraídas e analisadas aproximadamente **53.000 páginas de produtos**, permitindo examinar o código client-side (HTML, CSS e JavaScript), respostas assíncronas de rede e elementos interativos de navegação.

Os resultados quantitativos revelaram a identificação de **1.818 instâncias de padrões enganosos** distribuídas em 1.254 plataformas, o que representa cerca de 11,1% de todas as lojas virtuais auditadas. Além do percentual global, o dado de maior relevância prática apontado pelo estudo é que **grandes plataformas de comércio eletrônico (sites de alto tráfego) utilizam padrões manipulativos com frequência até três vezes maior** do que lojas de menor porte. A manipulação de interface não é, portanto, uma anomalia restrita a páginas periféricas, mas uma estratégia sistematicamente adotada pelos líderes de mercado.

Outro ponto crucial destacado no artigo e no seminário refere-se à terceirização dessas práticas, denominada no estudo como fraude de prateleira ou *Dark Patterns as a Service* (DPaaS). Os pesquisadores identificaram **22 empresas de software** que desenvolvem e comercializam extensões e plugins voltados exclusivamente a injetar padrões coercitivos em plataformas populares como Shopify, Magento e WooCommerce. Dessa forma, pequenos e médios comerciantes compram funcionalidades prontas para forjar dados em suas páginas sem precisar programar uma única linha de código.

---

## 3. Como os Padrões Enganosos Subvertem a Decisão

O estudo de Mathur et al. estruturou uma taxonomia analítica demonstrando como os padrões de interface operam para subverter a escolha do usuário. Conforme detalhado nos slides do seminário, essa subversão ocorre através de cinco dimensões operacionais principais:

1. **Assimétrico:** Impõe pesos, destaques ou dificuldades visuais desiguais entre as escolhas da interface. O exemplo clássico reside em destacar o botão de aceite com cores vivas e proporções avantajadas, enquanto o botão ou link de recusa é desenhado de forma opaca, minúscula ou camuflada no fundo da página.
2. **Manipulação Oculta:** Direciona a decisão do usuário sem que ele perceba que a interface foi intencionalmente calibrada para influenciá-lo. Ocorre, por exemplo, mediante a introdução de uma opção "isca" (*decoy effect*), em que uma alternativa visivelmente desvantajosa é apresentada para induzir a escolha de uma opção mais cara desejada pela empresa.
3. **Enganoso:** Induz o indivíduo a crenças factualmente falsas por meio de declarações mentirosas ou omissões diretas, como a exibição de cronômetros com falsas contagens regressivas ou mensagens alegando estoques críticos que não condizem com a realidade do banco de dados.
4. **Omissão de Informação:** Obscurece ou atrasa intencionalmente a apresentação de dados financeiros cruciais, como taxas de serviço, taxas de conveniência ou fretes obrigatórios, revelando-os unicamente na etapa derradeira do fluxo de compra.
5. **Restritivo:** Limita artificialmente o conjunto de opções disponíveis ao usuário a fim de forçá-lo a tomar uma ação específica de interesse do sistema, como proibir o prosseguimento da compra a menos que seja criado um cadastro vinculando contas de redes sociais.

---

## 4. Categorias de Dark Patterns Identificadas no Artigo e nos Slides

A partir do rastreamento automatizado, os pesquisadores catalogaram as armadilhas observadas em categorias bem definidas, discutidas minuciosamente no seminário:

| Categoria | Mecanismo Observado na Interface | Manifestação Concreta |
| :--- | :--- | :--- |
| **Urgência** | Imposição de prazo artificial para acelerar a decisão do usuário antes de uma reflexão calma. | Cronômetros falsos de contagem regressiva e mensagens vagas de tempo limitado. |
| **Escassez** | Indicação de alta demanda ou estoque baixo para aumentar o valor percebido do produto. | Alertas de "apenas 2 itens restantes" e avisos estáticos de procura extraordinária. |
| **Inclusão Sorrateira** | Adição não solicitada de produtos/serviços ao carrinho ou ocultação de cobranças obrigatórias. | Garantias embutidas por padrão e taxas de conveniência no final do checkout. |
| **Desvio de Atenção** | Uso de recursos visuais ou apelo emocional para afastar o usuário de escolhas desfavoráveis ao site. | *Confirmshaming* (vergonha na recusa) e botões assimétricos em avisos de cookies. |
| **Prova Social** | Exibição de depoimentos ou atividades de terceiros para induzir comportamento por efeito manada. | Pop-ups de "Maria comprou agora" gerados por script e avaliações clonadas. |
| **Obstrução** | Criação de barreiras e atritos severos para dificultar ações legítimas (padrão *Roach Motel*). | Assinatura em 1 clique vs. fluxo com múltiplos cliques e telas para cancelamento. |

*Tabela 1: Categorias de Dark Patterns identificadas no artigo de Mathur et al. (2019) e abordadas no seminário.*

No caso da **Urgência**, os pesquisadores demonstraram que grande parte dos cronômetros é fictícia: ao término da contagem, o relógio simplesmente é reiniciado ou a suposta oferta permanece ativa sem qualquer alteração de preço. Na **Escassez**, mensagens de disponibilidade limitada geram ansiedade e pressionam a compra por impulso.

Na **Inclusão Sorrateira** (*Sneaking*), destacam-se duas práticas graves. A primeira é a adição de itens adicionais ao carrinho (como garantias estendidas ou seguros de viagem) pré-marcados por padrão, explorando a desatenção e a inércia do consumidor. A segunda prática são os **Custos Ocultos**, amplamente observados na venda de ingressos para shows e eventos esportivos, em que "taxas de conveniência" significativas são ocultadas durante todo o preenchimento de dados e aparecem apenas no clique final de confirmação de pagamento.

No **Desvio de Atenção** (*Misdirection*), o *Confirmshaming* explora a humilhação emocional para impedir a recusa do usuário, associando o botão de cancelamento a frases constrangedoras (como *"Não, eu prefiro pagar o preço cheio"* ou *"Não, eu não gosto de economizar"*). Paralelamente, a **Prova Social Falsa** induz o efeito manada mediante notificações simuladas de compradores contemporâneos.

Por fim, a categoria de **Obstrução Absoluta** caracteriza o padrão conhecido como *Roach Motel*: plataformas desenham fluxos extremamente simples e desimpedidos para contratação e cadastro, mas impõem barreiras extenuantes, rotas labirínticas e telas propositalmente confusas quando o usuário tenta cancelar ou excluir sua conta.

---

## 5. Engenharia Reversa do Engano e Mecanismos Psicológicos

Um dos aspectos técnicos mais contundentes do artigo de Mathur et al. foi a realização de engenharia reversa no código das páginas para averiguar a autenticidade das informações. Os pesquisadores realizaram requisições periódicas a cada 4 horas durante 5 dias consecutivos nas páginas que continham contadores e notificações.

Ao inspecionarem o código JavaScript executado no navegador, os autores constataram que diversos sites utilizavam funções de geração numérica pseudoaleatória, como a chamada nativa `Math.random()`, associada a listas pré-programadas de nomes e cidades:

```javascript
// Lógica de geração sintética identificada na auditoria de scripts client-side
function gerarProvaSocialFicticia() {
  const nomes = ["Ana P.", "Carlos M.", "Juliana R.", "Lucas S."];
  const cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"];
  const nomeAleatorio = nomes[Math.floor(Math.random() * nomes.length)];
  const cidadeAleatoria = cidades[Math.floor(Math.random() * cidades.length)];
  const minutos = Math.floor(Math.random() * 15) + 1;
  
  exibirNotificacao(`${nomeAleatorio} de ${cidadeAleatoria} comprou este item há ${minutos} min.`);
}
```

Essa constatação técnica comprova que os dados de compras e visualizações em tempo real não mantinham nenhuma relação com transações reais ocorridas no banco de dados do servidor; tratava-se de simulação puramente cosmética no frontend com a finalidade de manipular a percepção do usuário.

Como discutido no slide sobre a *Psicologia do Design*, essas técnicas têm eficácia porque exploram atalhos mentais e vieses cognitivos consolidados na literatura científica:

* **Efeito Manada:** Tendência psicológica humana de validar decisões individuais observando e imitando o comportamento do grupo, o que torna notificações de compra recente extremamente persuasivas;
* **Viés da Escassez:** Atribuição de valor superior e urgência desmedida a produtos que aparentam estar em vias de esgotamento ou submetidos a limites rígidos de tempo;
* **Falácia do Custo Irrecuperável (Sunk Cost):** Relutância em abandonar um processo de compra quando o consumidor já investiu tempo e esforço substanciais preenchendo cadastros longos, facilitando a aceitação passiva de taxas ocultas cobradas na última tela.

---

## 6. Casos Reais, Aspectos Éticos e a Responsabilidade do Desenvolvedor

A discussão sobre dark patterns atinge implicações práticas evidentes nos tribunais e na rotina das equipes de desenvolvimento de software. Um dos casos mais emblemáticos apresentados no seminário foi a investigação e ação judicial movida pela Federal Trade Commission (FTC) contra a Amazon em 2023.

A denúncia da FTC evidenciou que a Amazon estruturou intencionalmente um fluxo de cancelamento de assinatura Prime com o codinome interno *"Iliad Flow"* (em alusão à Ilíada de Homero, uma jornada repleta de armadilhas e labirintos). Enquanto a adesão à assinatura Prime podia ser concluída com apenas um clique, o procedimento de cancelamento exigia atravessar quatro telas distintas e efetuar pelo menos seis cliques, repletos de textos ambíguos, botões com duplo sentido e tentativas sucessivas de dissuasão. O processo resultou em autuações pesadas e na obrigação de simplificar os fluxos da plataforma.

No âmbito jurídico brasileiro, tais práticas encontram vedação expressa no Código de Defesa do Consumidor (CDC, Lei nº 8.078/1990). O Artigo 37 proíbe publicidade enganosa ou abusiva, englobando cronômetros e estoques fraudulentos, enquanto o Artigo 39 proíbe a exigência de vantagens excessivas e a venda casada, vedando a inclusão sorrateira de produtos adicionais sem consentimento prévio. De forma análoga, a Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018) estipula que o consentimento do titular deve ser livre, informado e inequívoco; avisos de cookies que camuflam a recusa ou manipulam a atenção tornam o consentimento viciado e nulo perante a legislação.

No encerramento do seminário, debateu-se a **responsabilidade ética do desenvolvedor de computação**. Conforme previsto no Código de Ética da ACM (Association for Computing Machinery), os profissionais de tecnologia possuem a obrigação primordial de evitar danos e ser justos, não podendo justificar a codificação de algoritmos e interfaces desonestas sob a simples escusa de que estavam apenas "cumprindo ordens do time de produto". Diante da pressão de métricas de conversão a curto prazo em sprints de engenharia, cabe ao desenvolvedor alertar sobre riscos legais e reputacionais, promovendo uma arquitetura de software fundamentada no respeito à autonomia do usuário.

---

## 7. Declaração sobre o Uso de Ferramentas de Inteligência Artificial

Em cumprimento estrito às instruções da disciplina de Ética na Computação e ao critério estabelecido pelo docente para o seminário, declara-se que ferramentas de Inteligência Artificial Generativa foram utilizadas **estritamente como apoio à revisão gramatical, auxílio na organização de estilo e formatação final do documento**.

Toda a seleção dos tópicos abordados, a estrutura de apresentação, os dados empíricos extraídos do artigo científico base (Mathur et al., 2019) e as análises éticas e conceituais refletem com fidelidade o conteúdo dos slides e a pesquisa realizada pelos integrantes do grupo, que assumem total responsabilidade acadêmica pelo material apresentado.

---

## Referências Bibliográficas

1. **ACM.** *ACM Code of Ethics and Professional Conduct*. Association for Computing Machinery, 2018. Disponível em: <https://www.acm.org/code-of-ethics>. Acesso em: 10 out. 2026.
2. **BRASIL.** *Lei nº 8.078, de 11 de setembro de 1990*. Código de Defesa do Consumidor. Dispõe sobre a proteção do consumidor e dá outras providências. Brasília, DF: Presidência da República, 1990.
3. **BRASIL.** *Lei nº 13.709, de 14 de agosto de 2018*. Lei Geral de Proteção de Dados Pessoais (LGPD). Brasília, DF: Presidência da República, 2018.
4. **BRIGNULL, Harry.** *Dark Patterns: deceptions designed online*. A List Apart, v. 318, 2010. Disponível em: <https://alistapart.com/article/dark-patterns-deceptions-designed-online/>. Acesso em: 08 out. 2026.
5. **FEDERAL TRADE COMMISSION (FTC).** *FTC Takes Action Against Amazon for Enrolling Consumers in Prime Without Consent and Sabotaging Their Attempts to Cancel*. Washington: FTC Press Release, jun. 2023.
6. **MATHUR, Arunesh; ACAR, Gunes; FRIEDMAN, Michael J.; LUCHERINI, Elena; MAYER, Jonathan; CHETTY, Marshini; NARAYANAN, Arvind.** *Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites*. In: Proceedings of the ACM on Human-Computer Interaction, Vol. 3, No. CSCW, Article 81, Nov. 2019. DOI: 10.1145/3359183.
