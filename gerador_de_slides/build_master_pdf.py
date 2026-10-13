import os
import sys
import subprocess
import pymupdf

# HTML Template with Google Slides Design matching Space Grotesk + Inter
HTML_CONTENT = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Novos Slides - Ética na Computação</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
  @page {
    size: 960pt 540pt;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    background-color: #f3f4f6;
    font-family: 'Inter', sans-serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .slide {
    width: 960pt;
    height: 540pt;
    page-break-after: always;
    position: relative;
    padding: 32pt 48pt 28pt 48pt;
    background: #ffffff;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  .kicker {
    font-family: 'Inter', sans-serif;
    font-size: 13pt;
    font-weight: 700;
    color: #ef4444;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 6pt;
  }
  .slide-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 30pt;
    font-weight: 700;
    color: #111827;
    line-height: 1.15;
    margin-bottom: 6pt;
  }
  .slide-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 16.5pt;
    font-weight: 400;
    color: #4b5563;
    line-height: 1.35;
    margin-bottom: 18pt;
  }
  .cards-row {
    display: flex;
    gap: 16pt;
    flex: 1;
  }
  .card {
    background: #ffffff;
    border: 1.5pt solid #e5e7eb;
    border-radius: 10pt;
    padding: 18pt 20pt;
    flex: 1;
    display: flex;
    flex-direction: column;
    box-shadow: 0 1pt 3pt rgba(0,0,0,0.03);
  }
  .card-highlight {
    background: #fef2f2;
    border-color: #fca5a5;
  }
  .card-dark {
    background: #111827;
    border-color: #1f2937;
    color: #ffffff;
  }
  .card-dark .card-title {
    color: #f9fafb;
  }
  .card-dark .card-text {
    color: #cbd5e1;
  }
  .card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 19pt;
    font-weight: 700;
    color: #111827;
    margin-bottom: 8pt;
    line-height: 1.25;
  }
  .card-tag {
    display: inline-block;
    font-size: 10.5pt;
    font-weight: 700;
    text-transform: uppercase;
    color: #ef4444;
    background: #fee2e2;
    padding: 2.5pt 8pt;
    border-radius: 4pt;
    margin-bottom: 8pt;
    width: fit-content;
  }
  .card-text {
    font-family: 'Inter', sans-serif;
    font-size: 14pt;
    color: #4b5563;
    line-height: 1.5;
    flex: 1;
  }
  .card-text p {
    margin-bottom: 8pt;
  }
  .card-text p:last-child {
    margin-bottom: 0;
  }
  .vote-box {
    margin-top: 10pt;
    background: #eff6ff;
    border-left: 3.5pt solid #3b82f6;
    padding: 8pt 12pt;
    border-radius: 0 6pt 6pt 0;
    font-weight: 600;
    color: #1d4ed8;
    font-size: 12.5pt;
  }
  .stat-badge {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 26pt;
    font-weight: 700;
    color: #ef4444;
    margin-bottom: 4pt;
  }
  .quote-box {
    margin-top: 8pt;
    padding: 10pt 14pt;
    background: #f8fafc;
    border-left: 3.5pt solid #ef4444;
    font-style: italic;
    color: #334155;
    font-size: 13pt;
  }
</style>
</head>
<body>

  <!-- SLIDE NOVO 1: MOMENTO INTERATIVO 01 -->
  <div class="slide">
    <div class="kicker">MOMENTO INTERATIVO 01</div>
    <div class="slide-title">Você Realmente Escolheu Livremente?</div>
    <div class="slide-subtitle">Momento de reflexão e aquecimento com a turma antes de entrarmos nos dados do estudo</div>
    <div class="cards-row">
      <div class="card card-highlight">
        <div class="card-tag">Pergunta 1</div>
        <div class="card-title">O Contador Falso</div>
        <div class="card-text">
          <p><strong>Levante a mão quem já comprou algo online porque um contador dizia que a oferta acabava em 5 minutos?</strong></p>
          <p>Você tomou uma decisão 100% racional ou sentiu uma ponta de ansiedade e urgência artificial?</p>
        </div>
        <div class="vote-box">👉 Interação: Levantem a mão na sala</div>
      </div>
      <div class="card">
        <div class="card-tag">Pergunta 2</div>
        <div class="card-title">O Labirinto do Cancelamento</div>
        <div class="card-text">
          <p><strong>Quem aqui já tentou cancelar um streaming ou plano e quase desistiu no caminho?</strong></p>
          <p>Por que assinar exigiu 1 clique imediato, mas cancelar exigiu 5 telas confusas e ligação no 0800?</p>
        </div>
        <div class="vote-box">👉 Interação: Quem já passou por isso?</div>
      </div>
      <div class="card">
        <div class="card-tag">Pergunta 3</div>
        <div class="card-title">A Chantagem Emocional</div>
        <div class="card-text">
          <p><strong>Quem já viu um pop-up de desconto dizendo:</strong></p>
          <div class="quote-box">"[Sim, quero 50% de desconto!]"<br>"[Não, prefiro pagar o preço total]"</div>
          <p style="margin-top:8px;">Essa interface está te informando ou te manipulando emocionalmente?</p>
        </div>
        <div class="vote-box">👉 Interação: Confirmshaming</div>
      </div>
    </div>
  </div>

  <!-- SLIDE NOVO 2: INSPEÇÃO DE CÓDIGO -->
  <div class="slide">
    <div class="kicker">INSPEÇÃO DE CÓDIGO</div>
    <div class="slide-title">A Engenharia Reversa da Fraude</div>
    <div class="slide-subtitle">Como os pesquisadores desmascararam a manipulação diretamente no código JavaScript</div>
    <div class="cards-row">
      <div class="card">
        <div class="stat-badge">157</div>
        <div class="card-title">Cronômetros Reciclados</div>
        <div class="card-text">
          <p><strong>Monitoramento Contínuo:</strong> O crawler revisitou lojas a cada 4 horas por 5 dias consecutivos e gravou vídeos do comportamento.</p>
          <p><strong>A Farsa:</strong> Em 140 lojas, o timer chegava a 00:00 e reiniciava magicamente no reload, ou a oferta continuava válida indefinidamente.</p>
        </div>
      </div>
      <div class="card card-highlight">
        <div class="stat-badge">Math.random()</div>
        <div class="card-title">Prova Social Forjada</div>
        <div class="card-text">
          <p><strong>Pop-ups de Compra:</strong> Notificações simulando: <em>"Lucas de SP acabou de comprar este produto"</em>.</p>
          <p><strong>Descoberta no Código:</strong> Funções randômicas no cliente combinavam nomes e cidades fictícias a partir de listas estáticas no JavaScript.</p>
        </div>
      </div>
      <div class="card">
        <div class="stat-badge">17 Sites</div>
        <div class="card-title">Estoque Sintético Programado</div>
        <div class="card-text">
          <p><strong>Escassez Inventada:</strong> Mensagens de <em>"Apenas 2 em estoque!"</em>.</p>
          <p><strong>Mecanismo:</strong> 16 sites decrementavam o número de itens por temporizador de relógio e 1 site gerava o estoque de forma totalmente aleatória.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- SLIDE NOVO 3: MOMENTO INTERATIVO 02 -->
  <div class="slide">
    <div class="kicker">MOMENTO INTERATIVO 02</div>
    <div class="slide-title">Mini-Quiz: Persuasão Legítima ou Golpe?</div>
    <div class="slide-subtitle">Votação rápida com a turma para testar a fronteira entre marketing honesto e padrão enganoso</div>
    <div class="cards-row">
      <div class="card card-highlight">
        <div class="card-tag">CASO A</div>
        <div class="card-title">O Quarto de Hotel</div>
        <div class="card-text">
          <p>Um site de viagens exibe em vermelho vibrante:<br><strong>"Apenas 1 quarto disponível para suas datas!"</strong></p>
          <p>Ao ligar direto para a pousada, você descobre que há 8 quartos vazios. O site alega: <em>"Só tínhamos 1 quarto no nosso lote contratual"</em>.</p>
          <div class="quote-box">O usuário é induzido a crer que o hotel inteiro vai lotar.</div>
        </div>
        <div class="vote-box">👉 VOTAÇÃO: É Marketing ou Dark Pattern?</div>
      </div>
      <div class="card">
        <div class="card-tag">CASO B</div>
        <div class="card-title">O Frete Grátis Progressivo</div>
        <div class="card-text">
          <p>Você adiciona um item de R$ 70 ao carrinho. O site exibe uma barra colorida:<br><strong>"Faltam R$ 30 para você ganhar Frete Grátis!"</strong></p>
          <p>Você decide adicionar um produto extra de R$ 35 para economizar R$ 15 no valor do frete.</p>
          <div class="quote-box">As regras do benefício são 100% transparentes e cumpridas.</div>
        </div>
        <div class="vote-box">👉 VOTAÇÃO: É Manipulação ou Persuasão Legítima?</div>
      </div>
    </div>
  </div>

  <!-- SLIDE NOVO 4: DARK PATTERNS AS A SERVICE -->
  <div class="slide">
    <div class="kicker">MERCADO DE SOFTWARE</div>
    <div class="slide-title">Dark Patterns as a Service (DPaaS)</div>
    <div class="slide-subtitle">A industrialização da manipulação em um ecossistema B2B de plugins de terceiros</div>
    <div class="cards-row">
      <div class="card">
        <div class="card-tag">Ecossistema B2B</div>
        <div class="card-title">22 Empresas Mapeadas</div>
        <div class="card-text">
          <p>• O artigo identificou <strong>22 empresas terceirizadas</strong> que fornecem a infraestrutura pronta de manipulação para lojas virtuais.</p>
          <p>• Plugins turnkey para <strong>Shopify, WooCommerce, Magento e WordPress</strong>.</p>
          <p>• O lojista não precisa entender de psicologia nem programar: basta pagar US$ 20/mês para instalar scripts que forjam escassez e urgência.</p>
        </div>
      </div>
      <div class="card card-highlight">
        <div class="card-tag">Fraude Comercial</div>
        <div class="card-title">"Fake it till you make it"</div>
        <div class="card-text">
          <p>• O plugin <strong>Boost</strong> tinha uma página comercial oficial intitulada abertamente: <em>"Fake it till you make it"</em> (Finja até conseguir), anunciando criação de pedidos falsos.</p>
          <p>• <strong>Reação do Mercado:</strong> O plugin mais popular (<em>Beeketing</em>, presente em 406 lojas) foi temporariamente banido da Shopify App Store por violação grave de transparência.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- SLIDE NOVO 5: FILOSOFIA - LIVRE-ARBÍTRIO -->
  <div class="slide">
    <div class="kicker">DEBATE FILOSÓFICO 01</div>
    <div class="slide-title">O Mito do Livre-Arbítrio Digital</div>
    <div class="slide-subtitle">A autonomia humana resiste a uma arquitetura desenhada deliberadamente para coagir?</div>
    <div class="cards-row">
      <div class="card">
        <div class="card-tag">Filosofia da Mente</div>
        <div class="card-title">A Ilusão da Escolha Autônoma</div>
        <div class="card-text">
          <p>• O usuário acredita que tomou uma decisão livre ao clicar no botão final de checkout.</p>
          <p>• No entanto, essa decisão ocorreu sob <strong>condições viciadas</strong>: tempo artificial, estoque forjado, opções deliberadamente assimétricas e indução de pânico (FOMO).</p>
          <p>• Para haver livre-arbítrio real, é indispensável: <strong>informação verdadeira, tempo para reflexão e alternativas simétricas</strong> sem custo psicológico.</p>
        </div>
      </div>
      <div class="card card-dark">
        <div class="card-tag" style="background:#374151; color:#f87171;">Ética Deontológica</div>
        <div class="card-title">O Imperativo de Kant</div>
        <div class="card-text">
          <p>• <strong>Immanuel Kant</strong> formulou o princípio moral fundamental da dignidade humana:</p>
          <div class="quote-box" style="background:#1f2937; color:#f8fafc; border-color:#f87171;">
            "Aja de tal modo que use a humanidade sempre como um fim em si mesma, e nunca meramente como um meio."
          </div>
          <p style="margin-top:10px;">• O Dark Pattern comete a violação máxima de Kant: <strong>reduz o ser humano a um mero instrumento</strong> para bater métricas de faturamento e taxas de conversão.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- SLIDE NOVO 6: FILOSOFIA - PATERNALISMO -->
  <div class="slide">
    <div class="kicker">DEBATE FILOSÓFICO 02</div>
    <div class="slide-title">Paternalismo Libertário vs. Paternalismo Predatório</div>
    <div class="slide-subtitle">De Richard Thaler e o conceito de "Nudge" ao "Sludge" corporativo</div>
    <div class="cards-row">
      <div class="card">
        <div class="card-tag" style="color:#059669; background:#d1fae5;">O Bem Coletivo</div>
        <div class="card-title">Paternalismo Libertário (Nudge)</div>
        <div class="card-text">
          <p>• <strong>Richard Thaler & Cass Sunstein</strong> (Prêmio Nobel 2017): Toda interface possui uma arquitetura de escolha padrão. Não existe design neutro.</p>
          <p>• <strong>A Proposta:</strong> Usar o padrão para incentivar o que é melhor para o próprio cidadão (ex: doação de órgãos por padrão, poupança automática, senhas fortes).</p>
          <p>• <strong>Liberdade Preservada:</strong> Recusar a opção padrão custa zero esforço ao usuário.</p>
        </div>
      </div>
      <div class="card card-highlight">
        <div class="card-tag">A Corrupção do Conceito</div>
        <div class="card-title">Paternalismo Predatório (Sludge)</div>
        <div class="card-text">
          <p>• A corporação sequestra o poder da arquitetura de escolha para o benefício exclusivo da empresa.</p>
          <p>• A interface decide o que é lucrativo para a plataforma e <strong>pune com fricção o usuário</strong> que tenta discordar (ex: labirintos de cancelamento).</p>
          <p>• <strong>Dilema:</strong> O Estado deve ser paternalista e proibir certos designs em lei para nos proteger, ou o usuário deve arcar com suas escolhas?</p>
        </div>
      </div>
    </div>
  </div>

  <!-- SLIDE NOVO 7: A RESPONSABILIDADE DO DEV -->
  <div class="slide">
    <div class="kicker">RESPONSABILIDADE PROFISSIONAL</div>
    <div class="slide-title">A Responsabilidade do Desenvolvedor Frontend</div>
    <div class="slide-subtitle">A cultura de CRO a qualquer custo e a defesa moral: "Apenas cumpri ordens do Jira"</div>
    <div class="cards-row">
      <div class="card">
        <div class="card-tag">Pressão Corporativa</div>
        <div class="card-title">A Ditadura das Métricas (CRO & OKRs)</div>
        <div class="card-text">
          <p>• O sucesso de times de produto é frequentemente medido apenas por taxa de conversão (CRO), cliques e receita de curto prazo.</p>
          <p>• Testes A/B são utilizados para otimizar o engano: <em>"A variante que oculta o botão de cancelar aumentou o faturamento em 14%"</em>.</p>
          <p>• Quase nenhuma empresa mede arrependimento do usuário ou erosão da confiança da marca.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-tag">Deontologia Profissional</div>
        <div class="card-title">Código de Ética da ACM</div>
        <div class="card-text">
          <p>• <strong>Artigo 1.2:</strong> <em>"Evitar causar dano"</em> (Avoid harm).</p>
          <p>• <strong>Artigo 1.4:</strong> <em>"Ser justo e tomar ações para não discriminar nem enganar"</em>.</p>
          <p>• Dizer que "o chefe mandou" não isenta o engenheiro de responsabilidade moral.</p>
          <p>• Desenvolvedores não são digitadores de código; somos arquitetos do comportamento social digital.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- SLIDE NOVO 8: MOMENTO INTERATIVO 03 -->
  <div class="slide">
    <div class="kicker">MOMENTO INTERATIVO 03</div>
    <div class="slide-title">Dilema na Sprint: O Que Você Faria?</div>
    <div class="slide-subtitle">Simulação de uma reunião real de desenvolvimento para debate com os colegas</div>
    <div class="cards-row">
      <div class="card card-highlight">
        <div class="card-tag">O Cenário Real</div>
        <div class="card-title">A Task de Black Friday</div>
        <div class="card-text">
          <p>Você é um dev frontend recém-contratado. Falta 1 semana para a Black Friday.</p>
          <p>O Gerente de Produto (PM) abre uma task urgente no Jira:</p>
          <div class="quote-box">
            "Precisamos colocar um contador regressivo no checkout. Se o cliente der F5, o contador deve reiniciar em 15m. Nossos testes A/B mostram que isso aumenta a conversão em 18% e garante o bônus de final de ano da equipe."
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-tag">Sua Posição</div>
        <div class="card-title">Qual Sua Resposta na Reunião?</div>
        <div class="card-text">
          <p><strong>Opção A:</strong> Programa o script calado. Preciso do emprego e a responsabilidade jurídica é da empresa.</p>
          <p><strong>Opção B:</strong> Recusa frontalmente, dizendo que é contra seus princípios éticos e viola o Código de Defesa do Consumidor.</p>
          <p><strong>Opção C:</strong> Propõe uma alternativa ética: estoques transparentes e reais, alertando sobre risco de processo no Procon e danos graves à reputação da marca.</p>
        </div>
        <div class="vote-box">👉 PERGUNTA PARA A SALA: Quem escolheria A, B ou C?</div>
      </div>
    </div>
  </div>

  <!-- SLIDE NOVO 9: MARCO LEGAL -->
  <div class="slide">
    <div class="kicker">MARCO LEGAL</div>
    <div class="slide-title">O Cenário Jurídico: Da Teoria à Multa</div>
    <div class="slide-subtitle">Como as legislações mundiais estão punindo os padrões manipulativos com multas bilionárias</div>
    <div class="cards-row">
      <div class="card">
        <div class="card-tag">Brasil</div>
        <div class="card-title">Código de Defesa do Consumidor & LGPD</div>
        <div class="card-text">
          <p>• <strong>CDC Art. 37:</strong> Proíbe publicidade enganosa ou abusiva sob pena de sanções civis e criminais.</p>
          <p>• <strong>CDC Art. 39:</strong> Veda venda casada (<em>Sneak into basket</em>) e cobrança de custos não informados.</p>
          <p>• <strong>LGPD Art. 8º:</strong> O consentimento para coleta de dados precisa ser <em>livre, informado e inequívoco</em>. Botões assimétricos tornam o consentimento juridicamente nulo.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-tag">Internacional</div>
        <div class="card-title">FTC (EUA) e Digital Services Act (UE)</div>
        <div class="card-text">
          <p>• <strong>FTC (EUA):</strong> Ação histórica de US$ 2,5 bilhões contra a Amazon pelo cancelamento do Prime; multa de US$ 520 milhões contra a Epic Games (Fortnite) por compras in-app não autorizadas de menores.</p>
          <p>• <strong>Digital Services Act (União Europeia 2023):</strong> Artigo 25 proíbe expressamente plataformas digitais de utilizar Dark Patterns sob multa de até <strong>6% do faturamento global</strong>.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- SLIDE NOVO 10: SOLUÇÕES TÉCNICAS -->
  <div class="slide">
    <div class="kicker">SOLUÇÕES TÉCNICAS</div>
    <div class="slide-title">Contra-medidas Técnicas: A Defesa Digital</div>
    <div class="slide-subtitle">Como a própria tecnologia pode ser utilizada como escudo contra o design predatório</div>
    <div class="cards-row">
      <div class="card">
        <div class="card-tag">Lado do Usuário</div>
        <div class="card-title">Ferramentas de Proteção Ativa</div>
        <div class="card-text">
          <p>• <strong>AdBlockers para Dark Patterns:</strong> Extensões mantidas por comunidades que neutralizam pop-ups de escassez e cronômetros artificiais.</p>
          <p>• <strong>Auditoria de Contraste Automática:</strong> Scanners que detectam botões deliberadamente camuflados ou fora do padrão WCAG.</p>
          <p>• <strong>IA como Escudo Cognitivo:</strong> Agentes de IA locais no navegador que avisam: <em>"Atenção: este preço possui custos ocultos no checkout"</em>.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-tag">Plataformas & Indústria</div>
        <div class="card-title">O Papel dos Navegadores & Lojas</div>
        <div class="card-text">
          <p>• <strong>Padrões Nativos no Browser:</strong> Assim como os navegadores baniram pop-ups invasivos nos anos 2000, podem exigir simetria de botões de consentimento.</p>
          <p>• <strong>Moderação Severa em App Stores:</strong> Banimento definitivo de desenvolvedores que comercializam scripts fraudulentos.</p>
          <p>• <strong>Design System Ético:</strong> Testes automatizados de conformidade ética incorporados nos pipelines de CI/CD antes do deploy.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- SLIDE NOVO 11: DEBATE FINAL -->
  <div class="slide">
    <div class="kicker">CONCLUSÃO & DEBATE</div>
    <div class="slide-title">Debate Aberto & Perguntas Finais</div>
    <div class="slide-subtitle">Três provocações centrais para encerrar o seminário com o professor e os colegas</div>
    <div class="cards-row">
      <div class="card">
        <div class="card-tag">Questão 1</div>
        <div class="card-title">Responsabilidade do Usuário?</div>
        <div class="card-text">
          <p>O usuário tem a obrigação moral de ser mais atento ou o sistema tem a obrigação ética de não ser predatório?</p>
          <p style="margin-top:8px;">Até que ponto culpar o consumidor por 'cair no golpe' não é culpabilizar a vítima da manipulação cognitiva?</p>
        </div>
      </div>
      <div class="card card-highlight">
        <div class="card-tag">Questão 2</div>
        <div class="card-title">IA & O Futuro da Coerção</div>
        <div class="card-text">
          <p>Uma Inteligência Artificial treinada exclusivamente para maximizar receita inevitavelmente inventará novos Dark Patterns se não for restringida?</p>
          <p style="margin-top:8px;">Como auditar algoritmos de personalização de interface operando em tempo real?</p>
        </div>
      </div>
      <div class="card">
        <div class="card-tag">Questão 3</div>
        <div class="card-title">O Nosso Papel Profissional</div>
        <div class="card-text">
          <p>Qual é a linha vermelha que você, como futuro cientista da computação ou desenvolvedor, jamais aceitaria cruzar em uma interface?</p>
          <p style="margin-top:8px;">Estamos construindo ferramentas que libertam as pessoas ou prisões cognitivas digitais?</p>
        </div>
      </div>
    </div>
  </div>

</body>
</html>
"""

def generate():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))

    html_path = os.path.join(base_dir, "novos_slides.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print("Saved novos_slides.html")

    pdf_new_path = os.path.join(base_dir, "novos_slides.pdf")
    edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_new_path}",
        f"file:///{html_path.replace(os.sep, '/')}"
    ]
    print("Rendering new slides to PDF via Edge...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Edge return code:", res.returncode)
    
    if not os.path.exists(pdf_new_path):
        print("Error: novos_slides.pdf not generated")
        return

    # Now merge original slides and new slides into a cohesive master presentation
    orig_path = os.path.join(base_dir, "google_slides_original.pdf")
    orig_doc = pymupdf.open(orig_path)
    new_doc = pymupdf.open(pdf_new_path)
    
    print(f"Original pages: {len(orig_doc)}, New pages: {len(new_doc)}")
    
    # Master ordering:
    # 0: Orig P1 (Cover)
    # 1: New P1 (Interativo 01 - Você escolheu livremente?)
    # 2: Orig P2 (O Que São Dark Patterns)
    # 3: Orig P3 (Design persuasivo vs padrão enganoso)
    # 4: Orig P4 (O Estudo Base - 11K)
    # 5: Orig P5 (Escala e Terceirização)
    # 6: New P2 (Engenharia Reversa - Código JS)
    # 7: Orig P6 (Subvertem a decisão 1)
    # 8: Orig P7 (Subvertem a decisão 2)
    # 9: Orig P8 (Cat 01 - Urgência)
    # 10: Orig P9 (Cat 02 - Escassez)
    # 11: Orig P10 (Gráfico original)
    # 12: Orig P11 (Cat 03 - Sneak into Basket)
    # 13: Orig P12 (Cat 03 - Custos Ocultos)
    # 14: Orig P13 (Gráfico original - Ingressos)
    # 15: New P3 (Interativo 02 - Mini-Quiz)
    # 16: Orig P14 (Cat 04 - Confirmshaming)
    # 17: Orig P15 (Cat 04 - Prova Social)
    # 18: Orig P16 (Gráfico original - Labirinto)
    # 19: Orig P17 (Cat 05 - Obstrução Roach Motel)
    # 20: New P4 (DPaaS - Mercado de Plugins)
    # 21: Orig P18 (Psicologia do Design)
    # 22: New P5 (Filosofia - Livre-Arbítrio e Kant)
    # 23: New P6 (Filosofia - Paternalismo Nudge vs Sludge)
    # 24: New P7 (Responsabilidade do Dev - ACM)
    # 25: New P8 (Interativo 03 - Dilema na Sprint)
    # 26: Orig P19 (A Responsabilidade - LGPD / Dev)
    # 27: New P9 (Marco Legal - Multas e Leis)
    # 28: New P10 (Soluções Técnicas - Navegadores)
    # 29: Orig P20 (Perguntas?)
    # 30: New P11 (Debate Final - 3 Questões)
    # 31: Orig P21 (Image Sources)

    master_doc = pymupdf.open()
    
    # 1. Cover
    master_doc.insert_pdf(orig_doc, from_page=0, to_page=0)
    # 2. Interativo 01
    master_doc.insert_pdf(new_doc, from_page=0, to_page=0)
    # 3. Orig P2-P5
    master_doc.insert_pdf(orig_doc, from_page=1, to_page=4)
    # 4. New P2 (Código JS)
    master_doc.insert_pdf(new_doc, from_page=1, to_page=1)
    # 5. Orig P6-P13 (Taxonomia e categorias 1-3 com gráficos originais)
    master_doc.insert_pdf(orig_doc, from_page=5, to_page=12)
    # 6. New P3 (Mini-Quiz)
    master_doc.insert_pdf(new_doc, from_page=2, to_page=2)
    # 7. Orig P14-P17 (Cat 4-5)
    master_doc.insert_pdf(orig_doc, from_page=13, to_page=16)
    # 8. New P4 (DPaaS)
    master_doc.insert_pdf(new_doc, from_page=3, to_page=3)
    # 9. Orig P18 (Psicologia)
    master_doc.insert_pdf(orig_doc, from_page=17, to_page=17)
    # 10. New P5-P8 (Livre-Arbítrio, Paternalismo, Dev ACM, Simulação de Sprint)
    master_doc.insert_pdf(new_doc, from_page=4, to_page=7)
    # 11. Orig P19 (Responsabilidade)
    master_doc.insert_pdf(orig_doc, from_page=18, to_page=18)
    # 12. New P9-P10 (Marco Legal, Soluções Técnicas)
    master_doc.insert_pdf(new_doc, from_page=8, to_page=9)
    # 13. Orig P20 (Perguntas?)
    master_doc.insert_pdf(orig_doc, from_page=19, to_page=19)
    # 14. New P11 (Debate Final)
    master_doc.insert_pdf(new_doc, from_page=10, to_page=10)
    # 15. Orig P21 (Image Sources)
    master_doc.insert_pdf(orig_doc, from_page=20, to_page=20)
    
    out_final = os.path.join(project_root, "apresentacao", "Seminario_Etica_Dark_Patterns.pdf")
    master_doc.save(out_final)
    print(f"Master presentation generated with {len(master_doc)} slides at {out_final}")

if __name__ == "__main__":
    generate()
