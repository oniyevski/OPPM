import os, platform, time
from rich.prompt import Prompt
from rich.console import Console

os.system('title ONI PROXIFIER PROFILE MANAGER v1.0.0 developed by oniyevski')

console = Console(width=100)

def print_banner():
    os.system('cls')
    ascii_art = """                                        
               $$                   $$           
              $[$         $         $|$          
              $c[$      $$[$$      $[c$          
              $$z][$$$$$$z]z$$$$$$[]z$$          
               $$$$zz$$>i$$$i>$$zz$$$$           
                  $$$$zi>>$>i+z$$$$              
                  $$(z[[i>i>i[tz{$$              
                  $$[$$$X][]Y$$$]$$              
                   $%[$$$z[Y$$$]$$               
                   $$zzz$Uca$zzu$$               
                  $$$][z$$$$$z[[$$$              
              $$$$u$$zzz$$$$$zzz$$u$$$$          
              $uL$hLu$$$$$$$$$$Bu$$$$v$          
               $$uLhapLh$$$$$$$$$$$v$$           
                  $$$h$ha$$$$$$$$$$              
                      $$$$$$$$$                                                                                 
    """
    cleaned_ascii_art = "\n".join(line.strip() for line in ascii_art.splitlines())
    for line in cleaned_ascii_art.splitlines():
        console.print("[dark_orange3]" + line, justify="center", no_wrap=True)
    console.print(f"\n[sea_green1]ONI PROXIFIER PROFILE MANAGER", justify="center", no_wrap=True)
    console.print(f"[sky_blue2]v1.0.1", justify="center", no_wrap=True)
    console.print(f"[plum1]{platform.system()} {platform.release()} {platform.version()}", justify="center",
                  no_wrap=True)
    console.print(f"\n[turquoise2]developed by oniyevski\n", justify="center", no_wrap=True)


xml = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ProxifierProfile version="102" platform="Windows" product_id="0" product_minver="400">
	<Options>
		<Resolve>
			<AutoModeDetection enabled="false" />
			<ViaProxy enabled="true" />
			<BlockNonATypes enabled="false" />
			<ExclusionList OnlyFromListMode="false">%ComputerName%; localhost; *.local</ExclusionList>
			<DnsUdpMode>0</DnsUdpMode>
		</Resolve>
		<Encryption mode="disabled" />
		<ConnectionLoopDetection enabled="true" resolve="true" />
		<Udp mode="mode_bypass" />
		<LeakPreventionMode enabled="false" />
		<ProcessOtherUsers enabled="false" />
		<ProcessServices enabled="false" />
		<HandleDirectConnections enabled="false" />
		<HttpProxiesSupport enabled="false" />
	</Options>
	<ProxyList>
		<Proxy id="100" type="SOCKS5">
			<Authentication enabled="{AUTH_STATUS}">
				<Password>{PROXY_PASS}</Password>
				<Username>{PROXY_USERNAME}</Username>
			</Authentication>
			<Options>48</Options>
			<Port>{PROXY_PORT}</Port>
			<Address>{PROXY_ADRESS}</Address>
		</Proxy>
	</ProxyList>
	<ChainList />
	<RuleList>
		<Rule enabled="true">
			<Action type="Proxy">100</Action>
			<Applications>{PATHS}</Applications>
			<Name>ONI DISCORD UNBLOCKER</Name>
		</Rule>
		<Rule enabled="true">
			<Action type="Direct" />
			<Name>Default</Name>
		</Rule>
	</RuleList>
</ProxifierProfile>
"""

print_banner()

def error(text):
    console.print(f"[#FFFFFF on red] ERROR [/] {text}", justify="left", no_wrap=True)

try:
    discord_folder = os.path.expanduser(r'~\AppData\Local\Discord')
    exe_paths = []
    for root, dirs, files in os.walk(discord_folder):
        for file in files:
            if file.endswith('.exe'):
                if "update" in file.lower():
                    exe_paths.append(f'"{os.path.join(root, file)}"')
                else:
                    exe_paths.append(f'{file}')
except:
    console.print(
        f"[red]The proxy does not work on discord servers. Wait 5 seconds to try another proxy...",
        justify="center")
    time.sleep(5)

while True:
    ipv4_adress = Prompt.ask("[#FFFFFF on blue] IPv4 Proxy Adress [/]")
    try:
        check_ipv4_adress = ipv4_adress.split(".")
        if len(check_ipv4_adress) != 4:
            error("Please enter a valid proxy value.")
        else:
            for ip_block in check_ipv4_adress:
                ip_block = int(ip_block)
            break
    except ValueError:
        error("Enter a value adhering to the proxy structure.")
while True:
    ipv4_port = Prompt.ask("[#FFFFFF on blue] IPv4 Proxy Port [/]")
    try:
        int(ipv4_port)
        break
    except ValueError:
        error("Only numbers can be entered.")
while True:
    ipv4_authentication = Prompt.ask("[#FFFFFF on blue] IPv4 Proxy Authentication (yes or no) [/]")
    try:
        if ipv4_authentication.lower() in ["yes", "no"]:
            break
        else:
            error("Please enter yes or no.")
    except ValueError:
        error("Only numbers can be entered.")
if ipv4_authentication.lower() == "yes":
    auth_status = "true"
    ipv4_username = Prompt.ask("[#FFFFFF on blue] IPv4 Proxy Username [/]")
    ipv4_password = Prompt.ask("[#FFFFFF on blue] IPv4 Proxy Password [/]")
else:
    auth_status = "false"
    ipv4_username = ""
    ipv4_password = ""
print_banner()
formatted_paths = ';'.join(exe_paths)
xml = xml.replace("{PATHS}", formatted_paths).replace("{PROXY_ADRESS}", ipv4_adress).replace("{PROXY_PORT}",
                                                                                             ipv4_port).replace(
    "{PROXY_USERNAME}", ipv4_username).replace("{PROXY_PASS}", ipv4_password).replace("{AUTH_STATUS}",
                                                                                      auth_status)
with open("oni_discord_unblocker.ppx", "w", encoding="utf-8") as file:
    file.write(xml)
console.print(
    f"[green]Proxifier profile file has been saved in the directory where this programme is located. The software will shut down automatically within 10 seconds.",
    justify="center")
time.sleep(10)
exit()
