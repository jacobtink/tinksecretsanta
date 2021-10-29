# tinksecretsanta

At the moment, this code only work forward a SMTP test server. Next step is to include a secure login to your mail through SSL, that also can handle two-factor authentication.

## Set-Up

Start a server using this command. 
`python -m smtpd -n -c DebuggingServer localhost:1025`. 
Next, fill contacts_file.csv with any testdata you want to use. Then run the script using Python 3.
