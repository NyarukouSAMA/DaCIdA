import sys
from aste.processor import ASTEInterface
import sqlite3 as lite


class SysHandlerAnalyser(ASTEInterface):

    def withdraw(self):
        return sys.getwindowsversion()

    def analise(self):
        pass


if __name__ == '__main__':
    con = lite.connect('../aste/database/ASTE.db')
    cur = con.cursor()
    sys_handler_info = SysHandlerAnalyser(cur, 1, 1)
    print(sys_handler_info.get_withdraw_data(), sep='\n')