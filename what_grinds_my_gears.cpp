#include <iostream>

class Parent
{
    public:
        virtual void function() = 0;
};

class Child : public Parent
{
    public:
        void function()
        {
            std::cout << "This is the Child class!" << std::endl;
        }
};

class Uncle : public Parent
{
    public:
        void function()
        {
            std::cout << "This is the Uncle class!" << std::endl;
        }
};

void call_function(Parent& demo_class)
{
    demo_class.function();
}

int main(int argc, char* argv[])
{
    Child child_obj;
    Uncle uncle_obj;
    call_function(child_obj);
    call_function(uncle_obj);
    return 0;
}