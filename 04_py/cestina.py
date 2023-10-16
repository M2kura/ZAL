broken_txt = 'A tak se stalo, 6e dal39 den vyjelo aut94ko do sv2ta. P5edt9m se samoz5ejm2 rozlou4ilo se sv7mi rodi4i a vzalo si nutn0 v2ci sebou. To bylo ale nad3en9" Tolik jin7ch cest, tolik jin7ch cedul9 a nejen to" Aut94ko pozn8valo i nov0 zem2" Projelo celou Evropu i Asii, dokonce se vydalo i do Ameriky" A nejen6e pozn8valo zem2, ale tak0 pr8ci jin7ch aut.'

en_chars = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "[", "]", ";", "'", "/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "{", "}", ":", "\"", "<", ">", "?"]
cz_chars = [";", "+", "ě", "š", "č", "ř", "ž", "ý", "á", "í", "é", "=", "ú", ")", "ů", "§", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "%", "/", "(", "\"", "!", "?", ":", "_"]

print(cz_chars[en_chars.index("5")])

corect_text = ""
for pismeno in broken_txt:
    if pismeno in en_chars:
        corect_text += cz_chars[en_chars.index(pismeno)]
    else:
        corect_text += pismeno

print(corect_text)
