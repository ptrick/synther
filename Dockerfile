FROM continuumio/miniconda3


ENTRYPOINT [ "/bin/bash", "-c" ]

ADD . /synther
WORKDIR /synther

RUN chmod +x image.sh && ./image.sh

CMD [ "ls" ]