# This file was generated automatically by the Snowball to Python compiler
# http://snowballstem.org/

from .basestemmer import BaseStemmer
from .among import Among


class NorwegianStemmer(BaseStemmer):
    '''
    This class was automatically generated by a Snowball to Python compiler
    It implements the stemming algorithm defined by a snowball script.
    '''

    a_0 = [
        Among(u"a", -1, 1),
        Among(u"e", -1, 1),
        Among(u"ede", 1, 1),
        Among(u"ande", 1, 1),
        Among(u"ende", 1, 1),
        Among(u"ane", 1, 1),
        Among(u"ene", 1, 1),
        Among(u"hetene", 6, 1),
        Among(u"erte", 1, 3),
        Among(u"en", -1, 1),
        Among(u"heten", 9, 1),
        Among(u"ar", -1, 1),
        Among(u"er", -1, 1),
        Among(u"heter", 12, 1),
        Among(u"s", -1, 2),
        Among(u"as", 14, 1),
        Among(u"es", 14, 1),
        Among(u"edes", 16, 1),
        Among(u"endes", 16, 1),
        Among(u"enes", 16, 1),
        Among(u"hetenes", 19, 1),
        Among(u"ens", 14, 1),
        Among(u"hetens", 21, 1),
        Among(u"ers", 14, 1),
        Among(u"ets", 14, 1),
        Among(u"et", -1, 1),
        Among(u"het", 25, 1),
        Among(u"ert", -1, 3),
        Among(u"ast", -1, 1)
    ]

    a_1 = [
        Among(u"dt", -1, -1),
        Among(u"vt", -1, -1)
    ]

    a_2 = [
        Among(u"leg", -1, 1),
        Among(u"eleg", 0, 1),
        Among(u"ig", -1, 1),
        Among(u"eig", 2, 1),
        Among(u"lig", 2, 1),
        Among(u"elig", 4, 1),
        Among(u"els", -1, 1),
        Among(u"lov", -1, 1),
        Among(u"elov", 7, 1),
        Among(u"slov", 7, 1),
        Among(u"hetslov", 9, 1)
    ]

    g_v = [17, 65, 16, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 128]

    g_s_ending = [119, 125, 149, 1]

    I_x = 0
    I_p1 = 0


    def __r_mark_regions(self):
        # (, line 26
        self.I_p1 = self.limit
        # test, line 30
        v_1 = self.cursor
        # (, line 30
        # hop, line 30
        c = self.cursor + 3
        if 0 > c or c > self.limit:
            return False
        self.cursor = c
        # setmark x, line 30
        self.I_x = self.cursor
        self.cursor = v_1
        # goto, line 31
        try:
            while True:
                v_2 = self.cursor
                try:
                    if not self.in_grouping(NorwegianStemmer.g_v, 97, 248):
                        raise lab1()
                    self.cursor = v_2
                    raise lab0()
                except lab1: pass
                self.cursor = v_2
                if self.cursor >= self.limit:
                    return False
                self.cursor += 1
        except lab0: pass
        # gopast, line 31
        try:
            while True:
                try:
                    if not self.out_grouping(NorwegianStemmer.g_v, 97, 248):
                        raise lab3()
                    raise lab2()
                except lab3: pass
                if self.cursor >= self.limit:
                    return False
                self.cursor += 1
        except lab2: pass
        # setmark p1, line 31
        self.I_p1 = self.cursor
        # try, line 32
        try:
            # (, line 32
            if not self.I_p1 < self.I_x:
                raise lab4()
            self.I_p1 = self.I_x
        except lab4: pass
        return True

    def __r_main_suffix(self):
        # (, line 37
        # setlimit, line 38
        v_1 = self.limit - self.cursor
        # tomark, line 38
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 38
        # [, line 38
        self.ket = self.cursor
        # substring, line 38
        among_var = self.find_among_b(NorwegianStemmer.a_0)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        # ], line 38
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 44
            # delete, line 44
            if not self.slice_del():
                return False

        elif among_var == 2:
            # (, line 46
            # or, line 46
            try:
                v_3 = self.limit - self.cursor
                try:
                    if not self.in_grouping_b(NorwegianStemmer.g_s_ending, 98, 122):
                        raise lab1()
                    raise lab0()
                except lab1: pass
                self.cursor = self.limit - v_3
                # (, line 46
                # literal, line 46
                if not self.eq_s_b(u"k"):
                    return False
                if not self.out_grouping_b(NorwegianStemmer.g_v, 97, 248):
                    return False
            except lab0: pass
            # delete, line 46
            if not self.slice_del():
                return False

        elif among_var == 3:
            # (, line 48
            # <-, line 48
            if not self.slice_from(u"er"):
                return False
        return True

    def __r_consonant_pair(self):
        # (, line 52
        # test, line 53
        v_1 = self.limit - self.cursor
        # (, line 53
        # setlimit, line 54
        v_2 = self.limit - self.cursor
        # tomark, line 54
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_3 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_2
        # (, line 54
        # [, line 54
        self.ket = self.cursor
        # substring, line 54
        if self.find_among_b(NorwegianStemmer.a_1) == 0:
            self.limit_backward = v_3
            return False
        # ], line 54
        self.bra = self.cursor
        self.limit_backward = v_3
        self.cursor = self.limit - v_1
        # next, line 59
        if self.cursor <= self.limit_backward:
            return False
        self.cursor -= 1
        # ], line 59
        self.bra = self.cursor
        # delete, line 59
        if not self.slice_del():
            return False

        return True

    def __r_other_suffix(self):
        # (, line 62
        # setlimit, line 63
        v_1 = self.limit - self.cursor
        # tomark, line 63
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 63
        # [, line 63
        self.ket = self.cursor
        # substring, line 63
        among_var = self.find_among_b(NorwegianStemmer.a_2)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        # ], line 63
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 67
            # delete, line 67
            if not self.slice_del():
                return False

        return True

    def _stem(self):
        # (, line 72
        # do, line 74
        v_1 = self.cursor
        try:
            # call mark_regions, line 74
            if not self.__r_mark_regions():
                raise lab0()
        except lab0: pass
        self.cursor = v_1
        # backwards, line 75
        self.limit_backward = self.cursor
        self.cursor = self.limit
        # (, line 75
        # do, line 76
        v_2 = self.limit - self.cursor
        try:
            # call main_suffix, line 76
            if not self.__r_main_suffix():
                raise lab1()
        except lab1: pass
        self.cursor = self.limit - v_2
        # do, line 77
        v_3 = self.limit - self.cursor
        try:
            # call consonant_pair, line 77
            if not self.__r_consonant_pair():
                raise lab2()
        except lab2: pass
        self.cursor = self.limit - v_3
        # do, line 78
        v_4 = self.limit - self.cursor
        try:
            # call other_suffix, line 78
            if not self.__r_other_suffix():
                raise lab3()
        except lab3: pass
        self.cursor = self.limit - v_4
        self.cursor = self.limit_backward
        return True


class lab0(BaseException): pass


class lab1(BaseException): pass


class lab2(BaseException): pass


class lab3(BaseException): pass


class lab4(BaseException): pass
