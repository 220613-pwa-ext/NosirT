package com.revature.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {
    private WebDriver driver;

    @FindBy(xpath = "//input[@id='username-input']")
    private WebElement userInput;

    @FindBy(xpath = "//input[@id='password-input']")
    private WebElement passwordInput;

    @FindBy(xpath="//button[@id='login-button']")
    private WebElement loginBtn;

    public LoginPage (WebDriver driver){
        this.driver=driver;
        PageFactory.initElements(driver,this);
    }

    public void typeUsername(String name){
        userInput.sendKeys(name);
    }

    public void typePassword(String pass){
        userInput.sendKeys(pass);
    }

    public void clickLogin(){
        loginBtn.click();
    }

    public WebElement getUsernameInput(){
        return userInput;
    }

    public WebElement getPasswordInput(){
        return passwordInput;
    }

    public WebElement getLoginButton(){
        return loginBtn;
    }

    /*public WebElement getUsernameInput(){
        return driver.findElement(By.id("username-input"));
    }

    public WebElement getPasswordInput(){
        return driver.findElement(By.id("password-input"));
    }

    public WebElement getLoginButton(){
        return driver.findElement(By.id("login-button"));
    }*/

}
