# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:50:17 2013

@author: pascal
"""



#if __name__ == "__main__" and __package__ is None:
#    #__package__ = "expected.package.name"
#    __package__ = "Python-project-Pascal.dataanalysis.cal_avg"
#    from .model.course import Course
#    from .model.course_run import CourseRun
#    main()
#else:
#    from model.course import Course
#    from model.course_run import CourseRun


#from model.course import Course
#from model.course_run import CourseRun


def course_run_avg(course_run):
    #print course_run.grade_scale
    #print course_run.semester
    #print course_run.year
    #print "hey"
    
    for (grade, count) in course_run.grade_scale.items():
        print grade, count
# rembemer to convert keys to int.



# 1) func for avg of course run
# 2) func for avg of course
# 3) func for avg of department

#

def main():
    #Course = ...
    course_run = CourseRun(
            year = 2006,
            semester = 'Sommer',
            students_registered = 0,
            students_attended = 0,
            students_passed = 0,
            not_shown = 0,
            sick = 0,
            grade_scale = {'12' : 8,
               '10' : 27,
               '7' : 70,
               '4' : 19,
               '02' : 12,
               '00' : 9,
               '-3' : 4})
    course_run_avg(course_run)

#if __name__ == "__main__":
 #       main()


if __name__ == "__main__" and __package__ is None:
    import sys, os
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print parent_dir
    sys.path.insert(0, parent_dir)
    # Why is not needed!?
    #import dataanalysis
    #__package__ = str("dataanalysis")
    
    # THis does not work?
    #import dataanalysis.cal_avg
    #__package__ = "Python-project-Pascal.dataanalysis.cal_avg"
    
    from model.course import Course # NOT NEEDED FOR NOW
    from model.course_run import CourseRun
    del sys, os
    #main()
else: # THis else statement is executed if main.py imports this module by: import dataanalysis.cal_avg
    # main.py have not importet Course or CourseRun, so this WORKS
    from model.course import Course
    from model.course_run import CourseRun
    main()

#main()