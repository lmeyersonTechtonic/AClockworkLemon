All bash and python scripts as well as namely_thingy directory should live in your home directory.

Ensure that all bash scripts are executable (-rwxrwxrwx)

create your cron job a follows:
in your terminal type: `crontab -e`
in the vim editor that shows up enter: 
```
MAILTO=""
PATH=<your path>
SHELL=<your shell path>
0 8 * * 1-5 ./in-for-day.py
30 16 * * 1-5 ./out-for-day.py
```
Regarding Vim and crontab<br/>
to save, `esc` to get out of insert mode.<br/> Then `:w` followed by `:wq`.
This is redundant but I've had better luck with crontab saving with this redundant approach.
You should get a sytem warning pop up if saved successfully. 

Go to namely_thingy/cypress.json
on line #4 enter your id number as timeClockId

The cron tasks will skip if your machine is off or hibernating.
With the bash scripts in your home folder, you can manage manual clockin or clockout with
`./clockIn` or `./clockOut`