london_co = {
    "pc1": {
        "os": "Windows 10",
        "processor": "AMD Phenom II",
        "ram": "8 Gb",
        "motherboard": "MSI87343",
        "hdd": "1Tb",
    },
    "pc2": {
        "os": "Windows 10",
        "processor": "AMD Phenom I",
        "ram": "4 Gb",
        "motherboard": "MSI84599",
        "hdd": "2Tb",
    },
    "pc3": {
        "os": "Windows 7",
        "processor": "AMD Phenom III",
        "ram": "16 Gb",
        "motherboard": "MSI98987",
        "hdd": "1Tb",
    },

}
device = input("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")

print(london_co[device][parameter])

