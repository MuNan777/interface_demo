FROM python:3.10.7
WORKDIR /Project/demo

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["gunicorn", "index:app", "-c", "./gunicorn.conf.py"]