from qtest import qtest

qtest = qtest.QTestClient(username="patonab127@iconzap.com", password="qtest123", site_name="iconzap")
all_projects = qtest.get_projects()
project_names = [project['name'] for project in all_projects]
print(project_names)
get_test_runs = qtest.get_test_runs(project_id=127079,parent_id=5420572,parent_type='test-suite',expand=None, page=1, page_size=100)
print(get_test_runs)