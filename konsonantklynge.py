
# import og last ned korpus
from nltk.corpus import udhr
from nltk.corpus import words


'''finn vokabulæret i korpuset Norwegian_Norsk-Nynorsk-Latin1 frå
korpuset udhr'''

nynorsk_udhr  = udhr.words('Norwegian_Norsk-Nynorsk-Latin1')

nynorske_ord = sorted(set(nynorsk_udhr))


'''finn ord med konsonantklynger med regex'''


ccccc_ar_ordpar = [(ccccc, w) for w in nynorske_ord
                       for ccccc in re.findall(r'[QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm]{5}', w)]

print(ccccc_ar_ordpar)
