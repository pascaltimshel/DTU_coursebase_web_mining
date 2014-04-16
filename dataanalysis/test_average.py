# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:36:04 2013

@author: pascal
"""


import unittest
from model.course import Course
from model.course_run import CourseRun

class AverageTest(unittest.TestCase):
    BIO_DEP = Department(code = 27, title_en = 'Department of Systems Biology', title_da = 'Institut for Systembiologi')    
    
    EXPECTED_COURSE_RUNS = [
        CourseRun(
            year = 2009,
            semester = 'Vinter',
            students_registered = 0,
            students_attended = 0,
            students_passed = 0,
            not_shown = 22,
            sick = 1,
            grade_scale = {'12' : 8,
                           '10' : 27,
                           '7' : 70,
                           '4' : 19,
                           '02' : 12,
                           '00' : 9,
                           '-3' : 4}
        ),
        CourseRun(
            year = 2006,
            semester = 'Sommer',
            students_registered = 0,
            students_attended = 0,
            students_passed = 0,
            not_shown = 0,
            sick = 0,
            grade_scale = {}
        )]

    EXPECTED_COURSES = Course(
            code = '27002',
            language = 'Danish',
            title_en = 'Life Science',
            title_da = 'Biovidenskab',
            evaluation_type = '7 step scale',
            ects_credits = 5,
            course_type = 'BSc',
            course_runs = EXPECTED_COURSE_RUNS)
    

    #test_object = JSONDecoder()

    def test_average_for_real_course_run(self):
        expected_avg = 5.8
        self.assertEquals(expected_avg, )
    
    def test_average_for_empty_course_run(self):
        pass



if __name__ == '__main__':
    unittest.main()

# 1) Load courses
# 2) 

