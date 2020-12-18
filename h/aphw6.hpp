template <class O, class I>
O convert(I d){
    return O(d.begin(), d.end());
}

template <class T>
void show(T d){
    auto osi = std::ostream_iterator<Student>(std::cout," "); // using os_it to iterate between elements cout
    std::copy(d.begin(), d.end(), osi);
    std::cout << std::endl;
}

template <class T>
Student findRank(T d, int n){
    std::vector<Student> temp = convert<std::vector<Student>>(d); // convert to vector for using in sort
    std::sort(temp.begin(), temp.end(), []( Student s1, Student s2) { return s1.avg < s2.avg;}); // sort increasing using lambda func
    return temp[temp.size() - n]; // return the n'th rank student
}

template <class T>
T getRanks(T d){
    std::vector<Student> temp = convert<std::vector<Student>>(d);
    std::sort(temp.begin(), temp.end(), []( Student s1, Student s2) { return s1.avg > s2.avg;}); // sort decreasing
    return convert<T>(temp); // convert to input type
}

template <class T>
T getInterns(T d){
    std::vector<Student> temp = convert<std::vector<Student>>(d);
    std::sort(temp.begin(), temp.end(), []( Student s1, Student s2) { return s1.units > s2.units;); // sort decreasing
    return convert<T>(temp);;
}