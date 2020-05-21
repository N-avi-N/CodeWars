# Output format - "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34"

from statistics import mean


def stat(strg):
    text = strg.split()

    ls_sec = []

    for i in text:
        i = i.replace(',', '')
        h, m, s = i.split('|')
        ls_sec.append(int(h) * 60 ** 2 + int(m) * 60 + int(s))

    rang = time_convert(ranges(ls_sec))
    mea = time_convert(means(ls_sec))
    median = time_convert(medians(ls_sec))

    return "Range: " + rang + " Average: " + mea + " Median: " + median


def ranges(sec):
    return max(sec) - min(sec)


def means(sec):
    return int(mean(sec))


def medians(sec):
    sec.sort()
    if len(sec) % 2 == 0:
        a = sec[int(len(sec)/2)]
        b = sec[int((len(sec)-1)/2)]
        return int((a + b) / 2)
    else:
        return sec[int(len(sec) / 2)]

def time_convert(sec):
    hr = str(sec // 60**2).zfill(2)
    mi = str((sec - int(hr) * 60 ** 2) // 60).zfill(2)
    se = str((sec - int(hr) * 60 ** 2 - int(mi) * 60)).zfill(2)
    return hr + "|" + mi + "|" + se



