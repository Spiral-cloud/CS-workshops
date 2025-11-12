using System.Security.Cryptography.X509Certificates;

internal class Program
{
    private static void Main(string[] args)
    {
        // Console.Write("Enter a number: ");
        // int number = Convert.ToInt32(Console.ReadLine());
        // if (number % 2 == 1)
        // {
        //     Console.WriteLine("This number is odd");
        // }
        // else
        // {
        //     Console.WriteLine("This number is even");
        // }

        // Console.Write("What is the temperature: ");
        // int temp = Convert.ToInt16(Console.ReadLine());
        // if (temp < 10)
        // {
        //     Console.WriteLine("Too cold!");
        // }
        // else if (temp >= 10 && temp <= 25)
        // {
        //     Console.WriteLine("Comfortable");
        // }
        // else
        // {
        //     Console.WriteLine("Too hot");
        // }

        // Console.Write("Enter your age: ");
        // int age = Convert.ToInt32(Console.ReadLine());
        // Console.Write("Are you a student? (true/false) ");
        // bool student_status = bool.Parse(Console.ReadLine()!);
        // if (age >= 18 || age <= 65)
        // {
        //     Console.WriteLine("Discount applies");
        // }
        // else if (student_status == true)
        // {
        //     Console.WriteLine("Discount applies");
        // }
        // else
        // {
        //     Console.WriteLine("No discount applies");
        // }

        // int minimum_value = 40;
        // Console.Write("Enter your test score: ");
        // int test_score = Convert.ToInt32(Console.ReadLine());
        // int score = test_score >= minimum_value ? test_score : -test_score;
        // if (score < 0)
        // {
        //     Console.WriteLine("Fail");
        // }
        // else
        // {
        //     Console.WriteLine("Pass");
        // }
        // Console.WriteLine("1.Tea \n2.Coffee\n3.Water\n4.Exit ");
        // int choice = Convert.ToInt32(Console.ReadLine());
        // switch (choice)
        // {
        //     case 1:
        //         Console.WriteLine("You selected tea");
        //         break;
        //     case 2:
        //         Console.WriteLine("You selected coffee");
        //         break;
        //     case 3:
        //         Console.WriteLine("You selected water");
        //         break;
        //     case 4:
        //         break;

        // }
        // decimal base_price = 10.00m;
        // Console.Write("Enter your age: ");
        // int age = Convert.ToInt32(Console.ReadLine());
        // Console.Write("Are you a student (true/false) ");
        // bool student_status = bool.Parse(Console.ReadLine()!);
        // if (age < 18)
        // {
        //     base_price = base_price / 2;
        //     Console.WriteLine($"Discount: 50%");
        // }
        // else if (age >= 65)
        // {
        //     decimal percent = 0.3m;
        //     base_price = Decimal.Multiply(base_price, percent);
        //     Console.WriteLine($"Discount: 30%");
        // }
        // if (student_status == true)
        // {
        //     base_price = base_price / 4;
        //     Console.WriteLine($"Discount: 25%");
        // }

        // Console.WriteLine($"Final price: {base_price}");
        string suitOutput = "";
        string cardOutput = "";
        Console.Write("Enter a suit value: ");
        char suitValue = char.Parse(Console.ReadLine()!);
        Console.Write("Enter a card value: ");
        int cardValue = Convert.ToInt32(Console.ReadLine());
        if (suitValue == 's')
        {
            suitOutput = "spades";
        }
        else if (suitValue == 'h')
        {
            suitOutput = "hearts";
        }
        else if (suitValue == 'c')
        {
            suitOutput = "clubs";
        }
        else if (suitValue == 'd')
        {
            suitOutput = "diamonds";
        }
        else
        {
            suitOutput = "Invalid suit value";
        }
        if (cardValue == 7)
        {
            cardOutput = "Seven";
        }
        else if (cardValue == 8)
        {
            cardOutput = "Eight";
        }
        else if (cardValue == 9)
        {
            cardOutput = "Nine";
        }
        else if (cardValue == 10)
        {
            cardOutput = "Ten";
        }
        else if (cardValue == 11)
        {
            cardOutput = "Jack";
        }
        else if (cardValue == 12)
        {
            cardOutput = "Queen";
        }
        else if (cardValue == 13)
        {
            cardOutput = "King";
        }
        else if (cardValue == 14)
        {
            cardOutput = "Ace";
        }
        else
        {
            cardOutput = "Invalid card value";
        }
        Console.WriteLine($"{cardOutput} of {suitOutput}");
    }
}