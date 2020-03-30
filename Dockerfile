FROM python:3.6.2
RUN mkdir myproject 
WORKDIR myproject
COPY  . .
COPY wait-for-it.sh ./wait-for-it.sh
RUN chmod 777 wait-for-it.sh
RUN pip install -r requirements.txt
CMD ["cp","python-script.py"]
