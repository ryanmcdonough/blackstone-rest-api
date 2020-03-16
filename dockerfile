FROM python:3

ENV SPACY_MODEL=en_core_web_sm

RUN pip install flask flask-restful blackstone
RUN pip install https://blackstone-model.s3-eu-west-1.amazonaws.com/en_blackstone_proto-0.0.1.tar.gz

ADD server.py /

CMD [ "python", "./server.py" ]
