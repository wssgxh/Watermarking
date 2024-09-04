import os


def get_pdf_files(folder_path):
    pdf_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append((os.path.join(root, file), file))
    return pdf_files


def find_poppler_win_path():
    for root, dirs, files in os.walk(os.getcwd()):  # 从当前工作目录开始遍历
        if 'poppler-win' in dirs:
            return os.path.abspath(os.path.join(root, 'poppler-win'))
    return None


if __name__ == '__main__':
    # refer to doc: https://pypi.org/project/pdf2image/

    config = {
        'source_pdf_path': 'resource',
        'output_pdf_path': 'output.pdf',
        'watermark_text': 'for verification only'  # please update me
    }

    poppler_path = os.path.join(find_poppler_win_path(), 'Library', 'bin')
    os.environ['PATH'] += os.pathsep + poppler_path

    pdf_files_path = get_pdf_files(config['output_pdf_path'])

    for info in get_pdf_files(config['source_pdf_path']):
        watermarked_files_name = os.path.basename(info[1])[:-4] + '_watermarked.pdf'
        cmd = f"""watermark grid  {info[0]}  "{config['watermark_text']}" -s output/{watermarked_files_name} --save-as-image --unselectable"""
        os.system(cmd)
