using System;
using System.Linq;
using System.Collections.Generic;
using System.Drawing;
using System.Threading;
using System.Windows.Forms;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using WebDriverManager;
using WebDriverManager.DriverConfigs.Impl;
using OpenQA.Selenium.Support.UI;
using System.Security.Claims;
using System.ComponentModel;
using System.IO;
using System.Net.Mail;
using System.Net;

namespace Download_Assistant
{
    public partial class Form1 : Form
    {
        IWebDriver driver;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            openChrome("https://animesuge.to/anime/digimon-ghost-game-jvnr4/ep-1");
        }

        private void openChrome(string URL)
        {
            var options = new ChromeOptions();
            //options.AddArgument("headless");
            new DriverManager().SetUpDriver(new ChromeConfig());
            var chromeDriverService = ChromeDriverService.CreateDefaultService();
            chromeDriverService.HideCommandPromptWindow = true;
            
            driver = new ChromeDriver(chromeDriverService, options);
            driver.Manage().Window.Maximize();
            driver.Navigate().GoToUrl(URL);

            //driver.Manage().Window.FullScreen();
            //options.AddArgument("--window-position=-32000,-32000");
        }
    }
}
