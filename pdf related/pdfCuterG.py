import PyPDF2

def split_pdf(input_pdf, output_prefix, pages_per_file):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        total_pages = len(pdf_reader.pages)

        if total_pages % pages_per_file != 0:
            print("Invalid number of pages per file.")
            return

        num_files = total_pages // pages_per_file

        for file_num in range(num_files):
            start_page = file_num * pages_per_file
            end_page = start_page + pages_per_file

            pdf_writer = PyPDF2.PdfWriter()

            for page_num in range(start_page, end_page):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            output_pdf = f"{output_prefix}_part{file_num + 1}.pdf"

            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_path = r'pdf related\old.pdf'
    output_pdf_prefix = r'pdf related\new.pdf'
    pages_per_file = 4  # Change this to the desired number of pages per file

    split_pdf(input_pdf_path, output_pdf_prefix, pages_per_file)
