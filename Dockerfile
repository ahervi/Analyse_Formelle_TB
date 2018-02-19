FROM ubuntu
RUN apt-get update
RUN apt-get install -y wget tcsh
RUN wget http://www-cad.eecs.berkeley.edu/~mocha/download/c-mocha/distribution/linux/MOCHA.tar.gz
RUN tar -xzf MOCHA.tar.gz
RUN rm MOCHA.tar.gz
WORKDIR /MOCHA
ADD . .