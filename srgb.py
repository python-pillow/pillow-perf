from __future__ import division


def srgb2linear(s):
    if s < 0.0404482362771082:
        return s / 12.92
    return pow((s + 0.055) / 1.055, 2.4)


def linear2srgb(l):
    if l < 0.00313066844250063:
        return l * 12.92
    return pow(l, 1 / 2.4) * 1.055 - 0.055


if __name__ == '__main__':
    N = (1 << 8) - 1
    M = (1 << 12) - 1

    print '>>> srgb2linear'
    prev_l = None
    for s in xrange(N + 1):
        l = srgb2linear(s / N)
        l = int(round(l * M))
        if l == prev_l:
            print '{}: {}'.format(s, l)
        prev_l = l

    print '>>> linear2srgb'
    prev_s = None
    for l in xrange(N + 1):
        s = linear2srgb(l / N)
        s = int(round(s * M))
        if s == prev_s:
            print '{}: {}'.format(l, s)
        prev_s = s

    print '>>> roundtrip'
    for s in xrange(N + 1):
        prev_s = s
        l = srgb2linear(s / N)
        l = int(round(l * M))
        s = linear2srgb(l / M)
        s = int(round(s * N))
        if s != prev_s:
            print '{} {}: {}'.format(prev_s, s, l)
