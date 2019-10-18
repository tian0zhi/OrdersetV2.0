# encode = "utf-8"
# Author 天志
import system_config_
import system_function_
import execjs
import re


def verify_code_get(jsname):
	'''代码不麻烦，主要是分析js花了些时间'''
	url = "https://static.wechat.laixuanzuo.com/template/theme2/cache/layout/"+jsname+".js"
	
	pattern_js_bg = 'void 0\=\=\=.\&\&\(.\=""\);'
	pattern_js_end = '.\.ajax_get'
	pattern_js =pattern_js_bg + '.*' + pattern_js_end

	pattern_js_res = '\+"\&".*\+"\&yzm\="'


	exjs = system_function_.network(url)
	# print(exjs,'\n\n')

	funjs = re.search(pattern_js,exjs).group(0)
	funjs = funjs[19:-10]
	# print(funjs,'\n\n')

	resjs = re.search(pattern_js_res,exjs).group(0)
	resultcommond = resjs[5:-14]

	# print(type(exjs))
	exjs8 = exjs
	# print(exjs8)

	docjs = execjs.compile(exjs8 + funjs)

	# print(docjs.eval(resultcommond))
	return docjs.eval(resultcommond)

if __name__ == "__main__":
	updatejs = {
	'PWJtdTQCfH6ZZJTZ':'Mm5BnkjRsrFi2S7',
	'HJTWZ6E6JzXcyPzk':'cDcstt3RGBhEpp',
	'PXPYws7pZtw328nt':'E5YRWDQN',
	'sNQESfdPmDtGj3WT':'XEt4wXdtape',
	'hSimEXkQTisdjkAs':'5tED5rQ',
	'xJ5GrhTTPChNX6Hd':'tSyDr8r6RX',
	'Tt6miWZyMMJJEyty':'JE7zw6eBiPQPDjt',
	'GB7SAeMK4KDEDKHz':'BrdHPYENA',
	'sfhnce3YafQWGKXx':'DmnmYNycps',
	'tNMEJa5hm8Enpycb':'xWpjRdSXJZ',
	'nfz6zEN5R8hKHdhc':'QckKdtHsHxED7GN',
	'4fcbbWAZTJeifMei':'Ein8Tww6P',
	'YWNMnsyMkWKK8Rcz':'ZyhTWrKQkQ',
	'ttwiMG3AsNPNYZRH':'SWdYRr',
	'zBewHe36PariTpSd':'ckZ6DdPJBza',
	'd7bFkBG8GNQ6XkQy':'s4tMwrA2',
	'b8Rp2N3ecJp7jQd5':'wyxiCMGtzMa2a2',
	'jbRfiBJSTPWzCyMY':'kZpGEe26',
	'iASW7ppYcDRKChh2':'4CrfRiXpmM',
	'xRZY3RhFi3DYmcQW':'aMM6jbx',
	'R6ZZEHrw3J7f2Z8w':'fjpjRMFdb22Fjt',
	'jfefTyG3iDPnYwKP':'aEsGsw',
	'3DMWs7EWF5tk5tCR':'3pztJhcF3sNPS',
	'yDJWFcsbNT4wJEPT':'4GQJh8t7ymXkh4',
	'yj8KQch26ddJAAh5':'jPmAWAwYhmkC',
	'DacXwjadeacCt5NA':'dBbcAQ',
	'hS8j5DmAzQPY6adw':'AEfpWm7DiD',
	'icT7nin4dmDzsBXX':'wAz4Qmemxfep',
	'SHztymRWeZaibTFh':'p2YeKebryn',
	'SZ5ye436pYGWeBYr':'yQyNhCtdFyChdXa',
	'8YDFEjjbmePNiBsr':'zmXNHWA',
	'YkhiNEchfniTQC85':'eATYAftnA8a',
	'SHnQ85YYi2wTmSkc':'mKwYhbfp44TbnFn',
	'2eEykYfmteSD3fXQ':'Fi3KE63W2p8yXN7',
	'asDa44XJ4SA6trFZ':'sshmsyzDZjhX5',
	'da8TRxpnFXRHkwD6':'pY5f4pRhhiHY',
	'hf6za8dcSK6EQYsX':'rkKFmQTtDda',
	'TGaZBwdzeN4FPACF':'HS2CsW8Mesaa',
	'JCSMfTJyDwsF2cPy':'tmZnwB6PmYh',
	'2JdjmyamSetAFSyd':'nXWxkhjEKWhA',
	'rAm76y5J7KTwn5Sp':'F2PMmwb54Gf2xn',
	'wty5i8BD3RWDGaH7':'mNZtTSGtQef',
	'HX2Sp5dakH8PzrYE':'QFFPSEE7y3',
	'Za8tWeYMh433SfDf':'GkM3EMW2THydG',
	'SCWFWbs8KJDRzb28':'BtMJfmX',
	'NradnQYbj7sEzQ7n':'rRjdapPtPAkhGP',
	'atQZbWbRRPiZsNTZ':'bnEh8GX3',
	'8WYsYreWRJiKS78Q':'3i8KtR',
	'AwyTXw7Bhfis6aDp':'AHp6pYrsYaj',
	'SbHH2mnY4XAk62Zw':'eSYhJdzK',
	'B7Fni6nrHGdt7YDP':'sTDrS55Gj3mpczy',
	'B2YQSAnPwkDRz5Fm':'8FQdJBDRSb4JNRi',
	'FGQCAK3mM7Gshxxz':'4DzRNWxADiYmK',
	'4Mmwy4WjsJcmrTBf':'2tbzJ2rzdGxD',
	'GaR5Bsh44rAWBG56':'x7ZarCRXHib8mNi',
	'2NKYhwyti4825333':'sap3jsdRTdwaDae',
	'AkWFhDhAjW6T4d4s':'YXQdWGZ',
	'yxsz6TZrRmGQ8bjC':'hyYrrEQz',
	'JzP4xEmhZG4eHGEb':'kcDJbJKdGG7hA',
	'ANA7f2D6NRMZBj7p':'nYcQidmhDmy',
	'hhfCH3G74mS3SSnC':'WSjKJi86kK5WiYQ',
	'825KWFcSkr2DRPJG':'DrC2a84nJanD',
	'WXsR2eTZCQtcT6z4':'bP53MDr',
	'YZdmsc2MKQ43nDnt':'XatjDpYPns',
	'rNMzCjb7JjwXEtxN':'ns4Cdj4',
	'5QwQ3AjyKFAHcDTA':'frXTTPQi'
	}
	for i in updatejs.keys():
		vc = verify_code_get(i)
		if updatejs[i] == vc:
			print(i,' 对应验证码为:',vc)
		else :
			print('解析错误，请修改代码!\n')
