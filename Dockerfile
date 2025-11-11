FROM mcr.microsoft.com/azure-functions/python:4-python3.13-appservice

COPY . /home/site/wwwroot

RUN pip install -r /home/site/wwwroot/requirements.txt
