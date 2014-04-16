
#from model.course import Course
#from model.course_run import CourseRun

#from dataanalysis.cal_avg import *
#import dataanalysis.cal_avg_importTest
import dataanalysis.cal_avg

# 1) func for avg of course run
# 2) func for avg of course
# 3) func for avg of department


#def main():
#    #Course = ...
#    course_run = CourseRun(
#            year = 2006,
#            semester = 'Sommer',
#            students_registered = 0,
#            students_attended = 0,
#            students_passed = 0,
#            not_shown = 0,
#            sick = 0,
#            grade_scale = {'12' : 8,
#               '10' : 27,
#               '7' : 70,
#               '4' : 19,
#               '02' : 12,
#               '00' : 9,
#               '-3' : 4})
#    course_run_avg(course_run)

if __name__ == "__main__":
    dataanalysis.cal_avg.main()
    #main()
    print 'Note: we are in main.py if __name__ == "__main__"'
        

