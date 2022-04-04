Description:


1. Install pillow, pytesseract by using pip.
2. Install Tesseract-OCR.exe and configure enviroment.
   Download: https://github.com/UB-Mannheim/tesseract/wiki
   Steps:
   1. Double click tesseract.exe. 
      链接：https://pan.baidu.com/s/1HfpvdteCGpBAUiZhvVab_A 提取码：lvfn
   2. In python installion director, to search pytesseract.py. Open to modify it for below information:
      tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe', the right value is installion director of step 1(like C:\Program Files (x86)\Tesseract-OCR).
      RGB_MODE = 'RGB'
   3. unzip tessdata_language_sets.zip, copy chi_sim.traineddata and eng.traineddata to installion director of step 1.
      链接：https://pan.baidu.com/s/15raLAWiZklmAkw6Q4n_JWA  提取码：ex6g

