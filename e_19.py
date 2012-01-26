#!/usr/bin/env python
"""
 ##---
 # jlengrand
 #Created on : Thu Jan 19 10:12:06 CET 2012
 #
 # DESCRIPTION : Solves problem 19 of Project Euler
 You are given the following information, but you may prefer to do some research for yourself.

 1 Jan 1900 was a Monday.
 Thirty days has September,
 April, June and November.
 All the rest have thirty-one,
 Saving February alone,
 Which has twenty-eight, rain or shine.
 And on leap years, twenty-nine.
 A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
 How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
 ##---
"""
class Date:
    """
    Date object.
    Should be initiated with a given year, month and day.
    Designed to output the value of the day for a given date.

    Should not be used for dates before 1 Jan 1900
    Month : 1 to 12, should be an int
    Day : 1 to 31, should be an int
    """
    def __init__(self, year, month, day):
        """
        Only values needed are day, month and year
        """
        self.year = year
        self.month = month
        self.day = day

    def days_in_month(self):
        """
        Calculates the number of days in the current month
        """
        if self.month in [4, 6, 9, 11]:
            return 30
        elif self.month is 2:
            if self.is_leap_year():
                return 29
            else:
               return 28
        else:
            return 31

    def _is_end_year(self):
        """
        Checks whether this is the end of the current year.
        Simply checks if we are the 31 December
        """
        if (self.month == 12) and (self.day == 31):
            return True
        else:
            return False

    def is_leap_year(self):
        """
        Returns true or false depending if this year is a leap year or not.
        """
        if self.year % 100 == 0: # we are i a century
            if self.year % 400 == 0: #special century
                return True
            else:
                return False
        elif self.year % 4 == 0: # evenly divisible by 4
            return True
        else:
            return False

    def add_day(self):
        """
        Adds one day to the current Date.
        """
        if ((self.day + 1) > self.days_in_month()):
            self.day = 1
            if (self.month + 1) > 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1

    def __repr__(self):
        """
        Nice display for Date Object
        """
        return "%d/%d/%d" % (self.day, self.month, self.year)

    def __eq__(self, other_date):
        """
        Allows to check if two dates are the same day
        """
        if (self.day == other_date.day) and (self.month == other_date.month)  and (self.year == other_date.year):
                return True
        else:
            return False

def ptr_from_start(start_date):
    """
    Returns the pointer of day for start_date
    """
    #global ref_date
    #global ref_day
    #global days
    ref_date = Date(1900, 1, 1)
    ref_day = "monday"
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    day_ptr = days.index(ref_day) # We start from the reference
    temp_date = ref_date # We suppose the reference is anterior to start_date

    while not(temp_date == start_date):
            temp_date.add_day()
            curr_day = days[day_ptr]
            day_ptr = (day_ptr + 1 ) % len(days)

    return day_ptr

def days_in_period(string_day, nbr_day, start_date, end_date):
    """
    Returns the number of string_day that are the nbr_day of the month between
    start_date and end_date

    WARNING : No checks are made in any way ! Reference is ugly
    """
    #global ref_date
    #global ref_day
    #global days
    ref_date = Date(1900, 1, 1)
    ref_day = "monday"
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    day_ptr = ptr_from_start(start_date)

    curr_date = start_date
    end_ptr = 0

    while not (curr_date == end_date):
        curr_day = days[day_ptr]

        if (curr_day == string_day) and (curr_date.day == nbr_day):
            end_ptr += 1

        day_ptr = (day_ptr + 1 ) % len(days)        
        curr_date.add_day()

    return end_ptr

if __name__ == '__main__' :
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    start_date = Date(1901, 1, 1)
    end_date = Date(2000, 12, 31)
    print "Answer is : %d" %(days_in_period("sunday", 1, start_date, end_date))
    raw_input() # USed to keep Windows terminal open
