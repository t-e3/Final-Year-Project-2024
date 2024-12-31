from tkinter import *
from tkinter import ttk, messagebox
import webbrowser



def search():
    if questionField.get() != "":
        if temp.get() == 'domain':
            webbrowser.open(f'https://www.statscrop.com/www/{questionField.get()}')
            webbrowser.open(f'https://sitereport.netcraft.com/?url={questionField.get()}')
            webbrowser.open(f'https://builtwith.com/{questionField.get()}')
            webbrowser.open(f'https://www.robtex.com/dns-lookup/{questionField.get()}')
            webbrowser.open(f'https://securityheaders.com/?q={questionField.get()}')
            webbrowser.open(f'https://viewdns.info/dnssec/?domain={questionField.get()}')
            webbrowser.open(f'https://viewdns.info/portscan/?host={questionField.get()}')
            webbrowser.open(f'https://viewdns.info/ping/?domain={questionField.get()}' )
            webbrowser.open(f'https://viewdns.info/traceroute/?domain={questionField.get()}')
            webbrowser.open(f'https://crt.sh/?q={questionField.get()}')
            
        elif temp.get() == 'ip':
            
            webbrowser.open(f'https://whatismyipaddress.com/ip/{questionField.get()}')
            webbrowser.open(f'https://www.iplocation.net/search?cx=partner-pub-1026064395378929%3A2796854705&cof=FORID%3A10&ie=UTF-8&q={questionField.get()}')
            webbrowser.open(f'https://www.shodan.io/host/{questionField.get()}')
            webbrowser.open(f'https://www.criminalip.io/asset/report/search?query={questionField.get()}') 
            webbrowser.open(f'https://browserleaks.com/ip/{questionField.get()}')
            webbrowser.open(f'https://ipinfo.io/{questionField.get()}')
            webbrowser.open(f'https://db-ip.com/{questionField.get()}')
            webbrowser.open(f'https://www.virustotal.com/gui/ip-address/{questionField.get()}')
         
        elif temp.get() == 'people':
            webbrowser.open(f'https://www.bing.com/search?q={questionField.get()}')
            webbrowser.open(f'https://duckduckgo.com/?q={questionField.get()}')
            webbrowser.open(f'https://yandex.com/search/?text={questionField.get()}')
            webbrowser.open(f'https://search.aol.com/aol/search?q={questionField.get()}')
            webbrowser.open(f'https://www.qwant.com/?l=en&q={questionField.get()}') 
            webbrowser.open(f'https://swisscows.com/en/web?query={questionField.get()}')
            webbrowser.open(f'https://search.lycos.com/web/?q={questionField.get()}')
            webbrowser.open(f'https://www.webcrawler.com/serp?q={questionField.get()}')
            webbrowser.open(f'https://www.google.com/search?q=site:*.*+{questionField.get()}')
            
            
            
        else:
            messagebox.showerror('Error', 'Please search for people, domains, or IP addresses to view results in the browser.')



root = Tk()
root.geometry('660x400+150+150')
root.title('OSINT Community Central Web Crawler')
root.config(bg='#20879c')  # Set the background color to blue

temp = StringVar()
temp.set('domain')

queryLabel = Label(root, text='Query', font=('Arial', 14, 'bold'), bg='#20879c')
queryLabel.grid(row=0, column=0)

questionField = Entry(root, width=45, font=('Arial', 14, 'bold'), bd=4, relief=SUNKEN)
questionField.grid(padx=10, row=0, column=1)

searchButton = Button(root, bd=0, cursor='hand2', bg='#20879c', activebackground='#1cefff', command=search)
searchButton.grid(row=0, column=3, padx=5)

googleRadioButton = ttk.Radiobutton(root, text='Search Domains', value='domain', variable=temp)
googleRadioButton.place(x=75, y=40)

duckRadioButton = ttk.Radiobutton(root, text='Search IP Address', value='ip', variable=temp)
duckRadioButton.place(x=255, y=40)

amazonRadioButton = ttk.Radiobutton(root, text='Search People', value='people', variable=temp)
amazonRadioButton.place(x=460, y=40)

def enter_function(event):
    searchButton.invoke()

root.bind('<Return>', enter_function)

root.mainloop()