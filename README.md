# SQLI Labs: How to identify, fix and prevent SQL injection vulnerabilities in the software
<img src="/assets/sqli-with-ast.png" alt="sast" width="100%"><br/>
<h1>1. Introduction</h1><br/>
<p>When SQL queries are not implemented correctly in the code, malicious users can break this weaknesses and compromise the security of the database. In this project, we're going to show how to <b>identify</b>,<b>fix</b> and <b>prevent</b> SQL injection vulnerabilities in the software.</p><br/>
<h1>2. The 6 golden rules to prevent your software against SQL injection attacks.</h1><br/>
<div>
<h2>2.1 Use a database with the principle of least privilege</h2><br/>
<p>Grants your database user only the privileges needed to execute a SQL query. And revokes any other privileges that are not needed. Also limits remote authentication of your database to prevent unauthorized access.</p><br/>
<h2>2.2 Use AST (Application Security Testing) tools in your CI/CD</h2><br/>
<p>Integrate SCA, SAST and DAST tools into your CI/CD to scan your application to statically and dynamically identify early where the vulnerability is in your code so that it can be corrected before the application is put into production.</p><br/>
<h2>2.3 Well validate users input</h2><br/>
<p>Instead of validating input on the client side, validate all user input on the server side with only a list of allowed characters using regular expressions and reject any character not in this list.</p><br/>
<h2>2.4 Well sanitize users input</h2><br/>
<p>Adds an additional layer of protection by removing and replacing with a blank any character deemed malicious in user-entered data.</p><br/>
<h2>2.5 Use only prepared and parameterised queries</h2><br/>
<p>Using this, it allows the server to not execute the user-entered data as SQL code but will interpret it as plain text. This allows the server to not execute malicious code provided by the user in the data they entered.</p><br/>
<h2>2.6 Use a WAF (Web Application Firewall)</h2><br/>
<p>WAFs thoroughly analyze the content of HTTP/HTTPS requests (url, header, body, parameters, methods, etc.) sent by users before they reach the web server and block any request deemed malicious before being processed by the server. This helps protect your application against SQL attacks.</p><br/>
</div><br/>
<h1>2. Watches the video to learn how to fix identify and prevent SQL injections vulnerabilties.</h1><br/>
<div><a href="https://www.linkedin.com/posts/e-ben-sidi-87b51a242_cybersecurity-devsecops-sqlabrinjection-activity-7329500759811657728-UGJp?utm_source=share&utm_medium=member_desktop&rcm=ACoAADw7tV8BqIg_cwvMuPaiSHCfVjgxeNX_TUI">Please click here to watch the video about how to identify, fix and prevent SQL injection vulnerabilties in the software.</a></div>

