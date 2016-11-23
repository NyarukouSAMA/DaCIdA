import sqlite3 as lite

_GET_TASK_TEMPLATE = """
SELECT ti.test_id
FROM test_info as ti
WHERE ti.check_id = {0}
"""

_GET_TEST_INIT_TEMPLATE = """
SELECT mi.module_id,
       mi.code_string
FROM module_info mi, test_info ti
WHERE mi.module_id = ti.module_id AND
      ti.test_id {0} {1}
"""

class ASTEManager():
    def __init__(self, task):
        self.con = lite.connect('database/ASTE.db')
        self.cur = self.con.cursor()
        self._test_tuple = tuple(i[0] for i in self._get_query(_GET_TASK_TEMPLATE, task))
        if len(self._test_tuple) <= 1:
            self._test_tuple = self._test_tuple[0]
            self._init_tuples = [i for i in self._get_query(_GET_TEST_INIT_TEMPLATE, '=', self._test_tuple)]
        else:
            self._init_tuples = [i for i in self._get_query(_GET_TEST_INIT_TEMPLATE, 'in', self._test_tuple)]
        self._init_dict = zip(self._test_tuple, self._init_tuples)
        self._execute()

    def _execute(self):
        for package_tuple in self._init_dict:
            name_components = package_tuple[1][1].split('.')
            test_construct = __import__(name_components[0])
            for com in name_components[1:]:
                test_construct = getattr(test_construct, com)
            con = lite.connect('database/ASTE.db')
            cur = con.cursor()
            test_object = test_construct(cur, package_tuple[0], package_tuple[1][0])  # !!!!!!!!!!!!!! IMPORTANT CODE
            # From this moment program cap, for check how manager works with functional modules
            # During under development!
            print('Test with id = {0} and init code {1} withdraw returns from system next data:\n{2}\n'.format(
                package_tuple[0], package_tuple[1][1], test_object.get_withdraw_data())
            )
            con.close()


    def _get_query(self, template, *data):
        _query = template.format(*data)
        self.cur.execute(_query)
        return self.cur.fetchall()


if __name__ == '__main__':
    ASTEManager(1)