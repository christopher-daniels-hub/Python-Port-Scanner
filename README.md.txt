# Python Port Scanner

## Project Overview

I developed a custom Python port scanner as part of an authorized offensive 
cyberspace operations lab. The tool scanned TCP ports 1 through 1024 on a 
Windows Server and reported the ports that accepted a connection.

## Objective

The objective was to learn how port scanning works at the code level and how 
red team operators identify accessible services on a target system. The results 
helped identify the server’s potential attack surface without guessing 
passwords, modifying the server, or establishing a reverse shell.

## Lab Environment

- Kali Linux
- Windows Server
- Isolated virtual lab network
- Python 3

## Tools and Technologies

- Python
- Python socket module
- TCP/IP networking
- Nano text editor
- Kali Linux terminal

## How the Scanner Works

The script creates a TCP socket and attempts to connect to each port from 1 
through 1024. A port is reported as open when the connection attempt succeeds. 
A short timeout prevents the scanner from waiting too long for unresponsive ports.

## Lab Results

The scanner successfully identified the following open ports:

- Port 22
- Port 135
- Port 445

## Source Code

The following screenshot shows the Python port scanner created in Nano.

![Python port scanner code](screenshots/port-scanner-code.png)

## Scan Results

The scanner identified open ports 22, 135, and 445 on the authorized Windows Server.

![Port scanner results](screenshots/port-scanner-results.png)

## Skills Demonstrated

- Python scripting
- TCP socket programming
- Port scanning
- Network reconnaissance
- Linux command-line operation
- Result analysis
- Technical documentation
- Defensive security awareness

## Detection Considerations

A blue team could detect the scanner because it attempts connections to more 
than 1,000 ports on the same server within a short period. Firewalls, intrusion 
detection systems, endpoint security tools, Windows logs, and SIEM platforms 
could record the source address, destination ports, timestamps, and repeated 
connection attempts.

## Verification

I could verify the results by running the scan again, comparing the findings 
with an authorized tool such as Nmap, checking the Windows Server’s active 
services, and reviewing applicable firewall and server logs.

## Potential Improvements

Future improvements could include:

- Allowing the user to enter an authorized target address
- Allowing custom port ranges
- Adding service-name identification
- Improving error handling
- Saving results to a log file
- Adding controlled multithreading
- Displaying the scan start and completion times

## Ethical Statement

This tool was developed and tested only in an isolated and authorized academic 
lab environment. It should never be used to scan systems without explicit 
permission.