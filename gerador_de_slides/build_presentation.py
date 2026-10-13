import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = pptx.Presentation()
    # 16:9 Widescreen standard
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette - Modern Dark Slate & Neon Highlights
    C_BG = RGBColor(15, 23, 42)          # Deep Slate #0F172A
    C_CARD_BG = RGBColor(30, 41, 59)     # Slate 800 #1E293B
    C_CARD_BORDER = RGBColor(51, 65, 85) # Slate 700 #334155
    C_TEXT_LIGHT = RGBColor(248, 250, 252) # White/Ice #F8FAFC
    C_TEXT_MUTED = RGBColor(148, 163, 184) # Slate 400 #94A3B8
    C_CYAN = RGBColor(56, 189, 248)       # Sky 400 #38BDF8
    C_AMBER = RGBColor(251, 191, 36)      # Amber 400 #FBBF24
    C_ROSE = RGBColor(244, 63, 94)        # Rose 500 #F43F5E
    C_EMERALD = RGBColor(52, 211, 153)    # Emerald 400 #34D399
    C_PURPLE = RGBColor(192, 132, 252)    # Purple 400 #C084FC

    def set_background(slide):
        bg_shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5)
        )
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = C_BG
        bg_shape.line.fill.background()
        return bg_shape

    def add_badge(slide, text, color, left, top, width=Inches(2.5), height=Inches(0.4)):
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        badge.fill.solid()
        badge.fill.fore_color.rgb = color
        badge.line.fill.background()
        tf = badge.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = "Arial"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_BG
        p.alignment = PP_ALIGN.CENTER
        return badge

    def add_header(slide, title, subtitle=None, badge_text=None, badge_color=C_CYAN):
        set_background(slide)
        top_offset = Inches(0.6)
        
        if badge_text:
            add_badge(slide, badge_text, badge_color, Inches(0.8), top_offset, width=Inches(2.4), height=Inches(0.35))
            top_offset += Inches(0.45)
            
        tb = slide.shapes.add_textbox(Inches(0.8), top_offset, Inches(11.733), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Segoe UI"
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_LIGHT
        
        if subtitle:
            p2 = tf.add_paragraph()
            p2.text = subtitle
            p2.font.name = "Segoe UI"
            p2.font.size = Pt(15)
            p2.font.color.rgb = C_TEXT_MUTED
            p2.space_before = Pt(6)

    def add_card(slide, left, top, width, height, title=None, items=None, border_color=C_CARD_BORDER, title_color=C_CYAN):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        
        tf = card.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.TOP
        tf.margin_left = Inches(0.3)
        tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)
        tf.margin_bottom = Inches(0.3)
        
        first = True
        if title:
            p = tf.paragraphs[0]
            p.text = title
            p.font.name = "Segoe UI"
            p.font.size = Pt(18)
            p.font.bold = True
            p.font.color.rgb = title_color
            first = False
            
        if items:
            for item in items:
                p = tf.add_paragraph() if not first else tf.paragraphs[0]
                first = False
                p.text = item
                p.font.name = "Segoe UI"
                p.font.size = Pt(13)
                p.font.color.rgb = C_TEXT_LIGHT
                p.space_before = Pt(8)
                p.level = 0
        return card

    def add_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # =========================================================================
    # SLIDE 1: CAPA
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_background(s1)
    
    add_badge(s1, "ÉTICA NA COMPUTAÇÃO", C_CYAN, Inches(0.8), Inches(1.5), width=Inches(2.6), height=Inches(0.4))
    
    tb = s1.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(11.5), Inches(3.0))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = "Manipulação Comportamental e Arquitetura de Interfaces"
    p.font.name = "Segoe UI"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_LIGHT
    
    p2 = tf.add_paragraph()
    p2.text = "Dark Patterns em Escala: Do Código à Coerção Digital"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(22)
    p2.font.color.rgb = C_CYAN
    p2.space_before = Pt(12)
    
    p3 = tf.add_paragraph()
    p3.text = "Análise empírica do artigo de Mathur et al. (ACM CSCW, 2019) e o debate sobre paternalismo, livre-arbítrio e o dever do desenvolvedor."
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(14)
    p3.font.color.rgb = C_TEXT_MUTED
    p3.space_before = Pt(16)
    
    add_card(s1, Inches(0.8), Inches(5.6), Inches(11.733), Inches(1.1),
             title=None,
             items=[
                 "Seminário de Ética na Computação • Duração: 40 minutos • Apresentação em 4 Blocos Interativos"
             ],
             border_color=C_CYAN, title_color=C_CYAN)
    
    add_notes(s1, "ABERTURA (Integrante 1):\n"
                  "- Bom dia a todos e professor!\n"
                  "- Nosso seminário hoje vai além de uma simples lista de designs feios na internet. Vamos investigar como a própria arquitetura de software é desenhada para violar a autonomia humana.\n"
                  "- Vamos analisar o estudo histórico de Princeton (Mathur et al., 2019) com 11 mil lojas virtuais, o mercado bilionário de plugins manipulativos e os dilemas éticos que nós, futuros desenvolvedores, enfrentaremos.")

    # =========================================================================
    # SLIDE 2: [INTERATIVO 01] AQUECIMENTO
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Você Realmente Escolheu Livremente?", 
               "Momento de reflexão rápida com a turma antes de entrarmos nos dados", 
               "MOMENTO INTERATIVO 01", C_ROSE)
    
    add_card(s2, Inches(0.8), Inches(2.3), Inches(3.6), Inches(4.5),
             title="Pergunta 1: O Contador",
             items=[
                 "Levante a mão quem já comprou algo online porque um contador dizia que a oferta acabava em 5 minutos?",
                 "Você sentiu que a decisão foi 100% racional ou sentiu uma ponta de ansiedade?",
                 "O que você sentiria se soubesse que aquele contador era falso?"
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s2, Inches(4.8), Inches(2.3), Inches(3.6), Inches(4.5),
             title="Pergunta 2: O Labirinto",
             items=[
                 "Quem aqui já tentou cancelar uma assinatura de streaming ou academia e desistiu no meio do caminho?",
                 "Por que para assinar bastou 1 clique, mas para cancelar foram necessárias 5 telas e ligar no 0800?",
                 "Isso é descuido de design ou estratégia intencional?"
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s2, Inches(8.8), Inches(2.3), Inches(3.7), Inches(4.5),
             title="Pergunta 3: O Constrangimento",
             items=[
                 "Quem já viu um pop-up dizendo:",
                 "\"[SIM! Quero 50% de desconto]\"\n\"[NÃO, prefiro pagar o preço total]\"?",
                 "Essa interface está te informando ou está te manipulando emocionalmente?"
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s2, "INTERATIVO (Integrante 1):\n"
                  "- Interaja com a sala! Peça para levantarem a mão nas 3 perguntas.\n"
                  "- Destaque: 'Todos nós já caímos nisso. Isso não é falta de inteligência do usuário: é psicologia cognitiva e engenharia de software trabalhando juntas contra a nossa atenção'.\n"
                  "- Conecte diretamente com a definição do próximo slide.")

    # =========================================================================
    # SLIDE 3: O QUE SÃO DARK PATTERNS?
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "O Que São Dark Patterns?", "Interfaces desenhadas contra o melhor interesse de quem as utiliza", "CONCEITUAÇÃO", C_CYAN)
    
    add_card(s3, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="Origem & Definição",
             items=[
                 "• Conceito cunhado em 2010 por Harry Brignull (Especialista em UX).",
                 "• Definição Técnica: Escolhas de interface que beneficiam a plataforma ao coagir, direcionar ou enganar os usuários a tomar decisões involuntárias.",
                 "• Não é erro de usabilidade: Um bug é acidental; um dark pattern é intencional, otimizado e planejado.",
                 "• Foco no Lucro da Plataforma: Converte cliques em receita imediata sacrificando o bem-estar do usuário."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_card(s3, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="Os 4 Danos Diretos ao Usuário",
             items=[
                 "1. Prejuízo Financeiro: Compras não planejadas, assinaturas recorrentes indesejadas e taxas ocultas.",
                 "2. Captura Abusiva de Dados: Coleta forçada de consentimento e rastreamento invisível sob interfaces confusas.",
                 "3. Sequestro do Tempo: Dificuldade deliberada para realizar ações simples como exclusão de conta e cancelamento.",
                 "4. Violação da Autonomia: Quebra da tomada de decisão racional, gerando arrependimento pós-compra."
             ], border_color=C_EMERALD, title_color=C_EMERALD)
             
    add_notes(s3, "FALA (Integrante 1):\n"
                  "- Reforce a diferença: UI ruim é quando o desenvolvedor não soube posicionar o botão. Dark pattern é quando o botão foi deliberadamente escondido porque a empresa lucra com a sua confusão.")

    # =========================================================================
    # SLIDE 4: DESIGN PERSUASIVO VS. PADRÃO ENGANOSO
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "A Fronteira: Design Persuasivo vs. Padrão Enganoso", "Onde termina o marketing legítimo e onde começa a manipulação predatória?", "DISTINÇÃO ÉTICA", C_AMBER)
    
    add_card(s4, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="Design Persuasivo (Legítimo)",
             items=[
                 "• Objetivo: Ajudar o usuário a tomar uma decisão informada com base em informações reais.",
                 "• Exemplo: Oferecer política transparente de devolução e troca em 30 dias.",
                 "• Exemplo: Mostrar fotos em alta resolução de múltiplos ângulos do produto.",
                 "• Exemplo: Oferecer desconto promocional real e transparente.",
                 "• Características: Respeita o livre-arbítrio, fornece dados verdadeiros e mantém a simetria de escolha."
             ], border_color=C_EMERALD, title_color=C_EMERALD)
             
    add_card(s4, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="Padrão Enganoso / Dark Pattern",
             items=[
                 "• Objetivo: Subverter a tomada de decisão do usuário em benefício exclusivo do lojista.",
                 "• Exemplo: Cronômetro que diz 'oferta acaba em 10m', mas reseta no F5.",
                 "• Exemplo: 'Apenas 1 item restante' gerado por número randômico.",
                 "• Exemplo: Inserir garantia estendida no carrinho por padrão sem consentimento.",
                 "• Características: Baseado em falsidade, assimetria, ocultação e sequestro de atenção."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s4, "FALA (Integrante 1):\n"
                  "- O artigo de Mathur et al. deixa isso explícito: nem todo recurso de compra por impulso é um dark pattern. O teste divisor de águas é: a interface está subvertendo a decisão com informações falsas ou designs assimétricos?")

    # =========================================================================
    # SLIDE 5: O ESTUDO BASE (MATHUR ET AL., 2019)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "O Estudo Base: Mathur et al. (ACM CSCW, 2019)", "A primeira medição empírica automatizada em escala global na história da web", "METODOLOGIA CIENTÍFICA", C_CYAN)
    
    add_card(s5, Inches(0.8), Inches(2.3), Inches(3.6), Inches(4.5),
             title="11.227",
             items=[
                 "Lojas Virtuais Rastreadas",
                 "• Cobertura dos maiores e-commerces mundiais do ranking Alexa.",
                 "• Web crawler customizado baseado em Selenium e OpenWPM.",
                 "• Navegação autônoma em larga escala simulando comportamento real."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_card(s5, Inches(4.8), Inches(2.3), Inches(3.6), Inches(4.5),
             title="53.000",
             items=[
                 "Páginas de Produtos & Fluxos",
                 "• O robô navegou por páginas de produtos, adicionou ao carrinho e seguiu ao checkout.",
                 "• Extração de 13 milhões de segmentos textuais da interface.",
                 "• Captura sistemática de screenshots e logs de rede (arquivos HAR)."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_card(s5, Inches(8.8), Inches(2.3), Inches(3.7), Inches(4.5),
             title="1.818",
             items=[
                 "Dark Patterns Identificados",
                 "• Agrupamento de texto por NLP (TF-IDF + Clustering Hierárquico).",
                 "• Validação manual com concordância estatística rigorosa (Kappa de Cohen = 0,74).",
                 "• Classificação em 7 categorias e 15 tipos de manipulação."
             ], border_color=C_AMBER, title_color=C_AMBER)
             
    add_notes(s5, "FALA (Integrante 1):\n"
                  "- Apresente os números com orgulho metodológico: não foi um trabalho de faculdade olhando 10 sites; foram 11 mil lojas varridas por robôs com verificação científica de alto rigor no principal simpósio da ACM.")

    # =========================================================================
    # SLIDE 6: ESCALA E TERCEIRIZAÇÃO
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Os Resultados: Escala e o Mito dos Sites Pequenos", "Descobertas surpreendentes sobre a infecção do e-commerce mundial", "DADOS EMPÍRICOS", C_CYAN)
    
    add_card(s6, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="11,1% das Lojas Operam Dark Patterns",
             items=[
                 "• 1.254 lojas online continham ao menos um dark pattern explícito.",
                 "• Estimativa Conservadora: O robô só olhou páginas de produtos e checkouts em inglês. O número real é certamente muito maior.",
                 "• Concentração em Sites Populares: Ao contrário do que se imaginava, os sites mais famosos e acessados tinham até 3x mais probabilidade de usar dark patterns do que sites pequenos.",
                 "• Conclusão: Dark patterns não são desespero de lojas decadentes; são estratégia de gigantes para extrair receita máxima."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_card(s6, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="A Terceirização da Fraude (Plugins)",
             items=[
                 "• Lojas não criam essas técnicas do zero.",
                 "• 22 empresas terceirizadas foram identificadas vendendo scripts prontos de manipulação.",
                 "• Ecossistema de plugins para Shopify, WooCommerce, Magento e WordPress.",
                 "• Um único plugin malicioso pode infectar dezenas de milhares de lojas com uma linha de código.",
                 "• A desonestidade virou um modelo de negócios B2B escalável."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s6, "FALA (Integrante 1):\n"
                  "- Destaque o ponto chave: 'Sites grandes enganam com mais frequência'. Por que? Porque para um site que fatura bilhões, um ganho de 0,5% na conversão gerado por engano representa milhões de dólares.")

    # =========================================================================
    # SLIDE 7: A AUDITORIA TÉCNICA (JAVASCRIPT)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "A Engenharia Reversa da Fraude", "Como os pesquisadores provaram cientificamente a mentira dentro do código", "INSPEÇÃO DE CÓDIGO", C_EMERALD)
    
    add_card(s7, Inches(0.8), Inches(2.3), Inches(3.6), Inches(4.5),
             title="Cronômetros Reciclados",
             items=[
                 "157 Casos em 140 Sites",
                 "• O crawler revisitou lojas a cada 4h por 5 dias consecutivos e gravou vídeos.",
                 "• Constatação: O cronômetro chegava a 00:00 e reiniciava magicamente.",
                 "• Em outros casos, o tempo zerava e o preço promocional continuava ativo indefinidamente."
             ], border_color=C_EMERALD, title_color=C_EMERALD)
             
    add_card(s7, Inches(4.8), Inches(2.3), Inches(3.6), Inches(4.5),
             title="Math.random() em Ação",
             items=[
                 "Prova Social Forjada",
                 "• Pop-ups: 'Ana de Belo Horizonte acabou de comprar este produto'.",
                 "• Os pesquisadores inspecionaram o código JavaScript no frontend.",
                 "• Descobriram funções randômicas gerando compradores e localidades a partir de listas estáticas."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s7, Inches(8.8), Inches(2.3), Inches(3.7), Inches(4.5),
             title="Estoque Falso Programado",
             items=[
                 "Escassez Simulada",
                 "• Mensagens: 'Restam apenas 3 unidades!'.",
                 "• 16 sites decrementavam o estoque em horários pré-programados por temporizador.",
                 "• 1 site gerava o estoque de forma totalmente randômica a cada carregamento de página."
             ], border_color=C_AMBER, title_color=C_AMBER)
             
    add_notes(s7, "FALA (Integrante 1 passando a palavra para Integrante 2):\n"
                  "- Esse slide é crucial para uma turma de computação: não é fofoca, é análise de código. O JavaScript estava forjando dados ao vivo no navegador do cliente.\n"
                  "- Agora passo a palavra para o colega explicar a taxonomia dessas táticas.")

    # =========================================================================
    # SLIDE 8: DIMENSÕES DA MANIPULAÇÃO (PARTE 1)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Como os Padrões Enganosos Subvertem a Decisão (1/2)", "As 5 dimensões propostas na taxonomia de Mathur et al.", "TAXONOMIA", C_CYAN)
    
    add_card(s8, Inches(0.8), Inches(2.3), Inches(3.6), Inches(4.5),
             title="1. Assimétrico",
             items=[
                 "Pesos e esforços desiguais entre escolhas da interface.",
                 "• O caminho que a empresa deseja é destacado e instantâneo (1 clique).",
                 "• A opção do usuário é minimizada, escondida em tons de cinza ou requer múltiplos passos.",
                 "• Exemplo: Banner de cookies com botão verde 'Aceitar Todos' e link invisível para 'Recusar'."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_card(s8, Inches(4.8), Inches(2.3), Inches(3.6), Inches(4.5),
             title="2. Manipulação Oculta",
             items=[
                 "O efeito da escolha do design é invisível para o usuário.",
                 "• Direciona a decisão sem que a pessoa perceba que a interface foi desenhada para induzi-la.",
                 "• Uso do Decoy Effect (Efeito Chamariz): Adiciona uma opção 'isca' apenas para tornar o plano caro mais atraente.",
                 "• A pessoa acredita que decidiu por conta própria."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_card(s8, Inches(8.8), Inches(2.3), Inches(3.7), Inches(4.5),
             title="3. Enganoso",
             items=[
                 "Induz a falsas crenças por declarações mentirosas ou omissão.",
                 "• Criação de prazos falsos ('promoção acaba hoje').",
                 "• Informação de estoque artificial.",
                 "• Se o usuário soubesse da verdade (que o preço é permanente), sua decisão de compra seria diferente."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s8, "FALA (Integrante 2):\n"
                  "- Explicar as 3 primeiras dimensões: Assimetria (desigualdade de esforço), Ocultação (indução invisível) e Engano (mentira aberta).")

    # =========================================================================
    # SLIDE 9: DIMENSÕES DA MANIPULAÇÃO (PARTE 2)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Como os Padrões Enganosos Subvertem a Decisão (2/2)", "As dimensões de omissão e restrição de liberdade", "TAXONOMIA", C_CYAN)
    
    add_card(s9, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="4. Omissão de Informação",
             items=[
                 "Obscurece ou atrasa a apresentação de dados essenciais para a decisão de compra.",
                 "• O usuário só descobre o custo real após despender tempo e esforço consideráveis.",
                 "• Taxas de serviço, frete surpresa e impostos adicionados na última tela do checkout.",
                 "• Explora a Falácia do Custo Irrecuperável (Sunk Cost Fallacy): o usuário já digitou endereço, cartão e CPF, então aceita pagar a taxa a mais para não 'perder o tempo investido'."
             ], border_color=C_AMBER, title_color=C_AMBER)
             
    add_card(s9, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="5. Restritivo",
             items=[
                 "Limita artificialmente o conjunto de opções disponíveis.",
                 "• Força o usuário a realizar uma ação desejada pelo sistema para poder concluir sua tarefa.",
                 "• Obrigatoriedade de criar conta ou fazer login com redes sociais para ver o preço final.",
                 "• Bloqueio da navegação com pop-ups que não possuem botão de fechar ('X') evidente.",
                 "• Elimina alternativas legítimas do usuário."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s9, "FALA (Integrante 2):\n"
                  "- Conecte a dimensão de Omissão com a experiência diária: quem nunca comprou ingresso para show ou cinema e no último segundo apareceu uma 'Taxa de Conveniência' de 25%?")

    # =========================================================================
    # SLIDE 10: CATEGORIA 01: URGÊNCIA
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Categoria 01: Urgência", "Aceleração artificial do tempo de decisão para bloquear o pensamento crítico", "CATEGORIAS EMPÍRICAS", C_CYAN)
    
    add_card(s10, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="Cronômetros Falsos (393 instâncias)",
             items=[
                 "• Contagem regressiva dinâmica indicando expiração iminente da oferta.",
                 "• Mecanismo Enganoso: Quando o tempo zera, o relógio reinicia automaticamente ou a promoção continua ativa.",
                 "• Impacto Psicológico: Ativa o estresse e o medo de perder (FOMO).",
                 "• Impede que o usuário pesquise preços em sites concorrentes ou pondere sobre a real necessidade da compra."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s10, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="Mensagens de Tempo Limitado (88 instâncias)",
             items=[
                 "• Alertas estáticos: 'Promoção por tempo limitado!', 'Válido apenas hoje!'.",
                 "• Omissão de Prazo: Não informam quando a promoção realmente acaba.",
                 "• Permanência Disfarçada: O banner permanece exibido pelos mesmos dias ou meses.",
                 "• Viés Explorado: Viés de Escassez Temporal (Tendência a supervalorizar o que está prestes a acabar)."
             ], border_color=C_AMBER, title_color=C_AMBER)
             
    add_notes(s10, "FALA (Integrante 2):\n"
                  "- Explique que o cérebro humano sob pressão de tempo desliga a reflexão lógica e opera por impulso.")

    # =========================================================================
    # SLIDE 11: CATEGORIA 02: ESCASSEZ
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Categoria 02: Escassez", "Sinalização de estoque fictício ou demanda inflada", "CATEGORIAS EMPÍRICAS", C_CYAN)
    
    add_card(s11, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="Alertas de Baixo Estoque (632 instâncias)",
             items=[
                 "• O tipo mais comum encontrado no estudo (presente em 581 lojas).",
                 "• Notificações de 'Apenas 2 em estoque!' exibidas para praticamente todos os produtos do site.",
                 "• Incerteza Induzida: A dúvida gera urgência e eleva o valor percebido do item.",
                 "• Estoque Sintético: 17 sites com manipulação comprovada via código (redução por temporizador ou aleatória)."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s11, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="Mensagens de Alta Demanda (47 instâncias)",
             items=[
                 "• Avisos: 'Alta procura!', 'Este item está sendo muito visualizado agora!'.",
                 "• Alertas genéricos no carrinho que aparecem independente do produto adicionado.",
                 "• Pressão Social Indireta: Induz a sensação de competição contra outros consumidores anônimos.",
                 "• Viés da Escassez (Cialdini): Se outros querem e vai acabar, eu preciso garantir o meu agora."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_notes(s11, "FALA (Integrante 2):\n"
                  "- O estudo achou 632 casos disso. É a técnica mais barata e mais eficaz para induzir compra impulsiva.")

    # =========================================================================
    # SLIDE 12: CATEGORIA 03: INCLUSÃO SORRATEIRA
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Categoria 03: Inclusão Sorrateira (Sneaking)", "Produtos e serviços empurrados sem consentimento explícito", "CATEGORIAS EMPÍRICAS", C_CYAN)
    
    add_card(s12, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="Sneak into Basket (Itens Extras)",
             items=[
                 "• Novos produtos ou serviços entram no carrinho do usuário sem o seu consentimento explícito.",
                 "• Exemplos clássicos: Seguros de viagem embutidos em passagens aéreas, garantia estendida ou acessórios.",
                 "• Exploração do Padrão (Default Effect): A empresa aposta na desatenção do consumidor que segue avançando no fluxo sem conferir cada linha.",
                 "• Fricção Reversa: O usuário tem o trabalho de desmarcar o que nunca pediu."
             ], border_color=C_AMBER, title_color=C_AMBER)
             
    add_card(s12, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="Hidden Subscription (Assinatura Oculta)",
             items=[
                 "• Cobrança de taxas recorrentes sob a promessa de 'compra única' ou 'teste grátis'.",
                 "• O usuário acredita que está pagando R$ 9,90 por um ebook ou teste de 7 dias.",
                 "• Nas letras miúdas, autoriza uma cobrança mensal automática de R$ 99,00.",
                 "• Violação Gravíssima de Consentimento: Falta de transparência contratual deliberada."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s12, "FALA (Integrante 2):\n"
                  "- 'Sneak into basket' é proibido explicitamente pelo Código de Defesa do Consumidor brasileiro (venda casada).")

    # =========================================================================
    # SLIDE 13: CUSTOS OCULTOS
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "Categoria 03: Custos Ocultos (Hidden Costs)", "Cobranças reveladas apenas no último segundo do checkout", "CATEGORIAS EMPÍRICAS", C_CYAN)
    
    add_card(s13, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="O Mecanismo da Emboscada",
             items=[
                 "• Taxas significativas ('taxa de conveniência', 'manuseio', 'taxa administrativa') que não foram informadas na busca do produto.",
                 "• Reveladas exclusivamente na tela final de pagamento.",
                 "• O usuário já investiu 10 minutos preenchendo formulários, criando login e cadastrando o cartão.",
                 "• A desistência gera frustração, então o usuário capitula e aceita o custo extra."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s13, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="O Caso dos Ingressos de Shows",
             items=[
                 "• Setor clássico de aplicação abusiva de custos ocultos.",
                 "• Um ingresso anunciado por R$ 200,00 salta para R$ 260,00 no clique final por uma 'taxa de conveniência' digital.",
                 "• O usuário enfrenta fila virtual com tempo de expiração de 5 minutos, impedindo qualquer contestação.",
                 "• Combinação de 3 Dark Patterns simultâneos: Urgência + Custos Ocultos + Monopólio da interface."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_notes(s13, "FALA (Integrante 2 passando a palavra para o Momento Interativo):\n"
                  "- Agora vamos pausar a explicação e fazer um teste rápido com a turma para ver se vocês conseguem identificar a linha tênue.")

    # =========================================================================
    # SLIDE 14: [INTERATIVO 02] MINI-QUIZ COM A TURMA
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Mini-Quiz: Persuasão Legítima ou Golpe?", "Votação rápida com a turma para testar a percepção ética", "MOMENTO INTERATIVO 02", C_ROSE)
    
    add_card(s14, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="CASO A: O Hotel na Praia",
             items=[
                 "Cenário:",
                 "Um site de reservas exibe em vermelho: \"Apenas 1 quarto disponível para suas datas!\".",
                 "Ao ligar diretamente para a pousada, você descobre que há 8 quartos vazios.",
                 "O site alega: \"Só tínhamos 1 quarto no nosso lote contratual com o hotel\".",
                 "",
                 "VOTAÇÃO DA TURMA:",
                 "👉 É marketing legítimo ou é Dark Pattern?"
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s14, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="CASO B: O Frete Grátis Progressivo",
             items=[
                 "Cenário:",
                 "Você coloca um item de R$ 70 no carrinho. O site exibe uma barra colorida:",
                 "\"Faltam R$ 30 para você ganhar Frete Grátis!\".",
                 "Você adiciona um item desnecessário de R$ 35 para economizar R$ 15 de frete.",
                 "",
                 "VOTAÇÃO DA TURMA:",
                 "👉 É manipulação enganosa ou é design persuasivo aceitável?"
             ], border_color=C_EMERALD, title_color=C_EMERALD)
             
    add_notes(s14, "INTERATIVO (Integrante 2 & Integrante 3):\n"
                  "- Peça para a turma levantar a mão no Caso A e no Caso B.\n"
                  "- Resposta para debate:\n"
                  "  * Caso A: É Dark Pattern (Enganoso por omissão de contexto: o usuário acredita que o hotel vai lotar, quando na verdade apenas o lote do site acabou).\n"
                  "  * Caso B: É Design Persuasivo legítimo (Não há mentira nem assimetria; o usuário recebe a regra de jogo clara e escolhe livremente se quer ou não gastar mais para ter o benefício).")

    # =========================================================================
    # SLIDE 15: CATEGORIA 04: DESVIO DE ATENÇÃO
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Categoria 04: Desvio de Atenção (Misdirection)", "Manipulação visual e chantagem emocional para guiar a escolha", "CATEGORIAS EMPÍRICAS", C_CYAN)
    
    add_card(s15, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="Confirmshaming (169 instâncias)",
             items=[
                 "• Uso de linguagem constrangedora para fazer o usuário se sentir culpado ao recusar uma oferta.",
                 "• Opção 1: 'Sim, quero salvar o planeta e economizar!'",
                 "• Opção 2: 'Não, eu odeio economizar e não me importo.'",
                 "• Explora o Viés de Enquadramento (Framing Effect): manipula a autoimagem do usuário para coagir o consentimento."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s15, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="Interferência Visual",
             items=[
                 "• Uso deliberado de cores, contrastes e tipografia para ocultar rotas de saída.",
                 "• Botão de 'Concordar': Verde vibrante, grande, elevado, no centro da visão.",
                 "• Botão de 'Recusar': Texto cinza claro em fundo branco, fonte de 9px, parecendo texto corrido sem link.",
                 "• Violação direta das diretrizes de Acessibilidade e Usabilidade (WCAG)."
             ], border_color=C_AMBER, title_color=C_AMBER)
             
    add_notes(s15, "FALA (Integrante 3):\n"
                  "- Confirmshaming é uma das táticas mais tóxicas. Ela trata o usuário com desprezo e constrangimento.")

    # =========================================================================
    # SLIDE 16: CATEGORIA 04: PROVA SOCIAL FORJADA
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "Categoria 04: Prova Social Forjada (Social Proof)", "Notificações automáticas que simulam multidões imaginárias", "CATEGORIAS EMPÍRICAS", C_CYAN)
    
    add_card(s16, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="Activity Messages (313 instâncias)",
             items=[
                 "• Notificações pop-up no canto da tela:",
                 "  'João de Curitiba acabou de comprar este tênis'.",
                 "  '42 pessoas estão visualizando este produto agora'.",
                 "• Efeito Manada (Bandwagon Effect): Tendência biológica humana de confiar e imitar a escolha do grupo.",
                 "• O estudo descobriu que dezenas dessas notificações eram geradas por código estático, sem qualquer comprador real."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s16, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="Depoimentos Clonados & Forjados",
             items=[
                 "• Testemunhos e avaliações 5 estrelas cuja procedência é fictícia ou clonada de sites concorrentes.",
                 "• Fotos de perfil extraídas de bancos de imagens gratuitos ou geradas por IA (StyleGAN).",
                 "• Destruição da Confiança Digital: O usuário toma decisões financeiras com base em validações sociais fabricadas."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_notes(s16, "FALA (Integrante 3):\n"
                  "- O princípio da prova social é poderoso: na dúvida, nós olhamos o que os outros estão fazendo. Quando esse sinal é hackeado, perdemos o senso de referência.")

    # =========================================================================
    # SLIDE 17: CATEGORIA 05: OBSTRUÇÃO ABSOLUTA
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_header(s17, "Categoria 05: Obstrução (O Padrão 'Roach Motel')", "Fácil de entrar, impossível de sair: A armadilha do cancelamento", "CATEGORIAS EMPÍRICAS", C_ROSE)
    
    add_card(s17, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="A Teoria do 'Roach Motel'",
             items=[
                 "• Nome inspirado nas armadilhas de barata: o inseto entra facilmente atraído pelo cheiro, mas não consegue escapar.",
                 "• Inscrição / Assinatura: 1 clique, sem senhas complicadas, botão destacado.",
                 "• Cancelamento: Labirinto deliberado. Requer navegação profunda em configurações obscuras, formulários complexos ou contato telefônico obrigatório em horário comercial."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s17, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="O Caso FTC vs. Amazon ('Iliad Flow')",
             items=[
                 "• Ação histórica da Federal Trade Commission (EUA) contra a Amazon em 2023.",
                 "• Documentos internos revelaram que a Amazon batizou o fluxo de cancelamento do Prime de 'Iliad' (em alusão à Ilíada de Homero, uma jornada épica e árdua).",
                 "• O usuário enfrentava 6 páginas, dezenas de cliques, ofertas confusas e botões invertidos para conseguir cancelar.",
                 "• Multa e processo bilionário por manipular milhões de consumidores."
             ], border_color=C_AMBER, title_color=C_AMBER)
             
    add_notes(s17, "FALA (Integrante 3):\n"
                  "- Citar o caso da Amazon é imperdível: os próprios designers e executivos sabiam o que estavam fazendo, tanto que chamavam o fluxo de 'Ilíada'.")

    # =========================================================================
    # SLIDE 18: DARK PATTERNS AS A SERVICE (DPAAS)
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    add_header(s18, "Dark Patterns as a Service (DPaaS)", "A industrialização da manipulação em um ecossistema B2B de plugins", "MERCADO DE SOFTWARE", C_CYAN)
    
    add_card(s18, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="O Mercado das 22 Empresas",
             items=[
                 "• O estudo mapeou 22 empresas especializadas em comercializar scripts de manipulação prontos.",
                 "• Integrações nativas com Shopify, WooCommerce, Magento e PrestaShop.",
                 "• O lojista não precisa de programadores: ele paga uma mensalidade de US$ 20 e ativa contadores falsos e escassez inventada.",
                 "• Popularização da manipulação: pequenos lojistas adotando as táticas predatórias das grandes corporações."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_card(s18, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="O Escândalo 'Fake it till you make it'",
             items=[
                 "• Desonestidade explícita como marketing: O plugin *Boost* tinha uma página anunciando a criação de pedidos falsos para atrair compradores.",
                 "• O plugin *WooCommerce Notification* prometia explicitamente criar pedidos simulados com nomes inventados.",
                 "• Reação da Plataforma: A Shopify baniu temporariamente o aplicativo mais popular do estudo (*Beeketing*, presente em 406 lojas) após a repercussão pública.",
                 "• Dilema das App Stores: Até que ponto lojas de aplicativos são cúmplices das ferramentas que hospedam?"
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s18, "FALA (Integrante 3):\n"
                  "- Mostre como a manipulação foi empacotada como produto de software (SaaS). Um modelo de negócios inteiro construído sobre a mentira.")

    # =========================================================================
    # SLIDE 19: A PSICOLOGIA POR TRÁS
    # =========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    add_header(s19, "A Psicologia do Design: Por Que Caímos Nisso?", "Como interfaces exploram os atalhos evolutivos do cérebro humano", "CIÊNCIAS COGNITIVAS", C_CYAN)
    
    add_card(s19, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="Sistema 1 vs. Sistema 2 (Kahneman)",
             items=[
                 "• Daniel Kahneman (Rápido e Devagar - Prêmio Nobel):",
                 "• Sistema 1 (Rápido): Automático, intuitivo, emocional, gasta pouca energia.",
                 "• Sistema 2 (Lento): Reflexivo, analítico, exige concentração e esforço mental.",
                 "• A Estratégia do Dark Pattern: Sobrecaregar o usuário com urgência e escassez para forçar o Sistema 1 a assumir o controle e bloquear o Sistema 2."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_card(s19, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="Os Principais Vieses Explorados",
             items=[
                 "1. Efeito Ancoragem: Fixar o preço original inflado para fazer o desconto parecer imperdível.",
                 "2. Efeito Padrão (Default Effect): Inércia humana de não alterar opções pré-marcadas.",
                 "3. Falácia do Custo Irrecuperável: Dificuldade de abandonar uma compra após preencher muitas etapas.",
                 "4. Aversão à Perda (Loss Aversion): A dor da perda é 2x mais intensa que o prazer do ganho."
             ], border_color=C_AMBER, title_color=C_AMBER)
             
    add_notes(s19, "FALA (Integrante 3 passando para Integrante 4):\n"
                  "- Nossos cérebros evoluíram na savana para economizar energia. As interfaces usam nossa própria biologia contra nós.\n"
                  "- Agora passo a palavra para o colega aprofundar nas questões filosóficas de Livre-Arbítrio e Paternalismo.")

    # =========================================================================
    # SLIDE 20: [FILOSOFIA 01] O MITO DO LIVRE-ARBÍTRIO
    # =========================================================================
    s20 = prs.slides.add_slide(blank_layout)
    add_header(s20, "O Mito do Livre-Arbítrio Digital", "A autonomia humana resiste a uma arquitetura desenhada para coagir?", "DEBATE FILOSÓFICO 01", C_PURPLE)
    
    add_card(s20, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="A Ilusão da Escolha Autônoma",
             items=[
                 "• O usuário acredita que tomou uma decisão livre ao clicar em 'Comprar'.",
                 "• Mas essa decisão ocorreu sob condições viciadas: tempo artificial, estoque forjado, opções desiguais e indução de medo.",
                 "• Filosofia da Ação: Uma escolha só é verdadeiramente autônoma se o indivíduo possui:",
                 "  1. Acesso à informação fidedigna;",
                 "  2. Tempo hábil para deliberar;",
                 "  3. Alternativas simétricas sem punição psicológica."
             ], border_color=C_PURPLE, title_color=C_PURPLE)
             
    add_card(s20, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="O Imperativo Categórico de Kant",
             items=[
                 "• Immanuel Kant (Fundamentação da Metafísica dos Costumes):",
                 "• Princípio Moral Fundamental: 'Aja de tal modo que use a humanidade sempre como um fim e nunca meramente como um meio'.",
                 "• A Violação pelo Dark Pattern: O usuário deixa de ser tratado como sujeito de dignidade e passa a ser tratado como mero instrumento de extração de valor financeiro e métricas de conversão.",
                 "• Manipulação algorítmica é, em essência, a desumanização do usuário."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s20, "FALA (Integrante 4):\n"
                  "- Esse slide eleva a apresentação para o nível filosófico que o professor de ética adora: Kant e o Livre-Arbítrio.\n"
                  "- Se alguém coloca um cronômetro falso e você compra por medo, você agiu por livre-arbítrio ou foi manipulado?")

    # =========================================================================
    # SLIDE 21: [FILOSOFIA 02] PATERNALISMO LIBERTÁRIO VS PREDATÓRIO
    # =========================================================================
    s21 = prs.slides.add_slide(blank_layout)
    add_header(s21, "Paternalismo Libertário vs. Paternalismo Predatório", "De Richard Thaler e o conceito de 'Nudge' ao 'Sludge' corporativo", "DEBATE FILOSÓFICO 02", C_PURPLE)
    
    add_card(s21, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="Paternalismo Libertário (Nudge)",
             items=[
                 "• Richard Thaler & Cass Sunstein (Livro Nudge - Prêmio Nobel 2017):",
                 "• Premissa: Toda interface possui uma arquitetura de escolha neutra. É impossível não escolher um design padrão.",
                 "• A Proposta Ética: Usar a arquitetura de escolha para 'empurrar' o cidadão para o que é melhor para ELE MESMO.",
                 "• Exemplos Positivos: Deixar doação de órgãos ativada por padrão, poupança automática para aposentadoria, sugerir senhas fortes.",
                 "• Liberdade Preservada: O usuário pode recusar a qualquer momento com esforço zero."
             ], border_color=C_EMERALD, title_color=C_EMERALD)
             
    add_card(s21, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="A Corrupção: Sludge & Dark Patterns",
             items=[
                 "• O que acontece quando o poder da arquitetura de escolha é capturado pelo lucro da empresa?",
                 "• Surge o Paternalismo Predatório / Sludge: A interface decide o que é melhor para a EMPRESA e empurra o usuário para o prejuízo.",
                 "• O 'Nudge' do Bem vira a 'Armadilha' do Mal.",
                 "• A Pergunta Ética Crucial: O Estado deve ser paternalista e proibir certos designs em lei para proteger o cidadão, ou isso fere a liberdade do mercado?"
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s21, "FALA (Integrante 4):\n"
                  "- Aqui está exatamente a resposta ao colega que sugeriu paternalismo e livre-arbítrio!\n"
                  "- Conecte Thaler (Nudge) com Dark Patterns. Mostre que a mesma técnica que salva vidas (doação de órgãos) é corrompida no e-commerce para arrancar dinheiro.")

    # =========================================================================
    # SLIDE 22: O DILEMA ÉTICO DO DESENVOLVEDOR
    # =========================================================================
    s22 = prs.slides.add_slide(blank_layout)
    add_header(s22, "A Responsabilidade Ética do Desenvolvedor e Designer", "A cultura de CRO e a defesa moral: 'Eu só cumpri a tarefa do Jira'", "RESPONSABILIDADE PROFISSIONAL", C_AMBER)
    
    add_card(s22, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="A Ditadura das Métricas (CRO & OKRs)",
             items=[
                 "• Em muitas empresas de tecnologia, o sucesso é medido exclusivamente por taxa de conversão (CRO), cliques e faturamento trimestral.",
                 "• Testes A/B são utilizados para otimizar enganos: 'A variante que oculta o botão de cancelar aumentou o faturamento em 12%'.",
                 "• Ausência de Métricas Éticas: Quase nenhuma empresa mede arrependimento do usuário, sensação de engodo ou erosão de confiança a longo prazo."
             ], border_color=C_AMBER, title_color=C_AMBER)
             
    add_card(s22, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="O Código de Ética Profissional (ACM & SBC)",
             items=[
                 "• Código de Ética da ACM (Association for Computing Machinery):",
                 "  - Artigo 1.2: 'Contribuir para a sociedade e evitar causar dano' (Avoid Harm).",
                 "  - Artigo 1.4: 'Ser justo e tomar ações para não discriminar nem enganar'.",
                 "• A Falácia de Nuremberg no Software: Dizer que 'o chefe mandou' não isenta o programador de responsabilidade.",
                 "• Desenvolvedores não são digitadores de código; somos os engenheiros do tecido social digital."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s22, "FALA (Integrante 4):\n"
                  "- Chame a atenção da sala: todos nós seremos desenvolvedores, designers ou gerentes de produto. O que faremos quando nos pedirem para programar uma mentira?")

    # =========================================================================
    # SLIDE 23: [INTERATIVO 03] SIMULAÇÃO DE SPRINT
    # =========================================================================
    s23 = prs.slides.add_slide(blank_layout)
    add_header(s23, "Dilema na Sprint: O Que Você Faria?", "Simulação de uma reunião real de desenvolvimento com a turma", "MOMENTO INTERATIVO 03", C_ROSE)
    
    add_card(s23, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="O Cenário da Vida Real",
             items=[
                 "Você é um Desenvolvedor Frontend recém-contratado.",
                 "Falta 1 semana para a Black Friday.",
                 "O Gerente de Produto (PM) abre uma task urgente no Jira:",
                 "",
                 "\"Precisamos implementar um contador regressivo na página de checkout. Se o cliente atualizar a página, o contador deve reiniciar em 15 minutos. Nossos testes A/B mostram que isso aumenta a conversão em 18% e garante o bônus de final de ano da equipe.\""
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_card(s23, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="O Que Você Responde na Reunião?",
             items=[
                 "Opção A: Programa o script calado. Afinal, você precisa do emprego e a responsabilidade legal é da empresa.",
                 "Opção B: Recusa frontalmente, dizendo que é contra seus princípios éticos e viola o Código de Defesa do Consumidor.",
                 "Opção C: Propõe uma alternativa técnica e ética: cronômetro real com estoques transparentes, alertando sobre os riscos de processo e danos à marca.",
                 "",
                 "👉 PERGUNTA PARA A SALA: Quem escolheria A, B ou C? E por quê?"
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_notes(s23, "INTERATIVO (Integrante 4):\n"
                  "- Abra para 2 colegas da sala responderem!\n"
                  "- É um debate rico: na prática, muitos têm medo de serem demitidos (Opção A). O papel do bom profissional é saber articular a Opção C: mostrar que dark pattern destrói a marca, gera processos milionários no Procon e que a longo prazo clientes enganados não voltam.")

    # =========================================================================
    # SLIDE 24: O CENÁRIO JURÍDICO & REGULATÓRIO
    # =========================================================================
    s24 = prs.slides.add_slide(blank_layout)
    add_header(s24, "O Cenário Jurídico: Da Teoria à Multa", "Como as leis mundiais estão criminalizando e punindo os padrões enganosos", "MARCO LEGAL", C_CYAN)
    
    add_card(s24, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="No Brasil: CDC e LGPD",
             items=[
                 "• Código de Defesa do Consumidor (CDC):",
                 "  - Art. 37: Proíbe expressamente publicidade enganosa ou abusiva.",
                 "  - Art. 39: Veda venda casada (Sneak into basket) e exigência de vantagens manifestamente excessivas.",
                 "• Lei Geral de Proteção de Dados (LGPD):",
                 "  - Art. 8º: O consentimento deve ser 'livre, informado e inequívoco'.",
                 "  - Banners de cookies com botões assimétricos tornam o consentimento juridicamente nulo."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_card(s24, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="No Mundo: FTC, GDPR e DSA",
             items=[
                 "• Estados Unidos (FTC): Acordos e multas históricas contra Amazon, Epic Games (Fortnite - US$ 520 milhões por compras não autorizadas de crianças).",
                 "• União Europeia (Digital Services Act - DSA 2023):",
                 "  - Artigo 25: Proíbe expressamente plataformas online de desenhar interfaces que 'enganem, manipulem ou prejudiquem materialmente a capacidade dos usuários de tomar decisões livres'.",
                 "  - Multas que chegam a 6% do faturamento global anual da empresa."
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s24, "FALA (Integrante 4):\n"
                  "- Mostrar que a era do faroeste na web está acabando. Hoje, implementar dark pattern é passivo trabalhista e risco de conformidade grave.")

    # =========================================================================
    # SLIDE 25: CONTRA-MEDIDAS TÉCNICAS & O FUTURO
    # =========================================================================
    s25 = prs.slides.add_slide(blank_layout)
    add_header(s25, "Contra-medidas Técnicas: A Tecnologia Reativa", "Como engenheiros e pesquisadores estão construindo defesas contra o design predador", "SOLUÇÕES TÉCNICAS", C_EMERALD)
    
    add_card(s25, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
             title="Ferramentas de Defesa do Usuário",
             items=[
                 "• AdBlockers de Dark Patterns: Extensões de código aberto mantidas por comunidades que neutralizam pop-ups de escassez e timers falsos.",
                 "• Extensões de Auditoria Visual: Identificam desvios de contraste e botões ocultos em tempo real.",
                 "• IA como Escudo Cognitivo: Agentes de IA locais no navegador que alertam: 'Atenção: Este site foi flagrado usando cronômetros cíclicos'.",
                 "• Bancos de Dados Públicos: Sites colaborativos de denúncia (como darkpatterns.org e hall da vergonha)."
             ], border_color=C_EMERALD, title_color=C_EMERALD)
             
    add_card(s25, Inches(6.8), Inches(2.3), Inches(5.7), Inches(4.5),
             title="O Papel dos Navegadores & Plataformas",
             items=[
                 "• Padrões Nativos no Browser: Assim como navegadores bloquearam pop-ups nos anos 2000, browsers podem exigir simetria de botões e neutralizar scripts fraudulentos.",
                 "• Auditoria Contínua em App Stores: Banimento automático de plugins que violam políticas de transparência (como o caso Beeketing no Shopify).",
                 "• Design System Ético: Incorporação de testes de fricção e ética nos pipelines de CI/CD antes do deploy."
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_notes(s25, "FALA (Integrante 4):\n"
                  "- Se a tecnologia criou o problema, a tecnologia também pode criar as defesas.")

    # =========================================================================
    # SLIDE 26: DEBATE FINAL & PERGUNTAS
    # =========================================================================
    s26 = prs.slides.add_slide(blank_layout)
    add_header(s26, "Debate Aberto & Perguntas", "Questões para reflexão coletiva com o professor e os colegas", "CONCLUSÃO", C_AMBER)
    
    add_card(s26, Inches(0.8), Inches(2.3), Inches(3.6), Inches(4.5),
             title="Questão 1: Liberdade",
             items=[
                 "O usuário tem a obrigação moral de ser atento ou o sistema tem a obrigação ética de não ser predatório?",
                 "Até que ponto culpar o usuário não é culpabilizar a vítima da manipulação cognitiva?"
             ], border_color=C_AMBER, title_color=C_AMBER)
             
    add_card(s26, Inches(4.8), Inches(2.3), Inches(3.6), Inches(4.5),
             title="Questão 2: IA & Futuro",
             items=[
                 "Uma IA treinada para maximizar tempo de tela ou faturamento inevitavelmente criará Dark Patterns ainda mais refinados se não for freada?",
                 "Como auditar algoritmos de personalização em tempo real?"
             ], border_color=C_CYAN, title_color=C_CYAN)
             
    add_card(s26, Inches(8.8), Inches(2.3), Inches(3.7), Inches(4.5),
             title="Questão 3: O Nosso Papel",
             items=[
                 "Qual é a linha vermelha que você, como profissional de computação, jamais cruzaria em uma interface?",
                 "Estamos construindo ferramentas que libertam as pessoas ou prisões cognitivas digitais?"
             ], border_color=C_ROSE, title_color=C_ROSE)
             
    add_notes(s26, "ENCERRAMENTO (Todos os 4 Integrantes):\n"
                  "- 'Agradecemos a atenção de todos e abrimos agora para os comentários do professor e dos colegas!'\n"
                  "- Usem as 3 perguntas do slide caso a sala fique em silêncio inicial para puxar o debate.")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))
    output_path = os.path.join(project_root, "apresentacao", "Apresentacao_Etica_Dark_Patterns.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path} with {len(prs.slides)} slides.")

if __name__ == "__main__":
    create_deck()
