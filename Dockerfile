FROM ubuntu
RUN apt-get update
RUN apt-get install -y wget tcsh git
RUN wget http://www-cad.eecs.berkeley.edu/~mocha/download/c-mocha/distribution/linux/MOCHA.tar.gz
RUN tar -xzf MOCHA.tar.gz
RUN rm MOCHA.tar.gz
RUN git clone https://github.com/ahervi/Analyse_Formelle_TB.git
RUN cp Analyse_Formelle_TB/* /MOCHA
RUN rm -rf Analyse_Formelle_TB
WORKDIR /MOCHA

