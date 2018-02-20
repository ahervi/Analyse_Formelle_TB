FROM ubuntu
RUN apt-get update && \
apt-get install -y wget tcsh git nano && \
git config --global user.email "hervieu.antoine@gmail.com" && \
git config --global user.name "ahervi" && \
wget http://mtc.epfl.ch/software-tools/mocha/download/c-mocha/distribution/linux/MOCHA.tar.gz && \
tar -xzf MOCHA.tar.gz && \
rm MOCHA.tar.gz 
WORKDIR /MOCHA
