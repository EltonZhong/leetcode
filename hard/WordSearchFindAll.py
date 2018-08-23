# coding=utf-8
"""
给定二维数组board 和词word, 求 在a中找到b 的所有路径
word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.
This solution finds all the possible path for word
"""
from typing import List, Tuple
from datetime import datetime


class Solution:
    """
    Solution
    """

    def __init__(self) -> None:
        """
        self.board: List[List[str]] = None
        self.indexes: List[Tuple[int, int]] = None
        self.word: str = None
        self.len_x: int = None
        self.len_y: int = None
        """
        self.board = None
        self.indexes = None
        self.len_x = None
        self.len_y = None

    def findPathes(self, board: List[List[str]], word: str) -> List:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: List[str]
        """
        self.board = board
        self.len_x = len(board)
        self.len_y = len(board[0])
        self.indexes = [(i, j) for i in range(self.len_x) for j in range(self.len_y)]

        return self.find_indexes(word)

    def find_indexes(self, word: str) -> List[List[Tuple[int, int]]]:
        """
        Find all the possable ways for each word in the board
        Each possiable way is composed with a serials of indexes, which is constructed by the path's indexes
        :param word:
        :return:
        """
        if len(word) == 1:
            now_results = [[index] for index in self.indexes if self.board[index[0]][index[1]] == word]
            return now_results

        last_results = self.find_indexes(word[: -1])
        now_results = []

        if not len(last_results):
            return now_results

        for result in last_results:
            for (x, y) in self.get_adjacent_cells(result[-1][0], result[-1][1], result):
                if self.board[x][y] == word[-1]:
                    now_results.append(result + [(x, y)])

        return now_results

    def get_adjacent_cells(self, x: int, y: int, now_list: List[Tuple[int, int]]):
        """
        rt
        :param now_list: current cells used
        :param x:
        :param y:
        :return:
        """
        adjacent_cells = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        adjacent_cells = list(filter(lambda cell: cell[0] >= 0 and cell[1] >= 0, adjacent_cells))
        adjacent_cells = list(filter(lambda cell: cell[0] < self.len_x and cell[1] < self.len_y, adjacent_cells))

        # This way is adviced in python3, while above is not
        adjacent_cells = [cell for cell in adjacent_cells if cell not in now_list]
        return adjacent_cells


board_large = [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"],
               ["b", "c", "d", "e"],
               ["f", "g", "h", "i"], ["j", "k", "l", "m"], ["n", "o", "p", "q"], ["r", "s", "t", "u"],
               ["v", "w", "x", "y"],
               ["z", "z", "z", "z"]]
words_large = ["aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaac", "aaaaaaaaaaaaaaad", "aaaaaaaaaaaaaaae",
               "aaaaaaaaaaaaaaaf",
               "aaaaaaaaaaaaaaag", "aaaaaaaaaaaaaaah", "aaaaaaaaaaaaaaai", "aaaaaaaaaaaaaaaj", "aaaaaaaaaaaaaaak",
               "aaaaaaaaaaaaaaal",
               "aaaaaaaaaaaaaaam", "aaaaaaaaaaaaaaan", "aaaaaaaaaaaaaaao", "aaaaaaaaaaaaaaap", "aaaaaaaaaaaaaaaq",
               "aaaaaaaaaaaaaaar",
               "aaaaaaaaaaaaaaas", "aaaaaaaaaaaaaaat", "aaaaaaaaaaaaaaau", "aaaaaaaaaaaaaaav", "aaaaaaaaaaaaaaaw",
               "aaaaaaaaaaaaaaax",
               "aaaaaaaaaaaaaaay", "aaaaaaaaaaaaaaaz", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaac",
               "aaaaaaaaaaaaaaad",
               "aaaaaaaaaaaaaaae", "aaaaaaaaaaaaaaaf", "aaaaaaaaaaaaaaag", "aaaaaaaaaaaaaaah", "aaaaaaaaaaaaaaai",
               "aaaaaaaaaaaaaaaj",
               "aaaaaaaaaaaaaaak", "aaaaaaaaaaaaaaal", "aaaaaaaaaaaaaaam", "aaaaaaaaaaaaaaan", "aaaaaaaaaaaaaaao",
               "aaaaaaaaaaaaaaap",
               "aaaaaaaaaaaaaaaq", "aaaaaaaaaaaaaaar", "aaaaaaaaaaaaaaas", "aaaaaaaaaaaaaaat", "aaaaaaaaaaaaaaau",
               "aaaaaaaaaaaaaaav",
               "aaaaaaaaaaaaaaaw", "aaaaaaaaaaaaaaax", "aaaaaaaaaaaaaaay", "aaaaaaaaaaaaaaaz", "aaaaaaaaaaaaaaba",
               "aaaaaaaaaaaaaabb",
               "aaaaaaaaaaaaaabc", "aaaaaaaaaaaaaabd", "aaaaaaaaaaaaaabe", "aaaaaaaaaaaaaabf", "aaaaaaaaaaaaaabg",
               "aaaaaaaaaaaaaabh",
               "aaaaaaaaaaaaaabi", "aaaaaaaaaaaaaabj", "aaaaaaaaaaaaaabk", "aaaaaaaaaaaaaabl", "aaaaaaaaaaaaaabm",
               "aaaaaaaaaaaaaabn",
               "aaaaaaaaaaaaaabo", "aaaaaaaaaaaaaabp", "aaaaaaaaaaaaaabq", "aaaaaaaaaaaaaabr", "aaaaaaaaaaaaaabs",
               "aaaaaaaaaaaaaabt",
               "aaaaaaaaaaaaaabu", "aaaaaaaaaaaaaabv", "aaaaaaaaaaaaaabw", "aaaaaaaaaaaaaabx", "aaaaaaaaaaaaaaby",
               "aaaaaaaaaaaaaabz",
               "aaaaaaaaaaaaaaca", "aaaaaaaaaaaaaacb", "aaaaaaaaaaaaaacc", "aaaaaaaaaaaaaacd", "aaaaaaaaaaaaaace",
               "aaaaaaaaaaaaaacf",
               "aaaaaaaaaaaaaacg", "aaaaaaaaaaaaaach", "aaaaaaaaaaaaaaci", "aaaaaaaaaaaaaacj", "aaaaaaaaaaaaaack",
               "aaaaaaaaaaaaaacl",
               "aaaaaaaaaaaaaacm", "aaaaaaaaaaaaaacn", "aaaaaaaaaaaaaaco", "aaaaaaaaaaaaaacp", "aaaaaaaaaaaaaacq",
               "aaaaaaaaaaaaaacr",
               "aaaaaaaaaaaaaacs", "aaaaaaaaaaaaaact", "aaaaaaaaaaaaaacu", "aaaaaaaaaaaaaacv", "aaaaaaaaaaaaaacw",
               "aaaaaaaaaaaaaacx",
               "aaaaaaaaaaaaaacy", "aaaaaaaaaaaaaacz", "aaaaaaaaaaaaaada", "aaaaaaaaaaaaaadb", "aaaaaaaaaaaaaadc",
               "aaaaaaaaaaaaaadd",
               "aaaaaaaaaaaaaade", "aaaaaaaaaaaaaadf", "aaaaaaaaaaaaaadg", "aaaaaaaaaaaaaadh", "aaaaaaaaaaaaaadi",
               "aaaaaaaaaaaaaadj",
               "aaaaaaaaaaaaaadk", "aaaaaaaaaaaaaadl", "aaaaaaaaaaaaaadm", "aaaaaaaaaaaaaadn", "aaaaaaaaaaaaaado",
               "aaaaaaaaaaaaaadp",
               "aaaaaaaaaaaaaadq", "aaaaaaaaaaaaaadr", "aaaaaaaaaaaaaads", "aaaaaaaaaaaaaadt", "aaaaaaaaaaaaaadu",
               "aaaaaaaaaaaaaadv",
               "aaaaaaaaaaaaaadw", "aaaaaaaaaaaaaadx", "aaaaaaaaaaaaaady", "aaaaaaaaaaaaaadz", "aaaaaaaaaaaaaaea",
               "aaaaaaaaaaaaaaeb",
               "aaaaaaaaaaaaaaec", "aaaaaaaaaaaaaaed", "aaaaaaaaaaaaaaee", "aaaaaaaaaaaaaaef", "aaaaaaaaaaaaaaeg",
               "aaaaaaaaaaaaaaeh",
               "aaaaaaaaaaaaaaei", "aaaaaaaaaaaaaaej", "aaaaaaaaaaaaaaek", "aaaaaaaaaaaaaael", "aaaaaaaaaaaaaaem",
               "aaaaaaaaaaaaaaen",
               "aaaaaaaaaaaaaaeo", "aaaaaaaaaaaaaaep", "aaaaaaaaaaaaaaeq", "aaaaaaaaaaaaaaer", "aaaaaaaaaaaaaaes",
               "aaaaaaaaaaaaaaet",
               "aaaaaaaaaaaaaaeu", "aaaaaaaaaaaaaaev", "aaaaaaaaaaaaaaew", "aaaaaaaaaaaaaaex", "aaaaaaaaaaaaaaey",
               "aaaaaaaaaaaaaaez",
               "aaaaaaaaaaaaaafa", "aaaaaaaaaaaaaafb", "aaaaaaaaaaaaaafc", "aaaaaaaaaaaaaafd", "aaaaaaaaaaaaaafe",
               "aaaaaaaaaaaaaaff",
               "aaaaaaaaaaaaaafg", "aaaaaaaaaaaaaafh", "aaaaaaaaaaaaaafi", "aaaaaaaaaaaaaafj", "aaaaaaaaaaaaaafk",
               "aaaaaaaaaaaaaafl",
               "aaaaaaaaaaaaaafm", "aaaaaaaaaaaaaafn", "aaaaaaaaaaaaaafo", "aaaaaaaaaaaaaafp", "aaaaaaaaaaaaaafq",
               "aaaaaaaaaaaaaafr",
               "aaaaaaaaaaaaaafs", "aaaaaaaaaaaaaaft", "aaaaaaaaaaaaaafu", "aaaaaaaaaaaaaafv", "aaaaaaaaaaaaaafw",
               "aaaaaaaaaaaaaafx",
               "aaaaaaaaaaaaaafy", "aaaaaaaaaaaaaafz", "aaaaaaaaaaaaaaga", "aaaaaaaaaaaaaagb", "aaaaaaaaaaaaaagc",
               "aaaaaaaaaaaaaagd",
               "aaaaaaaaaaaaaage", "aaaaaaaaaaaaaagf", "aaaaaaaaaaaaaagg", "aaaaaaaaaaaaaagh", "aaaaaaaaaaaaaagi",
               "aaaaaaaaaaaaaagj",
               "aaaaaaaaaaaaaagk", "aaaaaaaaaaaaaagl", "aaaaaaaaaaaaaagm", "aaaaaaaaaaaaaagn", "aaaaaaaaaaaaaago",
               "aaaaaaaaaaaaaagp",
               "aaaaaaaaaaaaaagq", "aaaaaaaaaaaaaagr", "aaaaaaaaaaaaaags", "aaaaaaaaaaaaaagt", "aaaaaaaaaaaaaagu",
               "aaaaaaaaaaaaaagv",
               "aaaaaaaaaaaaaagw", "aaaaaaaaaaaaaagx", "aaaaaaaaaaaaaagy", "aaaaaaaaaaaaaagz", "aaaaaaaaaaaaaaha",
               "aaaaaaaaaaaaaahb",
               "aaaaaaaaaaaaaahc", "aaaaaaaaaaaaaahd", "aaaaaaaaaaaaaahe", "aaaaaaaaaaaaaahf", "aaaaaaaaaaaaaahg",
               "aaaaaaaaaaaaaahh",
               "aaaaaaaaaaaaaahi", "aaaaaaaaaaaaaahj", "aaaaaaaaaaaaaahk", "aaaaaaaaaaaaaahl", "aaaaaaaaaaaaaahm",
               "aaaaaaaaaaaaaahn",
               "aaaaaaaaaaaaaaho", "aaaaaaaaaaaaaahp", "aaaaaaaaaaaaaahq", "aaaaaaaaaaaaaahr", "aaaaaaaaaaaaaahs",
               "aaaaaaaaaaaaaaht",
               "aaaaaaaaaaaaaahu", "aaaaaaaaaaaaaahv", "aaaaaaaaaaaaaahw", "aaaaaaaaaaaaaahx", "aaaaaaaaaaaaaahy",
               "aaaaaaaaaaaaaahz",
               "aaaaaaaaaaaaaaia", "aaaaaaaaaaaaaaib", "aaaaaaaaaaaaaaic", "aaaaaaaaaaaaaaid", "aaaaaaaaaaaaaaie",
               "aaaaaaaaaaaaaaif",
               "aaaaaaaaaaaaaaig", "aaaaaaaaaaaaaaih", "aaaaaaaaaaaaaaii", "aaaaaaaaaaaaaaij", "aaaaaaaaaaaaaaik",
               "aaaaaaaaaaaaaail",
               "aaaaaaaaaaaaaaim", "aaaaaaaaaaaaaain", "aaaaaaaaaaaaaaio", "aaaaaaaaaaaaaaip", "aaaaaaaaaaaaaaiq",
               "aaaaaaaaaaaaaair",
               "aaaaaaaaaaaaaais", "aaaaaaaaaaaaaait", "aaaaaaaaaaaaaaiu", "aaaaaaaaaaaaaaiv", "aaaaaaaaaaaaaaiw",
               "aaaaaaaaaaaaaaix",
               "aaaaaaaaaaaaaaiy", "aaaaaaaaaaaaaaiz", "aaaaaaaaaaaaaaja", "aaaaaaaaaaaaaajb", "aaaaaaaaaaaaaajc",
               "aaaaaaaaaaaaaajd",
               "aaaaaaaaaaaaaaje", "aaaaaaaaaaaaaajf", "aaaaaaaaaaaaaajg", "aaaaaaaaaaaaaajh", "aaaaaaaaaaaaaaji",
               "aaaaaaaaaaaaaajj",
               "aaaaaaaaaaaaaajk", "aaaaaaaaaaaaaajl", "aaaaaaaaaaaaaajm", "aaaaaaaaaaaaaajn", "aaaaaaaaaaaaaajo",
               "aaaaaaaaaaaaaajp",
               "aaaaaaaaaaaaaajq", "aaaaaaaaaaaaaajr", "aaaaaaaaaaaaaajs", "aaaaaaaaaaaaaajt", "aaaaaaaaaaaaaaju",
               "aaaaaaaaaaaaaajv",
               "aaaaaaaaaaaaaajw", "aaaaaaaaaaaaaajx", "aaaaaaaaaaaaaajy", "aaaaaaaaaaaaaajz", "aaaaaaaaaaaaaaka",
               "aaaaaaaaaaaaaakb",
               "aaaaaaaaaaaaaakc", "aaaaaaaaaaaaaakd", "aaaaaaaaaaaaaake", "aaaaaaaaaaaaaakf", "aaaaaaaaaaaaaakg",
               "aaaaaaaaaaaaaakh",
               "aaaaaaaaaaaaaaki", "aaaaaaaaaaaaaakj", "aaaaaaaaaaaaaakk", "aaaaaaaaaaaaaakl", "aaaaaaaaaaaaaakm",
               "aaaaaaaaaaaaaakn",
               "aaaaaaaaaaaaaako", "aaaaaaaaaaaaaakp", "aaaaaaaaaaaaaakq", "aaaaaaaaaaaaaakr", "aaaaaaaaaaaaaaks",
               "aaaaaaaaaaaaaakt",
               "aaaaaaaaaaaaaaku", "aaaaaaaaaaaaaakv", "aaaaaaaaaaaaaakw", "aaaaaaaaaaaaaakx", "aaaaaaaaaaaaaaky",
               "aaaaaaaaaaaaaakz",
               "aaaaaaaaaaaaaala", "aaaaaaaaaaaaaalb", "aaaaaaaaaaaaaalc", "aaaaaaaaaaaaaald", "aaaaaaaaaaaaaale",
               "aaaaaaaaaaaaaalf",
               "aaaaaaaaaaaaaalg", "aaaaaaaaaaaaaalh", "aaaaaaaaaaaaaali", "aaaaaaaaaaaaaalj", "aaaaaaaaaaaaaalk",
               "aaaaaaaaaaaaaall",
               "aaaaaaaaaaaaaalm", "aaaaaaaaaaaaaaln", "aaaaaaaaaaaaaalo", "aaaaaaaaaaaaaalp", "aaaaaaaaaaaaaalq",
               "aaaaaaaaaaaaaalr",
               "aaaaaaaaaaaaaals", "aaaaaaaaaaaaaalt", "aaaaaaaaaaaaaalu", "aaaaaaaaaaaaaalv", "aaaaaaaaaaaaaalw",
               "aaaaaaaaaaaaaalx",
               "aaaaaaaaaaaaaaly", "aaaaaaaaaaaaaalz", "aaaaaaaaaaaaaama", "aaaaaaaaaaaaaamb", "aaaaaaaaaaaaaamc",
               "aaaaaaaaaaaaaamd",
               "aaaaaaaaaaaaaame", "aaaaaaaaaaaaaamf", "aaaaaaaaaaaaaamg", "aaaaaaaaaaaaaamh", "aaaaaaaaaaaaaami",
               "aaaaaaaaaaaaaamj",
               "aaaaaaaaaaaaaamk", "aaaaaaaaaaaaaaml", "aaaaaaaaaaaaaamm", "aaaaaaaaaaaaaamn", "aaaaaaaaaaaaaamo",
               "aaaaaaaaaaaaaamp",
               "aaaaaaaaaaaaaamq", "aaaaaaaaaaaaaamr", "aaaaaaaaaaaaaams", "aaaaaaaaaaaaaamt", "aaaaaaaaaaaaaamu",
               "aaaaaaaaaaaaaamv",
               "aaaaaaaaaaaaaamw", "aaaaaaaaaaaaaamx", "aaaaaaaaaaaaaamy", "aaaaaaaaaaaaaamz", "aaaaaaaaaaaaaana",
               "aaaaaaaaaaaaaanb",
               "aaaaaaaaaaaaaanc", "aaaaaaaaaaaaaand", "aaaaaaaaaaaaaane", "aaaaaaaaaaaaaanf", "aaaaaaaaaaaaaang",
               "aaaaaaaaaaaaaanh",
               "aaaaaaaaaaaaaani", "aaaaaaaaaaaaaanj", "aaaaaaaaaaaaaank", "aaaaaaaaaaaaaanl", "aaaaaaaaaaaaaanm",
               "aaaaaaaaaaaaaann",
               "aaaaaaaaaaaaaano", "aaaaaaaaaaaaaanp", "aaaaaaaaaaaaaanq", "aaaaaaaaaaaaaanr", "aaaaaaaaaaaaaans",
               "aaaaaaaaaaaaaant",
               "aaaaaaaaaaaaaanu", "aaaaaaaaaaaaaanv", "aaaaaaaaaaaaaanw", "aaaaaaaaaaaaaanx", "aaaaaaaaaaaaaany",
               "aaaaaaaaaaaaaanz",
               "aaaaaaaaaaaaaaoa", "aaaaaaaaaaaaaaob", "aaaaaaaaaaaaaaoc", "aaaaaaaaaaaaaaod", "aaaaaaaaaaaaaaoe",
               "aaaaaaaaaaaaaaof",
               "aaaaaaaaaaaaaaog", "aaaaaaaaaaaaaaoh", "aaaaaaaaaaaaaaoi", "aaaaaaaaaaaaaaoj", "aaaaaaaaaaaaaaok",
               "aaaaaaaaaaaaaaol",
               "aaaaaaaaaaaaaaom", "aaaaaaaaaaaaaaon", "aaaaaaaaaaaaaaoo", "aaaaaaaaaaaaaaop", "aaaaaaaaaaaaaaoq",
               "aaaaaaaaaaaaaaor",
               "aaaaaaaaaaaaaaos", "aaaaaaaaaaaaaaot", "aaaaaaaaaaaaaaou", "aaaaaaaaaaaaaaov", "aaaaaaaaaaaaaaow",
               "aaaaaaaaaaaaaaox",
               "aaaaaaaaaaaaaaoy", "aaaaaaaaaaaaaaoz", "aaaaaaaaaaaaaapa", "aaaaaaaaaaaaaapb", "aaaaaaaaaaaaaapc",
               "aaaaaaaaaaaaaapd",
               "aaaaaaaaaaaaaape", "aaaaaaaaaaaaaapf", "aaaaaaaaaaaaaapg", "aaaaaaaaaaaaaaph", "aaaaaaaaaaaaaapi",
               "aaaaaaaaaaaaaapj",
               "aaaaaaaaaaaaaapk", "aaaaaaaaaaaaaapl", "aaaaaaaaaaaaaapm", "aaaaaaaaaaaaaapn", "aaaaaaaaaaaaaapo",
               "aaaaaaaaaaaaaapp",
               "aaaaaaaaaaaaaapq", "aaaaaaaaaaaaaapr", "aaaaaaaaaaaaaaps", "aaaaaaaaaaaaaapt", "aaaaaaaaaaaaaapu",
               "aaaaaaaaaaaaaapv",
               "aaaaaaaaaaaaaapw", "aaaaaaaaaaaaaapx", "aaaaaaaaaaaaaapy", "aaaaaaaaaaaaaapz", "aaaaaaaaaaaaaaqa",
               "aaaaaaaaaaaaaaqb",
               "aaaaaaaaaaaaaaqc", "aaaaaaaaaaaaaaqd", "aaaaaaaaaaaaaaqe", "aaaaaaaaaaaaaaqf", "aaaaaaaaaaaaaaqg",
               "aaaaaaaaaaaaaaqh",
               "aaaaaaaaaaaaaaqi", "aaaaaaaaaaaaaaqj", "aaaaaaaaaaaaaaqk", "aaaaaaaaaaaaaaql", "aaaaaaaaaaaaaaqm",
               "aaaaaaaaaaaaaaqn",
               "aaaaaaaaaaaaaaqo", "aaaaaaaaaaaaaaqp", "aaaaaaaaaaaaaaqq", "aaaaaaaaaaaaaaqr", "aaaaaaaaaaaaaaqs",
               "aaaaaaaaaaaaaaqt",
               "aaaaaaaaaaaaaaqu", "aaaaaaaaaaaaaaqv", "aaaaaaaaaaaaaaqw", "aaaaaaaaaaaaaaqx", "aaaaaaaaaaaaaaqy",
               "aaaaaaaaaaaaaaqz",
               "aaaaaaaaaaaaaara", "aaaaaaaaaaaaaarb", "aaaaaaaaaaaaaarc", "aaaaaaaaaaaaaard", "aaaaaaaaaaaaaare",
               "aaaaaaaaaaaaaarf",
               "aaaaaaaaaaaaaarg", "aaaaaaaaaaaaaarh", "aaaaaaaaaaaaaari", "aaaaaaaaaaaaaarj", "aaaaaaaaaaaaaark",
               "aaaaaaaaaaaaaarl",
               "aaaaaaaaaaaaaarm", "aaaaaaaaaaaaaarn", "aaaaaaaaaaaaaaro", "aaaaaaaaaaaaaarp", "aaaaaaaaaaaaaarq",
               "aaaaaaaaaaaaaarr",
               "aaaaaaaaaaaaaars", "aaaaaaaaaaaaaart", "aaaaaaaaaaaaaaru", "aaaaaaaaaaaaaarv", "aaaaaaaaaaaaaarw",
               "aaaaaaaaaaaaaarx",
               "aaaaaaaaaaaaaary", "aaaaaaaaaaaaaarz", "aaaaaaaaaaaaaasa", "aaaaaaaaaaaaaasb", "aaaaaaaaaaaaaasc",
               "aaaaaaaaaaaaaasd",
               "aaaaaaaaaaaaaase", "aaaaaaaaaaaaaasf", "aaaaaaaaaaaaaasg", "aaaaaaaaaaaaaash", "aaaaaaaaaaaaaasi",
               "aaaaaaaaaaaaaasj",
               "aaaaaaaaaaaaaask", "aaaaaaaaaaaaaasl", "aaaaaaaaaaaaaasm", "aaaaaaaaaaaaaasn", "aaaaaaaaaaaaaaso",
               "aaaaaaaaaaaaaasp",
               "aaaaaaaaaaaaaasq", "aaaaaaaaaaaaaasr", "aaaaaaaaaaaaaass", "aaaaaaaaaaaaaast", "aaaaaaaaaaaaaasu",
               "aaaaaaaaaaaaaasv",
               "aaaaaaaaaaaaaasw", "aaaaaaaaaaaaaasx", "aaaaaaaaaaaaaasy", "aaaaaaaaaaaaaasz", "aaaaaaaaaaaaaata",
               "aaaaaaaaaaaaaatb",
               "aaaaaaaaaaaaaatc", "aaaaaaaaaaaaaatd", "aaaaaaaaaaaaaate", "aaaaaaaaaaaaaatf", "aaaaaaaaaaaaaatg",
               "aaaaaaaaaaaaaath",
               "aaaaaaaaaaaaaati", "aaaaaaaaaaaaaatj", "aaaaaaaaaaaaaatk", "aaaaaaaaaaaaaatl", "aaaaaaaaaaaaaatm",
               "aaaaaaaaaaaaaatn",
               "aaaaaaaaaaaaaato", "aaaaaaaaaaaaaatp", "aaaaaaaaaaaaaatq", "aaaaaaaaaaaaaatr", "aaaaaaaaaaaaaats",
               "aaaaaaaaaaaaaatt",
               "aaaaaaaaaaaaaatu", "aaaaaaaaaaaaaatv", "aaaaaaaaaaaaaatw", "aaaaaaaaaaaaaatx", "aaaaaaaaaaaaaaty",
               "aaaaaaaaaaaaaatz",
               "aaaaaaaaaaaaaaua", "aaaaaaaaaaaaaaub", "aaaaaaaaaaaaaauc", "aaaaaaaaaaaaaaud", "aaaaaaaaaaaaaaue",
               "aaaaaaaaaaaaaauf",
               "aaaaaaaaaaaaaaug", "aaaaaaaaaaaaaauh", "aaaaaaaaaaaaaaui", "aaaaaaaaaaaaaauj", "aaaaaaaaaaaaaauk",
               "aaaaaaaaaaaaaaul",
               "aaaaaaaaaaaaaaum", "aaaaaaaaaaaaaaun", "aaaaaaaaaaaaaauo", "aaaaaaaaaaaaaaup", "aaaaaaaaaaaaaauq",
               "aaaaaaaaaaaaaaur",
               "aaaaaaaaaaaaaaus", "aaaaaaaaaaaaaaut", "aaaaaaaaaaaaaauu", "aaaaaaaaaaaaaauv", "aaaaaaaaaaaaaauw",
               "aaaaaaaaaaaaaaux",
               "aaaaaaaaaaaaaauy", "aaaaaaaaaaaaaauz", "aaaaaaaaaaaaaava", "aaaaaaaaaaaaaavb", "aaaaaaaaaaaaaavc",
               "aaaaaaaaaaaaaavd",
               "aaaaaaaaaaaaaave", "aaaaaaaaaaaaaavf", "aaaaaaaaaaaaaavg", "aaaaaaaaaaaaaavh", "aaaaaaaaaaaaaavi",
               "aaaaaaaaaaaaaavj",
               "aaaaaaaaaaaaaavk", "aaaaaaaaaaaaaavl", "aaaaaaaaaaaaaavm", "aaaaaaaaaaaaaavn", "aaaaaaaaaaaaaavo",
               "aaaaaaaaaaaaaavp",
               "aaaaaaaaaaaaaavq", "aaaaaaaaaaaaaavr", "aaaaaaaaaaaaaavs", "aaaaaaaaaaaaaavt", "aaaaaaaaaaaaaavu",
               "aaaaaaaaaaaaaavv",
               "aaaaaaaaaaaaaavw", "aaaaaaaaaaaaaavx", "aaaaaaaaaaaaaavy", "aaaaaaaaaaaaaavz", "aaaaaaaaaaaaaawa",
               "aaaaaaaaaaaaaawb",
               "aaaaaaaaaaaaaawc", "aaaaaaaaaaaaaawd", "aaaaaaaaaaaaaawe", "aaaaaaaaaaaaaawf", "aaaaaaaaaaaaaawg",
               "aaaaaaaaaaaaaawh",
               "aaaaaaaaaaaaaawi", "aaaaaaaaaaaaaawj", "aaaaaaaaaaaaaawk", "aaaaaaaaaaaaaawl", "aaaaaaaaaaaaaawm",
               "aaaaaaaaaaaaaawn",
               "aaaaaaaaaaaaaawo", "aaaaaaaaaaaaaawp", "aaaaaaaaaaaaaawq", "aaaaaaaaaaaaaawr", "aaaaaaaaaaaaaaws",
               "aaaaaaaaaaaaaawt",
               "aaaaaaaaaaaaaawu", "aaaaaaaaaaaaaawv", "aaaaaaaaaaaaaaww", "aaaaaaaaaaaaaawx", "aaaaaaaaaaaaaawy",
               "aaaaaaaaaaaaaawz",
               "aaaaaaaaaaaaaaxa", "aaaaaaaaaaaaaaxb", "aaaaaaaaaaaaaaxc", "aaaaaaaaaaaaaaxd", "aaaaaaaaaaaaaaxe",
               "aaaaaaaaaaaaaaxf",
               "aaaaaaaaaaaaaaxg", "aaaaaaaaaaaaaaxh", "aaaaaaaaaaaaaaxi", "aaaaaaaaaaaaaaxj", "aaaaaaaaaaaaaaxk",
               "aaaaaaaaaaaaaaxl",
               "aaaaaaaaaaaaaaxm", "aaaaaaaaaaaaaaxn", "aaaaaaaaaaaaaaxo", "aaaaaaaaaaaaaaxp", "aaaaaaaaaaaaaaxq",
               "aaaaaaaaaaaaaaxr",
               "aaaaaaaaaaaaaaxs", "aaaaaaaaaaaaaaxt", "aaaaaaaaaaaaaaxu", "aaaaaaaaaaaaaaxv", "aaaaaaaaaaaaaaxw",
               "aaaaaaaaaaaaaaxx",
               "aaaaaaaaaaaaaaxy", "aaaaaaaaaaaaaaxz", "aaaaaaaaaaaaaaya", "aaaaaaaaaaaaaayb", "aaaaaaaaaaaaaayc",
               "aaaaaaaaaaaaaayd",
               "aaaaaaaaaaaaaaye", "aaaaaaaaaaaaaayf", "aaaaaaaaaaaaaayg", "aaaaaaaaaaaaaayh", "aaaaaaaaaaaaaayi",
               "aaaaaaaaaaaaaayj",
               "aaaaaaaaaaaaaayk", "aaaaaaaaaaaaaayl", "aaaaaaaaaaaaaaym", "aaaaaaaaaaaaaayn", "aaaaaaaaaaaaaayo",
               "aaaaaaaaaaaaaayp",
               "aaaaaaaaaaaaaayq", "aaaaaaaaaaaaaayr", "aaaaaaaaaaaaaays", "aaaaaaaaaaaaaayt", "aaaaaaaaaaaaaayu",
               "aaaaaaaaaaaaaayv",
               "aaaaaaaaaaaaaayw", "aaaaaaaaaaaaaayx", "aaaaaaaaaaaaaayy", "aaaaaaaaaaaaaayz", "aaaaaaaaaaaaaaza",
               "aaaaaaaaaaaaaazb",
               "aaaaaaaaaaaaaazc", "aaaaaaaaaaaaaazd", "aaaaaaaaaaaaaaze", "aaaaaaaaaaaaaazf", "aaaaaaaaaaaaaazg",
               "aaaaaaaaaaaaaazh",
               "aaaaaaaaaaaaaazi", "aaaaaaaaaaaaaazj", "aaaaaaaaaaaaaazk", "aaaaaaaaaaaaaazl", "aaaaaaaaaaaaaazm",
               "aaaaaaaaaaaaaazn",
               "aaaaaaaaaaaaaazo", "aaaaaaaaaaaaaazp", "aaaaaaaaaaaaaazq", "aaaaaaaaaaaaaazr", "aaaaaaaaaaaaaazs",
               "aaaaaaaaaaaaaazt",
               "aaaaaaaaaaaaaazu", "aaaaaaaaaaaaaazv", "aaaaaaaaaaaaaazw", "aaaaaaaaaaaaaazx", "aaaaaaaaaaaaaazy",
               "aaaaaaaaaaaaaazz",
               "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaac", "aaaaaaaaaaaaaaad", "aaaaaaaaaaaaaaae",
               "aaaaaaaaaaaaaaaf",
               "aaaaaaaaaaaaaaag", "aaaaaaaaaaaaaaah", "aaaaaaaaaaaaaaai", "aaaaaaaaaaaaaaaj", "aaaaaaaaaaaaaaak",
               "aaaaaaaaaaaaaaal",
               "aaaaaaaaaaaaaaam", "aaaaaaaaaaaaaaan", "aaaaaaaaaaaaaaao", "aaaaaaaaaaaaaaap", "aaaaaaaaaaaaaaaq",
               "aaaaaaaaaaaaaaar",
               "aaaaaaaaaaaaaaas", "aaaaaaaaaaaaaaat", "aaaaaaaaaaaaaaau", "aaaaaaaaaaaaaaav", "aaaaaaaaaaaaaaaw",
               "aaaaaaaaaaaaaaax",
               "aaaaaaaaaaaaaaay", "aaaaaaaaaaaaaaaz", "aaaaaaaaaaaaaaba", "aaaaaaaaaaaaaabb", "aaaaaaaaaaaaaabc",
               "aaaaaaaaaaaaaabd",
               "aaaaaaaaaaaaaabe", "aaaaaaaaaaaaaabf", "aaaaaaaaaaaaaabg", "aaaaaaaaaaaaaabh", "aaaaaaaaaaaaaabi",
               "aaaaaaaaaaaaaabj",
               "aaaaaaaaaaaaaabk", "aaaaaaaaaaaaaabl", "aaaaaaaaaaaaaabm", "aaaaaaaaaaaaaabn", "aaaaaaaaaaaaaabo",
               "aaaaaaaaaaaaaabp",
               "aaaaaaaaaaaaaabq", "aaaaaaaaaaaaaabr", "aaaaaaaaaaaaaabs", "aaaaaaaaaaaaaabt", "aaaaaaaaaaaaaabu",
               "aaaaaaaaaaaaaabv",
               "aaaaaaaaaaaaaabw", "aaaaaaaaaaaaaabx", "aaaaaaaaaaaaaaby", "aaaaaaaaaaaaaabz", "aaaaaaaaaaaaaaca",
               "aaaaaaaaaaaaaacb",
               "aaaaaaaaaaaaaacc", "aaaaaaaaaaaaaacd", "aaaaaaaaaaaaaace", "aaaaaaaaaaaaaacf", "aaaaaaaaaaaaaacg",
               "aaaaaaaaaaaaaach",
               "aaaaaaaaaaaaaaci", "aaaaaaaaaaaaaacj", "aaaaaaaaaaaaaack", "aaaaaaaaaaaaaacl", "aaaaaaaaaaaaaacm",
               "aaaaaaaaaaaaaacn",
               "aaaaaaaaaaaaaaco", "aaaaaaaaaaaaaacp", "aaaaaaaaaaaaaacq", "aaaaaaaaaaaaaacr", "aaaaaaaaaaaaaacs",
               "aaaaaaaaaaaaaact",
               "aaaaaaaaaaaaaacu", "aaaaaaaaaaaaaacv", "aaaaaaaaaaaaaacw", "aaaaaaaaaaaaaacx", "aaaaaaaaaaaaaacy",
               "aaaaaaaaaaaaaacz",
               "aaaaaaaaaaaaaada", "aaaaaaaaaaaaaadb", "aaaaaaaaaaaaaadc", "aaaaaaaaaaaaaadd", "aaaaaaaaaaaaaade",
               "aaaaaaaaaaaaaadf",
               "aaaaaaaaaaaaaadg", "aaaaaaaaaaaaaadh", "aaaaaaaaaaaaaadi", "aaaaaaaaaaaaaadj", "aaaaaaaaaaaaaadk",
               "aaaaaaaaaaaaaadl",
               "aaaaaaaaaaaaaadm", "aaaaaaaaaaaaaadn", "aaaaaaaaaaaaaado", "aaaaaaaaaaaaaadp", "aaaaaaaaaaaaaadq",
               "aaaaaaaaaaaaaadr",
               "aaaaaaaaaaaaaads", "aaaaaaaaaaaaaadt", "aaaaaaaaaaaaaadu", "aaaaaaaaaaaaaadv", "aaaaaaaaaaaaaadw",
               "aaaaaaaaaaaaaadx",
               "aaaaaaaaaaaaaady", "aaaaaaaaaaaaaadz", "aaaaaaaaaaaaaaea", "aaaaaaaaaaaaaaeb", "aaaaaaaaaaaaaaec",
               "aaaaaaaaaaaaaaed",
               "aaaaaaaaaaaaaaee", "aaaaaaaaaaaaaaef", "aaaaaaaaaaaaaaeg", "aaaaaaaaaaaaaaeh", "aaaaaaaaaaaaaaei",
               "aaaaaaaaaaaaaaej",
               "aaaaaaaaaaaaaaek", "aaaaaaaaaaaaaael", "aaaaaaaaaaaaaaem", "aaaaaaaaaaaaaaen", "aaaaaaaaaaaaaaeo",
               "aaaaaaaaaaaaaaep",
               "aaaaaaaaaaaaaaeq", "aaaaaaaaaaaaaaer", "aaaaaaaaaaaaaaes", "aaaaaaaaaaaaaaet", "aaaaaaaaaaaaaaeu",
               "aaaaaaaaaaaaaaev",
               "aaaaaaaaaaaaaaew", "aaaaaaaaaaaaaaex", "aaaaaaaaaaaaaaey", "aaaaaaaaaaaaaaez", "aaaaaaaaaaaaaafa",
               "aaaaaaaaaaaaaafb",
               "aaaaaaaaaaaaaafc", "aaaaaaaaaaaaaafd", "aaaaaaaaaaaaaafe", "aaaaaaaaaaaaaaff", "aaaaaaaaaaaaaafg",
               "aaaaaaaaaaaaaafh",
               "aaaaaaaaaaaaaafi", "aaaaaaaaaaaaaafj", "aaaaaaaaaaaaaafk", "aaaaaaaaaaaaaafl", "aaaaaaaaaaaaaafm",
               "aaaaaaaaaaaaaafn",
               "aaaaaaaaaaaaaafo", "aaaaaaaaaaaaaafp", "aaaaaaaaaaaaaafq", "aaaaaaaaaaaaaafr", "aaaaaaaaaaaaaafs",
               "aaaaaaaaaaaaaaft",
               "aaaaaaaaaaaaaafu", "aaaaaaaaaaaaaafv", "aaaaaaaaaaaaaafw", "aaaaaaaaaaaaaafx", "aaaaaaaaaaaaaafy",
               "aaaaaaaaaaaaaafz",
               "aaaaaaaaaaaaaaga", "aaaaaaaaaaaaaagb", "aaaaaaaaaaaaaagc", "aaaaaaaaaaaaaagd", "aaaaaaaaaaaaaage",
               "aaaaaaaaaaaaaagf",
               "aaaaaaaaaaaaaagg", "aaaaaaaaaaaaaagh", "aaaaaaaaaaaaaagi", "aaaaaaaaaaaaaagj", "aaaaaaaaaaaaaagk",
               "aaaaaaaaaaaaaagl",
               "aaaaaaaaaaaaaagm", "aaaaaaaaaaaaaagn", "aaaaaaaaaaaaaago", "aaaaaaaaaaaaaagp", "aaaaaaaaaaaaaagq",
               "aaaaaaaaaaaaaagr",
               "aaaaaaaaaaaaaags", "aaaaaaaaaaaaaagt", "aaaaaaaaaaaaaagu", "aaaaaaaaaaaaaagv", "aaaaaaaaaaaaaagw",
               "aaaaaaaaaaaaaagx",
               "aaaaaaaaaaaaaagy", "aaaaaaaaaaaaaagz", "aaaaaaaaaaaaaaha", "aaaaaaaaaaaaaahb", "aaaaaaaaaaaaaahc",
               "aaaaaaaaaaaaaahd",
               "aaaaaaaaaaaaaahe", "aaaaaaaaaaaaaahf", "aaaaaaaaaaaaaahg", "aaaaaaaaaaaaaahh", "aaaaaaaaaaaaaahi",
               "aaaaaaaaaaaaaahj",
               "aaaaaaaaaaaaaahk", "aaaaaaaaaaaaaahl", "aaaaaaaaaaaaaahm", "aaaaaaaaaaaaaahn", "aaaaaaaaaaaaaaho",
               "aaaaaaaaaaaaaahp",
               "aaaaaaaaaaaaaahq", "aaaaaaaaaaaaaahr", "aaaaaaaaaaaaaahs", "aaaaaaaaaaaaaaht", "aaaaaaaaaaaaaahu",
               "aaaaaaaaaaaaaahv",
               "aaaaaaaaaaaaaahw", "aaaaaaaaaaaaaahx", "aaaaaaaaaaaaaahy", "aaaaaaaaaaaaaahz", "aaaaaaaaaaaaaaia",
               "aaaaaaaaaaaaaaib",
               "aaaaaaaaaaaaaaic", "aaaaaaaaaaaaaaid", "aaaaaaaaaaaaaaie", "aaaaaaaaaaaaaaif", "aaaaaaaaaaaaaaig",
               "aaaaaaaaaaaaaaih",
               "aaaaaaaaaaaaaaii", "aaaaaaaaaaaaaaij", "aaaaaaaaaaaaaaik", "aaaaaaaaaaaaaail", "aaaaaaaaaaaaaaim",
               "aaaaaaaaaaaaaain",
               "aaaaaaaaaaaaaaio", "aaaaaaaaaaaaaaip", "aaaaaaaaaaaaaaiq", "aaaaaaaaaaaaaair", "aaaaaaaaaaaaaais",
               "aaaaaaaaaaaaaait",
               "aaaaaaaaaaaaaaiu", "aaaaaaaaaaaaaaiv", "aaaaaaaaaaaaaaiw", "aaaaaaaaaaaaaaix", "aaaaaaaaaaaaaaiy",
               "aaaaaaaaaaaaaaiz",
               "aaaaaaaaaaaaaaja", "aaaaaaaaaaaaaajb", "aaaaaaaaaaaaaajc", "aaaaaaaaaaaaaajd", "aaaaaaaaaaaaaaje",
               "aaaaaaaaaaaaaajf",
               "aaaaaaaaaaaaaajg", "aaaaaaaaaaaaaajh", "aaaaaaaaaaaaaaji", "aaaaaaaaaaaaaajj", "aaaaaaaaaaaaaajk",
               "aaaaaaaaaaaaaajl",
               "aaaaaaaaaaaaaajm", "aaaaaaaaaaaaaajn", "aaaaaaaaaaaaaajo", "aaaaaaaaaaaaaajp", "aaaaaaaaaaaaaajq",
               "aaaaaaaaaaaaaajr",
               "aaaaaaaaaaaaaajs", "aaaaaaaaaaaaaajt", "aaaaaaaaaaaaaaju", "aaaaaaaaaaaaaajv", "aaaaaaaaaaaaaajw",
               "aaaaaaaaaaaaaajx",
               "aaaaaaaaaaaaaajy", "aaaaaaaaaaaaaajz", "aaaaaaaaaaaaaaka", "aaaaaaaaaaaaaakb", "aaaaaaaaaaaaaakc",
               "aaaaaaaaaaaaaakd",
               "aaaaaaaaaaaaaake", "aaaaaaaaaaaaaakf", "aaaaaaaaaaaaaakg", "aaaaaaaaaaaaaakh", "aaaaaaaaaaaaaaki",
               "aaaaaaaaaaaaaakj",
               "aaaaaaaaaaaaaakk", "aaaaaaaaaaaaaakl", "aaaaaaaaaaaaaakm", "aaaaaaaaaaaaaakn", "aaaaaaaaaaaaaako",
               "aaaaaaaaaaaaaakp",
               "aaaaaaaaaaaaaakq", "aaaaaaaaaaaaaakr", "aaaaaaaaaaaaaaks", "aaaaaaaaaaaaaakt", "aaaaaaaaaaaaaaku",
               "aaaaaaaaaaaaaakv",
               "aaaaaaaaaaaaaakw", "aaaaaaaaaaaaaakx", "aaaaaaaaaaaaaaky", "aaaaaaaaaaaaaakz", "aaaaaaaaaaaaaala",
               "aaaaaaaaaaaaaalb",
               "aaaaaaaaaaaaaalc", "aaaaaaaaaaaaaald", "aaaaaaaaaaaaaale", "aaaaaaaaaaaaaalf", "aaaaaaaaaaaaaalg",
               "aaaaaaaaaaaaaalh",
               "aaaaaaaaaaaaaali", "aaaaaaaaaaaaaalj", "aaaaaaaaaaaaaalk", "aaaaaaaaaaaaaall"]

a = datetime.now()
for word in words_large:
    print(Solution().findPathes(board_large, word))
b = datetime.now()

print("cost time:")
print((b - a).seconds)
