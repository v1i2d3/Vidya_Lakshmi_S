


importjava.util.Arraylist;
importjava.util.Collections;
importjava.util.Comparator;
importjava.util.list;

//Define a student class to represent a student
class student{
  string name;
  string rollnumber;
double cgpa

public student(string name,string rollnumber,double cgpa) {
  this.name=name;
this.rollnumber=rollnumber;
this.cgpa=cgpa;
}
}
public class main {
  //comparator to compare students based on CGPA in descending Order
static class CGPAcomparator implements comparator<student>{
  @override
public int compare(student student1, student student2){
  //sort in descending order of CGPA
  return Double.compare(student2.cgpa, student1.cgpa);
}
}
//Function to sort a list of student objects based on CGPA in descending Order
static void sortstudents(list<student>
students)}
//Use the CGPAcomparator to sort the list
collections.sort(student,new CGPcomparator();
}
public static void main(string[] args) {
  //create a list of student objects
  list<student>students=new
Arraylist<>();
students.add(new student("Alice","A123", 3.8));
students.add(new student("Bob","B456", 3.5));
students.add(new student("charlie","C789",3.9));
students.add(new student("David","D101",3.2));
students.add(new student("Eve","E202",4.0));
//sort the list of student based on CGPA sortstudents(students);
//print the sorted list
system.out.println("Sorted list of students by CGPA(Descenting order):");
for(student student:students){
  system.out.println("Name:"+student.name+",rollnumber:"+student.rollnumber+",CGPA:"+student.cgpa);
}
}
}
                    








