FROM python:3.10-alpine  as build 

RUN pip install cryptography
RUN pip install rsa

COPY . .

FROM build 
ENTRYPOINT [ "python","fernet.py" ]
CMD [ "e", "Message","key"]