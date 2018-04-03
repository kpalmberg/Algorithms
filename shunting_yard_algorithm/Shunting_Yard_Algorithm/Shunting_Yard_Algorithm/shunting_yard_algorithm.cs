/* Author: Kevin Palmberg
 * Description: Implements Dijkstra's shunting yard algorithm to convert 
 * infix expressions to postfix (reverse polish notation). Program is in C#.*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace Shunting_Yard_Algorithm
{
    class Shunting_yard_algorithm
    {
        static string InfixToPostfix(string convert)
        {
            //char (operator) by int (precedence)
            //higher value = higher precedence
            Dictionary<string, int> precedence = new Dictionary<string, int>
            {
                { "-", 1 },
                { "+", 1 },
                { "/", 2 },
                { "*", 2 }
            };

            Queue<string> outputQueue = new Queue<string>(); //queue for the output

            Stack<string> operatorStack = new Stack<string>(); //stack for the operations

            //-------------------------------
            string pattern = @"[a-zA-Z]?\d+|[()e^/%x*+-]";
            MatchCollection parts = Regex.Matches(convert, pattern); //Separates input string into desired parts

            //Regex.Matches often includes "" as one of its parts, so this will create a list without any of those extra results
            List<string> partsList = new List<string>(); //create list to contain final result
            foreach (Match item in parts)
            {
                if (item.Value != "")
                {
                    partsList.Add(item.Value);
                }
            }
            //---------------------------------

            //Now that we have our expression parsed with parts separated into list, we implement shunting yard algorithm
            foreach (string token in partsList) //while there are tokens to be read
            {
                bool result = Int32.TryParse(token, out int number); //try converting token to integer

                if (result) //token was a number
                {
                    outputQueue.Enqueue(number.ToString()); //Result was convertable to int, go ahead and push to outputQueue
                }

                //This section is added to shunting yard algorithm to account for variables in the format (a-z)(0-9) or (A-Z)(0-9)
                //------------------------
                string variablePattern = @"[a-zA-Z]\d"; //Pattern to determine variable

                MatchCollection variableMatch = Regex.Matches(token, variablePattern); //check if it matches our pattern

                if (variableMatch.Count == 1) //is so the match collection will not be empty, and we can enqueue our token
                {
                    outputQueue.Enqueue(token); //enqueue the variable to the output queue
                }
                //-------------------------


                if ("+" == token || "-" == token || "*" == token || "/" == token) //token was an operator
                {
                    if (operatorStack.Count != 0) //if stack is not empty, else just push to stack
                    {
                        if ("(".CompareTo(operatorStack.Peek()) != 0) //don't need to check right bracket, will never be pushed to opeartorStack
                        {
                            while ((operatorStack.Count != 0) && (precedence[operatorStack.Peek()] > precedence[token])) //while there's an operator on the top of the stack with greater precedence than token
                            {
                                outputQueue.Enqueue(operatorStack.Pop()); //pop operators from the stack onto the output queue
                            }
                        }
                    }
                    operatorStack.Push(token); //Push the current operator onto the stack
                }

                if ("(" == token) //if the token is the left bracket
                {
                    operatorStack.Push(token); //push onto the opeartorStack
                }

                if (")" == token) //if the token is a right bracket
                {
                    while ("(" != operatorStack.Peek()) //while there's not a left bracket at the top of the stack
                    {
                        outputQueue.Enqueue(operatorStack.Pop()); //pop operator and push to the outputQueue
                    }

                    if ("(" == operatorStack.Peek()) //Once a left bracket is hit on top of the operatorStack
                    {
                        operatorStack.Pop(); //Pop the left bracket and discard it
                    }
                }
            }

            while (operatorStack.Count != 0) //while the operatorStack is not empty
            {
                outputQueue.Enqueue(operatorStack.Pop()); //Push the rest of the operator stack to the outputQueue
            }

            string postfixString = ""; //create a string for the output
            foreach (string token in outputQueue)
            {
                postfixString = postfixString + token + " "; //Concat each part of the outputQueue into a string seperated by spaces
            }

            return postfixString; //return final conversion result
        }

        static void Main(string[] args)
        {
            Console.WriteLine("This program uses the shuting yard algorithm to convert a infix represention to a postfix representation.\n");
            Console.WriteLine("To demonstrate we'll use the equation: 4+18/(9/3)");

            string postfixResult =  InfixToPostfix("4+18/(9-3)");

            Console.Write("The postfix result of the infix representation is: ");
            Console.WriteLine(postfixResult);

            string postfixResult2 = InfixToPostfix("a4+18/(9-b5)");

            Console.WriteLine("\nTesting same expression but with some variables.");
            Console.WriteLine("To demonstrate we'll use the equation: a4+18/(9-b5)");

            Console.WriteLine(postfixResult2 + "\n");
        }
    }
}
