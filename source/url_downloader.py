#!/usr/bin/env python
# -*- coding:utf-8 -*-

import wget

def url_downloader():
	star = "#########################################################"
	print star
	indirilecek_url_adresi = raw_input("İndirmek istediğiniz url adresini giriniz : ")
	dosya_ismi = wget.download(indirilecek_url_adresi)
	print star

url_downloader_ico = """
#########################################################
#       PYTHON - URL DOWNLOADER - GH0ST S0FTWARE        #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#        GitHub : linkedin.com/in/ismailtasdelen        #
#########################################################
"""

print url_downloader_ico

url_downloader()
