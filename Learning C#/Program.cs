using System;

namespace Learning_C_
{
    class Program
    {
        static void Main(string[] args)
        {
            // ListsAndArraysPractice(); --- Call Lists Practice Method
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
    }
}
