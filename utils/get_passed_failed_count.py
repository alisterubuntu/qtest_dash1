from qtest import qtest

qtest = qtest.QTestClient(username="patonab127@iconzap.com", password="qtest123", site_name="iconzap")
all_projects = qtest.get_projects()
project_names = [project['name'] for project in all_projects]
print(project_names)
get_test_runs = qtest.get_test_runs(project_id=127079,parent_id=5420572,parent_type='test-suite',expand=None, page=1, page_size=100)
print(f"Total Test Cases {get_test_runs['total']}")
total_testcases = get_test_runs['total']
for i in range(total_testcases):
    print(get_test_runs['items'][i]['latest_test_log']['status'])

#print(get_test_runs)