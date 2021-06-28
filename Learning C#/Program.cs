using System;

namespace Learning_C_
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            --- Lists and Arrays practice call ---

            ListsAndArraysPractice();
            */

            /* 
            --- Methods parameters and returns practice ---

            var squaredNum = Square(8);
            Console.WriteLine(squaredNum);
            */

            // Keep terminal window open until keypress
            Console.ReadKey();
        }

        static void ListsAndArraysPractice() {

            string[] movies = {"Lord of the Rings", "Harry Potter", "Star Trek", "The F Word", "Seven Psycopaths"};

            for (int i = 0; i < movies.Length; i++)
            {
                Console.WriteLine(movies[i]);
            }

            // Wait for keypress before closing
            Console.ReadKey();

        }

        static int Square(int inputNum) {
            int result = inputNum * inputNum;
            return result;
        }

        
    }
}
