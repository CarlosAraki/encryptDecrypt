FROM python as build 

RUN pip install cryptography
RUN pip install rsa

COPY . .

FROM build 

