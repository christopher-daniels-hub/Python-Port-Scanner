# Python Port Scanner

## Project Overview

I created a custom Python port scanner as part of an authorized college 
cybersecurity lab. The scanner checks a defined range of TCP ports and reports 
which ports accept a connection.

## Objective

The objective was to understand how network reconnaissance tools identify 
accessible services and how defenders can detect scanning activity.

## Lab Environment

- Kali Linux virtual machine
- Windows Server virtual machine
- Isolated VMware network
- Python 3

## Tools Used

- Python
- Python socket library
- Kali Linux
- Windows Server
- VMware

## Method

I created a Python script that attempted TCP connections to a specified range 
of ports on the target server. When a connection succeeded, the script recorded 
the port as open.

The scanner was used only against an authorized Windows Server located in an 
isolated college lab environment.

## Results

The scanner identified accessible ports on the target server. I compared the 
results with the services running on Windows Server to verify the scanner’s 
accuracy.

## Skills Demonstrated

- Python scripting
- TCP/IP networking
- Port and service identification
- Troubleshooting
- Result verification
- Security documentation
- Offensive and defensive security awareness

## Defensive Perspective

A security team could detect this activity through repeated connection attempts, 
Windows Firewall logs, intrusion detection alerts, and network traffic monitoring.

Organizations can reduce their exposure by closing unnecessary ports, restricting 
access through firewall rules, monitoring connection attempts, and regularly 
reviewing exposed services.

## Ethical Statement

This project was performed only in an isolated and authorized academic lab. 
Security testing should never be performed against systems without explicit 
permission.
