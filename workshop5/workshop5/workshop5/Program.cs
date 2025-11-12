using System.ComponentModel.DataAnnotations;
using System.Diagnostics.Metrics;
using System.Globalization;
using System.Xml.Serialization;


internal class Program
{
    private static void Main(string[] args)
    {
        // int counter = 1;
        // while (counter <= 5)
        // {
        //     Console.WriteLine(counter);
        //     counter++;
        // }
        // Console.WriteLine("Widget Quantity \t Price");
        // for (int counter = 10; counter <= 100; counter += 10)
        // {
        //     if (counter > 50)
        //     {
        //         Console.WriteLine($"{counter} \t\t\t £{counter * 4} ");
        //     }
        //     else if (counter > 80)
        //     {
        //         Console.WriteLine($"{counter} \t\t\t £{counter * 2.50} ");
        //     }
        //     else
        //     {
        //         Console.WriteLine($"{counter} \t\t\t £{counter * 5} ");
        //     }
        // }
        // int counter2 = 1;
        // Console.Write("Do you want to make another calculation? y/n ");
        // char widget_again = char.Parse(Console.ReadLine()!);
        // Console.Write("Input the number you want to calculate to: ");
        // int widget_amount = int.Parse(Console.ReadLine()!);
        // Console.WriteLine("Widget Quantity \t Price");
        // do
        // {
        //     if (widget_amount > 50)
        //     {
        //         Console.WriteLine($"{widget_amount} \t\t\t £{widget_amount * 4} ");
        //     }
        //     else if (widget_amount > 80)
        //     {
        //         Console.WriteLine($"{widget_amount} \t\t\t £{widget_amount * 2.50} ");
        //     }
        //     else
        //     {
        //         Console.WriteLine($"{widget_amount} \t\t\t £{widget_amount * 5} ");
        //     }
        //     Console.Write("Do you want to terminate the program? Enter Q/q: ");
        //     string end_program = Console.ReadLine()!;
        //     if (end_program == "q" || end_program == "Q")
        //     {
        //         break;
        //     }

        // } while (counter2 <= widget_amount)
        // Console.Write("Enter N: ");
        // int number = Convert.ToInt32(Console.ReadLine());
        // int result = number;

        // for (int i = 1; i < number; i++)
        // {
        //     result = result * i;
        // }
        // Console.WriteLine($"Sum = {result}");

        // int n = 5;
        // for (int i = 1; i <= n; i++)
        // {
        //     for (int j = 1; j <= i; j++)
        //     {
        //         Console.Write("*");
        //     }
        //     Console.WriteLine();
        // }

        // string myString = "your name here";
        // int string_length = myString.Length;
        // string newString = "";

        // foreach (char c in myString)
        // {
        //     if (c == ' ')
        //     {
        //         string_length -= 1;
        //         continue;
        //     }
        //     newString += c;
        // }
        // Console.WriteLine($"Without spaces: {newString}");
        // Console.WriteLine($"There are {string_length} characters.");

        Random rnd = new Random();
        int random = rnd.Next(1, 21);
        bool number_guessed = false;
        while(number_guessed = false)
        {
            int choice = int.Parse(Console.ReadLine()!);
            if (choice > random)
            {
                Console.WriteLine("Too high");
            }
            else if (choice < random)
            {
                Console.WriteLine("Too high");
            }
            else
            {
                Console.WriteLine("Correct number!");
                break;
            }
        }

        

        

    }
}