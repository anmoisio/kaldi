#!/usr/bin/env python3
import re
import sys

# suf1 = "(n|a|an|en|ä|än)?"
# suf2 = "(den|tä|ta|teen|i)?"
# suf3 = "s(i)?|den|tta|teen|ttä"
# digits = (
# (0, "nolla", suf1),
# (3, "kolme", suf1),
# (4, "neljä",suf1),
# (5, "vii",suf3),
# (6, "kuu",suf3),
# (7, "seitsemä", suf1),
# (8, "kahdeksa", suf1),
# (9, "yhdeksä", suf1),
# (1, "yks|yh", suf2),
# (2, "kaks|kah", suf2),

# )

# tens = "kymmenen|kymmentä|kyt"
# tois = "toist(a)?"
# hundred = "sata(a)?"
# thousand = "tuhat(ta)?"
# million = "miljoona(a)?"
# vuotias = "vuotias"


# def parse(word):
#     left_over = word
#     fixed = 0
#     working_thousand = 0
#     working = 0
#     rest=""

#     while len(left_over) > 0:
#         digit_found = False
#         for d, m1, m2 in digits:
#             m = re.match("^(({})({}))".format(m1, m2), left_over)
#             if m is not None:
#                 left_over = left_over[len(m.group(0)):]
#                 working += d
#                 digit_found = True
#                 break
#         if digit_found:
#             continue

#         m = re.match("^({})".format(tens), left_over)
#         if m is not None:
#             left_over = left_over[len(m.group(0)):]
#             working *= 10
#             continue

#         m = re.match("^({})".format(tois), left_over)
#         if m is not None:
#             left_over = left_over[len(m.group(0)):]
#             working += 10
#             continue


#         m = re.match("^({})".format(hundred), left_over)
#         if m is not None:
#             left_over = left_over[len(m.group(0)):]

#             if working > 0:
#                 working *= 100
#             else:
#                 working = 100

#             working_thousand += working
#             working = 0
#             continue

#         m = re.match("^({})".format(thousand), left_over)
#         if m is not None:
#             left_over = left_over[len(m.group(0)):]
#             w = working + working_thousand
#             fixed += max(w, 1) * 1000
#             working = 0
#             working_thousand = 0
#             continue

#         m = re.match("^({})".format(million), left_over)
#         if m is not None:
#             left_over = left_over[len(m.group(0)):]
#             w = working + working_thousand
#             fixed += w * 1000000
#             working = 0
#             working_thousand = 0
#             continue

#         if left_over == vuotias and (fixed + working + working_thousand) > 0:
#             rest = " - vuotias"
#             left_over = ""
#             continue
#         return word

#     return str(fixed + working + working_thousand) + rest


for line in sys.stdin:
    try:
        key, val = line.strip().split(None, 1)
    except ValueError:
        key = line.strip()
        val = ""
    if "<w>" in val:
        val = val.lower().replace(" ", "").replace("<w>", " ")
    else:
        val = val.lower().replace("+ +","").replace(" +", " ").replace("+ ", " ").replace("+","")

    # for m in ('.', ',', '!', '?', '/', '-'):
    #     val = val.replace(m, " {} ".format(m))
    # val = val.replace("~", "")
    # val = val.replace('viiva', '-')
    # val = val.replace('kautta', '/')
    # val = val.replace('plus', '+')
    # val = re.sub("\[[a-z]*\]", "", val)
    # val = re.sub("#[0-9,]+", "", val)
    # val = " ".join(parse(word) for word in val.split())

    # val = " ".join(word for word in val.split())
    print("{} {}".format(key, val, end=""))

