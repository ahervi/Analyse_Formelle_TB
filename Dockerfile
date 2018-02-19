FROM ubuntu
RUN apt-get update && \
apt-get install -y wget tcsh git nano && \
wget http://mtc.epfl.ch/software-tools/mocha/download/c-mocha/distribution/linux/MOCHA.tar.gz && \
tar -xzf MOCHA.tar.gz && \
rm MOCHA.tar.gz && \
cd /MOCHA && \
git clone https://github.com/ahervi/Analyse_Formelle_TB.git && \
cd Analyse_Formelle_TB && \
git config --global user.email "hervieu.antoine@gmail.com" && \
git config --global user.name "ahervi"
WORKDIR /MOCHA
