# tinksecretsanta

At the moment, this code cannot handle 2FA. You can either provide a dummy email, or run forwards a SMTP Test Server

## Set-Up

First, set testServerEnabled to True if you want to run forwards a server. You will not need any login for this. If this is false, you will need to provide credentials to the mail you want to send from.   
Then, start a server using this command. 
`python -m smtpd -n -c DebuggingServer localhost:1025`. 
Next, fill contacts_file.csv with any testdata you want to use. Then run the script using Python 3.
