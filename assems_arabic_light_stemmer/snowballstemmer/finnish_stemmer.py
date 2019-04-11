# This file was generated automatically by the Snowball to Python compiler
# http://snowballstem.org/

from .basestemmer import BaseStemmer
from .among import Among


class FinnishStemmer(BaseStemmer):
    '''
    This class was automatically generated by a Snowball to Python compiler
    It implements the stemming algorithm defined by a snowball script.
    '''

    a_0 = [
        Among(u"pa", -1, 1),
        Among(u"sti", -1, 2),
        Among(u"kaan", -1, 1),
        Among(u"han", -1, 1),
        Among(u"kin", -1, 1),
        Among(u"h\u00E4n", -1, 1),
        Among(u"k\u00E4\u00E4n", -1, 1),
        Among(u"ko", -1, 1),
        Among(u"p\u00E4", -1, 1),
        Among(u"k\u00F6", -1, 1)
    ]

    a_1 = [
        Among(u"lla", -1, -1),
        Among(u"na", -1, -1),
        Among(u"ssa", -1, -1),
        Among(u"ta", -1, -1),
        Among(u"lta", 3, -1),
        Among(u"sta", 3, -1)
    ]

    a_2 = [
        Among(u"ll\u00E4", -1, -1),
        Among(u"n\u00E4", -1, -1),
        Among(u"ss\u00E4", -1, -1),
        Among(u"t\u00E4", -1, -1),
        Among(u"lt\u00E4", 3, -1),
        Among(u"st\u00E4", 3, -1)
    ]

    a_3 = [
        Among(u"lle", -1, -1),
        Among(u"ine", -1, -1)
    ]

    a_4 = [
        Among(u"nsa", -1, 3),
        Among(u"mme", -1, 3),
        Among(u"nne", -1, 3),
        Among(u"ni", -1, 2),
        Among(u"si", -1, 1),
        Among(u"an", -1, 4),
        Among(u"en", -1, 6),
        Among(u"\u00E4n", -1, 5),
        Among(u"ns\u00E4", -1, 3)
    ]

    a_5 = [
        Among(u"aa", -1, -1),
        Among(u"ee", -1, -1),
        Among(u"ii", -1, -1),
        Among(u"oo", -1, -1),
        Among(u"uu", -1, -1),
        Among(u"\u00E4\u00E4", -1, -1),
        Among(u"\u00F6\u00F6", -1, -1)
    ]

    a_6 = [
        Among(u"a", -1, 8),
        Among(u"lla", 0, -1),
        Among(u"na", 0, -1),
        Among(u"ssa", 0, -1),
        Among(u"ta", 0, -1),
        Among(u"lta", 4, -1),
        Among(u"sta", 4, -1),
        Among(u"tta", 4, 9),
        Among(u"lle", -1, -1),
        Among(u"ine", -1, -1),
        Among(u"ksi", -1, -1),
        Among(u"n", -1, 7),
        Among(u"han", 11, 1),
        Among(u"den", 11, -1, "_FinnishStemmer__r_VI"),
        Among(u"seen", 11, -1, "_FinnishStemmer__r_LONG"),
        Among(u"hen", 11, 2),
        Among(u"tten", 11, -1, "_FinnishStemmer__r_VI"),
        Among(u"hin", 11, 3),
        Among(u"siin", 11, -1, "_FinnishStemmer__r_VI"),
        Among(u"hon", 11, 4),
        Among(u"h\u00E4n", 11, 5),
        Among(u"h\u00F6n", 11, 6),
        Among(u"\u00E4", -1, 8),
        Among(u"ll\u00E4", 22, -1),
        Among(u"n\u00E4", 22, -1),
        Among(u"ss\u00E4", 22, -1),
        Among(u"t\u00E4", 22, -1),
        Among(u"lt\u00E4", 26, -1),
        Among(u"st\u00E4", 26, -1),
        Among(u"tt\u00E4", 26, 9)
    ]

    a_7 = [
        Among(u"eja", -1, -1),
        Among(u"mma", -1, 1),
        Among(u"imma", 1, -1),
        Among(u"mpa", -1, 1),
        Among(u"impa", 3, -1),
        Among(u"mmi", -1, 1),
        Among(u"immi", 5, -1),
        Among(u"mpi", -1, 1),
        Among(u"impi", 7, -1),
        Among(u"ej\u00E4", -1, -1),
        Among(u"mm\u00E4", -1, 1),
        Among(u"imm\u00E4", 10, -1),
        Among(u"mp\u00E4", -1, 1),
        Among(u"imp\u00E4", 12, -1)
    ]

    a_8 = [
        Among(u"i", -1, -1),
        Among(u"j", -1, -1)
    ]

    a_9 = [
        Among(u"mma", -1, 1),
        Among(u"imma", 0, -1)
    ]

    g_AEI = [17, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]

    g_V1 = [17, 65, 16, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 32]

    g_V2 = [17, 65, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 32]

    g_particle_end = [17, 97, 24, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 32]

    B_ending_removed = False
    S_x = ""
    I_p2 = 0
    I_p1 = 0


    def __r_mark_regions(self):
        # (, line 41
        self.I_p1 = self.limit
        self.I_p2 = self.limit
        # goto, line 46
        try:
            while True:
                v_1 = self.cursor
                try:
                    if not self.in_grouping(FinnishStemmer.g_V1, 97, 246):
                        raise lab1()
                    self.cursor = v_1
                    raise lab0()
                except lab1: pass
                self.cursor = v_1
                if self.cursor >= self.limit:
                    return False
                self.cursor += 1
        except lab0: pass
        # gopast, line 46
        try:
            while True:
                try:
                    if not self.out_grouping(FinnishStemmer.g_V1, 97, 246):
                        raise lab3()
                    raise lab2()
                except lab3: pass
                if self.cursor >= self.limit:
                    return False
                self.cursor += 1
        except lab2: pass
        # setmark p1, line 46
        self.I_p1 = self.cursor
        # goto, line 47
        try:
            while True:
                v_3 = self.cursor
                try:
                    if not self.in_grouping(FinnishStemmer.g_V1, 97, 246):
                        raise lab5()
                    self.cursor = v_3
                    raise lab4()
                except lab5: pass
                self.cursor = v_3
                if self.cursor >= self.limit:
                    return False
                self.cursor += 1
        except lab4: pass
        # gopast, line 47
        try:
            while True:
                try:
                    if not self.out_grouping(FinnishStemmer.g_V1, 97, 246):
                        raise lab7()
                    raise lab6()
                except lab7: pass
                if self.cursor >= self.limit:
                    return False
                self.cursor += 1
        except lab6: pass
        # setmark p2, line 47
        self.I_p2 = self.cursor
        return True

    def __r_R2(self):
        if not self.I_p2 <= self.cursor:
            return False
        return True

    def __r_particle_etc(self):
        # (, line 54
        # setlimit, line 55
        v_1 = self.limit - self.cursor
        # tomark, line 55
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 55
        # [, line 55
        self.ket = self.cursor
        # substring, line 55
        among_var = self.find_among_b(FinnishStemmer.a_0)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        # ], line 55
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 62
            if not self.in_grouping_b(FinnishStemmer.g_particle_end, 97, 246):
                return False
        elif among_var == 2:
            # (, line 64
            # call R2, line 64
            if not self.__r_R2():
                return False
        # delete, line 66
        if not self.slice_del():
            return False

        return True

    def __r_possessive(self):
        # (, line 68
        # setlimit, line 69
        v_1 = self.limit - self.cursor
        # tomark, line 69
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 69
        # [, line 69
        self.ket = self.cursor
        # substring, line 69
        among_var = self.find_among_b(FinnishStemmer.a_4)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        # ], line 69
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 72
            # not, line 72
            v_3 = self.limit - self.cursor
            try:
                # literal, line 72
                if not self.eq_s_b(u"k"):
                    raise lab0()
                return False
            except lab0: pass
            self.cursor = self.limit - v_3
            # delete, line 72
            if not self.slice_del():
                return False

        elif among_var == 2:
            # (, line 74
            # delete, line 74
            if not self.slice_del():
                return False

            # [, line 74
            self.ket = self.cursor
            # literal, line 74
            if not self.eq_s_b(u"kse"):
                return False
            # ], line 74
            self.bra = self.cursor
            # <-, line 74
            if not self.slice_from(u"ksi"):
                return False
        elif among_var == 3:
            # (, line 78
            # delete, line 78
            if not self.slice_del():
                return False

        elif among_var == 4:
            # (, line 81
            # among, line 81
            if self.find_among_b(FinnishStemmer.a_1) == 0:
                return False
            # delete, line 81
            if not self.slice_del():
                return False

        elif among_var == 5:
            # (, line 83
            # among, line 83
            if self.find_among_b(FinnishStemmer.a_2) == 0:
                return False
            # delete, line 84
            if not self.slice_del():
                return False

        elif among_var == 6:
            # (, line 86
            # among, line 86
            if self.find_among_b(FinnishStemmer.a_3) == 0:
                return False
            # delete, line 86
            if not self.slice_del():
                return False

        return True

    def __r_LONG(self):
        # among, line 91
        if self.find_among_b(FinnishStemmer.a_5) == 0:
            return False
        return True

    def __r_VI(self):
        # (, line 93
        # literal, line 93
        if not self.eq_s_b(u"i"):
            return False
        if not self.in_grouping_b(FinnishStemmer.g_V2, 97, 246):
            return False
        return True

    def __r_case_ending(self):
        # (, line 95
        # setlimit, line 96
        v_1 = self.limit - self.cursor
        # tomark, line 96
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 96
        # [, line 96
        self.ket = self.cursor
        # substring, line 96
        among_var = self.find_among_b(FinnishStemmer.a_6)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        # ], line 96
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 98
            # literal, line 98
            if not self.eq_s_b(u"a"):
                return False
        elif among_var == 2:
            # (, line 99
            # literal, line 99
            if not self.eq_s_b(u"e"):
                return False
        elif among_var == 3:
            # (, line 100
            # literal, line 100
            if not self.eq_s_b(u"i"):
                return False
        elif among_var == 4:
            # (, line 101
            # literal, line 101
            if not self.eq_s_b(u"o"):
                return False
        elif among_var == 5:
            # (, line 102
            # literal, line 102
            if not self.eq_s_b(u"\u00E4"):
                return False
        elif among_var == 6:
            # (, line 103
            # literal, line 103
            if not self.eq_s_b(u"\u00F6"):
                return False
        elif among_var == 7:
            # (, line 111
            # try, line 111
            v_3 = self.limit - self.cursor
            try:
                # (, line 111
                # and, line 113
                v_4 = self.limit - self.cursor
                # or, line 112
                try:
                    v_5 = self.limit - self.cursor
                    try:
                        # call LONG, line 111
                        if not self.__r_LONG():
                            raise lab2()
                        raise lab1()
                    except lab2: pass
                    self.cursor = self.limit - v_5
                    # literal, line 112
                    if not self.eq_s_b(u"ie"):
                        self.cursor = self.limit - v_3
                        raise lab0()
                except lab1: pass
                self.cursor = self.limit - v_4
                # next, line 113
                if self.cursor <= self.limit_backward:
                    self.cursor = self.limit - v_3
                    raise lab0()
                self.cursor -= 1
                # ], line 113
                self.bra = self.cursor
            except lab0: pass
        elif among_var == 8:
            # (, line 119
            if not self.in_grouping_b(FinnishStemmer.g_V1, 97, 246):
                return False
            if not self.out_grouping_b(FinnishStemmer.g_V1, 97, 246):
                return False
        elif among_var == 9:
            # (, line 121
            # literal, line 121
            if not self.eq_s_b(u"e"):
                return False
        # delete, line 138
        if not self.slice_del():
            return False

        # set ending_removed, line 139
        self.B_ending_removed = True
        return True

    def __r_other_endings(self):
        # (, line 141
        # setlimit, line 142
        v_1 = self.limit - self.cursor
        # tomark, line 142
        if self.cursor < self.I_p2:
            return False
        self.cursor = self.I_p2
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 142
        # [, line 142
        self.ket = self.cursor
        # substring, line 142
        among_var = self.find_among_b(FinnishStemmer.a_7)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        # ], line 142
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 146
            # not, line 146
            v_3 = self.limit - self.cursor
            try:
                # literal, line 146
                if not self.eq_s_b(u"po"):
                    raise lab0()
                return False
            except lab0: pass
            self.cursor = self.limit - v_3
        # delete, line 151
        if not self.slice_del():
            return False

        return True

    def __r_i_plural(self):
        # (, line 153
        # setlimit, line 154
        v_1 = self.limit - self.cursor
        # tomark, line 154
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 154
        # [, line 154
        self.ket = self.cursor
        # substring, line 154
        if self.find_among_b(FinnishStemmer.a_8) == 0:
            self.limit_backward = v_2
            return False
        # ], line 154
        self.bra = self.cursor
        self.limit_backward = v_2
        # delete, line 158
        if not self.slice_del():
            return False

        return True

    def __r_t_plural(self):
        # (, line 160
        # setlimit, line 161
        v_1 = self.limit - self.cursor
        # tomark, line 161
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 161
        # [, line 162
        self.ket = self.cursor
        # literal, line 162
        if not self.eq_s_b(u"t"):
            self.limit_backward = v_2
            return False
        # ], line 162
        self.bra = self.cursor
        # test, line 162
        v_3 = self.limit - self.cursor
        if not self.in_grouping_b(FinnishStemmer.g_V1, 97, 246):
            self.limit_backward = v_2
            return False
        self.cursor = self.limit - v_3
        # delete, line 163
        if not self.slice_del():
            return False

        self.limit_backward = v_2
        # setlimit, line 165
        v_4 = self.limit - self.cursor
        # tomark, line 165
        if self.cursor < self.I_p2:
            return False
        self.cursor = self.I_p2
        v_5 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_4
        # (, line 165
        # [, line 165
        self.ket = self.cursor
        # substring, line 165
        among_var = self.find_among_b(FinnishStemmer.a_9)
        if among_var == 0:
            self.limit_backward = v_5
            return False
        # ], line 165
        self.bra = self.cursor
        self.limit_backward = v_5
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 167
            # not, line 167
            v_6 = self.limit - self.cursor
            try:
                # literal, line 167
                if not self.eq_s_b(u"po"):
                    raise lab0()
                return False
            except lab0: pass
            self.cursor = self.limit - v_6
        # delete, line 170
        if not self.slice_del():
            return False

        return True

    def __r_tidy(self):
        # (, line 172
        # setlimit, line 173
        v_1 = self.limit - self.cursor
        # tomark, line 173
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 173
        # do, line 174
        v_3 = self.limit - self.cursor
        try:
            # (, line 174
            # and, line 174
            v_4 = self.limit - self.cursor
            # call LONG, line 174
            if not self.__r_LONG():
                raise lab0()
            self.cursor = self.limit - v_4
            # (, line 174
            # [, line 174
            self.ket = self.cursor
            # next, line 174
            if self.cursor <= self.limit_backward:
                raise lab0()
            self.cursor -= 1
            # ], line 174
            self.bra = self.cursor
            # delete, line 174
            if not self.slice_del():
                return False

        except lab0: pass
        self.cursor = self.limit - v_3
        # do, line 175
        v_5 = self.limit - self.cursor
        try:
            # (, line 175
            # [, line 175
            self.ket = self.cursor
            if not self.in_grouping_b(FinnishStemmer.g_AEI, 97, 228):
                raise lab1()
            # ], line 175
            self.bra = self.cursor
            if not self.out_grouping_b(FinnishStemmer.g_V1, 97, 246):
                raise lab1()
            # delete, line 175
            if not self.slice_del():
                return False

        except lab1: pass
        self.cursor = self.limit - v_5
        # do, line 176
        v_6 = self.limit - self.cursor
        try:
            # (, line 176
            # [, line 176
            self.ket = self.cursor
            # literal, line 176
            if not self.eq_s_b(u"j"):
                raise lab2()
            # ], line 176
            self.bra = self.cursor
            # or, line 176
            try:
                v_7 = self.limit - self.cursor
                try:
                    # literal, line 176
                    if not self.eq_s_b(u"o"):
                        raise lab4()
                    raise lab3()
                except lab4: pass
                self.cursor = self.limit - v_7
                # literal, line 176
                if not self.eq_s_b(u"u"):
                    raise lab2()
            except lab3: pass
            # delete, line 176
            if not self.slice_del():
                return False

        except lab2: pass
        self.cursor = self.limit - v_6
        # do, line 177
        v_8 = self.limit - self.cursor
        try:
            # (, line 177
            # [, line 177
            self.ket = self.cursor
            # literal, line 177
            if not self.eq_s_b(u"o"):
                raise lab5()
            # ], line 177
            self.bra = self.cursor
            # literal, line 177
            if not self.eq_s_b(u"j"):
                raise lab5()
            # delete, line 177
            if not self.slice_del():
                return False

        except lab5: pass
        self.cursor = self.limit - v_8
        self.limit_backward = v_2
        # goto, line 179
        try:
            while True:
                v_9 = self.limit - self.cursor
                try:
                    if not self.out_grouping_b(FinnishStemmer.g_V1, 97, 246):
                        raise lab7()
                    self.cursor = self.limit - v_9
                    raise lab6()
                except lab7: pass
                self.cursor = self.limit - v_9
                if self.cursor <= self.limit_backward:
                    return False
                self.cursor -= 1
        except lab6: pass
        # [, line 179
        self.ket = self.cursor
        # next, line 179
        if self.cursor <= self.limit_backward:
            return False
        self.cursor -= 1
        # ], line 179
        self.bra = self.cursor
        # -> x, line 179
        self.S_x = self.slice_to(self.S_x)
        if self.S_x == '':
            return False
        # name x, line 179
        if not self.eq_s_b(self.S_x):
            return False
        # delete, line 179
        if not self.slice_del():
            return False

        return True

    def _stem(self):
        # (, line 183
        # do, line 185
        v_1 = self.cursor
        try:
            # call mark_regions, line 185
            if not self.__r_mark_regions():
                raise lab0()
        except lab0: pass
        self.cursor = v_1
        # unset ending_removed, line 186
        self.B_ending_removed = False
        # backwards, line 187
        self.limit_backward = self.cursor
        self.cursor = self.limit
        # (, line 187
        # do, line 188
        v_2 = self.limit - self.cursor
        try:
            # call particle_etc, line 188
            if not self.__r_particle_etc():
                raise lab1()
        except lab1: pass
        self.cursor = self.limit - v_2
        # do, line 189
        v_3 = self.limit - self.cursor
        try:
            # call possessive, line 189
            if not self.__r_possessive():
                raise lab2()
        except lab2: pass
        self.cursor = self.limit - v_3
        # do, line 190
        v_4 = self.limit - self.cursor
        try:
            # call case_ending, line 190
            if not self.__r_case_ending():
                raise lab3()
        except lab3: pass
        self.cursor = self.limit - v_4
        # do, line 191
        v_5 = self.limit - self.cursor
        try:
            # call other_endings, line 191
            if not self.__r_other_endings():
                raise lab4()
        except lab4: pass
        self.cursor = self.limit - v_5
        # or, line 192
        try:
            v_6 = self.limit - self.cursor
            try:
                # (, line 192
                # Boolean test ending_removed, line 192
                if not self.B_ending_removed:
                    raise lab6()
                # do, line 192
                v_7 = self.limit - self.cursor
                try:
                    # call i_plural, line 192
                    if not self.__r_i_plural():
                        raise lab7()
                except lab7: pass
                self.cursor = self.limit - v_7
                raise lab5()
            except lab6: pass
            self.cursor = self.limit - v_6
            # do, line 192
            v_8 = self.limit - self.cursor
            try:
                # call t_plural, line 192
                if not self.__r_t_plural():
                    raise lab8()
            except lab8: pass
            self.cursor = self.limit - v_8
        except lab5: pass
        # do, line 193
        v_9 = self.limit - self.cursor
        try:
            # call tidy, line 193
            if not self.__r_tidy():
                raise lab9()
        except lab9: pass
        self.cursor = self.limit - v_9
        self.cursor = self.limit_backward
        return True


class lab0(BaseException): pass


class lab1(BaseException): pass


class lab2(BaseException): pass


class lab3(BaseException): pass


class lab4(BaseException): pass


class lab5(BaseException): pass


class lab6(BaseException): pass


class lab7(BaseException): pass


class lab8(BaseException): pass


class lab9(BaseException): pass
