import wmi

c = wmi.WMI()  

#Get Informaton from Logical Disks
for disk in c.Win32_LogicalDisk():  
    print(f"Drive: {disk.DeviceID}")  
    print(f"Type: {disk.DriveType}")  
    print(f"Size: {disk.Size} bytes")  
    print(f"Free Space: {disk.FreeSpace} bytes")
    
    
#Get Information About Services
c = wmi.WMI()  
for service in c.Win32_Service():  
    print(f"Service: {service.Name}")  
    print(f"State: {service.State}")  
    print(f"StartMode: {service.StartMode}")
    
#Get Information About Processors
c = wmi.WMI()  
for processor in c.Win32_Processor():  
    print(f"CPU: {processor.Name}")  
    print(f"Speed: {processor.MaxClockSpeed} MHz")

#Get Information About OS
c = wmi.WMI()  
system = c.Win32_OperatingSystem()[0]  
print(f"OS: {system.Caption}")  
print(f"Version: {system.Version}")  
print(f"Manufacturer: {system.Manufacturer}")

#Get Information About Network Adapters
for nic in c.Win32_NetworkAdapterConfiguration():  
    print("======== Network Interface ========")  
    print(f"Description: {nic.Description}")  
    print(f"MAC Address: {nic.MacAddress}")  
    print(f"IP Address: {nic.IPAddress}")  
    print(f"Subnet Mask: {nic.IPSubnet}")  
    print(f"DHCP Enabled: {nic.DHCPEnabled}")  
    print(f"DHCP Server: {nic.DHCPServer}")  
    print(f"Default Gateway: {nic.DefaultIPGateway}")  
    print(f"DNS Servers: {nic.DNSServerSearchOrder}")  
    print("=================================")