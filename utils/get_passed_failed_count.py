from qtest import qtest
from collections import Counter

qtest = qtest.QTestClient(username="patonab127@iconzap.com", password="qtest123", site_name="iconzap")
all_projects = qtest.get_projects()
project_names = [project['name'] for project in all_projects]
print(project_names)
get_test_runs = qtest.get_test_runs(project_id=127079,parent_id=5420572,parent_type='test-suite',expand=None, page=1, page_size=100)
print(f"Total Test Cases {get_test_runs['total']}")
total_testcases = get_test_runs['total']
total_passed = 0
total_failed = 0
total_incomplete = 0

for i in range(total_testcases):
    if get_test_runs['items'][i]['latest_test_log']['status'] == 'Passed':
       total_passed = total_passed + 1
    elif get_test_runs['items'][i]['latest_test_log']['status'] == 'Failed':
       total_failed = total_failed + 1
    elif get_test_runs['items'][i]['latest_test_log']['status'] == 'Incomplete':
        total_incomplete = total_incomplete + 1

print(f"passed ={total_passed} , Failed = {total_failed}, In complete ={total_incomplete}".format(total_passed,total_failed,total_incomplete))
#print(get_test_runs)