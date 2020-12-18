#ifndef STUDENT_H
#define STUDENT_H

#include <iostream>

class Student{
    public:
        long id{};
        double avg{};
        size_t units{50};
        Student() = default;
        Student(long _id, double _avg, size_t _units);
        friend std::ostream& operator<<( std::ostream& os, const Student& st );
};

#endif