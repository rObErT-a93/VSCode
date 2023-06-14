import tkinter as tk

def ipv4_to_binary():
    ip_address = ip_entry.get()
    binary_address = '.'.join(format(int(x), '08b') for x in ip_address.split('.'))
    result_label.config(text="Binary: " + binary_address)
    
def binary_to_ipv4():
    binary_address = binary_entry.get()
    ip_address = '.'.join(format(int(x, 2)) for x in binary_address.split('.'))
    result_label.config(text="IPv4: " + ip_address)
    
# Create the main window
window = tk.Tk()
window.title("IPv4 Converter")

# Create the IP to Binry translation section
ip_label = tk.Label(window, text="IPv4 Address: ")
ip_label.pack()
ip_entry = tk.Entry(window)
ip_entry.pack()
ip_button = tk.Button(window, text="Translate to Binary", command=ipv4_to_binary)
ip_button.pack()

# Create the Binary to IP translation section
binary_label = tk.Label(window, text="Binary Address: ")
binary_label.pack()
binary_entry = tk.Entry(window)
binary_entry.pack()
binary_button = tk.Button(window, text="Translate to IPv4", command=binary_to_ipv4)
binary_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main loop
window.mainloop()
