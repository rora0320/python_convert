import PyPDF2
import os


def extract_text_from_pdf(pdf_path, txt_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()

    # 추출된 텍스트를 txt 파일에 저장
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)


def list_pdf_files_in_directory(directory):
    # 주어진 디렉토리에서 .pdf 확장자를 가진 파일 목록을 반환합니다.
    return [f for f in os.listdir(directory) if f.endswith('.pdf')]


if __name__ == "__main__":
    # 사용자로부터 PDF 파일 경로 입력 받기
    directory = "C:\\Users\\USER-0011\\PycharmProjects\\testPDF\\"

    # 디렉토리에 있는 PDF 파일 목록 가져오기
    pdf_files = list_pdf_files_in_directory(directory)

    # PDF 파일 목록 출력
    for idx, pdf_file in enumerate(pdf_files, 1):
        print(f"{idx}. {pdf_file}")

    # 사용자로부터 PDF 파일 선택 받기
    selection = int(input("이 중에 원하시는 파일의 번호를 골라주세요: "))
    pdf_path = os.path.join(directory, pdf_files[selection - 1])

    # 사용자로부터 txt 파일 경로 입력 받기
    txt_directory = input("txt 파일 경로를 입력해주세요: ")
    txt_filename = input("파일 이름을 확장자를 포함하여 입력해주세요: ")
    txt_path = os.path.join(txt_directory, txt_filename)

    # 함수 호출
    extract_text_from_pdf(pdf_path, txt_path)