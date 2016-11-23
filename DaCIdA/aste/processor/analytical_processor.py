"""
Необходимо доработать:
1. Обработку исключений!!!
2. Интерфейс сравнения
"""

from abc import ABCMeta, abstractmethod

_KEYS_TABLE_TEMPLATE = """
SELECT mi.key_search_tables FROM module_info as mi
WHERE mi.module_id = {0}
"""

_BENCHMARKS_TABLE_TEMPLATE = """
SELECT mi.benchmark_comparison_tables FROM module_info as mi
WHERE mi.module_id = {0}
"""

_GET_DATA_FROM_T_TEMPL = """
SELECT tn.* FROM {0} as tn
WHERE tn.module_id = {1}
"""

class ASTEInterface(metaclass=ABCMeta):

    def __init__(self, cur, test_id, module_id):
        self.cur = cur
        self.module_id = module_id
        self.__key_table_name = self._get_query(_KEYS_TABLE_TEMPLATE, self.module_id)[0]

        if self.__key_table_name:
            self.list_of_keys_data = list(self._get_query(_GET_DATA_FROM_T_TEMPL, self.__key_table_name, self.module_id))

        self.__benchmarks_table_name = self._get_query(_BENCHMARKS_TABLE_TEMPLATE, self.module_id)[0]
        if self.__benchmarks_table_name:
            self.list_of_standards_data = list(self._get_query(_GET_DATA_FROM_T_TEMPL, self.__benchmarks_table_name, self.module_id))
        self._withdraw_data = self.withdraw()

    def get_withdraw_data(self):
        return self._withdraw_data

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def analise(self):
        pass

    def _get_query(self, template, *data):
        _query = template.format(*data)
        self.cur.execute(_query)
        return self.cur.fetchone()


if __name__ == '__main__':
    pass