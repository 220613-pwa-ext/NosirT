package com.revature.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class IndexPage {
    private WebDriver driver;

    public IndexPage (WebDriver driver){
        this.driver=driver;
    }

    public WebElement getMainHeading(){
        return driver.findElement(By.xpath("//h1[1]"));
    }


    public WebElement getLogout(){
        return driver.findElement(By.xpath("//*[@id='logout-button']"));
    }
}
