import os
import sys
import subprocess
import pymupdf

def build_report():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))
    
    html_file = os.path.join(base_dir, "relatorio.html")
    pdf_raw = os.path.join(base_dir, "relatorio_raw.pdf")
    pdf_final = os.path.join(base_dir, "Relatorio_Etica_Dark_Patterns.pdf")
    
    edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_exe):
        # try 64-bit path
        edge_exe = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    
    if not os.path.exists(edge_exe):
        print(f"Error: msedge.exe not found")
        return False
        
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_raw}",
        f"file:///{html_file.replace(os.sep, '/')}"
    ]
    
    print("Executando renderização via Microsoft Edge...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Erro na execução do Edge:", res.stderr)
        return False
        
    if not os.path.exists(pdf_raw):
        print("Erro: PDF bruto não foi gerado.")
        return False
        
    doc = pymupdf.open(pdf_raw)
    total_pages = len(doc)
    print(f"Páginas brutas renderizadas: {total_pages}")
    
    # Processar documento final com cabeçalhos e rodapés acadêmicos
    final_doc = pymupdf.open()
    for i in range(total_pages):
        page = doc[i]
        # Dimensões da página (A4: 595.3 x 841.9 pt)
        width = page.rect.width
        height = page.rect.height
        
        # Cabeçalho acadêmico a partir da página 2
        if i > 0:
            header_text = "Ética na Computação • Manipulação Comportamental e Dark Patterns em Escala"
            page.insert_text(
                pymupdf.Point(54, 38),
                header_text,
                fontsize=8.5,
                fontname="helv",
                color=(0.35, 0.38, 0.42)
            )
            # Linha sutil no cabeçalho
            page.draw_line(
                pymupdf.Point(54, 44),
                pymupdf.Point(width - 54, 44),
                color=(0.85, 0.87, 0.90),
                width=0.6
            )
            
        # Rodapé em todas as páginas: numeração "Página X de Y" e linha sutil
        page.draw_line(
            pymupdf.Point(54, height - 42),
            pymupdf.Point(width - 54, height - 42),
            color=(0.85, 0.87, 0.90),
            width=0.6
        )
        footer_left = "Seminário de Ética na Computação — Relatório Técnico"
        page.insert_text(
            pymupdf.Point(54, height - 28),
            footer_left,
            fontsize=8.5,
            fontname="helv",
            color=(0.45, 0.48, 0.52)
        )
        footer_right = f"Página {i + 1} de {total_pages}"
        # Alinhamento à direita
        text_w = pymupdf.get_text_length(footer_right, fontname="helv", fontsize=8.5)
        page.insert_text(
            pymupdf.Point(width - 54 - text_w, height - 28),
            footer_right,
            fontsize=8.5,
            fontname="helv",
            color=(0.35, 0.38, 0.42)
        )
        
        final_doc.insert_pdf(doc, from_page=i, to_page=i)
        
    final_doc.save(pdf_final)
    print(f"Relatório final salvo com sucesso: {pdf_final} ({len(final_doc)} páginas)")
    
    doc.close()
    final_doc.close()
    if os.path.exists(pdf_raw):
        try:
            os.remove(pdf_raw)
        except Exception as e:
            print(f"Aviso ao remover temporário: {e}")
        
    return total_pages

if __name__ == "__main__":
    pages = build_report()
