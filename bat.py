import os

def main():
    obj = Bat()
    obj.run()
    print('[+]MISSION ACCOMPLISHED[!]')

class Bat:
    def __init__(self):
        print('[+]INNITIALIZING INSTALL PROCESS[!]')

    def prep(self):
        cd1 = ('sudo pacman -Syyu --noconfirm', 'sudo curl -O https://blackarch.org/strap.sh > strap.sh', 'sudo chmod +x strap.sh', 'sudo ./strap.sh')

        for cd in cd1:
            print('[!] INNITIALIZING COMMAND: ' + cd + '[!]')
            os.system(cd)
            print(cd + '[+] PREPERATION COMPLETED [!]')

    def install(self):
        tools = ('webapp', 'fuzzer', 'scanner', 'proxy', 'windows', 'dos', 'disassembler', 'cracker', 'voip', 'exploitation', 'recon', 'spoof', 'forensics', 'crypto', 'backdoor', 'networking', 'misc', 'defensive', 'wireless', 'automation', 'sniffer', 'binary', 'packer', 'reversing', 'mobile', 'malware', 'code-audit', 'social', 'honeypot', 'hardware', 'fingerprint', 'decompiler', 'config', 'debugger', 'firmware', 'bluetooth', 'database', 'automobile', 'nfc', 'tunnel', 'drone', 'unpacker', 'radio', 'keylogger', 'stego', 'scanner', 'anti-forensics', 'ids', 'gpu')

        for tool in tools:
            command = 'sudo pacman -S --noconfirm blackarch-' + tool
            print('[!] INNITIALIZING COMMAND: ' + command + '[!]')
            os.system(command)
            print(command + '[+] COMPLETED [!]')

    def run(self):
        bt = Bat()
        bt.prep()
        bt.install()

if __name__ == '__main__':
    main()
