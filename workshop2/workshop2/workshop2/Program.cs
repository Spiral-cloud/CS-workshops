using System.Security.Cryptography;

internal class Program
{
    private static void Main(string[] args)
    {
        //int number = 1; //An integer that is used when you need to do calculations using a number that do not involve decimal places
        //double pi = 3.14; // A number that can have multiple decimal places for when a more precise value is needed
        //decimal prices = 11.50m; // This data type is commonly used to represent prices. It must have the m or there will be an error 
        //char last_Initial = 'T'; // A variable that can only hold one character. Could be used for initials.
        //string course = "Foundations of programming"; //A string capable of storing characters. Calculationcause an error 
        //bool student = true; // A Boolean logic variable that can only hold the value true or false in lowercase
        //Console.Write($"Count: {number} \n pi: {pi} \n Price: £{prices} \n Initial: {last_Initial} \n Course {course} \n Student: {student}" );

        //Console.Write("Enter your full name: ");
        //string full_name = Console.ReadLine();
        //Console.Write("Enter your age: ");
        //int age = Convert.ToInt32(Console.ReadLine());
        //Console.Write("Are you a student, please input true or false: ");
        //bool student_status = bool.Parse(Console.ReadLine());
        //Console.Write("What is the price of your ticket: ");
        //decimal ticket_price = decimal.Parse(Console.ReadLine());
        //Console.WriteLine($"Name: \t\t{full_name}\n Age: \t\t{age}\n Student: \t{student_status}\n Price: \t£{ticket_price:F2}");
        //Console.WriteLine($"Name: {full_name} | Age: {age} | Student: {student_status} | Price {ticket_price:f2} ");

        //string item = "Guidebook";
        //decimal price = 10.00m;
        //string message = "Thanks for your purchase";
        //var current_directory = Directory.GetCurrentDirectory();
        //Console.WriteLine($"===  Museum Shop Receipt  === \n Item: \t{item}\n Price: \t\u00A3{price}\n Messgae: \t{message}\n Path: \t{current_directory} ");

        // Buggy program: fix me!
        //Console.WriteLine("=== Ticket ===");
        //string name = "Alex";
        //decimal price = 12.50m;
        //Console.Write("Student (true/false): ");
        //bool isStudent = bool.Parse(Console.ReadLine());
        //Console.WriteLine($"Name: {name}\nPrice: £{price:F2}\nStudent: {isStudent}");

        Console.Write("Enter your full name: ");
        string name = Console.ReadLine();
        Console.Write("Enter your age: ");
        int age = Convert.ToInt32(Console.ReadLine());
        Console.Write("Are you a student, please enter true or false: ");
        bool student = bool.Parse(Console.ReadLine());
        Console.Write("Enter the price of your ticket: ");
        decimal ticket_price = decimal.Parse(Console.ReadLine());
        string ID = "LINC-2025-0001";
        var date = DateTime.Now;
        DateTime date_part_only = date.Date;
        string date_only = date.ToString("dd/MM/yyyy");
        Console.WriteLine($"=== National Museum Ticket ===\n ID: \t\t{ID}\n Date: \t\t{date_only}\n Name: \t\t{name}\n Age: \t\t{age}\n Student: \t{student}\n Price: \t{ticket_price}");




        
    }
}