package com.revature.main;

import com.revature.exception.DenominatorCannotBeZero;

public class Calculator {
    public double divide(int num1, int num2 ) throws DenominatorCannotBeZero {
        if (num2 ==0){
            throw new DenominatorCannotBeZero("Not divided by zero");
        }
        return num1/num2;
    }
     public double divide(double num1, double num2){
        return num1/num2;
    }
}
