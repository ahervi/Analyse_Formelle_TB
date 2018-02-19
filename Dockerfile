FROM ubuntu
RUN apt-get update
RUN apt-get install -y wget tcsh git
RUN wget http://www-cad.eecs.berkeley.edu/~mocha/download/c-mocha/distribution/linux/MOCHA.tar.gz
RUN tar -xzf MOCHA.tar.gz
RUN rm MOCHA.tar.gz
WORKDIR /MOCHA
RUN git clone https://github.com/ahervi/Analyse_Formelle_TB.git
WORKDIR Analyse_Formelle_TB