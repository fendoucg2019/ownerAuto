#coding=utf-8
import unittest
from airtest.core.api import *
from BeautifulReport import BeautifulReport
def case_all():
    print('开始调用例进行测试')
    # testcase_dir=os.path.join(os.getcwd(),'../TestCase')
    testcase_dir="../TestCases/"
    discovery=unittest.defaultTestLoader.discover(testcase_dir,pattern='*.py',top_level_dir=None)
    return discovery
#HTMLTestRunner测试报告
# if __name__=="__main__":
#     report=open("../run_report/1.html",'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=report,title=u'2D游戏测试报告',description=u'2D测试用例结果情况',tester=u'2D测试组')
    # runner=unittest.TextTestRunner()
    # runner.run(case_all())
    # result = BeautifulReport(case_all())
    # result.report(filename='测试',description='测试deafult报告',log_path='')
#BeautifulReport测试报告
if __name__ == '__main__':
    # test_suite = unittest.defaultTestLoader.discover('../othermobile', pattern='*.py')
    result = BeautifulReport(case_all())
    result.report(filename='2D测试报告', description='2D测试报告', log_path='../run_report')