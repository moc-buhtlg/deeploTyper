# korOCR
костыльно заменил модель в файлике run.py из mangaOCR на paddleOCR корейскую.

env var   PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK = True   чтобы после загрузки модели не долбились в брандмаузер.

не крашатся:
- Python                3.10.0
- paddleocr             3.3.0
- paddlepaddle          3.2.0
- paddlex               3.3.13
