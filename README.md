# Simple Port Scanner

## What is this?

A small Python tool that checks which ports are open on a computer. Ports are like numbered 'doors' that programs use to talk over a network (web servers use 80 and 443). This is a simple version I built as a milestone project while learning Python.

## Usage

```
python scanner.py <host> <start_port> <end_port>
```

Example:

```
python scanner.py 127.0.0.1 1 1024
```

## How it works

For each port in the range, it tries to open a TCP connection. If the connection succeeds, the port is open. When it finishes, it prints how many ports it checked and how long the scan took.

## What I learned

I got to experience building a basic script in Python utilizing ports, sockets, and timeouts.

## Disclaimer

Only use on systems you own or have permission to test.
