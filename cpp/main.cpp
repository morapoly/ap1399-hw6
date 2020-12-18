#include "aphw6.h"
#include "gtest/gtest.h"

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    std::cout << "RUNNING TESTS ..." << std::endl;
    int ret{RUN_ALL_TESTS()};
    if (!ret)
        std::cout << "<<<SUCCESS>>>" << std::endl;
    else
        std::cout << "FAILED" << std::endl;
    
    // Student s1 {9423013, 18.2, 26};
    // Student s2 {9423037, 19.2, 30};
    // Student s3 {9423091, 19.1, 10};
    // std::deque<Student> d {s1, s2, s3};
    // std::vector<Student> v {convert<std::vector<Student>>(d)};
    // std::list<Student> l {convert<std::list<Student>>(d)};

    return 0;
}
