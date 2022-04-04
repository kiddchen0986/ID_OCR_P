Config enviroment:

Reference(https://blog.csdn.net/qq_38161040/article/details/90649497):
1. 我们需要 pillow 和 pytesseract 这两个库，pip install 安装就好了
2. 安装 Tesseract-OCR.exe 然后配置下就好了。 
   Download: https://github.com/UB-Mannheim/tesseract/wiki
   Steps:
   1. Double click tesseract.exe. Here attached <tesseract-ocr-w64-setup-v5.0.1.20220118.exe>
   2. In python installion director, to search pytesseract.py. Open to modify it for below information:
      tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe', the right value is installion director of step 1.
      RGB_MODE = 'RGB'
     
