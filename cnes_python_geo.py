# Python Script for treatment of CNES microdata with emphasis on spatial analysis

# Author: Erick de Oliveira Faria (https://orcid.org/0000-0003-0089-9602)#

import pandas as pd
import numpy as np
import geopandas as gpd
import os
import ftplib
import zipfile
import geopy

# Definir o diretório e nome do arquivo
path_cnes = ('path')
filename = ('BASE_DE_DADOS_CNES_201912.ZIP') #Change the date

os.mkdir(path_cnes)
os.chdir(path_cnes)

# Download from Datasus FTP
path = 'cnes/'
ftp = ftplib.FTP('ftp.datasus.gov.br') 
ftp.login('', '') 
ftp.cwd(path)
ftp.retrbinary('RETR' + filename, open(filename, 'wb').write)
ftp.quit()

# Unzip the file
with zipfile.ZipFile(filename,'r') as zip_ref:
    zip_ref.extractall(diretorio)


cnes = pd.read_csv('tbEstabelecimento201912.csv', sep=';', header=0,
                    usecols=[0,1,7,8,10,11], names=['cod_unidade','num_cnes','nom_logradouro',
                                                    'num_endereco','nom_bairro','num_cep'],
                  dtype={'cod_unidade':str,'nom_logradouro':str,'num_endereco':str,'nom_bairro':str,'num_cep':str})

cep = pd.read_csv('C:\\Users\\Jack Sparrow\\OneDrive - univ-lille.fr\\dados_secundarios\\cep_brasil\\cep.txt', 
                  sep='\t', names=['num_cep', 'cod_uf', 'cod_mun'], dtype={'num_cep':str})
mun = pd.read_csv('C:\\Users\\Jack Sparrow\\OneDrive - univ-lille.fr\\dados_secundarios\\municipio_brasil\\municipio.txt', 
                  sep='\t')

cep = pd.merge(cep, mun, on='cod_mun', how='left')
cnes= pd.merge(cnes, cep, on='num_cep', how='left')

# Merge the columns
cnes['endereco'] = (cnes['nom_logradouro'] + ', ' + cnes['num_endereco'] + ', ' + cnes['nom_bairro'] + ', ' + cnes['nom_mun'] 
                    + ', ' + cnes['cod_uf'] + ', ' + cnes['num_cep'])

# Excludes unnecessary variables
cnes.drop(['nom_logradouro', 'num_endereco', 'nom_bairro', 'num_cep', 'cod_uf', 'nom_mun', 'cod_mun'], axis=1, inplace=True)

# Saves the file before geocoding for verification
cnes.to_csv('cnes_end.txt', sep='\t', index=False)