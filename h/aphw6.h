#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <iterator>
#include <algorithm>
#include "student.h"

template <class O, class I>
O convert(I d);

template <class T>
void show(T d);

template <class T>
Student findRank(T d, int n);

template <class T>
T getRanks(T d);

template <class T>
T getInterns(T d);

#include "aphw6.hpp"