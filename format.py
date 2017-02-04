# coding=utf-8
import random
import re


def clean_str(string):
    string = string.strip().lower()
    string = re.sub(u"[0-9]", u" ", string)
    string = re.sub(u"[Ёё]", u"е", string)
    string = re.sub(u"[^А-Яа-я\-]", u" ", string)
    string = re.sub(
        u"[А-Яа-я]*(овн|ыч|вич|пелагея|антон|анна|афанаси|евсей|ваня" +
        u"илья|аглая|иван|аграфен|пульхери|обломов|матве)[А-Яа-я]*",
        u" ", string)
    string = re.sub(u" +([А-Яа-я\-]|ты|она|он|вы|они) +", u" ", string)
    string = re.sub(u"(-то|-с)", u"", string)
    string = re.sub(u"([аяуюэеоёиыИАЯУЮЭЕОЁ])-(?=[аяуюэеоёиыИАЯУЮЭЕОЁ])", u"", string)
    string = re.sub(r"(.)\1{3,}", " ", string)
    string = re.sub(r"--", "", string)
    string = re.sub(r"\s{2,}", " ", string)

    return string.strip().lower()


def shuffle_both(list_a, list_b):
    c = list(zip(list_a, list_b))
    random.shuffle(c)
    sh_a, sh_b = zip(*c)
    return [sh_a, sh_b]
