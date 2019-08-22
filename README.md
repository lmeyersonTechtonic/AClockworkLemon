All bash and python scripts as well as namely_thingy directory should live in your home directory.

Ensure that all bash scripts are executable (-rwxrwxrwx)<br/>
cd into namely_thing and run `npm i` to install the Cypress dependencies

create your cron job a follows:
in your terminal type: `crontab -e`
in the vim editor that shows up enter: 
```
MAILTO=""
PATH=<your path>
SHELL=<your shell path>
0 8 * * 1-5 python3 in-for-day.py
0 17 * * 1-5 python3 out-for-day.py
```
This is calling the in-for-day script at 8:AM Mon-Fri and the out-for-day script at 5:PM Mon - Fri

To obtain your PATH, in your terminal type `echo $PATH`<br/>
To obtain your SHELL path type `echo $SHELL`


Regarding Vim and crontab<br/>
to save, `esc` to get out of insert mode.<br/> Then `:w` followed by `:wq`.
This is redundant but I've had better luck with crontab saving with this redundant approach.
You should get a sytem warning pop up if saved successfully. 

Go to namely_thingy/cypress.json
on line #4 enter your id number as timeClockId

The cron tasks will be skipped if your machine is off or hibernating at the assigned execution time.
With the bash scripts in your home folder, you can manage manual clockin or clockout with
`./clockIn` or `./clockOut`. Note: calling the bash scripts directly will not call the Python GUI.

<hr/>
Test your setup in the following two steps:<br/>

* from your home directory, `./testClockIn`. You should see Cypress open and Cyperss terminal output should read `All specs passed!`.


* add this line to your crontab<br/>
```
* * * * * python3 trash.py
```
<br/>
this will run every minute and trigger the UI. You'll be prompted to confirm or cancel a run of "testClockin" every minute. Selecting "Confirm", you won't see the Cypress terminal output directly as it's running in the background but you will see Cypress popup and then remove itself from your dock. If it's working, you should be good to go. Remove the test script from your crontab and re-save.<br/>
From your terminal you can type `crontab -l` to view all cron jobs.
