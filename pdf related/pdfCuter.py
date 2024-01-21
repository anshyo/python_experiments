from PyPDF2 import PdfWriter , PdfReader

def nPdf(pdfPath , numOfPages):
    global totalPages
    pdfReader = PdfReader(open(pdfPath,"rb"))
    totalPages = len(pdfReader.pages)
    outputPdfs = []
    if numOfPages > totalPages:
        print("not sufficient amount of pages")
        return
    else:
        outputPdfs.extend(list(f"{numOfPages}"*int(totalPages/numOfPages)))
        outputPdfs.append(totalPages%numOfPages)
    m = []
    print(totalPages)
    outputPdfs = [100 , 100 , 100 , 100 , 43]
    for i in outputPdfs:
        m.append(int(i))
    outputPdfs = m
    pointer = 0
    for i in outputPdfs:
        if pointer <= totalPages:
            pdfWriter = PdfWriter()
            for j in range(i):
                pdfWriter.add_page(pdfReader.pages[pointer])
                pointer += 1
            print(pointer)
            o = f"pdf related\\pdftill{pointer}.pdf"
            pdfWriter.write(open(o , "wb"))
    
if __name__ == "__main__":
    nPdf(r"pdf related\old.pdf" , 100)