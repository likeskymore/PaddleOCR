from paddleocr import PaddleOCR,draw_ocr

ocr = PaddleOCR(rec_model_dir="E:\OCR_huggingface\PaddleOCR\PP-OCRv5_mobile_rec_infer",use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
img_path = 'E:\OCR_huggingface\datatest'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)


# draw result
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
print(txts)