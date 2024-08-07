import fitz  # PyMuPDF


def extract_bold_text_as_titles(pdf_path):
    # PDF 열기
    document = fitz.open(pdf_path)
    titles = []

    # 각 페이지를 순회하면서 텍스트 추출
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        # 블록 내 텍스트 처리
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        # 글씨체 굵기 확인 (bold)
                        fontname = span["font"]
                        fontflags = span["flags"]

                        # "bold" 단어가 폰트 이름에 있는지 확인
                        if "Bold" in fontname or fontflags & 2 ** 7:
                            titles.append(span["text"])

    return titles


def save_titles_as_html(titles, output_path):
    # HTML 구조 생성
    html_content = "<html><head><title>Extracted Titles</title></head><body>"
    for title in titles:
        html_content += f"<h1>{title}</h1>"
    html_content += "</body></html>"

    # HTML 파일로 저장
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)


if __name__ == "__main__":
    pdf_path = "C:\\Users\\USER-0011\\PycharmProjects\\testPDF\\MY1.pdf"
    html_output_path = "titles.html"

    # PDF에서 굵은 글씨 추출
    titles = extract_bold_text_as_titles(pdf_path)

    # 추출한 제목을 HTML 파일로 저장
    save_titles_as_html(titles, html_output_path)
    print(f"Extracted titles saved as {html_output_path}")