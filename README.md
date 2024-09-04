# PDF Watermarking Tool

This tool adds a watermark to PDF files in a given directory using the `poppler-win` library and `pdf2image`. It processes all PDF files in the `resource` directory and outputs the watermarked files to the `output` directory.

## Features

- Adds a grid watermark to PDF files
- Saves watermarked PDFs as images
- Customizable watermark text

## Prerequisites

1. Python 3.x installed
2. [poppler-win](https://github.com/oschwartz10612/poppler-windows) installed
3. Necessary Python packages (listed in `requirements.txt`)

## Installation

1. **Clone this repository**:

    ```bash
    git clone https://github.com/wssgxh/Watermarking.git
    cd Watermarking
    ```

2. **Install dependencies**:

    You can install the required Python packages using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3. **Download and set up `poppler-win`**:
## Prerequisites
1. **Only Windows with Python 3.12.5 tested**
2. Python 3.x installed
3. [poppler-win](https://github.com/oschwartz10612/poppler-windows) installed(check [poppler-win](poppler-win))
4. Necessary Python packages (listed in `requirements.txt`)
## Usage

1. **Place PDF files**: Place all the PDF files you want to watermark in the `resource` folder.

2. **Update Configuration**:

    In the Python script, you can update the `config` dictionary:

    ```python
    config = {
        'source_pdf_path': '',  # default is resource
        'output_pdf_path': 'output',
        'watermark_text': 'for verification only'  # Watermark text, please update it
    }
    ```

3. **Run the Script**:

    Execute the script:

    ```bash
    python main.py
    ```

4. **Find the output**:

    Watermarked PDF files will be saved as images in the `output` folder.

## Customization

- **Watermark Text**: You can customize the watermark text by editing the `watermark_text` value in the `config` dictionary.

- **Output Directory**: Change the output directory by modifying the `output_pdf_path` value in the `config` dictionary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows)
- [pdf2image](https://pypi.org/project/pdf2image/)
