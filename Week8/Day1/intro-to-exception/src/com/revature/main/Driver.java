package com.revature.main;

import com.revature.exception.DenominatorCannotBeZero;

import java.util.Scanner;

public class Driver {
    public static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        Calculator c = new Calculator();

        while (true) {

            try {
                System.out.println("Do you wnat to continue?(y/n): ");
                String choice = sc.nextLine();
                if (choice.equals("n")) {
                    break;
                }
                System.out.println("Enter numerator: ");
                int num1 = Integer.parseInt(sc.nextLine());

                System.out.println("Enter denominator: ");
                int num2 = Integer.parseInt(sc.nextLine());

                double result = c.divide(num1, num2);


            } catch (DenominatorCannotBeZero e) {
                System.out.println("Something is wrong with our arithmetic");
                System.out.println(e);
                System.out.println(e.getMessage());


            }
        }
    }
}
