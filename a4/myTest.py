from utils import pad_sents

s1 = ['I', 'am']
s2 = ['a', 'boy', 'and']
s3 = ['hi']

sents = [s1, s2, s3]
pad_token = 'A'

print(pad_sents(sents, pad_token))
