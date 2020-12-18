#include "student.h"

Student::Student(long _id, double _avg, size_t _units){
    id = _id;
    avg = _avg;
    units = _units;
}

std::ostream& operator<<(std::ostream& os, const Student& s)
{
    os << s.id;
    return os;
}